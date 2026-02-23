# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Quick Start
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py          # http://localhost:5001
# Kill port on restart: lsof -ti:5001 | xargs kill -9
```
No database or API keys needed. In-memory data + vendor_data.json fallback. Set `ANTHROPIC_API_KEY` for AI-powered PDF parsing (regex fallback works without it).

## Demo Logins
| Email | Password | Role | Notes |
|---|---|---|---|
| board@130e18.com | demo1234 | Board | **Primary demo** — 130 East 18th St, has contracts |
| board@120w72.com | demo1234 | Board | 120 West 72nd St |
| board@740park.com | demo1234 | Board | 740 Park Ave |
| admin@boardiq.com | admin | Admin | Sees all buildings |
| century@boardiq.com | century | Admin | Century Management portfolio |
| vendor@schindler.com | demo1234 | Vendor | Schindler Elevator Corp |
| vendor@cleanstar.com | demo1234 | Vendor | Clean Star Services |
| vendor@apexext.com | demo1234 | Vendor | Apex Exterminating |

## Architecture

**Single-file Flask app.** `app.py` (~6,800 lines) contains everything: routes, data models, and HTML templates as Python triple-quoted strings rendered via `render_template_string`. No separate template files, no JS framework.

### Data Layer (in-memory Python dicts, top of app.py)
- `BUILDINGS_DB` — 125+ buildings keyed by BBL (e.g. `bbl_1009270001`). 3 demo buildings have full vendor data.
- `DEMO_USERS` — login credentials, each user maps to buildings and a role (board/admin/vendor)
- `VENDOR_PROFILES` — vendor company data keyed by vendor_id (v001, v002, ...)
- `VENDOR_BIDS` — competitive bid records from BidBoard system
- `BUILDING_CONTRACTS` — contract records keyed by contract_id (c001, c002, ...). 5 seed contracts for 130 East 18th St.
- `CATEGORY_LABELS` — maps category codes (e.g. `ELEVATOR_MAINTENANCE`) to display names

### Inline HTML Templates (Python `"""..."""` strings in app.py)
- `LOGIN_HTML` (~line 2586) — login page
- `DASHBOARD_HTML` (~line 2640) — management dashboard with sidebar, all sections, JS
- `VENDOR_LANDING_HTML` (~line 4594) — vendor marketing/landing page
- `VENDOR_DASHBOARD_HTML` (~line 5079) — vendor portal dashboard
- `VENDOR_REGISTER_HTML` (~line 6660) — vendor registration form

### Supporting Files
- `benchmarking_engine.py` — peer group benchmarking with percentile calculations
- `buildings_db.py` — 125 Century Management buildings with compliance data
- `century_buildings.py` / `century_enriched.py` — building address/unit data
- `db.py` — PostgreSQL persistence (optional, falls back to JSON without `DATABASE_URL`)
- `invoice_pipeline.py` — legacy CSV invoice processing

### Two Distinct Design Systems
**Management Dashboard** — warm/editorial: `--bg:#f4f1eb`, `--ink:#2c2825`, `--gold:#c4893a`, `--green:#1a7a4a`, `--red:#c0392b`. Fonts: Playfair Display (headings), IBM Plex Mono (numbers), Plus Jakarta Sans (body). Fixed 220px left sidebar, 480px right-sliding detail panels, 680px upload drawers.

**Vendor Portal** — dark/modern: `--navy:#0A2342`, `--green:#00A550`, `--gold:#F59E0B`. System fonts. Sticky top nav bar, 240px left sidebar with tabs (Overview, Opportunities, Pipeline, etc.).

## Critical: JS Escaping in Python Strings

DASHBOARD_HTML and other templates are Python `"""..."""` strings containing JavaScript. When JS needs a literal backslash (e.g. for escaping quotes inside template literals):

- **WRONG:** `'building\'s'` — Python consumes `\`, JS sees unescaped `'` → SyntaxError
- **RIGHT:** `'building\\'s'` — Python outputs `\'`, JS correctly escapes the quote

This applies to all JS string escaping inside triple-quoted Python strings: `\\n`, `\\'`, `\\\\`, etc.

## Key UI Patterns

### openPanel(type, idx)
The main dashboard detail panel function (in DASHBOARD_HTML `<script>`) handles three branches:
```
if (type === 'vendor') { ... }
else if (type === 'contract') { ... }
else { /* compliance — default */ }
```
When adding new panel types, insert `else if` BEFORE the final `else` block.

### Data passed to templates
The `dashboard()` route computes and passes: `building`, `vendors`, `compliance_items`, `contracts`, `contracts_summary`, `contracts_json`, `benchmarks`, `CATEGORY_LABELS`, plus various computed stats. These become JS arrays via `{{ var | safe }}` for use in `openPanel()`.

### Invoice Upload Flow
Upload PDF → `pypdf` extracts text → Claude API (or regex fallback) parses → user reviews in table → commit updates `BUILDINGS_DB` vendor data. Two entry points: `/upload` (full page) and dashboard drawer.

## Routes Overview
- `/login`, `/logout`, `/` — auth
- `/dashboard` — main management dashboard (board/admin)
- `/vendor` — vendor portal dashboard (vendor role)
- `/vendors` — vendor landing/marketing page (public)
- `/vendor/register` — vendor registration
- `/upload` — full-page invoice upload
- `/api/upload-invoices`, `/api/commit-invoices` — invoice processing
- `/api/upload-contract`, `/api/save-contract`, `/api/request-contract` — contract management
- `/vendor/save-profile`, `/vendor/save-insurance`, `/vendor/save-pricing` — vendor profile
- `/vendor/bid`, `/vendor/bids` — vendor bidding
- `/vendor/upload-contract` — vendor-side contract upload

## Environment Variables
- `ANTHROPIC_API_KEY` — Claude API for PDF parsing (optional)
- `DATABASE_URL` — PostgreSQL connection (optional, falls back to JSON)
- `SECRET_KEY` — Flask sessions (hardcoded dev fallback)

## Deployment
Railway with gunicorn: `web: gunicorn -w 2 -b 0.0.0.0:$PORT --timeout 300 app:app`
