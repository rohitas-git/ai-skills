#!/usr/bin/env python3
"""Structurally lint a prompt-injection trust-boundary manifest.

The manifest records control claims and gaps. Passing lint does not mean the
controls are implemented or effective; only evidence-backed tests can do that.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import stat
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]{0,127}$")
MAX_BYTES = 5 * 1024 * 1024
MAX_ISSUES = 100
MAX_DEPTH = 64
TRUST = {"trusted", "mixed", "untrusted"}
CLASSIFICATIONS = {
    "public",
    "internal",
    "confidential",
    "restricted",
    "personal",
    "financial",
    "health",
    "credentials",
}
EFFECTS = {
    "read",
    "write",
    "delete",
    "execute",
    "external",
    "financial",
    "access-control",
    "network-egress",
}
RISKS = {"low", "medium", "high", "critical"}
CONFIRMATION = {"none", "risk-based", "always"}
CONTROL_STATUS = {"missing", "planned", "implemented", "verified"}
SINK_TYPES = {"ui", "api", "file", "database", "message", "code-execution", "agent", "log", "other"}


def add(items: list[dict[str, str]], level: str, path: str, message: str) -> None:
    items.append({"level": level, "path": path, "message": message})


def string_array(
    value: Any,
    path: str,
    items: list[dict[str, str]],
    *,
    nonempty: bool = False,
) -> set[str]:
    if not isinstance(value, list) or (nonempty and not value) or any(
        not isinstance(entry, str) or not entry.strip() for entry in value
    ):
        qualifier = "non-empty " if nonempty else ""
        add(items, "error", path, f"must be a {qualifier}array of non-empty strings")
        return set()
    values = set(value)
    if len(values) != len(value):
        add(items, "error", path, "values must be unique")
    return values


def identifier(value: Any, path: str, items: list[dict[str, str]]) -> str | None:
    if not isinstance(value, str) or not ID_RE.fullmatch(value):
        add(items, "error", path, "must use 1-128 safe identifier characters")
        return None
    return value


def text(value: Any, path: str, items: list[dict[str, str]]) -> str | None:
    if not isinstance(value, str) or not value.strip():
        add(items, "error", path, "must be a non-empty string")
        return None
    return value


def enum_value(value: Any, choices: set[str], path: str, items: list[dict[str, str]]) -> str | None:
    if not isinstance(value, str) or value not in choices:
        add(items, "error", path, f"must be one of {sorted(choices)}")
        return None
    return value


def timestamp(value: Any, path: str, items: list[dict[str, str]]) -> datetime | None:
    if not isinstance(value, str):
        add(items, "error", path, "must be an ISO 8601 timestamp")
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        add(items, "error", path, "must be a valid ISO 8601 timestamp")
        return None
    if parsed.tzinfo is None:
        add(items, "error", path, "timestamp must include a timezone")
        return None
    return parsed


def unique_object_ids(value: Any, path: str, items: list[dict[str, str]], *, nonempty: bool) -> set[str]:
    if not isinstance(value, list) or (nonempty and not value):
        qualifier = "non-empty " if nonempty else ""
        add(items, "error", path, f"must be a {qualifier}array")
        return set()
    seen: set[str] = set()
    for index, entry in enumerate(value):
        entry_path = f"{path}[{index}]"
        if not isinstance(entry, dict):
            add(items, "error", entry_path, "must be an object")
            continue
        entry_id = identifier(entry.get("id"), f"{entry_path}.id", items)
        if entry_id in seen:
            add(items, "error", f"{entry_path}.id", "duplicate id in this collection")
        elif entry_id:
            seen.add(entry_id)
    return seen


def validate_controls(value: Any, items: list[dict[str, str]]) -> set[str]:
    ids = unique_object_ids(value, "$.controls", items, nonempty=True)
    if not isinstance(value, list):
        return ids
    now = datetime.now(timezone.utc)
    for index, control in enumerate(value):
        path = f"$.controls[{index}]"
        if not isinstance(control, dict):
            continue
        text(control.get("kind"), f"{path}.kind", items)
        status = enum_value(control.get("status"), CONTROL_STATUS, f"{path}.status", items)
        text(control.get("enforcement_point"), f"{path}.enforcement_point", items)
        text(control.get("owner"), f"{path}.owner", items)
        evidence = string_array(control.get("evidence_ids"), f"{path}.evidence_ids", items)
        tests = string_array(control.get("test_ids"), f"{path}.test_ids", items)
        if status == "implemented" and not evidence:
            add(items, "warning", f"{path}.evidence_ids", "implemented control has no implementation evidence")
        if status == "verified":
            if not evidence:
                add(items, "error", f"{path}.evidence_ids", "verified control requires evidence IDs")
            if not tests:
                add(items, "error", f"{path}.test_ids", "verified control requires test IDs")
        if status in {"missing", "planned"} and (evidence or tests):
            add(items, "warning", path, f"{status} control includes evidence/test IDs; verify status")
        if status in {"missing", "planned"}:
            add(items, "warning", f"{path}.status", "control is not claimed implemented; visible coverage gap")
        time_limited = control.get("time_limited")
        if not isinstance(time_limited, bool):
            add(items, "error", f"{path}.time_limited", "must be boolean")
        expiry_value = control.get("expires_at")
        if time_limited:
            expiry = timestamp(expiry_value, f"{path}.expires_at", items)
            if expiry and expiry <= now and status == "verified":
                add(items, "error", f"{path}.expires_at", "verified time-limited control is expired")
        elif expiry_value is not None:
            add(items, "error", f"{path}.expires_at", "must be null when time_limited is false")
    return ids


def validate_control_refs(
    value: Any,
    path: str,
    items: list[dict[str, str]],
    control_ids: set[str],
    *,
    nonempty: bool = False,
) -> set[str]:
    refs = string_array(value, path, items, nonempty=nonempty)
    if refs - control_ids:
        add(items, "error", path, "contains unknown control IDs; inspect this field privately")
    return refs


def validate(data: Any) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    if not isinstance(data, dict):
        return [{"level": "error", "path": "$", "message": "manifest must be a JSON object"}]
    text(data.get("system"), "$.system", items)
    control_ids = validate_controls(data.get("controls"), items)

    assets = data.get("protected_assets")
    unique_object_ids(assets, "$.protected_assets", items, nonempty=True)
    if isinstance(assets, list):
        for index, asset in enumerate(assets):
            path = f"$.protected_assets[{index}]"
            if not isinstance(asset, dict):
                continue
            enum_value(asset.get("classification"), CLASSIFICATIONS, f"{path}.classification", items)
            text(asset.get("owner"), f"{path}.owner", items)

    sources = data.get("data_sources")
    unique_object_ids(sources, "$.data_sources", items, nonempty=True)
    if isinstance(sources, list):
        for index, source in enumerate(sources):
            path = f"$.data_sources[{index}]"
            if not isinstance(source, dict):
                continue
            trust = enum_value(source.get("trust"), TRUST, f"{path}.trust", items)
            string_array(source.get("modalities"), f"{path}.modalities", items, nonempty=True)
            refs = validate_control_refs(
                source.get("control_ids"), f"{path}.control_ids", items, control_ids, nonempty=trust in {"mixed", "untrusted"}
            )
            if trust in {"mixed", "untrusted"} and not refs:
                add(items, "warning", f"{path}.control_ids", "untrusted path has no placed control")

    sinks = data.get("sinks")
    sink_ids = unique_object_ids(sinks, "$.sinks", items, nonempty=True)
    if isinstance(sinks, list):
        for index, sink in enumerate(sinks):
            path = f"$.sinks[{index}]"
            if not isinstance(sink, dict):
                continue
            enum_value(sink.get("type"), SINK_TYPES, f"{path}.type", items)
            enum_value(sink.get("trust"), TRUST, f"{path}.trust", items)
            text(sink.get("owner"), f"{path}.owner", items)
            validate_control_refs(sink.get("control_ids"), f"{path}.control_ids", items, control_ids, nonempty=True)

    destinations = data.get("destinations")
    destination_ids = unique_object_ids(destinations, "$.destinations", items, nonempty=False)
    if isinstance(destinations, list):
        for index, destination in enumerate(destinations):
            path = f"$.destinations[{index}]"
            if not isinstance(destination, dict):
                continue
            text(destination.get("kind"), f"{path}.kind", items)
            text(destination.get("owner"), f"{path}.owner", items)
            validate_control_refs(destination.get("control_ids"), f"{path}.control_ids", items, control_ids, nonempty=True)

    memory = data.get("memory_stores")
    unique_object_ids(memory, "$.memory_stores", items, nonempty=False)
    if isinstance(memory, list):
        for index, store in enumerate(memory):
            path = f"$.memory_stores[{index}]"
            if not isinstance(store, dict):
                continue
            enum_value(store.get("trust"), TRUST, f"{path}.trust", items)
            string_array(store.get("read_principals"), f"{path}.read_principals", items, nonempty=True)
            string_array(store.get("write_principals"), f"{path}.write_principals", items, nonempty=True)
            validate_control_refs(store.get("control_ids"), f"{path}.control_ids", items, control_ids, nonempty=True)

    hops = data.get("agent_hops")
    unique_object_ids(hops, "$.agent_hops", items, nonempty=False)
    if isinstance(hops, list):
        for index, hop in enumerate(hops):
            path = f"$.agent_hops[{index}]"
            if not isinstance(hop, dict):
                continue
            text(hop.get("from_agent"), f"{path}.from_agent", items)
            text(hop.get("to_agent"), f"{path}.to_agent", items)
            validate_control_refs(hop.get("control_ids"), f"{path}.control_ids", items, control_ids, nonempty=True)

    credentials = data.get("credential_boundaries")
    unique_object_ids(credentials, "$.credential_boundaries", items, nonempty=False)
    if isinstance(credentials, list):
        for index, boundary in enumerate(credentials):
            path = f"$.credential_boundaries[{index}]"
            if not isinstance(boundary, dict):
                continue
            for field in ("credential_class", "holder", "audience", "storage"):
                text(boundary.get(field), f"{path}.{field}", items)
            passthrough = boundary.get("downstream_passthrough")
            if not isinstance(passthrough, bool):
                add(items, "error", f"{path}.downstream_passthrough", "must be boolean")
            elif passthrough:
                add(items, "error", f"{path}.downstream_passthrough", "credential passthrough must not cross this boundary")
            validate_control_refs(boundary.get("control_ids"), f"{path}.control_ids", items, control_ids, nonempty=True)

    tools = data.get("tools")
    unique_object_ids(tools, "$.tools", items, nonempty=False)
    external_tool = False
    if isinstance(tools, list):
        for index, tool in enumerate(tools):
            path = f"$.tools[{index}]"
            if not isinstance(tool, dict):
                continue
            effects = string_array(tool.get("effects"), f"{path}.effects", items, nonempty=True)
            if effects - EFFECTS:
                add(items, "error", f"{path}.effects", "contains unsupported effects; inspect this field privately")
            if effects & {"external", "network-egress"}:
                external_tool = True
            risk = enum_value(tool.get("risk"), RISKS, f"{path}.risk", items)
            destination_refs = string_array(
                tool.get("destination_ids"), f"{path}.destination_ids", items,
                nonempty=bool(effects & {"external", "network-egress"}),
            )
            if destination_refs - destination_ids:
                add(items, "error", f"{path}.destination_ids", "contains unknown destinations; inspect this field privately")
            sink_refs = string_array(tool.get("sink_ids"), f"{path}.sink_ids", items, nonempty=True)
            if sink_refs - sink_ids:
                add(items, "error", f"{path}.sink_ids", "contains unknown sinks; inspect this field privately")
            validate_control_refs(tool.get("control_ids"), f"{path}.control_ids", items, control_ids, nonempty=True)
            confirmation = tool.get("confirmation")
            if not isinstance(confirmation, dict):
                add(items, "error", f"{path}.confirmation", "must be a structured object")
                mode = None
            else:
                mode = enum_value(confirmation.get("mode"), CONFIRMATION, f"{path}.confirmation.mode", items)
                text(confirmation.get("enforcement_point"), f"{path}.confirmation.enforcement_point", items)
                text(confirmation.get("owner"), f"{path}.confirmation.owner", items)
            if risk == "critical" and mode == "none":
                add(items, "error", f"{path}.confirmation.mode", "critical tool must have risk-based or always confirmation")
            elif risk == "high" and mode == "none":
                add(items, "warning", f"{path}.confirmation.mode", "high-risk tool has no confirmation")
            if effects & {"delete", "execute", "external", "financial", "access-control"} and mode == "none":
                add(items, "warning", f"{path}.confirmation.mode", "consequential tool has no confirmation")
    if external_tool and not destination_ids:
        add(items, "error", "$.destinations", "external or egress tools require explicit destinations")

    for required_field in ("memory_stores", "agent_hops", "destinations", "credential_boundaries"):
        if required_field not in data:
            add(items, "error", f"$.{required_field}", "field is required; use an empty array when not applicable")
    return items


def unique_json_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON member")
        result[key] = value
    return result


def reject_constant(value: str) -> None:
    raise ValueError("non-standard JSON number")


def load_manifest(path: Path) -> Any:
    # Final-component protection, not a path sandbox. Caller selects a trusted location.
    if not hasattr(os, "O_NOFOLLOW") or not hasattr(os, "O_NONBLOCK"):
        raise OSError("safe file-open flags unavailable")
    flags = os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK
    descriptor = os.open(path, flags)
    with os.fdopen(descriptor, "rb") as source:
        info = os.fstat(source.fileno())
        if not stat.S_ISREG(info.st_mode) or info.st_size > MAX_BYTES:
            raise ValueError("input must be a regular file within the size limit")
        raw = source.read(MAX_BYTES + 1)
        if len(raw) > MAX_BYTES:
            raise ValueError("input exceeds size limit")
    data = json.loads(raw.decode("utf-8"), object_pairs_hook=unique_json_object,
                      parse_constant=reject_constant)
    pending = [(data, 0)]
    while pending:
        value, depth = pending.pop()
        if isinstance(value, (dict, list)):
            if depth >= MAX_DEPTH:
                raise ValueError("JSON nesting exceeds limit")
            entries = value.values() if isinstance(value, dict) else value
            pending.extend((entry, depth + 1) for entry in entries if isinstance(entry, (dict, list)))
    return data


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Structurally lint a prompt-injection boundary manifest; not a security certification",
        epilog="Read-only; Python 3.10+. Maximum 5 MiB regular UTF-8 JSON file; no final symlinks. "
               "Maximum 64 container levels; print at most 100 issues. Exit 0: structural pass (gaps may remain); "
               "1: violations; 2: invalid/unavailable input or unsupported safe-open platform.",
    )
    parser.add_argument("manifest", type=Path, help="boundary manifest JSON path")
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    args = parser.parse_args()
    try:
        data = load_manifest(args.manifest)
    except (OSError, ValueError, RecursionError):
        print("error: cannot read manifest; require a regular UTF-8 JSON file <=5 MiB, "
              "no final symlink, duplicate keys, non-standard numbers or excessive nesting; "
              "safe-open platform support required", file=sys.stderr)
        return 2
    items = validate(data)
    errors = sum(item["level"] == "error" for item in items)
    warnings = sum(item["level"] == "warning" for item in items)
    result = {
        "structural_status": "fail" if errors else "pass",
        "errors": errors,
        "warnings": warnings,
        "issues": items[:MAX_ISSUES],
        "issues_truncated": len(items) > MAX_ISSUES,
        "assurance": "none; verify implementation and adversarial-test evidence separately",
    }
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        for item in result["issues"]:
            print(f"{item['level'].upper()}: {item['path']}: {item['message']}")
        print(f"Structural manifest status: {result['structural_status'].upper()}")
        print(f"Summary: {errors} error(s), {warnings} warning(s)")
        if result["issues_truncated"]:
            print(f"Only the first {MAX_ISSUES} issues are shown; totals include all issues.")
        print("This lint result is not evidence that controls are implemented or effective.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
