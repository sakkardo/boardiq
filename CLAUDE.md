# BoardIQ — Claude Code Instructions

## Quick Start
```bash
# From the repo root:
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
# App runs on http://localhost:5001
```

## What This Is
BoardIQ is a property management intelligence platform for NYC co-op/condo buildings.
Single-file Flask app (app.py, 4,400+ lines) with inline Jinja2 templates and vanilla JS.
See CONTEXT.md for full project details, business model, and architecture.

## Primary Demo Login
- **board@130e18.com** / demo1234 — 130 East 18th Street (primary demo building)
- admin@boardiq.com / admin — sees all buildings
- See CONTEXT.md for all credentials

## Key Architecture
- `app.py` — entire application: routes, templates (render_template_string), CSS, JS, data models
- `benchmarking_engine.py` — peer group benchmarking with baseline percentiles
- `buildings_db.py` — 125 Century Management buildings with compliance data
- `db.py` — PostgreSQL layer (falls back to in-memory + JSON without DATABASE_URL)
- Buildings keyed by BBL (e.g. bbl_1009270001). 3 demo buildings have full vendor data.

## Critical Gotcha: JS Escaping in Python Strings
DASHBOARD_HTML is a Python `"""..."""` string. When writing JavaScript single-quoted strings inside it:
- **WRONG:** `'building\'s'` — Python consumes the `\`, JS sees unescaped `'` → SyntaxError
- **RIGHT:** `'building\\'s'` — Python outputs `\'`, JS correctly escapes the quote

## Invoice Upload (PDF)
- Route: `/upload` (full page) or dashboard drawer
- AI path needs ANTHROPIC_API_KEY env var (Claude API parses pages)
- Without API key: regex fallback parser works but less accurate
- Flow: upload PDF → extract text (pypdf) → parse invoices → match buildings → review → commit

## Running Locally
- No database needed (uses in-memory data + vendor_data.json)
- No API key needed (regex fallback for PDF parsing)
- Set ANTHROPIC_API_KEY for better PDF invoice parsing
- Flask debug mode causes port conflicts on restart — kill port 5001 processes first
