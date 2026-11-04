# NEWS

**Free AI News Newsletter**  
High-signal AI updates. Forever free. No spam. No paywall.

[![Live Site](https://img.shields.io/badge/Live_Site-ram133.github.io%2FNEWS-22d3ee)](https://ram133.github.io/NEWS/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> Curated AI news that actually matters — powered by pure GitHub + JSON.

**Live site:** https://ram133.github.io/NEWS/  
**Repo:** https://github.com/ram133/NEWS

---

## Latest Issue

**Issue #008 — November 04, 2026**  
ChatGPT search volume reaches ~20% of Google’s, AMD posts record AI-driven quarter, Anthropic open-sources FlashProve (model provenance), Google ties school Search access to AI tools.

→ [Read Issue #008](issues/008.md)

---

## What this is

A clean, no-nonsense AI news newsletter.

- Short, high-signal updates (no fluff)
- Focused on real developments that matter
- Completely free to read forever
- Funded only by relevant product advertisements inside each issue

No paywalls. No premium tiers. No spam.

---

## Automatic publishing (6 AM ChST every day)

A free GitHub Action runs every day at **6:00 AM ChST (Guam time)**:

- Pulls high-signal public stories (Hacker News AI filter + free sources)
- Generates a new markdown issue in `/issues/`
- Commits and publishes it automatically

No paid services. No external APIs that can disappear or start charging.

You can also trigger it manually from the **Actions** tab → **Daily AI News Publisher** → **Run workflow**.

---

## Sign up (Free) — GitHub only

This project uses **only GitHub**. No external form services, no third-party databases.

Email subscriptions are stored in a simple JSON file that acts as the database:

**`data/subscribers.json`**

### How to subscribe (easiest)

**One click:** [Watch this repository](https://github.com/ram133/NEWS/subscription)  
You will receive a GitHub notification every time a new issue is published.

### Email option

Use the form on the [live site](https://ram133.github.io/NEWS/#subscribe) or open a Subscribe issue.

Only your email address is stored. You can unsubscribe anytime.

---

## Import emails (bulk)

You can import multiple email addresses into `data/subscribers.json` for free.

### Method 1 — Pending file (easiest for bulk)

1. Edit `data/pending_import.txt`
2. Add one email per line (lines starting with `#` are ignored)
3. Commit and push
4. Go to **Actions** → **Import Subscribers** → **Run workflow**

The Action will process the file, add valid new emails, and clear the pending file.

### Method 2 — Direct in the Action

1. Go to **Actions** → **Import Subscribers** → **Run workflow**
2. Paste emails (one per line) into the `emails` input box
3. Run

### Method 3 — Local script

```bash
# From a text file (one email per line)
python scripts/import_subscribers.py emails.txt

# From a CSV (first column = email)
python scripts/import_subscribers.py emails.csv --csv

# Direct list
python scripts/import_subscribers.py --emails user1@example.com user2@example.com

# Dry-run (preview only)
python scripts/import_subscribers.py emails.txt --dry-run
```

The script validates format, deduplicates (case-insensitive), and preserves existing subscribers.

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
├── .github/workflows/
│   ├── daily-news.yml         # Runs every day at 6 AM ChST
│   └── import-subscribers.yml # Bulk email import
├── data/
│   ├── subscribers.json       # JSON database of email subscriptions
│   ├── pending_import.txt     # Drop emails here for bulk import
│   └── last_run.json          # Tracks last auto-publish
├── issues/                    # Published newsletter issues
├── scripts/
│   ├── generate_daily_issue.py
│   └── import_subscribers.py
├── index.html                 # Live site
└── README.md
```

---

## Credits

Built and maintained with **Grok** (xAI) as primary collaborator.

This is an independent project — not affiliated with xAI.

---

**Star this repo** if you want to follow the free AI newsletter from the beginning.
