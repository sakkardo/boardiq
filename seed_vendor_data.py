"""
Seed realistic vendor data for all Century Management buildings.
Uses benchmark percentile ranges from benchmarking_engine.py and real NYC vendor names.
Run once: python seed_vendor_data.py
"""

import random
import json
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

# Real NYC vendor names by category
VENDOR_POOL = {
    "ELEVATOR_MAINTENANCE": [
        "Schindler Elevator Corp", "Otis Elevator Company", "ThyssenKrupp Elevator",
        "KONE Inc.", "PS Marcato Elevator Company", "Champion Elevator Corp",
        "New York Elevator & Electrical", "National Elevator Inspection Services",
        "Liberty Elevator Corp", "Eastern Elevator Co",
    ],
    "INSURANCE": [
        "AmTrust Insurance Group", "Chubb Insurance", "New York-Alliant Insurance Services",
        "Hub International Northeast", "The Greenpoint Agency", "Mackoul & Associates",
        "Lovell Safety Management", "USI Insurance Services", "Brown & Brown of NY",
        "Marsh McLennan Agency",
    ],
    "CLEANING": [
        "Clean Star Services", "Gold Star Cleaning", "Planned Companies",
        "Pritchard Industries", "Able Services / ABM", "National Cleaning Corp",
        "Mop Squad Cleaning", "Pro-Tek Maintenance Corp", "ABC Maintenance Inc",
        "Metro Building Services",
    ],
    "BOILER_MAINTENANCE": [
        "Empire Boiler Service", "Five Star Boiler", "Mechanical Solutions Inc",
        "NYC Combustion Corp", "A&G Steam Corp", "Controlled Combustion Corp",
        "New York Boiler Works", "Reliable Mechanical Corp", "Atlas Boiler Works",
        "Manhattan Boiler & Equipment",
    ],
    "EXTERMINATING": [
        "Apex Exterminating", "Dial-A-Bug Pest Control", "Magic Exterminating",
        "Standard Pest Management", "Broadway Exterminating", "Pest Pro Exterminating",
        "Metro Pest Control", "City-Wide Exterminating", "Flash Exterminating",
        "Guardian Pest Control",
    ],
    "WATER_TREATMENT": [
        "Metro Water Treatment", "Nalco Water (Ecolab)", "Guardian Water Treatment",
        "Clarity Water Technologies", "Kurita Water Industries", "H2O Innovation",
        "SUEZ Water Technologies", "Safe Water Technologies", "ChemTreat Inc",
        "Industrial Water Treatment Inc",
    ],
    "WASTE_REMOVAL": [
        "NYC Waste Solutions", "Action Carting Environmental Services",
        "Mr. T Carting Corp", "Filco Carting Corp", "Viking Sanitation",
        "Liberty Ashes Inc", "Five Star Carting", "Interstate Waste Services",
        "Royal Waste Services", "Waste Management of NY",
    ],
    "MANAGEMENT_FEE": [
        "Century Management",  # All Century buildings use Century
    ],
    "HVAC_MAINTENANCE": [
        "Simon Industries, LLC", "Air Ideal Inc", "Arista Air Conditioning Corp",
        "Standard Refrigeration Co", "York International", "Trane Technologies",
        "Direct Air Group", "Air Temp Mechanical Services", "Cool-Temp Mechanical",
        "Metro HVAC Services",
    ],
    "PLUMBING_REPAIRS": [
        "Adriatic Plumbing & Heating", "Fred Smith Plumbing", "Kapnag Heating Corp",
        "Harris Plumbing & Heating", "JPR Plumbing & Heating", "A-1 Piping Inc",
        "Manhattan Mechanical Corp", "Roto-Rooter Plumbing NYC", "Metro Plumbing & Heating",
        "Varsity Plumbing & Heating",
    ],
    "LANDSCAPING": [
        "Elevated Outdoors / Ariston Flowers", "SavATree", "Dragonetti Brothers Florist",
        "New York Plantings Garden Design", "M&M Environmental", "Green Horizons Landscaping",
        "Brooklyn Plantology", "Manhattan Landscaping Inc", "Garden Design Associates",
        "Urban Roots NYC",
    ],
    "UTILITIES_ELECTRIC": [
        "Con Edison",
    ],
    "UTILITIES_WATER": [
        "NYC Water Board",
    ],
    "SECURITY": [
        "Allied Universal Security", "Securitas Security Services",
        "GardaWorld Security", "Kastle Systems", "Summit Security Services",
        "FJC Security Services", "Mulligan Security Corp", "Advance Security Concepts",
        "Borg Security Services", "Intercontinental Security",
    ],
    "PROFESSIONAL_SERVICES": [
        "Metric Consulting and Inspection", "RAND Engineering & Architecture",
        "Falcon Engineering Architecture", "Howard L. Zimmerman Architects",
        "Superstructures Engineers", "Philip Habib & Associates",
        "Langan Engineering", "WSP USA", "AKRF Inc", "VHB Engineering",
    ],
    "ENVIRONMENTAL": [
        "Innovacore Environmental", "Environmental Consulting & Management",
        "Langan Environmental", "Roux Associates", "Cornerstone Environmental Group",
    ],
}

# Per-unit annual cost ranges by category and building size
# Derived from BASELINE_BENCHMARKS p25-p90 ranges in benchmarking_engine.py
# with some spread for realism
COST_RANGES = {
    #                       small (≤50u)         medium (51-150u)     large (>150u)
    "ELEVATOR_MAINTENANCE": {"small": (200, 550), "medium": (220, 580), "large": (170, 480)},
    "INSURANCE":            {"small": (480, 1050), "medium": (450, 1000), "large": (400, 920)},
    "CLEANING":             {"small": (300, 700), "medium": (310, 720), "large": (270, 630)},
    "BOILER_MAINTENANCE":   {"small": (80, 230), "medium": (85, 250), "large": (68, 215)},
    "EXTERMINATING":        {"small": (35, 120), "medium": (32, 108), "large": (25, 92)},
    "WATER_TREATMENT":      {"small": (38, 122), "medium": (44, 132), "large": (34, 110)},
    "WASTE_REMOVAL":        {"small": (85, 250), "medium": (90, 260), "large": (74, 220)},
    "MANAGEMENT_FEE":       {"small": (550, 1180), "medium": (500, 1090), "large": (440, 990)},
    "HVAC_MAINTENANCE":     {"small": (95, 260), "medium": (100, 280), "large": (80, 230)},
    "PLUMBING_REPAIRS":     {"small": (120, 420), "medium": (130, 440), "large": (100, 390)},
    "LANDSCAPING":          {"small": (60, 200), "medium": (70, 220), "large": (55, 190)},
    "UTILITIES_ELECTRIC":   {"small": (1200, 2800), "medium": (1100, 2600), "large": (900, 2400)},
    "UTILITIES_WATER":      {"small": (350, 800), "medium": (320, 750), "large": (280, 680)},
    "SECURITY":             {"small": (180, 500), "medium": (200, 550), "large": (160, 480)},
    "PROFESSIONAL_SERVICES":{"small": (80, 220), "medium": (70, 200), "large": (55, 180)},
    "ENVIRONMENTAL":        {"small": (60, 200), "medium": (55, 190), "large": (45, 170)},
}

# Which categories each building should have (by probability)
# Every building gets core services; some get extras based on characteristics
CORE_CATEGORIES = [
    "ELEVATOR_MAINTENANCE", "INSURANCE", "CLEANING", "BOILER_MAINTENANCE",
    "EXTERMINATING", "MANAGEMENT_FEE", "UTILITIES_ELECTRIC", "UTILITIES_WATER",
]
COMMON_CATEGORIES = [
    ("WASTE_REMOVAL", 0.85),
    ("WATER_TREATMENT", 0.70),
    ("HVAC_MAINTENANCE", 0.65),
    ("PLUMBING_REPAIRS", 0.55),
    ("SECURITY", 0.40),
]
OCCASIONAL_CATEGORIES = [
    ("LANDSCAPING", 0.25),
    ("PROFESSIONAL_SERVICES", 0.30),
    ("ENVIRONMENTAL", 0.20),
]


def size_bucket(units):
    if units <= 50:
        return "small"
    elif units <= 150:
        return "medium"
    return "large"


def generate_vendor_data(building):
    """Generate realistic vendor_data for a building based on its characteristics."""
    units = building.get("units", 50)
    year_built = building.get("year_built", 1960)
    floors = building.get("floors", 10)
    bucket = size_bucket(units)

    random.seed(hash(building.get("id", "") + building.get("address", "")))

    categories = list(CORE_CATEGORIES)

    for cat, prob in COMMON_CATEGORIES:
        if random.random() < prob:
            categories.append(cat)

    for cat, prob in OCCASIONAL_CATEGORIES:
        if random.random() < prob:
            categories.append(cat)

    # Older buildings more likely to have environmental/plumbing
    if year_built < 1945:
        if "PLUMBING_REPAIRS" not in categories and random.random() < 0.7:
            categories.append("PLUMBING_REPAIRS")
        if "ENVIRONMENTAL" not in categories and random.random() < 0.4:
            categories.append("ENVIRONMENTAL")

    # Taller buildings more likely to need security
    if floors >= 15 and "SECURITY" not in categories and random.random() < 0.5:
        categories.append("SECURITY")

    # Buildings with outdoor space get landscaping
    if units > 100 and "LANDSCAPING" not in categories and random.random() < 0.35:
        categories.append("LANDSCAPING")

    vendor_data = []
    for cat in categories:
        if cat not in COST_RANGES or cat not in VENDOR_POOL:
            continue

        cost_range = COST_RANGES[cat][bucket]
        # Use a slightly right-skewed distribution (most buildings cluster near median)
        per_unit = int(random.triangular(cost_range[0], cost_range[1],
                                          cost_range[0] + (cost_range[1] - cost_range[0]) * 0.45))

        annual = per_unit * units
        # Round to nearest $100 for realism
        annual = round(annual / 100) * 100

        vendor_name = random.choice(VENDOR_POOL[cat])

        # Last bid year: random 2018-2025, with management fees often older
        if cat == "MANAGEMENT_FEE":
            last_bid_year = random.choice([2016, 2017, 2018, 2019, 2020])
        else:
            last_bid_year = random.randint(2019, 2025)

        # Months left on contract: 1-36 months
        months_left = random.randint(1, 36)

        vendor_data.append({
            "vendor": vendor_name,
            "category": cat,
            "annual": annual,
            "per_unit": round(annual / max(units, 1)),
            "last_bid_year": last_bid_year,
            "months_left": months_left,
        })

    return vendor_data


def main():
    # Import the app to get BUILDINGS_DB
    import app as boardiq_app

    count = 0
    for bbl, building in boardiq_app.BUILDINGS_DB.items():
        if building.get("vendor_data"):
            continue  # Skip buildings that already have data

        vdata = generate_vendor_data(building)
        building["vendor_data"] = vdata
        count += 1

        addr = building.get("address", bbl)
        units = building.get("units", "?")
        print(f"  {addr} ({units} units) → {len(vdata)} vendors")

    print(f"\nSeeded {count} buildings with vendor data.")

    # Persist using the app's save mechanism
    boardiq_app._save_vendor_data()
    print("Saved to disk.")

    # Also write a standalone JSON for reference
    output = {}
    for bbl, building in boardiq_app.BUILDINGS_DB.items():
        vd = building.get("vendor_data", [])
        if vd:
            output[bbl] = vd

    with open("vendor_data_seeded.json", "w") as f:
        json.dump(output, f, indent=2)
    print(f"Wrote vendor_data_seeded.json ({len(output)} buildings)")


if __name__ == "__main__":
    main()
