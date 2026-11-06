"""Dry-run-only demonstration of a packaged console-script entry point."""
import argparse
import csv
from pathlib import Path
import sys

def main(argv=None):
    parser = argparse.ArgumentParser(prog="clean-orders")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    if not args.dry_run:
        parser.error("this educational CLI supports only --dry-run")
    try:
        with args.input.open("r", encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
    except (OSError, UnicodeError, csv.Error) as exc:
        print("Cannot read CSV: " + type(exc).__name__, file=sys.stderr)
        return 2
    if not rows or not all("order_id" in row for row in rows):
        print("Input must contain order_id column and at least one data row", file=sys.stderr)
        return 2
    print(f"DRY_RUN {len(rows)} orders")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
