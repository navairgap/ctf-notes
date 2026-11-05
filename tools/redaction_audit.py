#!/usr/bin/env python3
"""Audit local CTF notes for common secret patterns without printing secret values."""
from __future__ import annotations

import argparse
import os
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

SKIP_DIRS = {".git", ".venv", "venv", "__pycache__", "node_modules"}
RULES: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("github-token", re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b")),
    ("aws-access-key-id", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("bearer-authorization", re.compile(r"(?im)^\s*authorization\s*:\s*bearer\s+\S+")),
    ("private-key-marker", re.compile(
        r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"
    )),
    ("credential-assignment", re.compile(
        r"""(?i)\b(?:password|passwd|api[_-]?key|access[_-]?token|secret)\b"""
        r"""\s*[:=]\s*["']?([A-Za-z0-9/+=._-]{12,})"""
    )),
)
PLACEHOLDERS = {
    "REPLACE_ME", "CHANGE_ME", "YOUR_TOKEN_HERE", "EXAMPLE_VALUE",
    "example-token", "not-a-real-token", "dummy-secret",
}


@dataclass(frozen=True, order=True)
class Finding:
    path: str
    line: int
    rule: str


def _has_real_value(match: re.Match[str]) -> bool:
    """Ignore obvious placeholders; never return or store captured secret text."""
    groups = match.groups()
    value = groups[-1] if groups else match.group(0)
    return value not in PLACEHOLDERS and not value.lower().startswith(
        ("replace_", "example_", "your_", "dummy_")
    )


def scan_file(path: Path, root: Path, max_bytes: int = 2 * 1024 * 1024) -> list[Finding]:
    """Inspect one bounded UTF-8 text file and return line-level rule names only."""
    try:
        if path.is_symlink() or not path.is_file() or path.stat().st_size > max_bytes:
            return []
        raw = path.read_bytes()
        if b"\0" in raw:
            return []
        text = raw.decode("utf-8")
    except (OSError, UnicodeError):
        return []

    findings: set[Finding] = set()
    relative = path.relative_to(root).as_posix()
    for line_number, line in enumerate(text.splitlines(), 1):
        for rule, pattern in RULES:
            for match in pattern.finditer(line):
                if rule != "credential-assignment" or _has_real_value(match):
                    findings.add(Finding(relative, line_number, rule))
    return sorted(findings)


def scan_tree(root: Path, max_bytes: int = 2 * 1024 * 1024) -> list[Finding]:
    root = root.resolve()
    if not root.is_dir():
        raise ValueError("scan root must be a directory")
    found: list[Finding] = []
    for directory, dirs, files in os.walk(root, followlinks=False):
        base = Path(directory)
        dirs[:] = [name for name in dirs
                   if name not in SKIP_DIRS and not (base / name).is_symlink()]
        for filename in files:
            candidate = base / filename
            found.extend(scan_file(candidate, root, max_bytes))
    return sorted(set(found))


def positive_int(value: str) -> int:
    try:
        number = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("max bytes must be a positive integer") from exc
    if number < 1:
        raise argparse.ArgumentTypeError("max bytes must be a positive integer")
    return number


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".", help="directory to audit")
    parser.add_argument("--max-bytes", type=positive_int, default=2 * 1024 * 1024,
                        help="skip files larger than this many bytes")
    args = parser.parse_args(argv)
    try:
        findings = scan_tree(Path(args.root), args.max_bytes)
    except (OSError, ValueError) as exc:
        print(f"redaction-audit: {exc}", file=sys.stderr)
        return 2

    for finding in findings:
        # Do not include matched text or surrounding source in the report.
        print(f"{finding.path}:{finding.line}: {finding.rule}")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
