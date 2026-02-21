# BoardIQ - Real Estate Board Intelligence Platform

NYC co-op/condo board intelligence tool. Vendor cost benchmarking, invoice processing, competitive bidding, and compliance tracking for Century Management buildings.

## Quick Start

```bash
pip install -r requirements.txt
python app.py
# → http://localhost:5001
```

Production (Heroku): `gunicorn app:app --timeout 300 --workers 2 --bind 0.0.0.0:$PORT`

## Demo Credentials

| Role | Email | Password |
|------|-------|----------|
| Board | `board@120w72.com` | `demo1234` |
| Board | `board@740park.com` | `demo1234` |
| Admin | `admin@boardiq.com` | `admin` |
| Vendor | `vendor@schindler.com` | `demo1234` |

## Architecture

**Monolithic Flask app** — all routes, templates, and data in a single server process with in-memory storage.

### Key Files

| File | Purpose |
|------|---------|
| `app.py` | Main Flask app (~5200 lines). Routes, inline HTML templates, in-memory DB, auth, BidBoard |
| `invoice_pipeline.py` | `InvoiceProcessor` class. PDF/CSV/Excel ingestion, 20-category taxonomy, rule-based classification (~85% accuracy), optional OpenAI fallback |
| `benchmarking_engine.py` | Peer group analytics. Neighborhood clustering, per-unit cost normalization, multiplier-based pricing |
| `century_buildings.py` | Enriched database of ~80 Century Management buildings with real NYC DOF/HPD data |
| `century_enriched.py` | Alternative enriched building data (124 buildings) |
| `buildings_db.py` | Enriched buildings database (124 buildings) with compliance, tax, violations |
| `enrich_century.py` | Data pipeline: geocodes buildings, pulls NYC Open Data (DOF + HPD), generates compliance deadlines. Takes 10-15 min, no API keys needed |

### Data Persistence

- **In-memory**: `BUILDINGS_DB`, `VENDOR_PROFILES`, `BID_PROJECTS` — reset on restart
- **Persisted**: `vendor_data.json` — building vendor costs saved/loaded automatically
- Buildings loaded from `century_buildings.py` on startup

### Templates

All HTML is embedded as Python strings in `app.py` (no templates/ directory):
- `LOGIN_HTML`, `DASHBOARD_HTML`, `BIDBOARD_HTML`, `BIDBOARD_DETAIL_HTML`, `VENDOR_DASHBOARD_HTML`, `VENDOR_REGISTER_HTML`

## Environment Variables

| Variable | Required | Purpose |
|----------|----------|---------|
| `ANTHROPIC_API_KEY` | No | AI-powered invoice classification (falls back to rule-based) |

## Key Routes

```
/login              - Authentication
/dashboard          - Main board dashboard
/switch-building/<bbl> - Switch active building
/api/building/<bbl> - Building JSON + benchmarks
/api/upload-invoices   - Process invoice files (PDF/CSV/Excel)
/api/commit-invoices   - Persist processed invoices
/bidboard           - Competitive vendor bidding system
/bidboard/<id>      - BidBoard project detail
/vendor             - Vendor dashboard
/vendor/register    - Vendor self-registration
```

## Conventions

- **Building IDs**: BBL format (`bbl_XXXXXXXXXXXX`) or `bldg_XXX`
- **Functions**: `snake_case`
- **Classes**: `PascalCase`
- **Template vars**: `UPPERCASE_HTML`
- **Data dicts**: `UPPERCASE` (`BUILDINGS_DB`, `DEMO_USERS`, `VENDOR_PROFILES`)
- **Section dividers**: Comment lines with `──` separators
- **Auth**: `@login_required` decorator, Flask session stores `user_email`, `user_role`, `active_building`

### Feature Pattern

New features follow this structure:
1. Data dictionary (e.g., `BID_PROJECTS`)
2. Helper functions to read/filter
3. `@app.route` handlers
4. Inline HTML template string
5. JSON API endpoint for AJAX

## Frontend Stack

- Vanilla JS (no frameworks)
- Inline CSS (no external framework)
- Google Fonts: Inter + Playfair Display
- Color palette: Navy `#0A2342`, Green `#00A550`, Background `#f4f2ef`
- Responsive flexbox layout

## Tech Stack

- Python 3 / Flask 3.1.2
- Pandas 2.2.3 (data processing)
- PyPDF 4.3.1 (PDF extraction)
- Gunicorn 22.0.0 (production)
- Deployed on Heroku

## No Tests Yet

No test suite exists. When adding tests, use `pytest`.

## Key Data Structures

- **BUILDINGS_DB**: Dict keyed by BBL. Each building has address, units, floors, year_built, is_prewar, building_class, tax_assessment, violations, compliance_deadlines, vendor_data
- **DEMO_USERS**: Dict of demo accounts with roles (`board`, `admin`, `vendor`) and assigned buildings
- **VENDOR_PROFILES**: Dict keyed by vendor_id with company info, insurance, pricing, subscription status
- **BID_PROJECTS**: Competitive bidding projects with invited vendors, bids, awards, savings calculations
- **CATEGORIES** (invoice_pipeline): 20 standardized service categories with keyword matching rules
