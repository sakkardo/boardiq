"""
BoardIQ — Benchmarking Engine
================================
Compares a building's vendor spend against the network of comparable buildings.
Returns percentile rankings, savings opportunities, and market position.

In production: network_data comes from the aggregated database of all buildings.
In MVP/demo: uses realistic seed data based on actual NYC market knowledge.
"""

import json
from typing import Optional

# ── Seed benchmarking data ────────────────────────────────────────────────────
# Based on real NYC co-op/condo market knowledge.
# In production this comes from the aggregated invoice database.
# Structured as: category → building_size_bucket → {p25, p50, p75, p90, sample_count}
# All values are per-unit-per-year in dollars.

NETWORK_BENCHMARKS = {
    "ELEVATOR_MAINTENANCE": {
        "description": "Monthly elevator maintenance contract (per unit per year)",
        "unit": "per_unit_annual",
        "by_size": {
            "small":   {"units_range": (20, 75),   "p25": 210, "p50": 290, "p75": 380, "p90": 480, "n": 34},
            "medium":  {"units_range": (75, 200),  "p25": 240, "p50": 345, "p75": 430, "p90": 550, "n": 67},
            "large":   {"units_range": (200, 500), "p25": 190, "p50": 280, "p75": 360, "p90": 440, "n": 29},
        },
        "factors": ["Number of elevator cabs", "Age of equipment", "Hours of coverage", "Location"],
        "last_updated": "2025-Q4",
    },
    "INSURANCE": {
        "description": "Building insurance annual premium (per unit per year)",
        "unit": "per_unit_annual",
        "by_size": {
            "small":   {"units_range": (20, 75),   "p25": 520, "p50": 680, "p75": 820, "p90": 980, "n": 41},
            "medium":  {"units_range": (75, 200),  "p25": 490, "p50": 640, "p75": 790, "p90": 940, "n": 72},
            "large":   {"units_range": (200, 500), "p25": 440, "p50": 580, "p75": 710, "p90": 860, "n": 31},
        },
        "factors": ["Building age", "Construction type", "Coverage limits", "Claims history", "Broker"],
        "last_updated": "2025-Q4",
    },
    "CLEANING": {
        "description": "Janitorial/cleaning services (per unit per year)",
        "unit": "per_unit_annual",
        "by_size": {
            "small":   {"units_range": (20, 75),   "p25": 320, "p50": 420, "p75": 520, "p90": 650, "n": 38},
            "medium":  {"units_range": (75, 200),  "p25": 340, "p50": 440, "p75": 540, "p90": 680, "n": 64},
            "large":   {"units_range": (200, 500), "p25": 290, "p50": 390, "p75": 480, "p90": 580, "n": 22},
        },
        "factors": ["Doorman vs non-doorman", "Frequency", "Square footage", "Staff included"],
        "last_updated": "2025-Q4",
    },
    "BOILER_MAINTENANCE": {
        "description": "Boiler/HVAC maintenance contract (per unit per year)",
        "unit": "per_unit_annual",
        "by_size": {
            "small":   {"units_range": (20, 75),   "p25": 85, "p50": 120, "p75": 160, "p90": 210, "n": 36},
            "medium":  {"units_range": (75, 200),  "p25": 90, "p50": 130, "p75": 175, "p90": 230, "n": 58},
            "large":   {"units_range": (200, 500), "p25": 75, "p50": 110, "p75": 150, "p90": 195, "n": 24},
        },
        "factors": ["Number of boilers", "System type", "Age", "Coverage scope"],
        "last_updated": "2025-Q4",
    },
    "EXTERMINATING": {
        "description": "Pest control/exterminating (per unit per year)",
        "unit": "per_unit_annual",
        "by_size": {
            "small":   {"units_range": (20, 75),   "p25": 38, "p50": 55, "p75": 78, "p90": 105, "n": 44},
            "medium":  {"units_range": (75, 200),  "p25": 35, "p50": 50, "p75": 72, "p90": 95,  "n": 71},
            "large":   {"units_range": (200, 500), "p25": 28, "p50": 42, "p75": 62, "p90": 82,  "n": 28},
        },
        "factors": ["Monthly vs quarterly", "Building age", "Pest history"],
        "last_updated": "2025-Q4",
    },
    "WATER_TREATMENT": {
        "description": "Water treatment services (per unit per year)",
        "unit": "per_unit_annual",
        "by_size": {
            "small":   {"units_range": (20, 75),   "p25": 42, "p50": 60, "p75": 82, "p90": 110, "n": 29},
            "medium":  {"units_range": (75, 200),  "p25": 48, "p50": 65, "p75": 88, "p90": 120, "n": 47},
            "large":   {"units_range": (200, 500), "p25": 38, "p50": 55, "p75": 75, "p90": 100, "n": 19},
        },
        "factors": ["Tower count", "Legionella testing frequency", "System type"],
        "last_updated": "2025-Q4",
    },
    "WASTE_REMOVAL": {
        "description": "Waste/trash removal (per unit per year)",
        "unit": "per_unit_annual",
        "by_size": {
            "small":   {"units_range": (20, 75),   "p25": 90, "p50": 130, "p75": 175, "p90": 230, "n": 32},
            "medium":  {"units_range": (75, 200),  "p25": 95, "p50": 135, "p75": 180, "p90": 240, "n": 53},
            "large":   {"units_range": (200, 500), "p25": 80, "p50": 115, "p75": 155, "p90": 200, "n": 21},
        },
        "factors": ["Pickup frequency", "Recycling included", "Compactor maintenance"],
        "last_updated": "2025-Q4",
    },
    "MANAGEMENT_FEE": {
        "description": "Property management fee (per unit per year)",
        "unit": "per_unit_annual",
        "by_size": {
            "small":   {"units_range": (20, 75),   "p25": 580, "p50": 720, "p75": 890, "p90": 1100, "n": 38},
            "medium":  {"units_range": (75, 200),  "p25": 540, "p50": 680, "p75": 840, "p90": 1020, "n": 61},
            "large":   {"units_range": (200, 500), "p25": 480, "p50": 610, "p75": 760, "p90": 920,  "n": 25},
        },
        "factors": ["Services included", "Building complexity", "Staff oversight"],
        "last_updated": "2025-Q4",
    },
    # Compliance cost benchmarks
    "FACADE_INSPECTION": {
        "description": "FISP/LL11 facade inspection and filing",
        "unit": "per_project",
        "by_size": {
            "small":   {"units_range": (20, 75),   "p25": 9000,  "p50": 13000, "p75": 18000, "p90": 25000, "n": 18},
            "medium":  {"units_range": (75, 200),  "p25": 12000, "p50": 17000, "p75": 23000, "p90": 32000, "n": 23},
            "large":   {"units_range": (200, 500), "p25": 16000, "p50": 22000, "p75": 30000, "p90": 42000, "n": 12},
        },
        "factors": ["Building height", "Facade material", "Scope of inspection", "Remediation required"],
        "last_updated": "2025-Q4",
    },
    "ENERGY_AUDIT": {
        "description": "LL87 energy audit and retro-commissioning",
        "unit": "per_project",
        "by_size": {
            "small":   {"units_range": (20, 75),   "p25": 6000,  "p50": 9000,  "p75": 13000, "p90": 18000, "n": 22},
            "medium":  {"units_range": (75, 200),  "p25": 8000,  "p50": 12000, "p75": 17000, "p90": 24000, "n": 41},
            "large":   {"units_range": (200, 500), "p25": 12000, "p50": 18000, "p75": 26000, "p90": 36000, "n": 19},
        },
        "factors": ["Building size", "Systems complexity", "Bundled with LL97"],
        "last_updated": "2025-Q4",
    },
}


def get_size_bucket(units: int) -> str:
    if units < 75:
        return "small"
    elif units < 200:
        return "medium"
    else:
        return "large"


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
                        last_bid_years: Optional[dict] = None) -> dict:
    """
    Main benchmarking function.
    Takes the output of invoice_pipeline.aggregate_by_vendor()
    and returns a complete benchmarking report for the dashboard.

    vendor_summary: {category: {vendor_name, total_annual, per_unit_annual}}
    units: residential unit count
    last_bid_years: {category: year_last_bid} — optional, from contract records
    """
    size_bucket = get_size_bucket(units)
    results = []
    total_savings_opportunity = 0
    total_annual_spend = 0

    for category, benchmark in NETWORK_BENCHMARKS.items():
        # Skip compliance categories — handled separately
        if benchmark["unit"] != "per_unit_annual":
            continue

        bench = benchmark["by_size"].get(size_bucket, benchmark["by_size"]["medium"])
        p25, p50, p75, p90 = bench["p25"], bench["p50"], bench["p75"], bench["p90"]
        n_buildings = bench["n"]

        # Find this category in the building's vendor data
        building_spend = None
        vendor_name = None
        for key, data in vendor_summary.items():
            if data.get("category") == category:
                building_spend = data.get("per_unit_annual", 0)
                vendor_name = data.get("vendor_name", "Unknown")
                break

        if building_spend is None:
            # Category not found in building's data
            results.append({
                "category": category,
                "category_label": benchmark["description"],
                "vendor_name": None,
                "annual_spend": None,
                "per_unit": None,
                "network_median": p50,
                "percentile": None,
                "status": {"status": "NO_DATA", "label": "No Data", "color": "gray"},
                "savings_opportunity": 0,
                "n_buildings": n_buildings,
            })
            continue

        annual_spend = building_spend * units
        total_annual_spend += annual_spend
        percentile = calculate_percentile(building_spend, p25, p50, p75, p90)
        status = get_status(percentile)

        # Calculate savings opportunity vs median
        savings_per_unit = max(0, building_spend - p50)
        savings_annual = round(savings_per_unit * units, 0)
        if status["action_recommended"]:
            total_savings_opportunity += savings_annual

        # Years since last competitive bid
        last_bid_year = (last_bid_years or {}).get(category)
        years_since_bid = None
        if last_bid_year:
            from datetime import datetime
            years_since_bid = datetime.now().year - int(last_bid_year)

        results.append({
            "category": category,
            "category_label": benchmark["description"],
            "vendor_name": vendor_name,
            "annual_spend": round(annual_spend, 0),
            "per_unit": round(building_spend, 2),
            "network_p25": p25,
            "network_median": p50,
            "network_p75": p75,
            "network_p90": p90,
            "percentile": percentile,
            "status": status,
            "savings_opportunity_annual": savings_annual,
            "savings_opportunity_per_unit": round(savings_per_unit, 2),
            "n_buildings": n_buildings,
            "factors": benchmark["factors"],
            "years_since_bid": years_since_bid,
            "last_bid_year": last_bid_year,
        })

    # Sort: above market first, then by savings opportunity
    results.sort(key=lambda x: (
        0 if x["status"].get("status") == "ABOVE_MARKET" else
        1 if x["status"].get("status") == "SLIGHTLY_ABOVE" else 2,
        -(x.get("savings_opportunity_annual") or 0)
    ))

    # Top 3 opportunities
    opportunities = [r for r in results
                     if r.get("savings_opportunity_annual", 0) > 0][:3]

    return {
        "units": units,
        "size_bucket": size_bucket,
        "total_annual_spend_benchmarked": round(total_annual_spend, 0),
        "total_savings_opportunity": round(total_savings_opportunity, 0),
        "savings_per_unit": round(total_savings_opportunity / units, 0),
        "net_savings_after_fee": round(total_savings_opportunity * 0.75, 0),  # after 25% fee
        "subscription_roi": round(total_savings_opportunity / (350 * 12), 1),  # vs annual sub
        "vendor_benchmarks": results,
        "top_opportunities": opportunities,
        "above_market_count": sum(1 for r in results
                                   if r["status"].get("action_recommended")),
        "at_or_below_count": sum(1 for r in results
                                  if not r["status"].get("action_recommended")
                                  and r["status"].get("status") != "NO_DATA"),
    }


if __name__ == "__main__":
    # Demo: Run against the sample data from invoice_pipeline
    import sys
    sys.path.insert(0, ".")

    from invoice_pipeline import InvoiceProcessor, create_sample_csv

    print("Running full pipeline demo...\n")

    # Step 1: Process invoices
    proc = InvoiceProcessor()
    sample_file = create_sample_csv()
    summary = proc.process_file(sample_file, "BBL_1022150001", 120)

    # Flatten vendor data for benchmarking
    vendor_flat = {}
    for cat_key, cat_data in summary["by_category"].items():
        for vendor in cat_data["vendors"]:
            key = f"{vendor['vendor_name']}::{vendor['category']}"
            vendor_flat[key] = vendor

    # Step 2: Benchmark
    last_bids = {
        "ELEVATOR_MAINTENANCE": 2016,
        "INSURANCE": 2022,
        "CLEANING": 2023,
        "BOILER_MAINTENANCE": 2023,
        "EXTERMINATING": 2024,
        "WATER_TREATMENT": 2019,
        "WASTE_REMOVAL": 2024,
    }

    report = benchmark_building(vendor_flat, units=120, last_bid_years=last_bids)

    # Print results
    print("="*65)
    print("  BOARDIQ VENDOR BENCHMARKING REPORT")
    print("  120 West 72nd Street · 120 units · Upper West Side")
    print("="*65)
    print(f"  {'VENDOR CATEGORY':<35} {'PER UNIT':>8} {'MEDIAN':>8} {'PCTILE':>7}  STATUS")
    print(f"  {'-'*35} {'-'*8} {'-'*8} {'-'*7}  {'-'*20}")

    for r in report["vendor_benchmarks"]:
        if r.get("per_unit") is None:
            continue
        icon = r["status"]["icon"]
        label = r["status"]["label"]
        print(f"  {r['category_label'][:35]:<35} "
              f"${r['per_unit']:>6.0f}  "
              f"${r['network_median']:>6.0f}  "
              f"{r['percentile']:>5}th  "
              f"{icon} {label}")

    print()
    print(f"  TOTAL SAVINGS OPPORTUNITY:  ${report['total_savings_opportunity']:,.0f}/year")
    print(f"  NET AFTER 25% SUCCESS FEE:  ${report['net_savings_after_fee']:,.0f}/year")
    print(f"  SUBSCRIPTION ROI:           {report['subscription_roi']}x")
    print()
    print(f"  Contracts above market:     {report['above_market_count']}")
    print(f"  Contracts at/below market:  {report['at_or_below_count']}")
    print()
    print("  TOP OPPORTUNITIES:")
    for i, opp in enumerate(report["top_opportunities"], 1):
        yrs = f" (no bid in {opp['years_since_bid']} years)" if opp.get("years_since_bid") else ""
        print(f"  {i}. {opp['category_label']}{yrs}")
        print(f"     You pay ${opp['per_unit']:.0f}/unit vs median ${opp['network_median']}/unit")
        print(f"     Savings opportunity: ${opp['savings_opportunity_annual']:,.0f}/year")
    print("="*65)
