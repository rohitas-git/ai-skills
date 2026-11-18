#!/usr/bin/env python3
"""Save or inspect one local project-task checkpoint. Never execute its contents."""

from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import secrets
import stat
import subprocess
import sys

MAX_BYTES = 1024 * 1024
STATE = "continuation.json"
LOCK = ".continuation.lock"
SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
SHA = re.compile(r"[a-f0-9]{64}\Z")
TEXT = {"goal", "phase", "next_action", "operation_state"}
LISTS = {"scope", "exclusions", "authority_limits", "decisions", "owned_paths",
         "protected_paths", "artifacts", "remaining", "services"}
RESULTS = {"PASS", "FAIL", "BLOCKED", "NOT_RUN"}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def decode(data):
    if len(data) > MAX_BYTES:
        raise ValueError("checkpoint input exceeds 1 MiB")
    return json.loads(data)


def text(value):
    return isinstance(value, str) and bool(value.strip()) and len(value) <= 8192


def relative(value):
    path = Path(value)
    if not value or path.is_absolute() or ".." in path.parts or ".git" in path.parts or "\\" in value or not path.parts:
        raise ValueError("paths must be project-relative, without traversal or .git")
    return path


def validate(record, task):
    if not isinstance(record, dict) or set(record) != TEXT | LISTS | {"status", "evidence"}:
        raise ValueError("record fields must match the documented checkpoint contract")
    if not all(text(record[key]) for key in TEXT):
        raise ValueError("goal, phase, next_action and operation_state must be nonempty text")
    if record["status"] not in {"in_progress", "paused", "blocked", "complete"}:
        raise ValueError("invalid task status")
    for key in LISTS:
        if not isinstance(record[key], list) or len(record[key]) > 1000 or not all(text(item) for item in record[key]):
            raise ValueError(f"{key} must be a bounded list of nonempty text")
    for value in record["owned_paths"] + record["protected_paths"]:
        path = relative(value)
        if path.parent == Path(".scratch") / task and (path.name in {STATE, LOCK} or path.name.startswith(".continuation-")):
            raise ValueError("checkpoint storage cannot fingerprint or protect itself")
    if len(set(record["owned_paths"])) != len(record["owned_paths"]):
        raise ValueError("duplicate owned paths")
    if record["status"] == "complete" and record["remaining"]:
        raise ValueError("a complete task cannot have remaining work")
    evidence = record["evidence"]
    if not isinstance(evidence, list) or len(evidence) > 1000:
        raise ValueError("evidence must be a bounded list")
    for item in evidence:
        if not isinstance(item, dict) or set(item) != {"claim", "result", "locator"} or not text(item["claim"]) or not text(item["locator"]) or item["result"] not in RESULTS:
            raise ValueError("evidence requires claim, result and locator; receipts are claims to verify")


def project_root(value):
    supplied = Path(value).absolute()
    if supplied.is_symlink():
        raise ValueError("project root must not be a symlink")
    root = supplied.resolve(strict=True)
    if not root.is_dir():
        raise ValueError("project root must be a directory")
    return root


def git(root, *args, optional=False):
    result = subprocess.run(["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-C", str(root), *args],
                            capture_output=True, timeout=30)
    if result.returncode and not optional:
        raise ValueError("Git identity/status unavailable; no checkpoint was published")
    return result.stdout if result.returncode == 0 else b""


def identity(root, task):
    actual = Path(os.fsdecode(git(root, "rev-parse", "--show-toplevel")).strip()).resolve()
    if actual != root:
        raise ValueError("--project must name the Git project root, not a nested directory")
    exclusions = [f":(exclude,literal).scratch/{task}/{name}" for name in (STATE, LOCK)]
    exclusions.append(f":(exclude,glob).scratch/{task}/.continuation-*.tmp")
    status = git(root, "status", "--porcelain=v1", "-z", "--untracked-files=all", "--ignore-submodules=all", "--", ".", *exclusions)
    return {"project": str(root),
            "branch": os.fsdecode(git(root, "symbolic-ref", "--quiet", "--short", "HEAD", optional=True)).strip() or None,
            "head": os.fsdecode(git(root, "rev-parse", "--verify", "--quiet", "HEAD", optional=True)).strip() or None,
            "status_sha256": digest(status)}


def file_digest(root, name):
    """Hash a declared regular file without following any project-relative symlink."""
    descriptor = os.open(root, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    try:
        parts = relative(name).parts
        for part in parts[:-1]:
            child = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=descriptor)
            os.close(descriptor)
            descriptor = child
        source = os.open(parts[-1], os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=descriptor)
        with os.fdopen(source, "rb") as handle:
            before = os.fstat(handle.fileno())
            if not stat.S_ISREG(before.st_mode):
                raise ValueError("owned paths must name regular files, not directories or devices")
            sha = hashlib.file_digest(handle, "sha256").hexdigest()
            after = os.fstat(handle.fileno())
            if (before.st_size, before.st_mtime_ns, before.st_ctime_ns) != (after.st_size, after.st_mtime_ns, after.st_ctime_ns):
                raise ValueError("declared file changed during capture; retry at a safe boundary")
            return sha
    except FileNotFoundError:
        return None  # A deleted/not-yet-created declared file is meaningful candidate state.
    finally:
        os.close(descriptor)


def workspace(root, task, record):
    current = identity(root, task)
    current["files"] = {name: file_digest(root, name) for name in sorted(record["owned_paths"])}
    if identity(root, task) != {key: value for key, value in current.items() if key != "files"}:
        raise ValueError("Git state changed during capture; retry at a safe boundary")
    current["fingerprint"] = digest(json.dumps(current, sort_keys=True).encode())
    return current


@contextmanager
def storage(root, task, create=False):
    descriptor = os.open(root, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    try:
        for part in (".scratch", task):
            if create:
                try:
                    os.mkdir(part, 0o700, dir_fd=descriptor)
                except FileExistsError:
                    pass
            child = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=descriptor)
            os.close(descriptor)
            descriptor = child
        yield descriptor
    finally:
        os.close(descriptor)


def read_state(directory):
    fd = os.open(STATE, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=directory)
    with os.fdopen(fd, "rb") as handle:
        info = os.fstat(handle.fileno())
        if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
            raise ValueError("checkpoint must be a regular, non-hardlinked file")
        raw = handle.read(MAX_BYTES + 1)
    packet = decode(raw)
    if not isinstance(packet, dict) or set(packet) != {"schema_version", "task", "revision", "updated_at", "workspace", "record"} or packet.get("schema_version") != 1 or type(packet.get("revision")) is not int or packet["revision"] < 1 or not isinstance(packet.get("workspace"), dict):
        raise ValueError("invalid checkpoint envelope")
    if not isinstance(packet.get("task"), str) or not SLUG.fullmatch(packet["task"]):
        raise ValueError("invalid checkpoint task")
    validate(packet.get("record"), packet["task"])
    captured = packet["workspace"]
    if set(captured) != {"project", "branch", "head", "status_sha256", "files", "fingerprint"} or not text(captured["project"]) or not isinstance(captured["files"], dict):
        raise ValueError("invalid saved workspace")
    if any(captured[key] is not None and not text(captured[key]) for key in ("branch", "head")) or not SHA.fullmatch(str(captured["status_sha256"])):
        raise ValueError("invalid saved Git identity")
    if set(captured["files"]) != set(packet["record"]["owned_paths"]) or any(value is not None and not SHA.fullmatch(str(value)) for value in captured["files"].values()):
        raise ValueError("invalid declared-file fingerprints")
    expected = digest(json.dumps({key: value for key, value in captured.items() if key != "fingerprint"}, sort_keys=True).encode())
    if captured["fingerprint"] != expected or datetime.fromisoformat(packet["updated_at"]).tzinfo is None:
        raise ValueError("invalid workspace fingerprint")
    return raw, packet


def publish(directory, raw):
    name = f".continuation-{secrets.token_hex(8)}.tmp"
    fd = os.open(name, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600, dir_fd=directory)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(raw)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(name, STATE, src_dir_fd=directory, dst_dir_fd=directory)
        os.fsync(directory)
    finally:
        try:
            os.unlink(name, dir_fd=directory)
        except FileNotFoundError:
            pass


def save(root, task, record, create=False, expected=None):
    validate(record, task)
    identity(root, task)  # Reject a non-project/nested root before creating storage.
    with storage(root, task, create=True) as directory:
        lock_fd = os.open(LOCK, os.O_WRONLY | os.O_CREAT | os.O_NOFOLLOW | os.O_NONBLOCK, 0o600, dir_fd=directory)
        with os.fdopen(lock_fd, "wb") as lock:
            if not stat.S_ISREG(os.fstat(lock.fileno()).st_mode) or os.fstat(lock.fileno()).st_nlink != 1:
                raise ValueError("checkpoint lock must be a regular, non-hardlinked file")
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            try:
                old_raw, old = read_state(directory)
            except FileNotFoundError:
                old_raw, old = None, None
            if old and (old["task"] != task or old["workspace"].get("project") != str(root)):
                raise ValueError("saved project/task differs; do not overwrite it")
            if create and old_raw is not None:
                raise ValueError("checkpoint already exists; inspect and use --expect for an owned update")
            if not create and (old_raw is None or digest(old_raw) != expected):
                raise ValueError("checkpoint changed or missing; inspect before updating")
            packet = {"schema_version": 1, "task": task, "revision": old["revision"] + 1 if old else 1,
                      "updated_at": datetime.now(timezone.utc).isoformat(),
                      "workspace": workspace(root, task, record), "record": record}
            raw = (json.dumps(packet, indent=2, ensure_ascii=False) + "\n").encode()
            if len(raw) > MAX_BYTES:
                raise ValueError("checkpoint exceeds 1 MiB")
            publish(directory, raw)
    return {"path": str(root / ".scratch" / task / STATE), "sha256": digest(raw), "revision": packet["revision"]}


def inspect(root, task):
    with storage(root, task) as directory:
        raw, packet = read_state(directory)
    if packet["task"] != task or packet["workspace"].get("project") != str(root):
        raise ValueError("saved project/task differs; do not resume from it")
    current = workspace(root, task, packet["record"])
    matches = current == packet["workspace"]
    changes = [key for key in ("branch", "head", "status_sha256") if current[key] != packet["workspace"][key]]
    changes.extend(f"file:{name}" for name, sha in current["files"].items() if sha != packet["workspace"]["files"][name])
    return {"disposition": "workspace_matches" if matches else "reconcile_required", "sha256": digest(raw),
            "changes": changes, "saved": packet, "current_workspace": current,
            "limits": "Declared files plus Git status/HEAD only; submodule internals, ignored undeclared files and services are not proved. Saved evidence/authority are historical claims. Nothing is executed."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("save", "inspect"):
        command = sub.add_parser(name)
        command.add_argument("--project", required=True, type=Path)
        command.add_argument("--task", required=True)
        if name == "save":
            command.add_argument("--input", required=True, type=Path)
            mode = command.add_mutually_exclusive_group(required=True)
            mode.add_argument("--create", action="store_true")
            mode.add_argument("--expect")
    args = parser.parse_args()
    try:
        if not SLUG.fullmatch(args.task) or len(args.task) > 80:
            raise ValueError("task must be an at-most-80-character lowercase kebab slug")
        root = project_root(args.project)
        if args.command == "save":
            if args.expect is not None and not SHA.fullmatch(args.expect):
                raise ValueError("--expect requires the inspected SHA-256")
            source_fd = os.open(args.input, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
            with os.fdopen(source_fd, "rb") as source:
                if not stat.S_ISREG(os.fstat(source.fileno()).st_mode):
                    raise ValueError("--input must be a regular, non-symlink JSON file")
                record = decode(source.read(MAX_BYTES + 1))
            result = save(root, args.task, record, args.create, args.expect)
        else:
            result = inspect(root, args.task)
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 3 if result.get("disposition") == "reconcile_required" else 0
    except (OSError, ValueError, TypeError, KeyError, subprocess.TimeoutExpired) as error:
        print(f"checkpoint error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
