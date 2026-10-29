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

## Sign up (Free) — GitHub only

This project uses **only GitHub**. No external form services, no third-party databases.

Email subscriptions are stored in a simple JSON file that acts as the database:

**`data/subscribers.json`**

### How to subscribe

1. Open a new [GitHub Issue](https://github.com/ram133/NEWS/issues/new?title=Subscribe&body=Email%3A%20%0A%0A(please%20include%20your%20email%20address)) with the title **Subscribe** and put your email address in the body.
2. Your email is added to `data/subscribers.json`.
3. Alternatively, star or watch this repository to receive GitHub notifications when new issues are published.

Only your email address is stored. You can unsubscribe anytime by opening another issue.

---

## Automatic updates (free forever)

- New issues are published as markdown files in `/issues`
- The live site always surfaces the latest issue
- GitHub Actions handle bulk subscriber import (no paid services)
- Future: scheduled workflows can pull free public sources and draft new issues

Everything stays inside this repository. No external SaaS required.

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
├── .github/workflows/     # Import + future auto-update actions
├── data/
│   └── subscribers.json   # JSON database of email subscriptions
├── issues/                # Published newsletter issues
├── scripts/               # Local tools
├── ads/                   # Ad guidelines
├── index.html             # Beautiful live site
└── README.md
```

---

## Credits

Built and maintained with **Grok** (xAI) as primary collaborator.

This is an independent project — not affiliated with xAI.

---

**Star this repo** if you want to follow the free AI newsletter from the beginning.
