# BoardIQ Dashboard — Full Design Critique

**Date:** February 27, 2026
**Reviewed:** mybuildingiq.com (live production)
**Logged in as:** board@130e18.com (130 East 18th Street)

---

## First Impression

The dashboard immediately communicates authority and seriousness. The warm, editorial palette (cream background, dark ink, gold accents) feels intentional for the audience — NYC co-op and condo board members who expect a premium, trustworthy experience. The four KPI cards at the top ("Annual Overspend $794,129", "6 of 10 contracts above market", "4 urgent deadlines", "$73K–$130K compliance cost") deliver a clear punch: your building is losing money and you need to act. This is strong.

The Playfair Display headings paired with IBM Plex Mono for numbers creates a financial-intelligence feel that distinguishes BoardIQ from typical property management tools. The overall emotional reaction is "this is a serious tool built by people who understand buildings."

---

## What Works Well

**Vendor Intelligence table.** The left-side vendor table with annual cost, per-unit cost, and market position bars is the strongest section of the dashboard. The red/green color coding on "Above Market" vs. "Below Market" is instantly readable. Pairing this with the right-side savings breakdown ("Total Identified Savings: $794,129/yr") creates immediate urgency. The priority cards with "Initiate Rebid via BidBoard →" CTAs provide a clear next step. This is best-in-class for the use case.

**Compliance Calendar.** Each compliance item shows the law name, a plain-English description, the consequence of missing it (in a warm red callout), network cost ranges from comparable buildings, and dual CTAs ("Start BidBoard →" / "View Requirements"). The urgency labels ("DUE IN 2 MONTHS · ACT NOW") use appropriate color coding. The detail panel (tested on Elevator Inspection) is thorough with sections for What This Requires, Who Does This Work, Step-by-Step Timeline, DOB Filing, and Board Tip.

**Contract Intelligence.** The AI Analysis expandable sections on each contract card are a standout feature. The red/orange callout pills ("Contract expired Dec 31, 2025 — vendor operating without agreement", "Plumbing spend is 89% above network median") surface actionable intelligence without requiring the user to dig. The status badges (Expired, Expiring Soon, Active) and document status ("No Document" vs. "Document On File") give quick triage ability.

**Education Center.** The new section successfully extends the editorial tone. The featured guide banner with stat boxes ($268/ton penalty, ~$31K avg penalty, 84% of boards unaware) is compelling. The personalized building callout in the FISP guide — "Your building (130 East 18th Street) has a FISP deadline of Dec 2026 (10 months away)" — is the feature's most valuable aspect, grounding abstract compliance law in the user's specific building. The "Related Actions" CTAs at the bottom of each guide ("View in Compliance Calendar →", "Start BidBoard for This Category →") create a useful loop back into the operational dashboard.

**Sidebar navigation.** Clean, well-organized with logical groupings (Intelligence → Compliance → Building → Resources). The badge counts (Savings 6, BidBoard 2, Compliance Calendar 4, Contracts 6) provide at-a-glance building health. The gold "NEW" badge on Education draws attention appropriately.

---

## Issues and Recommendations

### 1. Page Length and Information Architecture

**Problem:** The single-page dashboard is extremely long. Scrolling from the Vendor Intelligence table at the top to the Education Center at the bottom requires 8–10 full scroll gestures. A board member looking for their elevator contract has to scroll past compliance items, BidBoard requests, and five other contracts to find it. This creates cognitive load and makes the dashboard feel like a report rather than a tool.

**Recommendation:** Consider making each sidebar nav item scroll to its section *and* collapse other sections, or switch to a tabbed layout where clicking "Contracts" shows only the contracts section. The sidebar already has the right structure — it just needs to control the main content area more actively. Alternatively, add a "jump to top" floating button and section anchors.

### 2. Vendor Detail Panel Is Too Short

**Problem:** The vendor slide-in panel (tested on Con Edison) shows Annual Spend, Per Unit, Network Median, Savings Opportunity, a percentile slider, Key Factors, and two CTAs. This is good, but compared to the compliance and education panels — which are rich with sections, timelines, and tips — the vendor panel feels sparse. For the dashboard's highest-value insight (you're overpaying $475K/yr on property management), the user deserves more context: historical spend trend, what comparable buildings pay, what a competitive bid typically achieves.

**Recommendation:** Enrich the vendor panel with: (a) a mini spend history chart, (b) the "what good looks like" median breakdown, (c) links to the related contract if one exists, and (d) a "Learn More" link to the relevant Education guide (e.g., Competitive Bidding).

### 3. BidBoard Section Feels Disconnected

**Problem:** The "BidBoard — Active Bid Requests" section sits between Compliance and Contracts with minimal visual weight. It shows two rows (Elevator Annual Inspection, Pest Control Rebid) with "0 BIDS" and "OPEN" badges, but there's no context about what BidBoard is, what happens next, or how the board should engage. A board member seeing "0 BIDS" might think the system isn't working rather than understanding bids take time.

**Recommendation:** Add a brief contextual line like "Bids typically arrive within 5–7 business days" when count is 0. Consider adding a timeline indicator showing when the request was sent. Also, visually connect BidBoard items to the compliance items or contracts they originated from — right now the relationship is implicit.

### 4. Contract Cards Lack Click Interaction

**Problem:** Unlike vendors (which open a detail panel) and compliance items (which have "View Requirements" buttons), contract cards don't have a click-to-open-panel interaction. The "BoardIQ AI Analysis" accordion is the only interactive element. If a board member wants to see full contract terms, scope of work details, or take action on an expiring contract, there's no pathway deeper.

**Recommendation:** Add an `openPanel('contract', idx)` interaction to contract cards, with a detail panel showing the full contract scope, all terms, document preview (if uploaded), renewal timeline, and action buttons (Initiate Rebid, Request Document, Send to Attorney).

### 5. Education Guide Cards Could Show Building Relevance

**Problem:** The guide cards display generic descriptions and read times, but don't surface whether the guide is relevant to this specific building. A board member sees 8 cards and has to decide which ones matter. The personalized callout is only visible *after* opening a guide.

**Recommendation:** Add a small indicator on the card itself — something like a gold dot or "Relevant to your building" tag — for guides where the `buildingCallout()` function would return content. This would help boards prioritize which guides to read first.

### 6. Featured Guide Banner May Need Rotation

**Problem:** The LL97 featured guide banner is static. Every time the board member visits, they see the same featured content. Over time this becomes wallpaper.

**Recommendation:** Rotate the featured guide based on the building's most urgent compliance deadline. If the elevator inspection is due in 2 months, feature the Elevator guide. If a contract is expiring, feature Competitive Bidding. This personalizes the Education section's first impression.

### 7. Savings Panel and Upload Box Compete for Attention

**Problem:** On the right side of the Vendor Intelligence section, the "Total Identified Savings" panel and the "Upload Invoice Data" dashed box sit in the same column. The upload box — a dashed outline with "CSV or Excel from Yardi / AvidXchange / manual export" — has nearly the same visual weight as the savings panel above it. For a board member, the savings number ($794,129/yr) is the most important element on the page, but the upload box dilutes its impact.

**Recommendation:** Move the upload functionality to the Invoice Upload sidebar nav item or make it a smaller, secondary link rather than a large dashed box. The savings column should maintain its emotional punch without distraction.

### 8. Mobile Responsiveness

**Problem:** The 220px fixed sidebar and 480px slide-in panels suggest this is designed desktop-first. Board members often review building information on tablets during meetings or on phones when discussing issues informally. The current layout likely breaks on smaller screens.

**Recommendation:** Implement a responsive breakpoint where the sidebar collapses to a hamburger menu below 768px, and slide-in panels become full-screen modals on mobile. The KPI cards should stack vertically on narrow screens.

### 9. Color Contrast on Warning Callouts

**Problem:** The warm-red callout pills on contracts (e.g., "Contract expired Dec 31, 2025 — vendor operating without agreement") use a light red background with darker red text. While visually distinctive, the contrast between the background and text could be tighter for accessibility. Similarly, the gold "FEATURED GUIDE" badge text is small and may be hard to read.

**Recommendation:** Run the callout color combinations through a WCAG AA contrast checker. Aim for at least 4.5:1 contrast ratio on all text. The gold-on-cream combinations throughout the site should be verified.

### 10. Peer Group Context Could Be More Prominent

**Problem:** The "PEER GROUP: 48 post-war coops in Midtown Manhattan, 125+ units" line sits quietly below the KPI cards. This is actually crucial context — it's the basis for every "Above Market" and "Below Market" comparison on the page. Most board members won't notice it.

**Recommendation:** Consider making the peer group a more prominent element, perhaps as a subtle banner or incorporated into the Vendor Intelligence header. When a board member sees "99th percentile," they should immediately understand "compared to what."

---

## Summary

BoardIQ's dashboard is a strong, differentiated product with genuine intelligence value. The warm editorial design, personalized compliance data, vendor benchmarking, and AI-powered contract analysis create a compelling experience for NYC co-op and condo boards. The new Education Center adds meaningful depth with the personalized callouts being a standout feature.

The primary areas for improvement center on information density (the page is very long), interaction consistency (some sections open panels, others don't), and surfacing building-specific relevance earlier in the user flow. The visual design is cohesive and well-executed — refinements should focus on usability patterns and progressive disclosure rather than aesthetic changes.

**Priority fixes (highest impact, lowest effort):**

1. Make contract cards clickable with a detail panel
2. Add building-relevance indicators to Education guide cards
3. Rotate the featured guide based on most urgent deadline
4. Enrich the vendor detail panel with more context
5. Add "jump to section" behavior to sidebar nav clicks
