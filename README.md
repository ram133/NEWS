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

**Issue #001 — October 27, 2026**  
Anthropic S-1 filing, OpenAI GPT-6.1 Terra price cut, security concerns, and major compute financing.

→ [Read Issue #001](issues/001.md)

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
│   └── import-subscribers.yml
├── data/
│   ├── subscribers.json       # JSON database of email subscriptions
│   └── last_run.json          # Tracks last auto-publish
├── issues/                    # Published newsletter issues
├── scripts/
│   └── generate_daily_issue.py
├── index.html                 # Live site
└── README.md
```

---

## Credits

Built and maintained with **Grok** (xAI) as primary collaborator.

This is an independent project — not affiliated with xAI.

---

**Star this repo** if you want to follow the free AI newsletter from the beginning.
