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

# Pre-war multipliers (older buildings often cost more to maintain)
ERA_MULTIPLIERS = {
    "prewar":   1.10,
    "postwar":  1.00,
}

# Ownership type multipliers
TYPE_MULTIPLIERS = {
    "coop":   1.00,
    "condo":  0.97,  # Condos often have slightly lower shared service costs
}


def get_neighborhood_cluster(neighborhood: str, borough: str) -> str:
    """Map a neighborhood to its pricing cluster."""
    for cluster, neighborhoods in NEIGHBORHOOD_CLUSTERS.items():
        if neighborhood in neighborhoods:
            return cluster
    # Fallback by borough
    fallback = {
        "Manhattan": "MIDTOWN",
        "Brooklyn":  "BK_OTHER",
        "Queens":    "QNS_PRIME",
        "Bronx":     "BX_SI",
        "Staten Island": "BX_SI",
    }
    return fallback.get(borough, "MIDTOWN")


def get_size_bucket(units: int) -> str:
    if units < 50:
        return "small"
    elif units < 125:
        return "medium"
    else:
        return "large"


def get_peer_group_description(units: int, neighborhood: str, borough: str,
                                is_prewar: bool, building_type: str) -> dict:
    """Build a human-readable description of the peer group used for comparison."""
    cluster = get_neighborhood_cluster(neighborhood, borough)
    size = get_size_bucket(units)
    era = "pre-war" if is_prewar else "post-war"
    btype = building_type.lower()

    size_labels = {"small": "20–50 units", "medium": "50–125 units", "large": "125+ units"}
    cluster_labels = {
        "UWS_UES":   "Upper West / Upper East Side",
        "MIDTOWN":   "Midtown Manhattan",
        "DOWNTOWN":  "Downtown Manhattan",
        "LES_EV":    "Lower East Side / East Village",
        "BK_PRIME":  "Prime Brooklyn",
        "BK_OTHER":  "Brooklyn",
        "QNS_PRIME": "Queens",
        "BX_SI":     "Bronx / Staten Island",
    }

    # Approximate peer building count (seeded, realistic-feeling numbers)
    peer_counts = {
        "UWS_UES": {"small": 112, "medium": 89, "large": 64},
        "MIDTOWN":  {"small": 87,  "medium": 71, "large": 48},
        "DOWNTOWN": {"small": 94,  "medium": 62, "large": 31},
        "LES_EV":   {"small": 78,  "medium": 44, "large": 18},
        "BK_PRIME": {"small": 103, "medium": 67, "large": 29},
        "BK_OTHER": {"small": 95,  "medium": 58, "large": 22},
        "QNS_PRIME":{"small": 74,  "medium": 49, "large": 21},
        "BX_SI":    {"small": 61,  "medium": 38, "large": 14},
    }
    peer_n = peer_counts.get(cluster, {}).get(size, 45)

    return {
        "cluster": cluster,
        "cluster_label": cluster_labels.get(cluster, cluster),
        "size_bucket": size,
        "size_label": size_labels[size],
        "era": era,
        "building_type": btype,
        "peer_building_count": peer_n,
        "description": (
            f"{peer_n} {era} {btype}s in {cluster_labels.get(cluster, cluster)}, "
            f"{size_labels[size]}"
        ),
        "multiplier": (
            CLUSTER_MULTIPLIERS.get(cluster, 1.0) *
            ERA_MULTIPLIERS.get("prewar" if is_prewar else "postwar", 1.0) *
            TYPE_MULTIPLIERS.get(btype, 1.0)
        ),
    }


# ── Baseline benchmark data (medium, UWS/UES, post-war, co-op) ───────────────
# All multipliers adjust from this baseline. Values are per-unit-per-year ($).

BASELINE_BENCHMARKS = {
    "ELEVATOR_MAINTENANCE": {
        "description": "Elevator maintenance contract",
        "unit": "per_unit_annual",
        "by_size": {
            "small":  {"p25": 230, "p50": 310, "p75": 405, "p90": 510},
            "medium": {"p25": 245, "p50": 350, "p75": 440, "p90": 560},
            "large":  {"p25": 195, "p50": 285, "p75": 365, "p90": 450},
        },
        "factors": ["Number of cabs", "Equipment age", "Hours of coverage", "Modernization status"],
    },
    "INSURANCE": {
        "description": "Building insurance (property & liability)",
        "unit": "per_unit_annual",
        "by_size": {
            "small":  {"p25": 540, "p50": 700, "p75": 845, "p90": 1010},
            "medium": {"p25": 505, "p50": 655, "p75": 810, "p90": 965},
            "large":  {"p25": 455, "p50": 595, "p75": 730, "p90": 880},
        },
        "factors": ["Building age", "Construction type", "Coverage limits", "Claims history", "Broker"],
    },
    "CLEANING": {
        "description": "Janitorial / cleaning services",
        "unit": "per_unit_annual",
        "by_size": {
            "small":  {"p25": 335, "p50": 435, "p75": 535, "p90": 665},
            "medium": {"p25": 350, "p50": 455, "p75": 555, "p90": 695},
            "large":  {"p25": 300, "p50": 400, "p75": 495, "p90": 595},
        },
        "factors": ["Doorman vs non-doorman", "Frequency", "Staffing overlap", "Square footage"],
    },
    "BOILER_MAINTENANCE": {
        "description": "Boiler / HVAC maintenance contract",
        "unit": "per_unit_annual",
        "by_size": {
            "small":  {"p25": 90,  "p50": 125, "p75": 168, "p90": 218},
            "medium": {"p25": 95,  "p50": 135, "p75": 180, "p90": 238},
            "large":  {"p25": 78,  "p50": 115, "p75": 155, "p90": 202},
        },
        "factors": ["Number of boilers", "System type (steam/hot water)", "Age", "Coverage scope"],
    },
    "EXTERMINATING": {
        "description": "Pest control / exterminating",
        "unit": "per_unit_annual",
        "by_size": {
            "small":  {"p25": 40, "p50": 58, "p75": 82,  "p90": 110},
            "medium": {"p25": 37, "p50": 53, "p75": 75,  "p90": 99},
            "large":  {"p25": 30, "p50": 44, "p75": 65,  "p90": 86},
        },
        "factors": ["Monthly vs quarterly", "Building age", "Common area size"],
    },
    "WATER_TREATMENT": {
        "description": "Water treatment (Legionella / cooling towers)",
        "unit": "per_unit_annual",
        "by_size": {
            "small":  {"p25": 44, "p50": 63, "p75": 85,  "p90": 115},
            "medium": {"p25": 50, "p50": 68, "p75": 91,  "p90": 124},
            "large":  {"p25": 40, "p50": 57, "p75": 78,  "p90": 104},
        },
        "factors": ["Tower count", "Testing frequency", "System complexity"],
    },
    "WASTE_REMOVAL": {
        "description": "Waste / trash removal",
        "unit": "per_unit_annual",
        "by_size": {
            "small":  {"p25": 95,  "p50": 135, "p75": 182, "p90": 238},
            "medium": {"p25": 100, "p50": 140, "p75": 188, "p90": 248},
            "large":  {"p25": 83,  "p50": 120, "p75": 161, "p90": 208},
        },
        "factors": ["Pickup frequency", "Recycling included", "Compactor maintenance"],
    },
    "MANAGEMENT_FEE": {
        "description": "Property management fee",
        "unit": "per_unit_annual",
        "by_size": {
            "small":  {"p25": 600, "p50": 740, "p75": 915, "p90": 1125},
            "medium": {"p25": 555, "p50": 698, "p75": 862, "p90": 1045},
            "large":  {"p25": 494, "p50": 626, "p75": 779, "p90": 943},
        },
        "factors": ["Services included", "Building complexity", "Staff oversight", "Market rate"],
    },
    "FACADE_INSPECTION": {
        "description": "FISP / LL11 facade inspection",
        "unit": "per_project",
        "by_size": {
            "small":  {"p25": 9200,  "p50": 13300, "p75": 18400, "p90": 25500},
            "medium": {"p25": 12300, "p50": 17400, "p75": 23500, "p90": 32700},
            "large":  {"p25": 16400, "p50": 22500, "p75": 30700, "p90": 43000},
        },
        "factors": ["Building height", "Facade material", "Scope", "Remediation required"],
    },
    "ENERGY_AUDIT": {
        "description": "LL87 energy audit & retro-commissioning",
        "unit": "per_project",
        "by_size": {
            "small":  {"p25": 6100,  "p50": 9200,  "p75": 13300, "p90": 18400},
            "medium": {"p25": 8200,  "p50": 12300, "p75": 17400, "p90": 24500},
            "large":  {"p25": 12300, "p50": 18400, "p75": 26500, "p90": 36700},
        },
        "factors": ["Building size", "Systems complexity", "Bundled with LL97 prep"],
    },
}


def apply_peer_multiplier(benchmarks: dict, multiplier: float) -> dict:
    """Scale all p-values in a benchmark dict by the peer group multiplier."""
    return {
        k: round(v * multiplier) if isinstance(v, (int, float)) else v
        for k, v in benchmarks.items()
    }


def calculate_percentile(value: float, p25: float, p50: float,
                          p75: float, p90: float) -> int:
    """Estimate percentile for a given value against benchmark distribution."""
    if value <= p25:
        return max(5, int(25 * value / p25))
    elif value <= p50:
        return int(25 + 25 * (value - p25) / (p50 - p25))
    elif value <= p75:
        return int(50 + 25 * (value - p50) / (p75 - p50))
    elif value <= p90:
        return int(75 + 15 * (value - p75) / (p90 - p75))
    else:
        return min(99, int(90 + 9 * (value - p90) / (p90 * 0.3)))


def get_status(percentile: int) -> dict:
    """Convert percentile to dashboard status."""
    if percentile >= 80:
        return {"status": "ABOVE_MARKET", "label": "Above Market",
                "color": "red", "icon": "↑", "action_recommended": True}
    elif percentile >= 60:
        return {"status": "SLIGHTLY_ABOVE", "label": "Slightly Above",
                "color": "yellow", "icon": "↑", "action_recommended": True}
    elif percentile >= 40:
        return {"status": "AT_MARKET", "label": "At Market",
                "color": "green", "icon": "✓", "action_recommended": False}
    else:
        return {"status": "BELOW_MARKET", "label": "Below Market",
                "color": "green", "icon": "✓", "action_recommended": False}


def benchmark_building(vendor_summary: dict, units: int = 100,
                        last_bid_years: Optional[dict] = None,
                        neighborhood: str = "Upper West Side",
                        borough: str = "Manhattan",
                        is_prewar: bool = True,
                        building_type: str = "coop") -> dict:
    """
    Main benchmarking function.

    Takes the output of invoice_pipeline.aggregate_by_vendor() and returns
    a complete benchmarking report against the building's specific peer group.

    vendor_summary : {category: {vendor_name, total_annual, per_unit_annual}}
    units          : residential unit count
    last_bid_years : {category: year_last_bid}  (optional)
    neighborhood   : building neighborhood (e.g. "Upper West Side")
    borough        : Manhattan / Brooklyn / Queens / Bronx / Staten Island
    is_prewar      : True if building was built before 1945
    building_type  : "coop" or "condo"
    """
    size_bucket = get_size_bucket(units)
    peer_group = get_peer_group_description(units, neighborhood, borough,
                                             is_prewar, building_type)
    multiplier = peer_group["multiplier"]

    results = []
    total_savings_opportunity = 0
    total_annual_spend = 0

    for category, baseline in BASELINE_BENCHMARKS.items():
        if baseline["unit"] != "per_unit_annual":
            continue

        raw_bench = baseline["by_size"].get(size_bucket,
                                             baseline["by_size"]["medium"])
        bench = apply_peer_multiplier(raw_bench, multiplier)
        p25, p50, p75, p90 = bench["p25"], bench["p50"], bench["p75"], bench["p90"]

        # Find this category in the building's vendor data
        building_spend = None
        vendor_name = None
        for key, data in vendor_summary.items():
            if data.get("category") == category:
                building_spend = data.get("per_unit_annual", 0)
                vendor_name = data.get("vendor_name", "Unknown")
                break

        if building_spend is None:
            results.append({
                "category": category,
                "category_label": baseline["description"],
                "vendor_name": None,
                "annual_spend": None,
                "per_unit": None,
                "peer_median": p50,
                "peer_p25": p25,
                "peer_p75": p75,
                "peer_p90": p90,
                "percentile": None,
                "status": {"status": "NO_DATA", "label": "No Data", "color": "gray"},
                "savings_opportunity_annual": 0,
                "n_peer_buildings": peer_group["peer_building_count"],
            })
            continue

        annual_spend = building_spend * units
        total_annual_spend += annual_spend
        percentile = calculate_percentile(building_spend, p25, p50, p75, p90)
        status = get_status(percentile)

        savings_per_unit = max(0, building_spend - p50)
        savings_annual = round(savings_per_unit * units, 0)
        if status["action_recommended"]:
            total_savings_opportunity += savings_annual

        last_bid_year = (last_bid_years or {}).get(category)
        years_since_bid = None
        if last_bid_year:
            from datetime import datetime
            years_since_bid = datetime.now().year - int(last_bid_year)

        results.append({
            "category": category,
            "category_label": baseline["description"],
            "vendor_name": vendor_name,
            "annual_spend": round(annual_spend, 0),
            "per_unit": round(building_spend, 2),
            "peer_p25": p25,
            "peer_median": p50,
            "peer_p75": p75,
            "peer_p90": p90,
            "percentile": percentile,
            "status": status,
            "savings_opportunity_annual": savings_annual,
            "savings_opportunity_per_unit": round(savings_per_unit, 2),
            "n_peer_buildings": peer_group["peer_building_count"],
            "factors": baseline["factors"],
            "years_since_bid": years_since_bid,
            "last_bid_year": last_bid_year,
        })

    # Sort: above market first, then by savings
    results.sort(key=lambda x: (
        0 if x["status"].get("status") == "ABOVE_MARKET" else
        1 if x["status"].get("status") == "SLIGHTLY_ABOVE" else 2,
        -(x.get("savings_opportunity_annual") or 0)
    ))

    opportunities = [r for r in results
                     if r.get("savings_opportunity_annual", 0) > 0][:3]

    return {
        "units": units,
        "size_bucket": size_bucket,
        "peer_group": peer_group,
        "total_annual_spend_benchmarked": round(total_annual_spend, 0),
        "total_savings_opportunity": round(total_savings_opportunity, 0),
        "savings_per_unit": round(total_savings_opportunity / units, 0) if units else 0,
        "net_savings_after_fee": round(total_savings_opportunity * 0.75, 0),
        "subscription_roi": round(total_savings_opportunity / (350 * 12), 1),
        "vendor_benchmarks": results,
        "top_opportunities": opportunities,
        "above_market_count": sum(1 for r in results
                                   if r["status"].get("action_recommended")),
        "at_or_below_count": sum(1 for r in results
                                  if not r["status"].get("action_recommended")
                                  and r["status"].get("status") != "NO_DATA"),
    }


# ── Backwards compatibility shim ─────────────────────────────────────────────
# The old engine used NETWORK_BENCHMARKS. Keep it accessible so existing
# app.py imports don't break while we migrate.
NETWORK_BENCHMARKS = BASELINE_BENCHMARKS


if __name__ == "__main__":
    # Demo: Gramercy Plaza — 130 East 18th Street, 113 units, pre-war co-op
    print("=" * 65)
    print("  BOARDIQ PEER-GROUP BENCHMARKING DEMO")
    print("  130 East 18th Street · Gramercy · 113 units · Pre-war Co-op")
    print("=" * 65)

    # Simulated vendor data as if extracted from uploaded invoices
    vendor_data = {
        "Schindler::ELEVATOR_MAINTENANCE": {
            "category": "ELEVATOR_MAINTENANCE",
            "vendor_name": "Schindler Elevator",
            "per_unit_annual": 480,
        },
        "AIG::INSURANCE": {
            "category": "INSURANCE",
            "vendor_name": "AIG Building Insurance",
            "per_unit_annual": 890,
        },
        "CleanTech::CLEANING": {
            "category": "CLEANING",
            "vendor_name": "CleanTech Services",
            "per_unit_annual": 395,
        },
        "BronxBoiler::BOILER_MAINTENANCE": {
            "category": "BOILER_MAINTENANCE",
            "vendor_name": "Reliable Mechanical",
            "per_unit_annual": 155,
        },
        "Orkin::EXTERMINATING": {
            "category": "EXTERMINATING",
            "vendor_name": "Orkin Pest Control",
            "per_unit_annual": 48,
        },
        "ACME::MANAGEMENT_FEE": {
            "category": "MANAGEMENT_FEE",
            "vendor_name": "AKAM Associates",
            "per_unit_annual": 920,
        },
        "WasteNY::WASTE_REMOVAL": {
            "category": "WASTE_REMOVAL",
            "vendor_name": "Waste Management NY",
            "per_unit_annual": 118,
        },
    }

    last_bids = {
        "ELEVATOR_MAINTENANCE": 2016,
        "INSURANCE": 2021,
        "MANAGEMENT_FEE": 2019,
        "CLEANING": 2023,
    }

    report = benchmark_building(
        vendor_summary=vendor_data,
        units=113,
        last_bid_years=last_bids,
        neighborhood="Gramercy",
        borough="Manhattan",
        is_prewar=True,
        building_type="coop",
    )

    pg = report["peer_group"]
    print(f"\n  Peer Group: {pg['description']}")
    print(f"  Pricing adjusted for: {pg['cluster_label']} · pre-war · co-op")
    print(f"  Multiplier vs baseline: {pg['multiplier']:.2f}x\n")

    print(f"  {'VENDOR CATEGORY':<38} {'YOURS':>7} {'PEER MED':>9} {'PCTILE':>7}  STATUS")
    print(f"  {'-'*38} {'-'*7} {'-'*9} {'-'*7}  {'-'*20}")

    for r in report["vendor_benchmarks"]:
        if r.get("per_unit") is None:
            continue
        icon = r["status"]["icon"]
        label = r["status"]["label"]
        print(f"  {r['category_label'][:38]:<38} "
              f"${r['per_unit']:>5.0f}  "
              f"${r['peer_median']:>7}  "
              f"{r['percentile']:>5}th  "
              f"{icon} {label}")

    print()
    print(f"  TOTAL SAVINGS VS PEER MEDIAN:  ${report['total_savings_opportunity']:,.0f}/year")
    print(f"  NET AFTER 25% SUCCESS FEE:     ${report['net_savings_after_fee']:,.0f}/year")
    print(f"  Contracts above market:        {report['above_market_count']}")
    print()
    print("  TOP OPPORTUNITIES:")
    for i, opp in enumerate(report["top_opportunities"], 1):
        yrs = f" — not rebid since {opp['last_bid_year']}" if opp.get("last_bid_year") else ""
        print(f"  {i}. {opp['category_label']}{yrs}")
        print(f"     You: ${opp['per_unit']:.0f}/unit  |  Peer median: ${opp['peer_median']}/unit")
        print(f"     Potential savings: ${opp['savings_opportunity_annual']:,.0f}/year")
    print("=" * 65)
