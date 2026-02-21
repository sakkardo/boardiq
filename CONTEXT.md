# BoardIQ — Project Context

## What This Is
BoardIQ is a property management intelligence platform for NYC co-op and condo buildings.
It brings pricing transparency and vendor analysis to building boards managed by Century Management.

## Live URLs
- Production: https://boardiq-production.up.railway.app
- GitHub: https://github.com/sakkardo/boardiq
- Railway project: industrious-prosperity (upgraded to paid plan)

## Login Credentials (Demo)
- board@130e18.com / demo1234 (130 East 18th St — primary demo building)
- board@120w72.com / demo1234 (120 W 72nd St)
- board@740park.com / demo1234 (740 Park Ave)
- admin@boardiq.com / admin (all buildings)
- century@boardiq.com / century (management company — sees all buildings)
- vendor@schindler.com / demo1234 (Elevator vendor)

## Tech Stack
- Backend: Flask (Python), deployed on Railway
- Data: In-memory Python dicts + JSON fallback (vendor_data.json) + PostgreSQL when DATABASE_URL set
- AI: Anthropic API (claude-sonnet-4-20250514) for invoice parsing (falls back to regex without API key)
- PDF parsing: pypdf for text extraction + Claude API for intelligence
- Frontend: Jinja2 templates (render_template_string), vanilla JS, no framework
- All HTML/CSS/JS is inline in app.py — single file architecture

## Repository Structure
- app.py — entire application (4,400+ lines, single file with inline templates)
- century_buildings.py — 125 Century Management buildings with addresses, BBLs, units
- buildings_db.py — 125 buildings with compliance data and context fields
- benchmarking_engine.py — compares vendor costs across buildings using peer groups
- invoice_pipeline.py — CSV invoice processing (legacy, mostly superseded by app.py)
- db.py — PostgreSQL persistence layer (falls back gracefully without DB)
- Procfile — gunicorn config: web: gunicorn -w 2 -b 0.0.0.0:$PORT --timeout 300 app:app
- requirements.txt — flask, pandas, gunicorn, pypdf, psycopg2-binary

## Environment Variables
- ANTHROPIC_API_KEY — Claude API key for PDF invoice AI parsing (optional, regex fallback exists)
- DATABASE_URL — PostgreSQL connection string (optional, JSON fallback exists)
- SECRET_KEY — Flask session key (using hardcoded dev key if not set)

## Three User Types
1. Board members — see their building's vendor spend, benchmarks, compliance deadlines, BidBoard
2. Management companies (Century) — see all buildings, upload invoices, approve vendor changes
3. Vendors — register, build profile, subscribe ($250/yr) to see building opportunities

## Working Features (as of Feb 2026)
1. **Dashboard** with building intelligence, vendor benchmarks, savings analysis
2. **Compliance Calendar** with law descriptions (LL11, LL97, LL87, LL152, LL26, Elevator)
3. **Peer Benchmarking** — buildings compared against similar size/age/neighborhood peers
4. **BidBoard** — compliance panel shows scope of work + sample vendor bids with pricing
5. **Invoice Upload (PDF)** — upload → extract → match buildings → review → commit to vendor data
   - AI path: Claude API parses pages in batches of 15 (needs ANTHROPIC_API_KEY)
   - Regex fallback: extracts vendor, amount, address, category without API key
   - Upload page at /upload with full review/commit flow
   - Dashboard drawer upload also available (↑ Upload Invoices button)
6. **Vendor Intelligence** — per-unit cost vs network median, percentile ranking, savings opportunities
7. **Sample CSV Download** at /api/sample-csv

## Core Feature: Invoice Upload
- URL: /upload (full page) or dashboard drawer (↑ Upload Invoices button)
- User uploads multi-page PDF invoices
- pypdf extracts text from each page
- If ANTHROPIC_API_KEY set: Claude API reads pages in batches of 15, returns structured JSON
- If no API key: regex fallback parser extracts vendor, amount, address, category
- Building matched via fuzzy address matching + known building name aliases
- User reviews extracted invoices in table, can reassign buildings/categories via dropdowns
- Committed invoices update building vendor_data and feed benchmarking
- Data persists to vendor_data.json (and PostgreSQL if DATABASE_URL set)

## Key Technical Notes
- DASHBOARD_HTML is a Python triple-quoted string (""") containing Jinja2 + JS template literals
- When using single quotes in JS strings inside """, must use \\\\' (double backslash) so Python outputs \\' for JS
- The openPanel() function builds compliance detail panels with nested template literals
- BidBoard vendor bids use an IIFE inside a template literal for dynamic bid generation
- Buildings keyed by BBL (Borough-Block-Lot) identifier, e.g. bbl_1009270001
- 3 demo buildings have full vendor data: 120 W 72nd, 740 Park Ave, 130 E 18th
- 125 Century buildings in buildings_db.py have compliance data but no vendor data

## Business Model
- Management companies: pay data licensing fee (~$500-1000/mo) for portfolio visibility
- Vendors: pay $250/year to access building opportunity marketplace
- Future: savings-share bonus when boards approve vendor switches based on BoardIQ recommendations

## Next Priorities
1. Push to GitHub and deploy to Railway (Railway upgraded to paid plan)
2. Set ANTHROPIC_API_KEY in Railway for AI-powered PDF parsing
3. Add real domain (boardiq.com or boardiq.io)
4. AvidXchange API integration (Century is a customer — replace manual PDF upload)
5. Stripe integration for vendor $250/year subscriptions
6. Real authentication (replace hardcoded DEMO_USERS)
