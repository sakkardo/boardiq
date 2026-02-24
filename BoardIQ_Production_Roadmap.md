# BoardIQ — Production Roadmap

**Target:** 100 buildings, 25 vendors, 1–2 management companies
**Date:** February 23, 2026

---

## Where We Are Today

BoardIQ is a working prototype deployed on Railway. The core loop works: upload invoices → AI parses them → vendor intelligence shows savings opportunities with peer benchmarking. Here's an honest snapshot of what's built vs. what needs work.

### What's Working
- **Invoice upload pipeline** — PDF upload → Claude AI extraction (with regex fallback) → user review → commit to building. Searchable building dropdown, numerical sort, detailed confirmation screen.
- **Vendor intelligence & benchmarking** — 17 service categories with peer-group percentile comparisons (p25/p50/p75/p90). Size-based buckets, neighborhood clusters, era multipliers.
- **Contract management** — Upload PDFs, AI-powered parsing with confidence indicators, manual entry, 5 seed contracts for demo building.
- **Three user roles** — Board members (see their building), Admin/management (see portfolio), Vendors (separate portal with profile, insurance, pricing, bid submission).
- **Vendor portal** — Registration, profile management, insurance tracking, BidBoard with competitive bidding flow.
- **125 Century Management buildings** loaded with address data.
- **PostgreSQL persistence** for vendor data + contracts via Railway (JSON fallback for local dev).

### What's Placeholder or Seed Data
- Only 3 buildings have real vendor data (130 E 18th, 120 W 72nd, 740 Park Ave). The other 122 Century buildings are address-only shells.
- Benchmarking baselines are estimated, not derived from real market data.
- BidBoard has seed bids but no real workflow (no notifications, no bid comparison view for boards).
- Vendor profiles are demo data — Schindler, Clean Star, Apex Exterminating.
- Auth is simple dict lookup, no password hashing, no sessions beyond Flask's default.

### What's Missing for Production
- No real database schema for buildings, users, invoices (only vendor_data and contracts persist to Postgres).
- No email/notifications system.
- No multi-tenancy — management companies can't self-onboard.
- No user management (invite, roles, permissions).
- No audit trail or activity logging.
- No file storage (PDFs live in memory during session only).
- No billing/subscription system.

---

## The Four User Roles in Production

### 1. Management Company (Admin)
The primary customer. Century Management is the prototype. They manage multiple buildings and want to reduce vendor costs across their portfolio.

**Core workflows:**
- Upload invoices in bulk across buildings
- View portfolio-wide vendor spend and savings opportunities
- Manage contracts and renewal deadlines
- Run competitive bids through BidBoard
- Onboard new buildings and board members

### 2. Board Members
Co-op/condo board members who want transparency into their building's vendor spend.

**Core workflows:**
- View their building's vendor intelligence (spend vs. peers)
- Review contracts and upcoming renewals
- Approve or reject vendor changes proposed by management
- See bid results from BidBoard

### 3. Vendors
Service providers (elevator, cleaning, plumbing, etc.) who want to win and retain building contracts.

**Core workflows:**
- Maintain company profile, insurance docs, pricing
- Browse and bid on opportunities via BidBoard
- Upload contracts from their side
- Track their pipeline of buildings served

### 4. Super Admin (BoardIQ team)
Internal admin for managing the platform.

**Core workflows:**
- Onboard new management companies
- Monitor usage, manage billing
- Maintain benchmark data
- Support and troubleshooting

---

## Phased Roadmap

### Phase 1: Make It Real (Weeks 1–4)
**Goal:** Turn the prototype into something one management company can use daily.

**Database & Persistence**
- Full Postgres schema: buildings, users, invoices, contracts, vendors, bids
- Migrate all in-memory dicts to database queries
- File storage for uploaded PDFs (S3 or Railway volume)
- Keep the single-file Flask architecture — no need to break it apart yet

**Auth & Users**
- Password hashing (bcrypt)
- Session management with proper expiry
- Invite flow: management admin invites board members via email
- Role-based access: who can see what, who can edit

**Invoice Pipeline Hardening**
- Store parsed invoices permanently (not just in session)
- Invoice history per building (uploaded date, who uploaded, amounts)
- Duplicate detection (same vendor + amount + period)
- Better category matching with ML-assisted classification over time

**Estimated effort:** 1 developer, 4 weeks full-time
**Cost:** ~$8,000–12,000 (contractor) or founder time

---

### Phase 2: Multi-Building Operations (Weeks 5–8)
**Goal:** Handle 100 buildings efficiently. Make vendor intelligence actually useful.

**Building Onboarding**
- Bulk building import from CSV (address, units, BBL, year built)
- Auto-populate NYC building data from public records (PLUTO/HPD APIs — free)
- Building profile pages with key stats

**Vendor Intelligence Upgrades**
- Real benchmark data from committed invoices (replace estimated baselines)
- Trend analysis: is spend going up or down year-over-year?
- Savings calculator: "switching to p25 vendor would save $X/year"
- Portfolio rollup: total savings opportunity across all 100 buildings

**Contract Management**
- Renewal alerts (30/60/90 day warnings)
- Contract comparison: same service across buildings
- Auto-renew tracking and cancellation deadline alerts
- Email notifications for approaching deadlines

**Estimated effort:** 1 developer, 4 weeks
**Cost:** ~$8,000–12,000

---

### Phase 3: BidBoard & Vendor Marketplace (Weeks 9–14)
**Goal:** Connect the demand side (buildings) with supply side (vendors). This is where BoardIQ becomes a platform.

**BidBoard for Management Companies**
- Create bid requests: select category, buildings, requirements
- Invite specific vendors or open to marketplace
- Side-by-side bid comparison with scoring
- Board member approval workflow
- Award notification and contract generation

**Vendor Portal Upgrades**
- Vendor onboarding flow (self-serve registration → profile → verification)
- Insurance document upload and expiry tracking
- Automated RFP notifications matching vendor categories/geography
- Performance dashboard: buildings served, contract values, ratings

**Email & Notifications**
- Transactional emails: bid invites, contract alerts, invoice confirmations
- Weekly digest for board members
- Use SendGrid or AWS SES ($0.10/1000 emails)

**Estimated effort:** 1–2 developers, 6 weeks
**Cost:** ~$15,000–25,000

---

### Phase 4: Second Management Company & Scale (Weeks 15–20)
**Goal:** Prove the model works for more than one customer.

**Multi-Tenancy**
- Management company isolation: each sees only their buildings
- Shared vendor marketplace across management companies
- Configurable branding per management company (logo, colors)

**Reporting & Analytics**
- Monthly PDF reports per building (auto-generated)
- Portfolio-level analytics dashboard
- Export to CSV/Excel for board meetings
- Year-over-year comparisons

**Compliance Tracking** (already seeded in the codebase)
- Harden the compliance module: elevator inspections, boiler, fire safety, backflow
- Violation tracking from NYC open data APIs (free)
- Compliance calendar with deadlines

**Estimated effort:** 1–2 developers, 6 weeks
**Cost:** ~$15,000–25,000

---

## Infrastructure & Monthly Costs

### Current (Prototype)
| Item | Cost |
|------|------|
| Railway (web + Postgres) | $5–10/mo |
| Domain (mybuildingiq.com) | $12/yr |
| **Total** | **~$15/mo** |

### Production at 100 Buildings / 25 Vendors

| Item | Monthly Cost | Notes |
|------|-------------|-------|
| Railway Pro (or AWS/Render) | $25–50 | 1 web dyno + Postgres |
| Postgres storage | $10–20 | ~1GB for 100 buildings |
| S3 file storage | $5–10 | PDF uploads, ~5GB |
| Anthropic API (Claude) | $30–80 | ~500 invoice parses + 100 contract parses/mo |
| SendGrid email | $0–15 | Free tier covers <100 emails/day |
| Domain + SSL | $1 | Already have it |
| **Total** | **$70–175/mo** |

### At 500 Buildings (growth target)

| Item | Monthly Cost |
|------|-------------|
| Infrastructure (Railway/AWS) | $100–200 |
| Postgres | $50–100 |
| S3 | $15–30 |
| Anthropic API | $150–400 |
| Email (SendGrid paid) | $20–30 |
| **Total** | **$335–760/mo** |

The economics are very favorable. The biggest variable cost is Claude API usage, which scales linearly with PDF uploads. At ~$0.08 per invoice parse and ~$0.15 per contract parse, it stays manageable.

---

## Revenue Model Suggestion

| Plan | Target | Price | What They Get |
|------|--------|-------|---------------|
| **Building** | Individual co-op boards | $49/mo per building | Vendor intelligence, contract tracking, benchmarking |
| **Portfolio** | Management companies (10+ buildings) | $29/mo per building | Everything above + bulk upload, portfolio analytics, BidBoard |
| **Enterprise** | Large managers (50+ buildings) | $19/mo per building | Everything above + API access, custom reports, dedicated support |
| **Vendor** | Service providers | Free or $99/mo | Profile, bid on opportunities, track pipeline |

**At 100 buildings on Portfolio plan:** $2,900/mo revenue vs. ~$150/mo costs = strong unit economics.

---

## Development Cost Summary

| Phase | Timeline | Cost Range | What You Get |
|-------|----------|-----------|--------------|
| Phase 1: Make It Real | Weeks 1–4 | $8K–12K | Real database, auth, persistent invoices |
| Phase 2: Multi-Building | Weeks 5–8 | $8K–12K | 100 buildings working, real benchmarks, contract alerts |
| Phase 3: BidBoard | Weeks 9–14 | $15K–25K | Vendor marketplace, bid workflow, notifications |
| Phase 4: Scale | Weeks 15–20 | $15K–25K | Multi-tenant, reporting, compliance |
| **Total** | **~5 months** | **$46K–74K** | **Full production platform** |

These estimates assume hiring a contractor at $50–75/hr. If built by a co-founder, the cash cost drops to infrastructure only (~$150/mo). If using AI-assisted development (as we've been doing), a single developer can likely compress timelines by 30–40%.

---

## What I'd Build Next (If Starting Tomorrow)

The highest-leverage next step is **Phase 1** — specifically the database migration. Right now, every time Railway restarts, non-persisted data resets. The three things that would make the biggest immediate difference:

1. **Full Postgres persistence** — buildings, users, invoices all survive restarts
2. **PDF file storage** — uploaded invoices and contracts stored permanently in S3
3. **Password hashing + invite flow** — so you can give real board members real logins

Everything else in the prototype works well enough to demo and sell. The invoice→vendor intelligence pipeline is the core value prop and it's functional today. The goal should be: close one management company customer, then build Phase 2–4 alongside their real usage.
