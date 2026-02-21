# BoardIQ — Project Context

## What This Is
BoardIQ is a property management intelligence platform for NYC co-op and condo buildings.
It brings pricing transparency and vendor analysis to building boards managed by Century Management.

## Live URLs
- Production: https://boardiq-production.up.railway.app
- GitHub: https://github.com/sakkardo/boardiq
- Railway project: industrious-prosperity

## Login Credentials (Demo)
- century@boardiq.com / century (management company — sees all buildings)
- admin@boardiq.com / admin (all buildings)
- board@120w72.com / demo1234 (120 W 72nd St)
- board@740park.com / demo1234 (740 Park Ave)
- vendor@schindler.com / demo1234 (Elevator vendor)

## Tech Stack
- Backend: Flask (Python), deployed on Railway
- Data: In-memory Python dicts (no database yet — data resets on redeploy)
- AI: Anthropic API (claude-sonnet-4-20250514) for invoice parsing
- PDF parsing: pypdf for text extraction + Claude API for intelligence
- Frontend: Jinja2 templates, vanilla JS, no framework

## Repository Structure
- app.py — entire application (4,100+ lines, single file)
- century_buildings.py — 125 Century Management buildings with addresses, BBLs, units
- buildings_db.py — demo buildings with seeded vendor/compliance data
- benchmarking_engine.py — compares vendor costs across buildings
- invoice_pipeline.py — CSV invoice processing
- Procfile — gunicorn config (should be: web: gunicorn -w 2 -b 0.0.0.0:$PORT --timeout 300 app:app)
- requirements.txt — flask, pandas, gunicorn, pypdf

## Environment Variables (set in Railway)
- ANTHROPIC_API_KEY — Claude API key for invoice parsing
- SECRET_KEY — Flask session key (not yet set, using hardcoded dev key)

## Three User Types
1. Board members — see their building's vendor spend, benchmarks, compliance deadlines
2. Management companies (Century) — see all buildings, upload invoices, approve vendor changes
3. Vendors — register, build profile, subscribe ($250/yr) to see building opportunities

## Core Feature: Invoice Upload
- URL: /upload
- User uploads a multi-page PDF of invoices (e.g. 169-page Century invoice report)
- pypdf extracts text from each page
- Claude API reads pages in batches of 15, extracts: vendor, service address, amount, contract vs one-time, category
- Building matched via fuzzy address matching against century_buildings.py
- User reviews extracted invoices, corrects mismatches via dropdown, then commits
- Committed invoices populate building vendor_data and feed benchmarking

## Current Bugs / Known Issues
1. Invoice upload timing out on large PDFs — Procfile needs --timeout 300 (fix ready, not yet deployed)
2. pypdf crashes on UTF-16 encoded pages — fixed in latest app.py (not yet deployed)
3. Data resets on every Railway redeploy — need PostgreSQL (not yet added)
4. No real authentication — using hardcoded demo users dict

## What Needs To Be Deployed (pending)
Two files need to be uploaded to GitHub to fix invoice upload:
- app.py (latest version with AI parser + UTF-16 fix + batch size 15)
- Procfile with: web: gunicorn -w 2 -b 0.0.0.0:$PORT --timeout 300 app:app

## Next Priorities
1. Deploy the two pending files (fixes invoice timeout)
2. Add PostgreSQL via Railway add-on (persists data across deploys)
3. Add real domain (boardiq.com or boardiq.io)
4. Upgrade Railway from trial to paid ($5/mo Hobby plan — trial running out)
5. AvidXchange API integration (Century is a customer — need API credentials from their accounting team)
6. Stripe integration for vendor $250/year subscriptions

## Business Model
- Management companies: pay data licensing fee (~$500-1000/mo) for portfolio visibility
- Vendors: pay $250/year to access building opportunity marketplace
- Future: savings-share bonus when boards approve vendor switches based on BoardIQ recommendations

## Key Technical Decisions
- Single app.py file for simplicity (move to modular structure when complexity demands it)
- AI-powered invoice parsing (not regex) — Claude API reads pages as text, returns structured JSON
- Fuzzy building matching — normalizes addresses to match invoices to buildings
- Annualization logic — recurring contracts × 12, one-time repairs at face value

## AvidXchange Integration Plan
- Century Management is an AvidXchange customer
- Path 1 (immediate): ask Century's accounting admin for API credentials
- Path 2 (formal): apply to AvidXchange partner program
- Goal: replace manual PDF upload with nightly automated invoice sync
