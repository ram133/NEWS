# NEWS

**Free AI News Newsletter**  
Curated AI updates. Forever free. Supported by product advertisements.

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![Free Forever](https://img.shields.io/badge/price-free%20forever-brightgreen.svg)]()
[![GitHub only](https://img.shields.io/badge/infra-GitHub%20only-blue.svg)]()

---

## Latest Issue

**[Issue #001 — October 27, 2026](issues/001.md)**  
Anthropic S-1 filing, OpenAI GPT-6.1 Terra price cut, security concerns, and major compute financing.

---

## What this is

A clean, no-nonsense AI news newsletter.

- Short, high-signal updates (no fluff)
- Focused on real developments that matter
- Completely free to read forever
- Funded only by relevant product advertisements inside each issue

No paywalls. No premium tiers. No spam.

---

## Sign up (Free) — GitHub only

This project uses **only GitHub**. No external form services, no third-party databases.

Email subscriptions are stored in a simple JSON file that acts as the database:

**[`data/subscribers.json`](data/subscribers.json)**

### How to subscribe

1. Open a new [GitHub Issue](https://github.com/ram133/NEWS/issues/new?title=Subscribe&body=Email%3A%20%0A%0A(please%20include%20your%20email%20address)) with the title **Subscribe** and put your email address in the body.
2. The maintainer will add your email to `data/subscribers.json`.
3. Alternatively, star or watch this repository to receive GitHub notifications when new issues are published.

Only your email address is stored. You can unsubscribe anytime by opening another issue or replying to a newsletter.

---

## Import subscribers (for maintainer)

You can bulk-import emails into the JSON database with the included script.

### Quick start

```bash
# From a plain text file (one email per line)
python scripts/import_subscribers.py emails.txt

# From a CSV (first column = email)
python scripts/import_subscribers.py emails.csv --csv

# Directly on the command line
python scripts/import_subscribers.py --emails user1@example.com user2@example.com

# Preview first (no changes written)
python scripts/import_subscribers.py emails.txt --dry-run
```

See `data/import_example.txt` for a ready-to-use sample file.

The script automatically:
- Validates basic email format
- Deduplicates (case-insensitive)
- Keeps existing subscribers
- Updates the `updated` date in the JSON

After running, commit the updated `data/subscribers.json`.

---

## Advertisement policy

- Only relevant AI / developer / productivity tools
- Clearly labeled as advertisements
- Never more than a small portion of the issue
- We only accept products we would actually consider using ourselves

This keeps the newsletter free for readers while remaining sustainable.

---

## Repository structure

```
NEWS/
├── data/
│   ├── subscribers.json     # JSON database of email subscriptions
│   └── import_example.txt   # Sample file for bulk import
├── scripts/
│   └── import_subscribers.py  # Import tool
├── issues/                  # Published newsletter issues
├── templates/               # Issue templates
├── ads/                     # Ad guidelines
├── website/                 # Landing page
└── README.md
```

---

## Credits

Built and maintained with **Grok** (xAI) as primary collaborator.  
This is an independent project — not affiliated with xAI.

---

**Star this repo** if you want to follow the free AI newsletter from the beginning.
