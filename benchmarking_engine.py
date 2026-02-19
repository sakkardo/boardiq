"""
BoardIQ — Benchmarking Engine (v2 — Peer Group Edition)
=========================================================
Compares a building's vendor pricing against a curated peer group:
  • Similar building size (units within ±50%)
  • Same borough / neighborhood cluster
  • Same era (pre-war vs post-war)
  • Same ownership type (co-op vs condo)

In production: peer_data comes from the aggregated invoice database.
In MVP/demo: uses realistic seed data with peer-group-specific pricing.
All values are per-unit-per-year in dollars unless noted.
"""

import json
from typing import Optional

# ── Neighborhood clusters ─────────────────────────────────────────────────────
# Neighborhoods are grouped into clusters that share similar real estate
# dynamics and vendor pricing. Pricing adjusts by cluster.

NEIGHBORHOOD_CLUSTERS = {
    "UWS_UES":    ["Upper West Side", "Upper East Side", "Morningside Heights",
                   "Carnegie Hill", "Yorkville", "Lenox Hill"],
    "MIDTOWN":    ["Midtown West", "Midtown East", "Murray Hill", "Turtle Bay",
                   "Hell's Kitchen", "Gramercy", "Kips Bay", "Sutton Place"],
    "DOWNTOWN":   ["Greenwich Village", "West Village", "SoHo", "TriBeCa",
                   "Flatiron", "Chelsea", "NoHo", "Nolita", "Little Italy"],
    "LES_EV":     ["Lower East Side", "East Village", "Alphabet City"],
    "BK_PRIME":   ["Park Slope", "Brooklyn Heights", "Cobble Hill", "Carroll Gardens",
                   "Boerum Hill", "DUMBO", "Fort Greene", "Prospect Heights"],
    "BK_OTHER":   ["Williamsburg", "Greenpoint", "Bushwick", "Crown Heights",
                   "Bay Ridge", "Sunset Park", "Flatbush", "Prospect Lefferts Gardens"],
    "QNS_PRIME":  ["Astoria", "Long Island City", "Jackson Heights", "Sunnyside",
                   "Forest Hills", "Rego Park", "Flushing"],
    "BX_SI":      ["Riverdale", "Fordham", "Pelham Bay", "Concourse",
                   "St. George", "Stapleton"],
}

# Cluster pricing multipliers vs baseline (medium UWS/UES building)
CLUSTER_MULTIPLIERS = {
    "UWS_UES":   1.00,
    "MIDTOWN":   1.05,
    "DOWNTOWN":  1.08,
    "LES_EV":    0.92,
    "BK_PRIME":  0.95,
    "BK_OTHER":  0.87,
    "QNS_PRIME": 0.85,
    "BX_SI":     0.80,
}