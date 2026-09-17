#!/usr/bin/env python3
"""Create a bounded static inventory of an agent skill or archive.

Target code is never executed and archive members are never extracted. Findings
are evidence and heuristics for manual review, not malware verdicts.
"""

from __future__ import annotations

import argparse
import bz2
import hashlib
import io
import json
import lzma
import os
from pathlib import Path, PurePosixPath
import re
import stat
import struct
import sys
import tarfile
import tempfile
from typing import Any, Iterable
import zipfile
import zlib
from urllib.parse import urlsplit


MAX_TEXT_BYTES = 1_000_000
MAX_FILE_BYTES = 64 * 1024 * 1024
MAX_PACKAGE_BYTES = 256 * 1024 * 1024
MAX_PACKAGE_ENTRIES = 10_000
MAX_TAR_EXPANDED_BYTES = 64 * 1024 * 1024
MAX_FINDINGS = 1_000
MAX_ARCHIVE_CONTAINER_BYTES = 500_000_000
MAX_ARCHIVE_MEMBERS = 100_000
MAX_ARCHIVE_MEMBER_RECORDS = 5_000
MAX_ARCHIVE_CENTRAL_DIRECTORY_BYTES = 100_000_000
MAX_ARCHIVE_MEMBER_BYTES = 250_000_000
MAX_ARCHIVE_UNCOMPRESSED_BYTES = 1_000_000_000
MAX_ARCHIVE_RATIO = 100.0
TEXT_EXTENSIONS = {
    ".md", ".txt", ".yaml", ".yml", ".json", ".toml", ".ini", ".cfg",
    ".py", ".js", ".mjs", ".cjs", ".ts", ".tsx", ".jsx", ".sh",
    ".bash", ".zsh", ".ps1", ".rb", ".go", ".rs", ".java", ".xml",
    ".html", ".css", ".sql", ".csv",
}
MANIFEST_NAMES = {
    "package.json", "package-lock.json", "pnpm-lock.yaml", "yarn.lock",
    "requirements.txt", "pyproject.toml", "poetry.lock", "pipfile",
    "pipfile.lock", "cargo.toml", "cargo.lock", "go.mod", "go.sum",
    "gemfile", "gemfile.lock", "composer.json", "composer.lock",
}
ARCHIVE_EXTENSIONS = {".zip", ".tar", ".gz", ".tgz", ".bz2", ".xz", ".7z", ".rar"}
BINARY_EXTENSIONS = {
    ".exe", ".dll", ".dylib", ".so", ".bin", ".class", ".jar", ".wasm",
    ".dmg", ".pkg", ".deb", ".rpm",
}
PATTERNS: list[tuple[str, str, str, re.Pattern[str]]] = [
    ("SC001", "high", "Potential destructive or privileged shell behavior", re.compile(
        r"\b(?:sudo|launchctl|systemctl|crontab)\b|\brm\s+(?:-[a-zA-Z]*r[a-zA-Z]*f|-[a-zA-Z]*f[a-zA-Z]*r)\b|\b(?:mkfs|shutdown|reboot)\b",
        re.I,
    )),
    ("SC002", "high", "Remote content may be piped to an interpreter", re.compile(
        r"(?:curl|wget)[^\n|]{0,300}\|\s*(?:sh|bash|zsh|python(?:3)?|node)\b",
        re.I,
    )),
    ("SC003", "medium", "Dynamic execution or subprocess capability", re.compile(
        r"\b(?:eval|exec)\s*\(|\bos\.system\s*\(|\bsubprocess\.(?:run|call|Popen)\s*\(|\bchild_process\b|\b(?:spawn|execFile)\s*\(",
        re.I,
    )),
    ("SC004", "medium", "Network client or outbound request capability", re.compile(
        r"\b(?:requests\.(?:get|post|put|patch|delete)|urllib\.request|httpx\.|fetch\s*\(|axios\.|curl\s|wget\s)",
        re.I,
    )),
    ("SC005", "medium", "Credential or environment access requires review", re.compile(
        r"(?:\.env\b|os\.environ|process\.env|keychain|credentials?|api[_-]?key|access[_-]?token|secret[_-]?key)",
        re.I,
    )),
    ("SC006", "high", "Instruction may attempt authority or reporting bypass", re.compile(
        r"(?:ignore|override|bypass)\s+(?:all\s+)?(?:previous|prior|system|developer|safety|approval)\s+(?:instructions?|rules?|checks?)|(?:do not|don't|never)\s+(?:tell|report|mention|disclose)\s+(?:the\s+)?user",
        re.I,
    )),
    ("SC007", "medium", "Broad or sensitive filesystem path requires review", re.compile(
        r"(?:/etc/|/var/|/Users/|/home/|~/(?:\.ssh|\.aws|\.config)|\$HOME|\bHOME\b)",
        re.I,
    )),
]
URL_RE = re.compile(r"https?://[^\s<>'\"`\])}]+", re.I)


class OutputPathError(Exception):
    """Raised when a report destination cannot be used without risking evidence."""


class Findings(list):
    """Bound report growth without concealing omitted findings."""
    omitted = 0

    def append(self, value: dict[str, Any]) -> None:
        if len(self) < MAX_FINDINGS:
            super().append(value)
        else:
            self.omitted += 1


def lexical_path(path: Path) -> Path:
    """Return an absolute normalized path without requiring the leaf to exist."""
    return Path(os.path.abspath(os.path.normpath(os.fspath(path))))


def resolved_path(path: Path) -> Path:
    try:
        return path.resolve(strict=False)
    except (OSError, RuntimeError) as exc:
        raise OutputPathError(f"cannot resolve path safely: {path}: {exc}") from exc


def is_within(candidate: Path, directory: Path) -> bool:
    return candidate == directory or directory in candidate.parents


def validate_output_path(
    output: Path,
    inputs: Iterable[Path],
    protected_directories: Iterable[Path] = (),
) -> Path:
    """Fail closed when an output could overwrite or mutate audit evidence."""
    output_lexical = lexical_path(output)
    output_resolved = resolved_path(output)
    try:
        output_stat = output.lstat()
    except FileNotFoundError:
        output_exists = False
    except OSError as exc:
        raise OutputPathError(f"cannot inspect output path: {output}: {exc}") from exc
    else:
        output_exists = True
        if not stat.S_ISREG(output_stat.st_mode):
            raise OutputPathError(f"output exists and is not a regular file: {output}")

    for source in inputs:
        if output_lexical == lexical_path(source) or output_resolved == resolved_path(source):
            raise OutputPathError(f"output aliases an input path: {output}")
        if output_exists and source.exists():
            try:
                if os.path.samefile(output, source):
                    raise OutputPathError(f"output aliases an input inode: {output}")
            except OutputPathError:
                raise
            except OSError as exc:
                raise OutputPathError(
                    f"cannot safely compare output and input paths: {output}: {exc}"
                ) from exc

    for directory in protected_directories:
        directory_lexical = lexical_path(directory)
        directory_resolved = resolved_path(directory)
        if is_within(output_lexical, directory_lexical) or is_within(output_resolved, directory_resolved):
            raise OutputPathError(
                f"output must be outside the audited directory: {directory}"
            )

    parent = output_lexical.parent
    if not parent.exists():
        raise OutputPathError(f"output directory does not exist: {parent}")
    if not parent.is_dir():
        raise OutputPathError(f"output parent is not a directory: {parent}")
    return output_resolved


def atomic_write_text(
    output: Path,
    payload: str,
    inputs: Iterable[Path],
    protected_directories: Iterable[Path] = (),
    *, replace: bool = False,
) -> None:
    """Create a private report without clobbering; replace only when explicit."""
    input_paths = tuple(inputs)
    protected_paths = tuple(protected_directories)
    destination = validate_output_path(output, input_paths, protected_paths)
    parent = destination.parent
    temp_path: Path | None = None
    try:
        file_descriptor, temp_name = tempfile.mkstemp(
            prefix=f".{output.name}.", suffix=".tmp", dir=parent
        )
        temp_path = Path(temp_name)
        with os.fdopen(file_descriptor, "w", encoding="utf-8", newline="") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        destination = validate_output_path(output, input_paths, protected_paths)
        if destination.parent != parent:
            raise OutputPathError(f"output directory changed during write: {output.parent}")
        if replace:
            os.replace(temp_path, destination)
            temp_path = None
        else:
            os.link(temp_path, destination)  # Atomic create-if-absent; no overwrite race.
    except OutputPathError:
        raise
    except OSError as exc:
        raise OutputPathError(f"unable to write output atomically: {output}: {exc}") from exc
    finally:
        if temp_path is not None:
            try:
                temp_path.unlink()
            except FileNotFoundError:
                pass
            except OSError:
                pass


def read_regular_snapshot(path: Path, limit: int) -> tuple[bytes, os.stat_result]:
    if not hasattr(os, "O_NOFOLLOW") or not hasattr(os, "O_NONBLOCK"):
        raise OSError("safe-open flags unavailable")
    descriptor = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    with os.fdopen(descriptor, "rb") as handle:
        before = os.fstat(handle.fileno())
        if not stat.S_ISREG(before.st_mode) or before.st_size > limit:
            raise ValueError("not a regular file within byte budget")
        raw = handle.read(limit + 1)
        after = os.fstat(handle.fileno())
        identity = lambda s: (s.st_dev, s.st_ino, s.st_size, s.st_mtime_ns, s.st_ctime_ns)
        if len(raw) > limit or identity(before) != identity(after) or len(raw) != before.st_size:
            raise ValueError("file changed or exceeded byte budget")
    return raw, before


def canonical_hash(records: list[dict[str, Any]]) -> str:
    canonical = json.dumps(records, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def canonical_manifest(files: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], str]:
    keys = ("path", "type", "bytes", "sha256", "mode", "executable", "target")
    records = [
        {key: item[key] for key in keys if key in item}
        for item in sorted(files, key=lambda value: (value.get("path", ""), value.get("type", "")))
    ]
    return records, canonical_hash(records)


def add_finding(
    findings: list[dict[str, Any]], finding_id: str, severity: str, title: str,
    file: str, evidence: str, *, confidence: str = "high", line: int | None = None,
    claim_status: str = "observed",
) -> None:
    finding: dict[str, Any] = {
        "id": finding_id,
        "severity": severity,
        "confidence": confidence,
        "claim_status": claim_status,
        "file": file,
        "evidence": evidence,
        "title": title,
    }
    if line is not None:
        finding["line"] = line
    findings.append(finding)


def relative_label(path: Path, root: Path) -> str:
    if root.is_file() or root.is_symlink():
        return path.name
    return path.relative_to(root).as_posix()


def iter_entries(root: Path, on_error=None) -> Iterable[Path]:
    if not stat.S_ISDIR(root.lstat().st_mode):
        yield root
        return
    pending = [root]
    while pending:
        current = pending.pop()
        try:
            with os.scandir(current) as entries:
                for entry in entries:
                    path = Path(entry.path)
                    yield path
                    if entry.name != ".git" and entry.is_dir(follow_symlinks=False):
                        pending.append(path)
        except OSError:
            if on_error:
                on_error(current)


def looks_text(path: Path, sample: bytes) -> bool:
    if b"\x00" in sample:
        return False
    if path.suffix.lower() in TEXT_EXTENSIONS or path.name.lower() in MANIFEST_NAMES:
        return True
    if not sample:
        return True
    printable = sum(byte in b"\t\n\r" or 32 <= byte < 127 for byte in sample)
    return printable / len(sample) > 0.85


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end < 0:
        return {}
    result: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line or line[:1].isspace():
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip("'\"")
    return result


def archive_path_issue(name: str) -> str | None:
    normalized = name.replace("\\", "/")
    if "\x00" in normalized:
        return "NUL byte in member name"
    path = PurePosixPath(normalized)
    if path.is_absolute() or normalized.startswith("//") or re.match(r"^[A-Za-z]:", normalized):
        return "absolute or drive-qualified member path"
    if ".." in path.parts:
        return "parent-traversal member path"
    return None


def safe_archive_member_record(
    name: str, entry_type: str, size: int, compressed_size: int | None = None,
    link_target: str | None = None,
) -> dict[str, Any]:
    record: dict[str, Any] = {"path": name, "type": entry_type, "bytes": size}
    if compressed_size is not None:
        record["compressed_bytes"] = compressed_size
        record["expansion_ratio"] = round(size / max(compressed_size, 1), 2)
    if link_target:
        record["link_target"] = link_target
    return record


def zip_directory_preflight(raw: bytes) -> tuple[int, int]:
    """Read the bounded EOCD trailer before zipfile allocates the directory."""
    with io.BytesIO(raw) as handle:
        size = len(raw)
        tail_size = min(size, 65_557)
        handle.seek(size - tail_size)
        tail = handle.read(tail_size)
    signature = b"PK\x05\x06"
    position = len(tail) - 22
    while position >= 0:
        if tail[position:position + 4] == signature:
            fields = struct.unpack_from("<4s4H2LH", tail, position)
            comment_length = fields[7]
            if position + 22 + comment_length == len(tail):
                disk_number, central_disk = fields[1], fields[2]
                entries_on_disk, total_entries = fields[3], fields[4]
                central_bytes = fields[5]
                if disk_number or central_disk or entries_on_disk != total_entries:
                    raise ValueError("multi-disk ZIP archives are not supported for bounded inspection")
                if total_entries == 0xFFFF or central_bytes == 0xFFFFFFFF:
                    raise ValueError("ZIP64 central-directory limits could not be established without deeper parsing")
                return total_entries, central_bytes
        position -= 1
    raise ValueError("valid ZIP end-of-central-directory record was not found")


def inspect_zip(raw: bytes, label: str, findings: list[dict[str, Any]]) -> dict[str, Any]:
    try:
        declared_members, central_directory_bytes = zip_directory_preflight(raw)
    except (OSError, ValueError, struct.error) as exc:
        add_finding(findings, "SC-ARCHIVE-PREFLIGHT", "high", "ZIP preflight could not establish safe bounds",
                    label, type(exc).__name__)
        return {
            "path": label,
            "format": "zip",
            "inspection_method": "bounded EOCD preflight only; members not read or extracted",
            "inspection_complete": False,
            "error": type(exc).__name__,
        }
    if declared_members > MAX_ARCHIVE_MEMBERS or central_directory_bytes > MAX_ARCHIVE_CENTRAL_DIRECTORY_BYTES:
        add_finding(findings, "SC-ARCHIVE-DIRECTORY-LIMIT", "high", "ZIP central directory exceeds inspection limits",
                    label, f"members={declared_members}, central_directory_bytes={central_directory_bytes}")
        return {
            "path": label,
            "format": "zip",
            "inspection_method": "bounded EOCD preflight only; members not read or extracted",
            "inspection_complete": False,
            "declared_members": declared_members,
            "central_directory_bytes": central_directory_bytes,
            "reason": "central-directory resource limit exceeded",
        }
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        infos = archive.infolist()
        selected = infos[:MAX_ARCHIVE_MEMBERS]
        inventory: list[dict[str, Any]] = []
        canonical_records: list[dict[str, Any]] = []
        total_uncompressed = 0
        total_compressed = 0
        risky_members = 0
        member_paths: set[str] = set()
        for info in selected:
            mode = info.external_attr >> 16
            file_type = stat.S_IFMT(mode) if mode else 0
            if info.is_dir() or file_type == stat.S_IFDIR:
                entry_type = "directory"
            elif file_type == stat.S_IFLNK:
                entry_type = "symlink"
            elif file_type not in (0, stat.S_IFREG):
                entry_type = "special"
            else:
                entry_type = "file"
            record = safe_archive_member_record(
                info.filename, entry_type, info.file_size, info.compress_size
            )
            record.update(mode=stat.S_IMODE(mode), crc32=info.CRC,
                          encrypted=bool(info.flag_bits & 1), compression_method=info.compress_type)
            canonical_records.append(record)
            if len(inventory) < MAX_ARCHIVE_MEMBER_RECORDS:
                inventory.append(record)
            total_uncompressed += info.file_size
            total_compressed += info.compress_size
            issue = archive_path_issue(getattr(info, "orig_filename", info.filename))
            if issue:
                risky_members += 1
                add_finding(findings, "SC-ARCHIVE-PATH", "high", issue.capitalize(), label,
                            f"archive member {info.filename!r}")
            normalized_path = info.filename.replace("\\", "/").casefold()
            if normalized_path in member_paths:
                risky_members += 1
                add_finding(findings, "SC-ARCHIVE-COLLISION", "medium", "Archive member path collision requires review",
                            label, "duplicate or case-insensitive member path; inspect member inventory")
            member_paths.add(normalized_path)
            if entry_type == "symlink":
                risky_members += 1
                add_finding(findings, "SC-ARCHIVE-SYMLINK", "high", "Archive contains a symlink",
                            label, f"archive member {info.filename!r}")
            elif entry_type == "special":
                risky_members += 1
                add_finding(findings, "SC-ARCHIVE-SPECIAL", "high", "Archive contains a special entry",
                            label, f"archive member {info.filename!r}, mode={oct(mode)}")
            ratio = info.file_size / max(info.compress_size, 1)
            if info.file_size > MAX_ARCHIVE_MEMBER_BYTES:
                risky_members += 1
                add_finding(findings, "SC-ARCHIVE-MEMBER-SIZE", "high", "Archive member exceeds size limit",
                            label, f"{info.filename!r}: {info.file_size} bytes")
            if info.file_size > 1_000_000 and ratio > MAX_ARCHIVE_RATIO:
                risky_members += 1
                add_finding(findings, "SC-ARCHIVE-RATIO", "high", "Archive member has excessive expansion ratio",
                            label, f"{info.filename!r}: {ratio:.2f}:1")

        complete = len(infos) <= MAX_ARCHIVE_MEMBERS and len(infos) == declared_members
        if len(infos) != declared_members:
            add_finding(findings, "SC-ARCHIVE-COUNT-MISMATCH", "high", "ZIP directory count disagrees with trailer",
                        label, f"trailer={declared_members}, parsed={len(infos)}")
        if len(infos) > MAX_ARCHIVE_MEMBERS:
            add_finding(findings, "SC-ARCHIVE-MEMBER-LIMIT", "high", "Archive member limit reached",
                        label, f"{len(infos)} declared members; inspected first {MAX_ARCHIVE_MEMBERS}")
        overall_ratio = total_uncompressed / max(total_compressed, 1)
        if total_uncompressed > MAX_ARCHIVE_UNCOMPRESSED_BYTES:
            add_finding(findings, "SC-ARCHIVE-TOTAL-SIZE", "high", "Archive declared expansion exceeds limit",
                        label, f"{total_uncompressed} bytes across inspected members")
        if total_uncompressed > 10_000_000 and overall_ratio > MAX_ARCHIVE_RATIO:
            add_finding(findings, "SC-ARCHIVE-TOTAL-RATIO", "high", "Archive has excessive aggregate expansion ratio",
                        label, f"{overall_ratio:.2f}:1 across inspected members")
        return {
            "path": label,
            "format": "zip",
            "inspection_method": "central-directory metadata only; members not read or extracted",
            "inspection_complete": complete,
            "declared_members": len(infos),
            "central_directory_bytes": central_directory_bytes,
            "members_inspected": len(selected),
            "member_inventory": inventory,
            "member_inventory_truncated": len(canonical_records) > len(inventory),
            "canonical_member_manifest_sha256": canonical_hash(sorted(canonical_records, key=lambda item: item["path"])),
            "declared_uncompressed_bytes_inspected": total_uncompressed,
            "declared_compressed_bytes_inspected": total_compressed,
            "aggregate_expansion_ratio": round(overall_ratio, 2),
            "risky_member_observations": risky_members,
        }


def tar_entry_type(member: tarfile.TarInfo) -> str:
    if member.isdir():
        return "directory"
    if member.isfile():
        return "file"
    if member.issym():
        return "symlink"
    if member.islnk():
        return "hardlink"
    return "special"


def bounded_tar_bytes(raw: bytes) -> bytes:
    """Bound decompression before tarfile can interpret PAX/longname headers."""
    chunks = []
    expanded = 0
    while raw:
        if raw.startswith(b"\x1f\x8b"):
            decoder = zlib.decompressobj(31)
        elif raw.startswith(b"BZh"):
            decoder = bz2.BZ2Decompressor()
        elif raw.startswith(b"\xfd7zXZ\x00"):
            decoder = lzma.LZMADecompressor(memlimit=64 * 1024 * 1024)
        else:
            if chunks:
                raise ValueError("unsupported trailing compressed data")
            if len(raw) > MAX_TAR_EXPANDED_BYTES:
                raise ValueError("expanded tar byte limit")
            return raw
        chunk = decoder.decompress(raw, MAX_TAR_EXPANDED_BYTES - expanded + 1)
        expanded += len(chunk)
        if expanded > MAX_TAR_EXPANDED_BYTES or not decoder.eof:
            raise ValueError("expanded tar limit or incomplete stream")
        chunks.append(chunk)
        raw = decoder.unused_data
    return b"".join(chunks)


def inspect_tar(raw: bytes, label: str, findings: list[dict[str, Any]]) -> dict[str, Any]:
    inventory: list[dict[str, Any]] = []
    canonical_records: list[dict[str, Any]] = []
    total_uncompressed = 0
    risky_members = 0
    complete = True
    with tarfile.open(fileobj=io.BytesIO(bounded_tar_bytes(raw)), mode="r:") as archive:
        for index, member in enumerate(archive):
            if index >= MAX_ARCHIVE_MEMBERS:
                complete = False
                add_finding(findings, "SC-ARCHIVE-MEMBER-LIMIT", "high", "Archive member limit reached",
                            label, f"inspection stopped after {MAX_ARCHIVE_MEMBERS} members")
                break
            entry_type = tar_entry_type(member)
            link_target = member.linkname if entry_type in {"symlink", "hardlink"} else None
            record = safe_archive_member_record(member.name, entry_type, member.size, link_target=link_target)
            record["mode"] = member.mode
            canonical_records.append(record)
            if len(inventory) < MAX_ARCHIVE_MEMBER_RECORDS:
                inventory.append(record)
            total_uncompressed += member.size
            issue = archive_path_issue(member.name)
            if issue:
                risky_members += 1
                add_finding(findings, "SC-ARCHIVE-PATH", "high", issue.capitalize(), label,
                            f"archive member {member.name!r}")
            if entry_type in {"symlink", "hardlink"}:
                risky_members += 1
                add_finding(findings, "SC-ARCHIVE-LINK", "high", f"Archive contains a {entry_type}",
                            label, f"{member.name!r} -> {member.linkname!r}")
                target_issue = archive_path_issue(member.linkname)
                if target_issue:
                    add_finding(findings, "SC-ARCHIVE-LINK-TARGET", "high", "Archive link target is unsafe",
                                label, f"{member.name!r} -> {member.linkname!r}: {target_issue}")
            elif entry_type == "special":
                risky_members += 1
                add_finding(findings, "SC-ARCHIVE-SPECIAL", "high", "Archive contains a special entry",
                            label, f"archive member {member.name!r}, type={member.type!r}")
            if member.size > MAX_ARCHIVE_MEMBER_BYTES:
                risky_members += 1
                add_finding(findings, "SC-ARCHIVE-MEMBER-SIZE", "high", "Archive member exceeds size limit",
                            label, f"{member.name!r}: {member.size} bytes")
            if total_uncompressed > MAX_ARCHIVE_UNCOMPRESSED_BYTES:
                complete = False
                add_finding(findings, "SC-ARCHIVE-TOTAL-SIZE", "high", "Archive declared expansion exceeds limit",
                            label, f"inspection stopped after {total_uncompressed} declared bytes")
                break
    outer_bytes = len(raw)
    overall_ratio = total_uncompressed / max(outer_bytes, 1)
    if total_uncompressed > 10_000_000 and overall_ratio > MAX_ARCHIVE_RATIO:
        add_finding(findings, "SC-ARCHIVE-TOTAL-RATIO", "high", "Archive has excessive aggregate expansion ratio",
                    label, f"{overall_ratio:.2f}:1 for inspected headers")
    return {
        "path": label,
        "format": "tar",
        "inspection_method": "tar header metadata only; members not extracted",
        "inspection_complete": complete,
        "members_inspected": len(canonical_records),
        "member_inventory": inventory,
        "member_inventory_truncated": len(canonical_records) > len(inventory),
        "canonical_member_manifest_sha256": canonical_hash(sorted(canonical_records, key=lambda item: item["path"])),
        "declared_uncompressed_bytes_inspected": total_uncompressed,
        "container_bytes": outer_bytes,
        "aggregate_expansion_ratio": round(overall_ratio, 2),
        "risky_member_observations": risky_members,
    }


def inspect_archive(raw: bytes, label: str, findings: list[dict[str, Any]]) -> dict[str, Any]:
    size = len(raw)
    if size > MAX_ARCHIVE_CONTAINER_BYTES:
        add_finding(findings, "SC-ARCHIVE-CONTAINER-LIMIT", "high", "Archive metadata inspection skipped at size limit",
                    label, f"{size} bytes exceeds {MAX_ARCHIVE_CONTAINER_BYTES}")
        return {
            "path": label,
            "format": "unknown",
            "inspection_method": "skipped before archive parsing",
            "inspection_complete": False,
            "reason": "container byte limit exceeded",
        }
    try:
        if zipfile.is_zipfile(io.BytesIO(raw)):
            return inspect_zip(raw, label, findings)
        return inspect_tar(raw, label, findings)
    except (OSError, ValueError, tarfile.TarError, zipfile.BadZipFile, EOFError, zlib.error, lzma.LZMAError) as exc:
        add_finding(findings, "SC-ARCHIVE-READ", "high", "Archive metadata could not be inspected",
                    label, type(exc).__name__)
        return {
            "path": label,
            "format": "unreadable",
            "inspection_method": "metadata parse attempted; members not extracted",
            "inspection_complete": False,
            "error": type(exc).__name__,
        }


def scan(root: Path) -> dict[str, Any]:
    files: list[dict[str, Any]] = []
    findings = Findings()
    archives: list[dict[str, Any]] = []
    content_review_queue: list[dict[str, Any]] = []
    urls: set[str] = set()
    manifests: list[str] = []
    total_bytes = 0
    bytes_read = 0
    inventory_complete = True
    hash_inventory_complete = True
    regular_count = 0
    text_files_scanned = 0
    skill_frontmatter: dict[str, str] = {}

    def gap(label: str, reason: str, record=None) -> None:
        content_review_queue.append({
            "path": label, "reason": reason, "status": "unresolved",
            "required_action": "bounded read-only review or retain explicit blocking coverage gap",
            **({key: record[key] for key in ("bytes", "sha256") if key in record} if record else {}),
        })

    def walk_error(path: Path) -> None:
        nonlocal inventory_complete
        inventory_complete = False
        gap(relative_label(path, root), "directory could not be enumerated")

    for index, entry in enumerate(iter_entries(root, walk_error)):
        if index >= MAX_PACKAGE_ENTRIES:
            inventory_complete = False
            gap(".", "package entry limit reached; remaining paths are not inventoried")
            break
        label = relative_label(entry, root)
        if entry.name == ".git":
            inventory_complete = False
            gap(label, "Git metadata excluded; review any relevant hooks/configuration separately")
            continue
        try:
            info = entry.lstat()
            mode = info.st_mode
        except OSError:
            inventory_complete = False
            gap(label, "entry metadata unreadable")
            add_finding(findings, "SC-READ", "medium", "Entry could not be inspected",
                        label, "metadata unavailable")
            continue

        if stat.S_ISLNK(mode):
            try:
                target = os.readlink(entry)
            except OSError:
                inventory_complete = False
                gap(label, "symlink target unreadable")
                continue
            escapes = Path(target).is_absolute()
            if not escapes:
                try:
                    resolved = (entry.parent / target).resolve()
                    escapes = root.is_dir() and root.resolve() not in (resolved, *resolved.parents)
                except (OSError, RuntimeError):
                    escapes = True
            files.append({"path": label, "type": "symlink", "target": target})
            gap(label, "symlink content not followed; validate target identity and required scope")
            add_finding(findings, "SC-SYMLINK", "high" if escapes else "low",
                        "Symlink escapes package root" if escapes else "Package contains a symlink",
                        label, target)
            continue
        if stat.S_ISDIR(mode):
            files.append({"path": label, "type": "directory", "mode": stat.S_IMODE(mode)})
            continue
        if not stat.S_ISREG(mode):
            files.append({"path": label, "type": "special"})
            gap(label, "special filesystem entry not read")
            add_finding(findings, "SC-SPECIAL", "high", "Package contains a special filesystem entry",
                        label, "non-regular, non-directory entry")
            continue

        regular_count += 1
        size = info.st_size
        total_bytes += size
        executable = bool(mode & (stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH))
        suffix = entry.suffix.lower()
        record = {
            "path": label,
            "type": "file",
            "bytes": size,
            "mode": stat.S_IMODE(mode),
            "executable": executable,
        }
        files.append(record)
        try:
            if size > MAX_FILE_BYTES or size + 1 > MAX_PACKAGE_BYTES - bytes_read:
                raise ValueError("byte budget exceeded")
            # Reserve before opening: failed/changed reads also consume the total budget.
            bytes_read += size + 1
            raw, snapshot = read_regular_snapshot(entry, size)
            if (snapshot.st_dev, snapshot.st_ino, snapshot.st_mtime_ns, snapshot.st_ctime_ns) != (info.st_dev, info.st_ino, info.st_mtime_ns, info.st_ctime_ns):
                raise ValueError("entry changed before snapshot")
        except (OSError, ValueError):
            hash_inventory_complete = False
            gap(label, "unreadable, changed, unsupported safe-open platform, or byte budget exceeded", record)
            add_finding(findings, "SC-READ", "medium", "Regular file was not fully inspected", label,
                        "content/hash unavailable; inspect coverage queue")
            continue
        digest = hashlib.sha256(raw).hexdigest()
        record["sha256"] = digest
        if entry.name.lower() in MANIFEST_NAMES:
            manifests.append(label)
        archive_like = (suffix in ARCHIVE_EXTENSIONS or suffix == ".jar" or
                        raw.startswith((b"PK\x03\x04", b"PK\x05\x06", b"\x1f\x8b", b"BZh", b"\xfd7zXZ\x00")) or
                        raw[257:262] == b"ustar")
        if archive_like:
            archives.append(inspect_archive(raw, label, findings))
            gap(label, "archive member contents not reviewed; metadata inspection is separate", record)
        if suffix in BINARY_EXTENSIONS:
            add_finding(findings, "SC-BINARY", "medium", "Opaque executable or binary artifact",
                        label, suffix)
        if executable:
            add_finding(findings, "SC-EXEC", "low", "Executable file requires manual review",
                        label, "executable permission bit set")

        if archive_like:
            continue
        is_text = looks_text(entry, raw[:8192])
        if size > MAX_TEXT_BYTES:
            content_review_queue.append({
                "path": label,
                "bytes": size,
                "sha256": digest,
                "appears_text": is_text,
                "reason": f"content pattern scan limited to files at or below {MAX_TEXT_BYTES} bytes",
                "required_action": "perform bounded read-only chunked/manual review or record why opaque content is accepted",
                "status": "unresolved",
            })
            add_finding(findings, "SC-CONTENT-SKIPPED", "medium",
                        "File content requires separate bounded review", label,
                        f"{size} bytes; SHA-256 {digest}")
            continue
        if not is_text:
            gap(label, "opaque/non-text content was not pattern scanned", record)
            continue
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            gap(label, "non-UTF-8 content requires an appropriate bounded decoder", record)
            continue
        text_files_scanned += 1
        for match in URL_RE.finditer(text):
            try:
                parsed = urlsplit(match.group())
                if parsed.hostname:
                    # Origins only: omit userinfo, path, query and fragment (may contain secrets).
                    host = parsed.hostname
                    if ":" in host:
                        host = f"[{host}]"
                    urls.add(f"{parsed.scheme}://{host}" + (f":{parsed.port}" if parsed.port else ""))
            except ValueError:
                pass  # Regex URL candidates are not validation or complete endpoint discovery.
        if label == "SKILL.md":
            skill_frontmatter = {key: "present; value intentionally omitted" for key in parse_frontmatter(text)}
        for rule_id, severity, title, pattern in PATTERNS:
            for match_index, match in enumerate(pattern.finditer(text)):
                if match_index >= 10:
                    findings.omitted += 1
                    continue
                line = text.count("\n", 0, match.start()) + 1
                snippet = "pattern matched; inspect original line privately (source text omitted)"
                add_finding(findings, rule_id, severity, title, label, snippet,
                            confidence="low", line=line, claim_status="observed")

    # This flat frontmatter hint is not a YAML parser or catalog-conformance check.

    severity_order = {"critical": 0, "high": 1, "medium": 2, "low": 3, "informational": 4}
    findings.sort(key=lambda item: (severity_order.get(item["severity"], 99), item.get("file", ""), item.get("line", 0)))
    manifest_records, manifest_digest = canonical_manifest(files)
    archive_incomplete = (not inventory_complete or not hash_inventory_complete or
                          any(not item.get("inspection_complete", False) for item in archives))
    return {
        "target": str(root.resolve()),
        "method": "read-only static heuristics and non-extracting archive metadata inspection; target code was not executed",
        "claim_status_vocabulary": ["observed", "inferred", "unknown"],
        "claims": [
            {"claim": "reported filesystem hashes and metadata", "status": "observed"},
            {"claim": "risk implications of heuristic pattern matches", "status": "inferred"},
            {"claim": "runtime safety and absence of malicious behavior", "status": "unknown"},
        ],
        "limits": [
            f"At most {MAX_PACKAGE_ENTRIES} entries, {MAX_FILE_BYTES} bytes per file and {MAX_PACKAGE_BYTES} bytes read per package.",
            f"TAR decompression is bounded to {MAX_TAR_EXPANDED_BYTES} bytes before metadata parsing; XZ decoder memory is capped at 64 MiB.",
            "Use a stable private snapshot: final symlinks are not followed, but parent-directory races are not sandboxed.",
            "Git metadata is excluded and reported as a coverage gap. Report paths and origin hosts remain private/untrusted metadata.",
            "URL origins omit userinfo/path/query/fragment; this is not complete endpoint analysis or a general secret scrubber.",
            "Frontmatter reports top-level key hints only, not validated YAML or activation semantics.",
            f"Content pattern scanning is limited to files at or below {MAX_TEXT_BYTES} bytes.",
            f"Archive metadata inspection stops at {MAX_ARCHIVE_MEMBERS} members, a {MAX_ARCHIVE_CENTRAL_DIRECTORY_BYTES}-byte ZIP directory, or {MAX_ARCHIVE_UNCOMPRESSED_BYTES} declared bytes.",
            "Archive members are not extracted or executed; nested member contents are not recursively scanned.",
            "Pattern matches require manual validation and may be benign.",
            "No malware-absence or runtime-safety claim is made.",
        ],
        "summary": {
            "regular_files": regular_count,
            "total_bytes": total_bytes,
            "text_files_pattern_scanned": text_files_scanned,
            "content_review_queue": len(content_review_queue),
            "archives": len(archives),
            "archives_with_incomplete_member_inspection": sum(
                not item.get("inspection_complete", False) for item in archives
            ),
            "findings": len(findings) + findings.omitted,
            "findings_omitted": findings.omitted,
            "manifests": len(manifests),
            "urls": len(urls),
        },
        "coverage": {
            "inventory_complete": inventory_complete,
            "hash_inventory_complete": hash_inventory_complete and inventory_complete,
            "content_pattern_scan_complete": not content_review_queue and inventory_complete,
            "findings_display_complete": not findings.omitted,
            "archive_metadata_inspection_complete": not archive_incomplete,
            "unresolved_content_review_paths": [item["path"] for item in content_review_queue],
        },
        "canonical_manifest_algorithm": "v2: SHA-256 of sorted UTF-8 canonical JSON records (path/type/bytes/hash/mode/executable/target); compare only matching algorithms and complete inventories",
        "canonical_manifest_sha256": manifest_digest,
        "canonical_manifest_entries": len(manifest_records),
        "skill_frontmatter": skill_frontmatter,
        "manifests": sorted(manifests),
        "urls": sorted(urls),
        "files": files,
        "archives": archives,
        "content_review_queue": content_review_queue,
        "findings": findings,
    }


def compare(current: dict[str, Any], baseline: dict[str, Any]) -> dict[str, Any]:
    new = {item["path"]: item for item in canonical_manifest(current["files"])[0]}
    old = {item["path"]: item for item in canonical_manifest(baseline["files"])[0]}
    unknown = {path for mapping in (new, old) for path, item in mapping.items()
               if item.get("type") == "file" and not item.get("sha256")}
    complete = all(report["coverage"].get("hash_inventory_complete", False) for report in (current, baseline))
    return {
        "comparison_complete": complete and current["canonical_manifest_algorithm"] == baseline["canonical_manifest_algorithm"],
        "unknown": sorted(unknown),
        "note": "Compare content, type, mode and link target; partial inventories cannot establish absence or unchanged content.",
        "added": sorted(set(new) - set(old)),
        "removed": sorted(set(old) - set(new)),
        "changed": sorted(path for path in set(new) & set(old) - unknown if new[path] != old[path]),
        "unchanged": sorted(path for path in set(new) & set(old) - unknown if new[path] == old[path]),
        "canonical_manifest_changed": current["canonical_manifest_sha256"] != baseline["canonical_manifest_sha256"],
        "current_canonical_manifest_sha256": current["canonical_manifest_sha256"],
        "baseline_canonical_manifest_sha256": baseline["canonical_manifest_sha256"],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__, epilog=
        "Python 3.10+, no dependencies/network. Exit 0: scan completed (not security approval); "
        "1: coverage gaps or omitted findings; 2: input/output failure. "
        "Use a private immutable snapshot. Report metadata remains sensitive/untrusted.")
    parser.add_argument("target", type=Path, help="File or directory to inspect without executing")
    parser.add_argument("--baseline", type=Path, help="Known-good file or directory for canonical/hash comparison")
    parser.add_argument(
        "--output", type=Path,
        help="Create a private JSON report outside audited directories; input aliases are refused",
    )
    parser.add_argument("--replace", action="store_true", help="Explicitly replace an existing regular report; requires --output")
    parser.add_argument("--pretty", action="store_true", help="Indent JSON output")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.replace and not args.output:
        print("error: --replace requires --output", file=sys.stderr)
        return 2
    if not args.target.exists() and not args.target.is_symlink():
        print(f"error: target does not exist: {args.target}", file=sys.stderr)
        return 2
    if args.baseline and not args.baseline.exists() and not args.baseline.is_symlink():
        print(f"error: baseline does not exist: {args.baseline}", file=sys.stderr)
        return 2
    inputs = [args.target] + ([args.baseline] if args.baseline else [])
    protected_directories = [path for path in inputs if path.is_dir()]
    if args.output:
        try:
            validate_output_path(args.output, inputs, protected_directories)
            if args.output.exists() and not args.replace:
                raise OutputPathError("report exists; choose a new path or explicitly authorize --replace")
        except OutputPathError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 2
    try:
        report = scan(args.target)
        baseline_report = None
        if args.baseline:
            baseline_report = scan(args.baseline)
            report["baseline"] = str(args.baseline.resolve())
            report["baseline_coverage"] = baseline_report["coverage"]
            report["baseline_summary"] = baseline_report["summary"]
            report["baseline_content_review_queue"] = baseline_report["content_review_queue"]
            report["comparison"] = compare(report, baseline_report)
    except (OSError, ValueError, RuntimeError):
        print("error: input inventory unavailable; use a stable accessible snapshot", file=sys.stderr)
        return 2
    payload = json.dumps(report, indent=2 if args.pretty else None, sort_keys=True) + "\n"
    if args.output:
        try:
            validate_output_path(args.output, inputs, protected_directories)
            atomic_write_text(args.output, payload, inputs, protected_directories, replace=args.replace)
        except OutputPathError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 2
    else:
        sys.stdout.write(payload)
    reports = [report] + ([baseline_report] if baseline_report else [])
    complete_fields = ("inventory_complete", "hash_inventory_complete", "content_pattern_scan_complete",
                       "archive_metadata_inspection_complete", "findings_display_complete")
    return 0 if all(item["coverage"][field] for item in reports for field in complete_fields) else 1


if __name__ == "__main__":
    raise SystemExit(main())
