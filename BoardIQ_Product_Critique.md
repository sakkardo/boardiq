# BoardIQ — Expert Product Critique
### Prepared for Client Demo Preparation | February 2026

---

## Executive Summary

BoardIQ is a remarkably mature prototype for a vertical SaaS product targeting NYC co-op and condo boards. In a market dominated by generic property management tools (Yardi, AppFolio, Buildium), BoardIQ carves out a differentiated niche: **vendor cost intelligence + compliance tracking**, two of the biggest pain points for volunteer board members who often lack real estate expertise.

The product's greatest strength is its *specificity*. It doesn't try to be a general property management suite — it laser-focuses on the questions board members actually ask: "Are we overpaying our elevator company?" and "Are we compliant with Local Law 97?" That focus, combined with polished design and real NYC data, makes it demo extremely well.

Below is a detailed assessment organized around what will impress clients, what needs refinement, and a recommended demo flow.

---

## What Will Impress Clients (Lead With These)

### 1. Instant "Aha Moment" — Peer Benchmarking
The moment a board member sees their elevator contract flagged as "28% above market" with a horizontal bar showing exactly where they sit relative to 125+ comparable buildings — that's the sale. This is the single most powerful screen in the product. The peer group matching (by building size, age, and type) adds credibility; it's not comparing a 6-unit walkup to a 400-unit doorman tower.

**Demo tip:** Start every demo on the vendor benchmarking section. Let the numbers do the talking. The gold/green color coding and per-unit spend breakdowns are immediately legible even to non-technical board members.

### 2. Compliance Command Center — Fear as a Feature
NYC compliance is genuinely terrifying for board members. Missing a FISP deadline can result in DOB violations, and LL97 carbon penalties are starting to bite. BoardIQ turns this anxiety into organized, actionable intelligence. The urgency badges (HIGH in red, MEDIUM in amber), countdown-style deadlines, and cost ranges give boards the feeling of control.

The Education Center is the secret weapon here. Most competitors just list deadlines. BoardIQ *explains* what each law means, what it costs, and what steps to take — written for board members, not lawyers. The personalized building callouts ("Your building has 3 months until FISP — here's what to budget") are particularly effective.

### 3. Dual-Sided Marketplace — BidBoard Network
The vendor portal transforms BoardIQ from a reporting tool into a *platform*. Showing prospects that there's a vendor side — with qualified contractors actively bidding on work — demonstrates network effects and recurring value. The competitive bidding workflow (request bids → receive proposals → compare → award) is the kind of end-to-end workflow that justifies a subscription.

### 4. Design Quality — Punches Above Its Weight
The warm editorial design system (Playfair Display headings, gold accents, cream backgrounds) is a deliberate departure from the "blue SaaS dashboard" aesthetic. It feels premium, trustworthy, and appropriate for the audience (typically older, affluent board members in NYC co-ops). The IBM Plex Mono for numbers adds a financial-grade feel that reinforces data credibility.

### 5. Data Density Without Overwhelm
The 220px sidebar + sliding detail panel architecture is well-chosen. The main view shows high-level cards with key metrics; clicking any card opens a rich 480px panel with full context. This progressive disclosure pattern keeps the interface clean while still surfacing deep data when needed.

---

## Areas for Improvement (Prioritized)

### High Priority — Fix Before Client Demos

**H1. Empty States Need Polish**
When a building has no bids, no contracts uploaded, or no invoice data, the empty states are minimal. For demos, every section should either have seed data or show a compelling placeholder that communicates what *would* be there. Empty sections during a live demo kill momentum.

*Difficulty: Low (1-2 hours). Add richer empty state messaging with mockup previews or "upload to see..." CTAs.*

**H2. Data Entry Story**
The upload-to-insight flow is the core value loop, but it's currently buried. A new client's first question will be "How does my data get in here?" The compact upload bar at the bottom of the dashboard is easy to miss. Consider making the first-time experience more guided — a welcome wizard or prominent "Start here" callout for buildings with no vendor data.

*Difficulty: Medium (4-6 hours). Create a first-run experience overlay or guided setup flow.*

**H3. Contract Management Depth**
The 5 seed contracts for 130 E 18th St are good, but the contract detail panels could show more actionable intelligence: renewal countdown timers, auto-renew warnings, market comparison of the contract value, and suggested negotiation talking points. The AI-generated summaries are a great start — push them further.

*Difficulty: Medium (3-4 hours). Enrich contract panels with more computed insights.*

### Medium Priority — Strengthen for Serious Prospects

**M1. Portfolio View for Management Companies**
The `/portfolio` route exists for users with 20+ buildings, but management companies are likely the highest-value customers. The portfolio dashboard should showcase aggregate savings opportunities, compliance risk heatmaps across all buildings, and vendor consolidation analysis. This is the "enterprise" tier pitch.

*Difficulty: High (8-12 hours). Requires new visualizations and aggregate computations.*

**M2. Mobile Experience**
While responsive breakpoints have been added, the core experience is desktop-first. Board members often check things on phones during meetings or commutes. The sidebar collapse works, but the detail panels, charts, and data tables need more mobile-specific attention.

*Difficulty: Medium (4-6 hours). Iterative CSS refinements and touch-friendly interactions.*

**M3. Notification / Alert System**
Compliance deadlines and contract expirations generate urgency, but there's no notification system. Email digests ("Your building has 2 compliance deadlines this quarter") or in-app notification bells would drive re-engagement. For demos, even a mock notification dropdown signals product maturity.

*Difficulty: Medium-High (6-8 hours for functional, 2 hours for mock UI).*

### Lower Priority — Polish After Product-Market Fit

**L1. Report Generation / Export**
Board members need to present findings to their fellow board members at meetings. A "Generate Board Report" button that produces a PDF summary of vendor benchmarks, compliance status, and contract alerts would be enormously valuable and demo well.

**L2. Historical Trend Lines**
Currently the dashboard shows point-in-time snapshots. Showing how vendor costs or compliance status have changed over time adds depth and demonstrates ongoing value (not just a one-time lookup).

**L3. Integration Story**
The upload flow supports CSV/PDF from Yardi, AvidXchange, etc. For enterprise clients, direct API integrations with property management systems would be expected. Even listing "Coming Soon: Yardi Integration" signals roadmap maturity.

---

## Competitive Positioning

### What Makes BoardIQ Different

| Competitor | What They Do | What BoardIQ Does Better |
|---|---|---|
| **Yardi / AppFolio / Buildium** | Full property management (rent rolls, maintenance requests, accounting) | BoardIQ provides *intelligence* on top of operational data — benchmarks, compliance, competitive bidding. It's not trying to replace Yardi; it consumes Yardi data. |
| **VendorPM** | Vendor qualification and compliance tracking | BoardIQ adds real cost benchmarking against peer buildings — not just "is this vendor qualified" but "are we overpaying?" |
| **Building Engines** | Operations and amenity management | No vendor cost intelligence or compliance education. Different focus entirely. |
| **Spreadsheets** | Most boards use Excel for everything | BoardIQ replaces the treasurer's spreadsheet with live data, peer comparisons, and a bidding marketplace. |

### Key Differentiator to Emphasize
"BoardIQ is the only platform that tells you *what your building should be paying* — not just what it is paying. We benchmark every vendor contract against hundreds of similar NYC buildings, so your board can negotiate from a position of knowledge."

---

## Recommended Demo Flow (10-12 Minutes)

### Minute 0-1: Splash Page
Show the new landing page. Let the stats strip land (125+ buildings, 15K+ units, $XM tracked). Communicate scale and credibility before logging in.

### Minute 1-3: The Aha Moment
Log in as `board@130e18.com`. Immediately scroll to the vendor benchmarking section. Point out the "Above Market" alerts in gold. Click on the elevator vendor — show the detail panel with per-unit spend comparison, peer percentile, and the savings opportunity call-out. This is the "are we overpaying?" moment.

### Minute 3-5: Compliance Deep Dive
Scroll to the Compliance Calendar. Click on an upcoming deadline (elevator inspection or FISP). Show the cost range, deadline urgency, and comparable building data. Open the Education Center and show a personalized guide — emphasize that it tells the board *what to do*, not just *what's due*.

### Minute 5-7: Contracts & Bidding
Open a contract card. Show the AI-generated summary, key terms, and expiry alert. Show the "Request Bids" workflow — one click sends an RFP to qualified vendors in the BidBoard network. This is the "what do we do about it?" answer.

### Minute 7-9: Vendor Portal (Quick Peek)
Switch to the vendor login (`vendor@schindler.com`). Show the vendor's view: building opportunities, bid submissions, insurance tracking. This demonstrates the two-sided marketplace value — "vendors are already competing for your business."

### Minute 9-10: The Close
Switch back to the board view. Show the peer group banner ("Pre-war co-ops, 200-600 units"). Emphasize: "Every number you see is compared against buildings just like yours." Show the upload entry point — "Getting started takes 5 minutes with a CSV from your property manager."

### Minute 10-12: Q&A
Let the prospect explore. They'll click things. The detail panels and education guides will do the selling.

---

## Final Assessment

BoardIQ is in a strong position for client demos. The product has genuine depth — it's not a mockup or a slide deck; it's a working application with real data, interactive panels, and a dual-sided marketplace. The design quality signals professionalism, and the NYC-specific focus (co-op laws, building types, peer groups) makes it feel purpose-built rather than generic.

The biggest risk in demos is pacing. There's a lot to show, and it's tempting to show everything. Resist that. Lead with the benchmarking "aha moment," follow with compliance urgency, and close with the bidding workflow. That three-beat arc — *discover the problem → understand the urgency → here's the solution* — will land every time.

**Overall Grade: A-**
The product is demo-ready. The areas for improvement (empty states, first-run experience, portfolio depth) are refinements, not blockers. Ship the splash page, tighten the demo script, and start booking meetings.
