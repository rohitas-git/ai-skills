#!/usr/bin/env python3
"""Append one private, spreadsheet-safe decision row. Adapted from pstack log.sh (MIT)."""
import argparse
from datetime import datetime, timezone
import fcntl
import os
from pathlib import Path
import stat

HEADER = 'ts\tphase\tdecision\twhy\tevidence\tresult\n'


def clean(value):
    value = value.replace('\t', ' ').replace('\r', ' ').replace('\n', ' ')
    return "'" + value if value.lstrip().startswith(('=', '+', '-', '@')) else value


def append_row(path, cells):
    path = Path(os.path.abspath(path))
    if path.is_symlink():
        raise ValueError('log file must not be a symlink')
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor = os.open(path, os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_NOFOLLOW | os.O_NONBLOCK, 0o600)
    with os.fdopen(descriptor, 'r+', encoding='utf-8', newline='') as handle:
        fcntl.flock(handle, fcntl.LOCK_EX)
        if not stat.S_ISREG(os.fstat(handle.fileno()).st_mode):
            raise ValueError('log must be a regular file')
        first = handle.readline()
        if first and first != HEADER:
            raise ValueError('existing file is not a decision log; nothing appended')
        handle.seek(0, os.SEEK_END)
        if not first:
            handle.write(HEADER)
        timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
        handle.write('\t'.join([timestamp, *map(clean, cells)]) + '\n')
        handle.flush()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('logfile', type=Path)
    for cell in ['phase', 'decision', 'why', 'evidence', 'result']:
        parser.add_argument(cell)
    args = parser.parse_args()
    try:
        append_row(args.logfile, [getattr(args, cell) for cell in ['phase', 'decision', 'why', 'evidence', 'result']])
    except (OSError, ValueError) as error:
        parser.exit(2, f'{error}\n')


if __name__ == '__main__':
    main()
