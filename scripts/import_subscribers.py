#!/usr/bin/env python3
"""
Import email subscribers into data/subscribers.json

Usage examples:
  # From a plain text file (one email per line)
  python scripts/import_subscribers.py emails.txt

  # From a CSV (first column = email, optional header)
  python scripts/import_subscribers.py emails.csv --csv

  # Direct list of emails
  python scripts/import_subscribers.py --emails user1@example.com user2@example.com

  # Dry-run (show what would be added, no write)
  python scripts/import_subscribers.py emails.txt --dry-run

The script:
  - Validates basic email format
  - Deduplicates (case-insensitive)
  - Preserves existing subscribers
  - Updates the "updated" timestamp
  - Writes clean JSON back to data/subscribers.json
"""

import argparse
import csv
import json
import re
import sys
from datetime import date
from pathlib import Path

# Paths relative to repo root
REPO_ROOT = Path(__file__).resolve().parent.parent
SUBSCRIBERS_FILE = REPO_ROOT / "data" / "subscribers.json"

EMAIL_RE = re.compile(r"^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$")


def is_valid_email(email: str) -> bool:
    return bool(EMAIL_RE.match(email.strip()))


def load_subscribers() -> dict:
    if not SUBSCRIBERS_FILE.exists():
        return {
            "description": "Email subscriptions for the NEWS newsletter. Managed only within this GitHub repository. No external services.",
            "updated": str(date.today()),
            "subscribers": [],
        }
    with open(SUBSCRIBERS_FILE, encoding="utf-8") as f:
        return json.load(f)


def save_subscribers(data: dict) -> None:
    data["updated"] = str(date.today())
    with open(SUBSCRIBERS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def normalize(email: str) -> str:
    return email.strip().lower()


def collect_from_file(path: Path, is_csv: bool) -> list[str]:
    emails = []
    with open(path, encoding="utf-8", newline="") as f:
        if is_csv:
            reader = csv.reader(f)
            first = True
            for row in reader:
                if not row:
                    continue
                candidate = row[0].strip()
                # Skip header if it looks like one
                if first and candidate.lower() in {"email", "e-mail", "emails", "address"}:
                    first = False
                    continue
                first = False
                if candidate:
                    emails.append(candidate)
        else:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    emails.append(line)
    return emails


def main() -> None:
    parser = argparse.ArgumentParser(description="Import emails into data/subscribers.json")
    parser.add_argument("file", nargs="?", help="Text or CSV file containing emails")
    parser.add_argument("--csv", action="store_true", help="Treat input file as CSV (use first column)")
    parser.add_argument("--emails", nargs="+", help="Emails passed directly on the command line")
    parser.add_argument("--dry-run", action="store_true", help="Show changes without writing")
    args = parser.parse_args()

    if not args.file and not args.emails:
        parser.error("Provide either a file or --emails")

    new_emails: list[str] = []

    if args.emails:
        new_emails.extend(args.emails)

    if args.file:
        path = Path(args.file)
        if not path.exists():
            print(f"Error: file not found: {path}", file=sys.stderr)
            sys.exit(1)
        new_emails.extend(collect_from_file(path, args.csv))

    # Validate & normalize
    valid = []
    invalid = []
    for e in new_emails:
        if is_valid_email(e):
            valid.append(normalize(e))
        else:
            invalid.append(e)

    if invalid:
        print("Skipped invalid emails:")
        for e in invalid:
            print(f"  - {e}")

    data = load_subscribers()
    existing = {normalize(s) for s in data.get("subscribers", [])}

    to_add = sorted(set(valid) - existing)

    if not to_add:
        print("No new valid emails to add.")
        if args.dry_run:
            print("(dry-run — nothing written)")
        return

    print(f"Will add {len(to_add)} new subscriber(s):")
    for e in to_add:
        print(f"  + {e}")

    if args.dry_run:
        print("\n(dry-run — nothing written)")
        return

    data["subscribers"] = sorted(existing | set(to_add))
    save_subscribers(data)
    print(f"\nUpdated {SUBSCRIBERS_FILE}")
    print(f"Total subscribers now: {len(data['subscribers'])}")


if __name__ == "__main__":
    main()
