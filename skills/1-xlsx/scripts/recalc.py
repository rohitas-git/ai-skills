#!/usr/bin/env python3
"""Recalculate an XLSX copy with an isolated LibreOffice profile.

The source is never modified. Parsing untrusted input requires the caller to
confirm that this entire process is already inside a verified sandbox.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import zipfile

ERROR_VALUES = {"#VALUE!", "#DIV/0!", "#REF!", "#NAME?", "#NULL!", "#NUM!", "#N/A"}


class RecalcError(Exception):
    """A safe recalculation precondition or operation failed."""


def resolved(path: Path) -> Path:
    try:
        return path.resolve(strict=False)
    except (OSError, RuntimeError) as exc:
        raise RecalcError(f"cannot resolve path safely: {path}: {exc}") from exc


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_paths(source: Path, output: Path, overwrite: bool) -> tuple[Path, Path]:
    output_lexical = Path(os.path.abspath(os.path.normpath(os.fspath(output))))
    if output_lexical.is_symlink():
        raise RecalcError(f"output must not be a symbolic link: {output_lexical}")
    source = resolved(source)
    output = resolved(output_lexical)
    if not source.is_file() or source.suffix.lower() != ".xlsx":
        raise RecalcError(f"source must be an existing regular .xlsx file: {source}")
    if source == output:
        raise RecalcError("output must not alias the source")
    try:
        if output.exists() and os.path.samefile(source, output):
            raise RecalcError("output aliases the source inode")
    except OSError as exc:
        raise RecalcError(f"cannot compare source and output safely: {exc}") from exc
    if not output.parent.is_dir():
        raise RecalcError(f"output directory does not exist: {output.parent}")
    if output.exists():
        if not output.is_file():
            raise RecalcError(f"output exists and is not a regular file: {output}")
        if not overwrite:
            raise RecalcError("output exists; pass --overwrite only with target-specific authority")
    return source, output


def archive_hazards(source: Path) -> list[str]:
    try:
        with zipfile.ZipFile(source) as archive:
            names = [name.lower() for name in archive.namelist()]
    except (OSError, zipfile.BadZipFile) as exc:
        raise RecalcError(f"invalid XLSX ZIP package: {exc}") from exc
    checks = {
        "VBA project": "vbaproject.bin",
        "embedded object": "/embeddings/",
        "external link": "/externallinks/",
        "custom UI": "/customui/",
    }
    return [label for label, marker in checks.items() if any(marker in name for name in names)]


def workbook_summary(path: Path) -> dict[str, object]:
    try:
        from openpyxl import load_workbook
    except ImportError as exc:
        raise RecalcError("openpyxl is required to verify recalculated formulas") from exc
    formulas = load_workbook(path, data_only=False, read_only=True)
    values = load_workbook(path, data_only=True, read_only=True)
    formula_count = 0
    errors: list[str] = []
    try:
        for formula_sheet, value_sheet in zip(formulas.worksheets, values.worksheets):
            for formula_row, value_row in zip(formula_sheet.iter_rows(), value_sheet.iter_rows()):
                for formula_cell, value_cell in zip(formula_row, value_row):
                    if isinstance(formula_cell.value, str) and formula_cell.value.startswith("="):
                        formula_count += 1
                    if isinstance(value_cell.value, str) and value_cell.value in ERROR_VALUES:
                        errors.append(f"{value_sheet.title}!{value_cell.coordinate}:{value_cell.value}")
    finally:
        formulas.close()
        values.close()
    return {"formula_count": formula_count, "error_count": len(errors), "errors": errors[:100]}


def atomic_copy(source: Path, output: Path, overwrite: bool) -> None:
    descriptor, temp_name = tempfile.mkstemp(prefix=f".{output.name}.", suffix=".tmp", dir=output.parent)
    temp = Path(temp_name)
    try:
        with os.fdopen(descriptor, "wb") as target, source.open("rb") as origin:
            shutil.copyfileobj(origin, target)
            target.flush()
            os.fsync(target.fileno())
        if overwrite:
            os.replace(temp, output)
        else:
            try:
                os.link(temp, output)
            except FileExistsError as exc:
                raise RecalcError("output appeared during write; refusing to overwrite") from exc
            temp.unlink()
    finally:
        try:
            temp.unlink()
        except FileNotFoundError:
            pass


def recalculate(
    source: Path, output: Path, timeout: int, overwrite: bool, trust_basis: str
) -> dict[str, object]:
    if trust_basis not in {"trusted", "verified-sandbox"}:
        raise RecalcError("trust basis must be 'trusted' or 'verified-sandbox'")
    source, output = validate_paths(source, output, overwrite)
    executable = shutil.which("soffice")
    if not executable:
        raise RecalcError("LibreOffice soffice is not installed")
    source_hash = sha256(source)
    hazards = archive_hazards(source)
    if hazards:
        raise RecalcError(
            "recalculation helper refuses active/external package features: " + ", ".join(hazards)
        )
    with tempfile.TemporaryDirectory(prefix="xlsx-recalc-") as directory:
        root = Path(directory)
        profile = root / "profile"
        converted = root / "converted"
        profile.mkdir()
        converted.mkdir()
        command = [
            executable,
            f"-env:UserInstallation={profile.resolve().as_uri()}",
            "--headless",
            "--nologo",
            "--nodefault",
            "--nolockcheck",
            "--norestore",
            "--convert-to",
            "xlsx",
            "--outdir",
            str(converted),
            str(source),
        ]
        completed = subprocess.run(command, capture_output=True, text=True, timeout=timeout, check=False)
        candidate = converted / source.name
        if completed.returncode != 0 or not candidate.is_file():
            raise RecalcError(
                f"LibreOffice failed ({completed.returncode}): {(completed.stderr or completed.stdout).strip()}"
            )
        summary = workbook_summary(candidate)
        source, output = validate_paths(source, output, overwrite)
        if sha256(source) != source_hash:
            raise RecalcError("source changed during recalculation; output not promoted")
        atomic_copy(candidate, output, overwrite)
    return {
        "status": "success" if summary["error_count"] == 0 else "errors_found",
        "source": str(source),
        "source_sha256": source_hash,
        "output": str(output),
        "output_sha256": sha256(output),
        "engine": executable,
        "isolated_profile": True,
        "source_modified": False,
        "trust_basis": trust_basis,
        "archive_hazards": hazards,
        **summary,
        "limitations": [
            "Sandbox confirmation is an operator assertion, not proof of isolation.",
            "No visible error token does not prove formula correctness or cross-engine compatibility.",
            "External links, queries, macros, and embedded objects were not intentionally refreshed or executed.",
        ],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    trust = parser.add_mutually_exclusive_group(required=True)
    trust.add_argument("--trusted-input", action="store_true")
    trust.add_argument("--sandbox-profile-confirmed", action="store_true")
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--timeout", type=int, default=60)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        trust_basis = "trusted" if args.trusted_input else "verified-sandbox"
        result = recalculate(
            args.source, args.output, max(1, args.timeout), args.overwrite, trust_basis
        )
    except (RecalcError, OSError, subprocess.TimeoutExpired) as exc:
        print(json.dumps({"status": "error", "error": str(exc)}))
        return 2
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
