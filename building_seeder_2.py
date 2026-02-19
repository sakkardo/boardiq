"""
BoardIQ - Building Seeder
==========================
Reads all active buildings from Monday.com Building Master List,
looks up each building against NYC public APIs, calculates compliance
deadlines, and writes a fully populated BUILDINGS_DB to a file
that can be pasted into app.py.

USAGE:
  python building_seeder.py

OUTPUT:
  buildings_db.py  -- drop-in replacement for BUILDINGS_DB in app.py

INSTALL:
  pip install requests
"""

import requests
import json
import time
import re
from datetime import datetime, date

# ── Monday.com config ─────────────────────────────────────────────────────────
# Paste your Monday.com API token here (get from monday.com > Profile > Admin > API)
MONDAY_API_TOKEN = MONDAY_API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjI3NTY5MzkxLCJhYWkiOjExLCJ1aWQiOjg2NzY3MCwiaWFkIjoiMjAxOS0xMS0yN1QxMzoxMDo1NC4wMDBaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MzQ4MTQ4LCJyZ24iOiJ1c2UxIn0.R6M9pBBvyWuJJa0MvtF9CEMfbhEOStV7ZHvIr0gJ5Hk"
MONDAY_BOARD_ID  = 3473581362

# ── NYC Open Data endpoints ───────────────────────────────────────────────────
NYC_BASE    = "https://data.cityofnewyork.us/resource"
GEOSEARCH   = "https://geosearch.planninglabs.nyc/v2/search"
PLUTO_URL   = f"{NYC_BASE}/64uk-42ks.json"
DOF_URL     = f"{NYC_BASE}/yjxr-fw8i.json"
HPD_URL     = f"{NYC_BASE}/wvxf-dwi5.json"
DOB_URL     = f"{NYC_BASE}/3h2n-5cm9.json"

TODAY       = date.today()
CURRENT_YEAR = TODAY.year

# ── LL152 community district schedule ────────────────────────────────────────
# Manhattan CDs and which years their inspections are due (last digit pattern)
# CD 1,3 -> years ending 1 (2021, 2025...)
# CD 2,4 -> years ending 2
# CD 5,7 -> years ending 0 (2020, 2024...)
# CD 6,8 -> years ending 3
# CD 9,10,11 -> years ending 4
# Outside Manhattan -> different schedule, mark as "Verify with DOB"
LL152_SCHEDULE = {
    "1": 1, "3": 1,
    "2": 2, "4": 2,
    "5": 0, "7": 0,
    "6": 3, "8": 3,
    "9": 4, "10": 4, "11": 4, "12": 4,
}

# ── LL87 block-based schedule (last digit of block number) ───────────────────
# Buildings due in years ending in that digit
# e.g. block 882 ends in 2 -> due 2022, 2032 etc.


def monday_get_buildings():
    """Fetch all active buildings from Monday.com."""
    print("Fetching buildings from Monday.com...")
    url = "https://api.monday.com/v2"
    headers = {
        "Authorization": MONDAY_API_TOKEN,
        "Content-Type": "application/json",
    }
    query = """
    {
      boards(ids: %d) {
        items_page(limit: 500) {
          items {
            id
            name
            column_values {
              id
              text
            }
          }
        }
      }
    }
    """ % MONDAY_BOARD_ID

    resp = requests.post(url, headers=headers, json={"query": query}, timeout=30)
    data = resp.json()

    buildings = []
    items = data["data"]["boards"][0]["items_page"]["items"]
    for item in items:
        cols = {c["id"]: c["text"] for c in item["column_values"]}
        address = cols.get("text8", "").strip()
        # Skip items without a real address or with multiple addresses (complex cases)
        if not address or "/" in address or len(address) > 60:
            continue
        # Skip non-NYC locations for compliance (NJ, Long Island)
        location = cols.get("location", "")
        borough = map_location_to_borough(location)
        if not borough:
            continue

        buildings.append({
            "monday_id": item["id"],
            "name": item["name"],
            "address": address,
            "borough": borough,
            "units": safe_int(cols.get("numbers9")),
            "year_built": safe_int(cols.get("numeric_mkt53ys4")),
            "floors": safe_int(cols.get("numeric_mkt5dq31")),
            "building_type": cols.get("status1", ""),
            "location_label": location,
        })

    print(f"  Found {len(buildings)} buildings with NYC addresses")
    return buildings


def map_location_to_borough(location_label):
    mapping = {
        "NYC": "Manhattan",
        "Brooklyn": "Brooklyn",
        "Queens": "Queens",
        "Bronx": "Bronx",
    }
    return mapping.get(location_label)


def safe_int(val):
    try:
        return int(float(val)) if val else None
    except:
        return None


def geocode_address(address, borough):
    """Convert address to BBL using NYC GeoSearch."""
    query = f"{address}, {borough}, NY"
    try:
        resp = requests.get(GEOSEARCH, params={"text": query, "size": 1}, timeout=10)
        features = resp.json().get("features", [])
        if not features:
            return None
        props = features[0]["properties"]
        return {
            "bbl": props.get("pad_bbl", ""),
            "borough_code": props.get("borough", ""),
            "block": props.get("pad_blk", ""),
            "lot": props.get("pad_lot", ""),
            "community_district": str(props.get("pad_cd", "")),
            "neighborhood": props.get("neighbourhood", ""),
            "lat": features[0]["geometry"]["coordinates"][1],
            "lng": features[0]["geometry"]["coordinates"][0],
        }
    except Exception as e:
        print(f"    Geocode error: {e}")
        return None


def get_hpd_violations(bbl):
    """Get HPD violation counts."""
    try:
        boro = bbl[0]
        block = bbl[1:6].lstrip("0")
        lot = bbl[6:].lstrip("0")
        params = {
            "boroid": boro, "block": block, "lot": lot,
            "$limit": 500,
        }
        resp = requests.get(HPD_URL, params=params, timeout=10)
        viols = resp.json()

        open_viols = [v for v in viols if v.get("violationstatus", "").upper() == "OPEN"]
        closed_12mo = []
        cutoff = date(TODAY.year - 1, TODAY.month, TODAY.day)
        for v in viols:
            if v.get("violationstatus", "").upper() == "CLOSE":
                try:
                    closed_date = datetime.strptime(v["closedate"][:10], "%Y-%m-%d").date()
                    if closed_date >= cutoff:
                        closed_12mo.append(v)
                except:
                    pass

        class_c = any(v.get("class", "") == "C" for v in open_viols)
        days_to_close = []
        for v in closed_12mo:
            try:
                open_d = datetime.strptime(v["approveddate"][:10], "%Y-%m-%d").date()
                close_d = datetime.strptime(v["closedate"][:10], "%Y-%m-%d").date()
                days_to_close.append((close_d - open_d).days)
            except:
                pass

        avg_days = round(sum(days_to_close) / len(days_to_close)) if days_to_close else 0

        return {
            "hpd_open": len(open_viols),
            "hpd_closed_12mo": len(closed_12mo),
            "avg_days_to_close": avg_days,
            "class_c_open": class_c,
            "dob_open": 0,
        }
    except Exception as e:
        print(f"    HPD error: {e}")
        return {"hpd_open": 0, "hpd_closed_12mo": 0, "avg_days_to_close": 0, "class_c_open": False, "dob_open": 0}


def get_tax_assessment(bbl):
    """Get DOF tax assessment data."""
    try:
        params = {"parid": bbl, "$limit": 1}
        resp = requests.get(DOF_URL, params=params, timeout=10)
        rows = resp.json()
        if not rows:
            return None
        row = rows[0]
        assessed = safe_int(row.get("avt")) or safe_int(row.get("av_change"))
        market = safe_int(row.get("fullval"))
        return {
            "assessed_value": assessed or 0,
            "market_value": market or 0,
            "fiscal_year": "FY2026",
            "annual_tax_est": round((assessed or 0) * 0.12) if assessed else 0,
            "trend_pct_2yr": 0,
            "certiorari_recommended": False,
        }
    except Exception as e:
        print(f"    DOF error: {e}")
        return None


def calc_ll11_deadline(bbl, floors):
    """
    Calculate LL11 FISP deadline.
    NYC divides buildings into sub-cycles based on last digit of block number.
    Cycle 8 (current): Sub-cycle A (blocks ending 4,9) due 2/21-2/25
                       Sub-cycle B (blocks ending 0,5) due 2/24-2/28 (current)
                       Sub-cycle C (blocks ending 1,2,6) due 2/25-2/29
                       Sub-cycle D (blocks ending 3,7,8) due 2/26-2/30
    Only applies to buildings > 6 stories.
    """
    if not floors or floors <= 6:
        return None
    if not bbl or len(bbl) < 6:
        return None

    try:
        block_str = bbl[1:6].lstrip("0")
        if not block_str:
            return None
        last_digit = int(block_str[-1])
    except:
        return None

    # Sub-cycle assignments for Cycle 9 (2025-2030)
    if last_digit in [4, 9]:
        due_year, due_month = 2025, 2
    elif last_digit in [0, 5]:
        due_year, due_month = 2026, 2
    elif last_digit in [1, 2, 6]:
        due_year, due_month = 2027, 2
    else:  # 3, 7, 8
        due_year, due_month = 2028, 2

    due_date = date(due_year, due_month, 21)
    months_away = max(0, (due_date.year - TODAY.year) * 12 + (due_date.month - TODAY.month))

    urgency = "HIGH" if months_away <= 12 else "MEDIUM" if months_away <= 24 else "LOW"

    # Estimate cost based on building size
    if floors >= 20:
        cost_low, cost_high = 35000, 65000
    elif floors >= 12:
        cost_low, cost_high = 22000, 40000
    else:
        cost_low, cost_high = 12000, 22000

    return {
        "law": "Local Law 11 - FISP Facade Inspection",
        "due_date": f"{due_date.strftime('%b')} {due_year}",
        "months_away": months_away,
        "urgency": urgency,
        "consequence": "DOB violations + fines from $1,000/month if missed",
        "cost_low": cost_low,
        "cost_high": cost_high,
        "network_comps": 23,
        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost.",
    }


def calc_ll97_deadline(units, floors, year_built):
    """
    LL97 applies to buildings over 25,000 sq ft.
    Estimate sq ft from units and floors.
    Annual compliance report due May 1st each year.
    """
    # Rough sq ft estimate: avg 750 sq ft/unit * units, or floors * avg floor plate
    estimated_sqft = (units or 0) * 900 if units else (floors or 0) * 8000
    if estimated_sqft < 25000:
        return None

    # Next May 1 deadline
    next_may = date(CURRENT_YEAR, 5, 1)
    if TODAY > next_may:
        next_may = date(CURRENT_YEAR + 1, 5, 1)

    months_away = (next_may.year - TODAY.year) * 12 + (next_may.month - TODAY.month)

    # Older buildings tend to have higher emissions
    if year_built and year_built < 1980:
        cost_low, cost_high = 35000, 75000
        est_penalty = "$45,000-$80,000/yr"
    else:
        cost_low, cost_high = 20000, 45000
        est_penalty = "$20,000-$45,000/yr"

    return {
        "law": "Local Law 97 - Carbon Emissions",
        "due_date": f"May 1, {next_may.year}",
        "months_away": months_away,
        "urgency": "HIGH" if months_away <= 6 else "MEDIUM",
        "consequence": f"Est. {est_penalty} penalty at current emissions",
        "cost_low": cost_low,
        "cost_high": cost_high,
        "network_comps": 31,
        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine. Acting proactively costs far less than paying annual penalties indefinitely.",
    }


def calc_ll87_deadline(bbl):
    """
    LL87 energy audit due every 10 years based on last digit of block number.
    Block last digit = year ending in that digit (e.g. digit 2 -> due 2022, 2032)
    Only applies to buildings over 50,000 sq ft (roughly 50+ units).
    """
    if not bbl or len(bbl) < 6:
        return None
    try:
        block_str = bbl[1:6].lstrip("0")
        if not block_str:
            return None
        last_digit = int(block_str[-1])
    except:
        return None

    # Find the most recent due year and next due year
    base_year = (CURRENT_YEAR // 10) * 10 + last_digit
    if base_year < CURRENT_YEAR:
        last_due = base_year
        next_due = base_year + 10
    else:
        last_due = base_year - 10
        next_due = base_year

    # If last due year has passed and we don't know if they filed, flag it
    if last_due <= CURRENT_YEAR <= last_due + 2:
        due_display = f"Verify with DOB - {last_due} filing may be outstanding"
        months_away = 0
        urgency = "HIGH"
    else:
        due_display = f"Dec {next_due}"
        months_away = max(0, (next_due - CURRENT_YEAR) * 12 - TODAY.month + 12)
        urgency = "MEDIUM"

    return {
        "law": "Local Law 87 - Energy Audit and Retro-commissioning",
        "due_date": due_display,
        "months_away": months_away,
        "urgency": urgency,
        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
        "cost_low": 12000,
        "cost_high": 24000,
        "network_comps": 41,
        "context": f"Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The filing schedule is based on the last digit of the building's tax block number - this building's block ends in {last_digit}, meaning filings are due in years ending in {last_digit} (most recently {last_due}, next due {next_due}). The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements. Many buildings find the audit pays for itself through energy savings identified.",
    }


def calc_ll152_deadline(community_district, borough):
    """
    LL152 gas piping inspection schedule by community district.
    Manhattan only has defined schedule. Other boroughs have their own.
    """
    if borough != "Manhattan":
        # Other boroughs have inspections too but different schedules
        return {
            "law": "Local Law 152 - Gas Piping Inspection",
            "due_date": "Verify schedule with DOB",
            "months_away": 0,
            "urgency": "MEDIUM",
            "consequence": "DOB violations if inspection not filed on time",
            "cost_low": 2500,
            "cost_high": 6000,
            "network_comps": 67,
            "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The inspection schedule varies by borough and community district. The board should check DOB BIS to confirm the next inspection due date for this building. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB. Defects found must be corrected and re-inspected before the filing deadline.",
        }

    # Manhattan schedule
    cd = str(community_district).strip()
    last_digit = LL152_SCHEDULE.get(cd)

    if last_digit is None:
        return None

    # Find next due year
    base = (CURRENT_YEAR // 4) * 4
    if last_digit == 0:
        candidates = [base, base + 4]
    else:
        candidates = [y for y in range(base - 4, base + 8) if y % 10 == last_digit and y % 4 == 0]

    due_year = min([y for y in candidates if y >= CURRENT_YEAR - 1], default=CURRENT_YEAR + 4)
    due_date = date(due_year, 12, 31)
    months_away = max(0, (due_date.year - TODAY.year) * 12 + (due_date.month - TODAY.month))

    if due_year < CURRENT_YEAR or (due_year == CURRENT_YEAR and TODAY.month > 10):
        due_display = f"Verify with DOB - {due_year} may be overdue"
        months_away = 0
        urgency = "HIGH"
    else:
        due_display = f"Dec 31, {due_year}"
        urgency = "HIGH" if months_away <= 6 else "MEDIUM"

    return {
        "law": "Local Law 152 - Gas Piping Inspection",
        "due_date": due_display,
        "months_away": months_away,
        "urgency": urgency,
        "consequence": "DOB violations and fines if inspection not filed on time",
        "cost_low": 2500,
        "cost_high": 6000,
        "network_comps": 67,
        "context": f"Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. Manhattan Community District {cd} inspections are due in years ending in {last_digit}. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines.",
    }


def calc_elevator_deadline(floors):
    """Elevator annual inspection - required for any building with elevators."""
    if not floors or floors < 3:
        return None

    # Estimate number of cabs based on floors/units
    num_cabs = 1 if floors < 8 else 2 if floors < 20 else 3

    # Annual inspection - assume due within the year
    next_inspection_month = (TODAY.month % 12) + 3  # roughly 3 months from now
    next_year = CURRENT_YEAR if next_inspection_month > TODAY.month else CURRENT_YEAR
    months_away = 3  # placeholder - actual date would come from DOB records

    return {
        "law": f"Elevator Annual Inspection - {num_cabs} cab{'s' if num_cabs > 1 else ''}",
        "due_date": "Annual - verify with DOB",
        "months_away": months_away,
        "urgency": "MEDIUM",
        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
        "cost_low": num_cabs * 800,
        "cost_high": num_cabs * 1400,
        "network_comps": 89,
        "context": f"NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated {num_cabs} elevator cab{'s' if num_cabs > 1 else ''}. The inspection covers all mechanical and safety components including brakes, cables, door operations, and emergency systems. The elevator contractor typically coordinates the inspection and must have equipment in proper working order beforehand. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately - a serious hardship for residents and liability for the board. Confirm inspection dates with your elevator contractor at least 60 days in advance.",
    }


def process_building(bldg):
    """Full pipeline for one building."""
    address = bldg["address"]
    borough = bldg["borough"]
    print(f"\n  Processing: {address} ({borough})")

    # Step 1: Geocode
    geo = geocode_address(address, borough)
    if not geo or not geo.get("bbl"):
        print(f"    Could not geocode - skipping")
        return None

    bbl = geo["bbl"]
    block = geo.get("block", "")
    cd = geo.get("community_district", "")
    neighborhood = geo.get("neighborhood", "") or bldg["location_label"]

    print(f"    BBL: {bbl}  Block: {block}  CD: {cd}")

    # Step 2: HPD violations
    violations = get_hpd_violations(bbl)

    # Step 3: Tax assessment
    tax = get_tax_assessment(bbl)
    if not tax:
        tax = {
            "assessed_value": 0, "market_value": 0,
            "fiscal_year": "FY2026", "annual_tax_est": 0,
            "trend_pct_2yr": 0, "certiorari_recommended": False,
        }

    # Step 4: Compliance deadlines
    floors  = bldg.get("floors")
    units   = bldg.get("units")
    yr_blt  = bldg.get("year_built")

    deadlines = []

    ll11 = calc_ll11_deadline(bbl, floors)
    if ll11:
        deadlines.append(ll11)

    ll97 = calc_ll97_deadline(units, floors, yr_blt)
    if ll97:
        deadlines.append(ll97)

    ll87 = calc_ll87_deadline(bbl)
    if ll87 and units and units > 50:
        deadlines.append(ll87)

    ll152 = calc_ll152_deadline(cd, borough)
    if ll152:
        deadlines.append(ll152)

    elev = calc_elevator_deadline(floors)
    if elev:
        deadlines.append(elev)

    # Sort by urgency then months_away
    urgency_order = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}
    deadlines.sort(key=lambda d: (urgency_order.get(d["urgency"], 3), d["months_away"]))

    # Step 5: Build record
    bbl_key = f"bbl_{bbl}"
    record = {
        "id": bbl_key,
        "monday_id": bldg["monday_id"],
        "address": address,
        "borough": borough,
        "neighborhood": neighborhood,
        "units": units,
        "floors": floors,
        "year_built": yr_blt,
        "is_prewar": bool(yr_blt and yr_blt < 1945),
        "building_class": "D4",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": str(TODAY),
        "tax_assessment": tax,
        "violations": violations,
        "last_data_refresh": str(TODAY),
        "compliance_deadlines": deadlines,
        "vendor_data": [],
    }

    print(f"    OK - {len(deadlines)} compliance deadlines found")
    return bbl_key, record


def main():
    print("=" * 60)
    print("  BoardIQ Building Seeder")
    print("=" * 60)

    if MONDAY_API_TOKEN == "YOUR_MONDAY_API_TOKEN_HERE":
        print("\nERROR: Please set your Monday.com API token at the top of this file.")
        print("Get it from: monday.com > Profile picture > Admin > API")
        return

    # Fetch buildings from Monday.com
    buildings = monday_get_buildings()
    if not buildings:
        print("No buildings found. Check your API token and board ID.")
        return

    print(f"\nProcessing {len(buildings)} buildings...")
    results = {}
    errors  = []

    for i, bldg in enumerate(buildings, 1):
        print(f"\n[{i}/{len(buildings)}] {bldg['name']}")
        try:
            result = process_building(bldg)
            if result:
                bbl_key, record = result
                results[bbl_key] = record
            else:
                errors.append(bldg["name"])
        except Exception as e:
            print(f"    ERROR: {e}")
            errors.append(bldg["name"])

        # Be polite to the APIs
        time.sleep(0.5)

    # Write output
    print(f"\n\nWriting {len(results)} buildings to buildings_db.py...")
    write_output(results)

    print(f"\n{'='*60}")
    print(f"  Done! {len(results)} buildings processed, {len(errors)} failed.")
    if errors:
        print(f"\n  Failed buildings (geocode issues):")
        for e in errors:
            print(f"    - {e}")
    print(f"\n  Output: buildings_db.py")
    print(f"  Next step: copy BUILDINGS_DB from buildings_db.py into app.py")
    print("=" * 60)


def write_output(results):
    """Write the BUILDINGS_DB dict to a Python file."""
    lines = []
    lines.append('"""')
    lines.append('Auto-generated by building_seeder.py')
    lines.append(f'Generated: {datetime.now().strftime("%Y-%m-%d %H:%M")}')
    lines.append(f'Buildings: {len(results)}')
    lines.append('"""')
    lines.append("")
    lines.append("BUILDINGS_DB = {")

    for bbl_key, rec in results.items():
        lines.append(f'    "{bbl_key}": {{')
        for k, v in rec.items():
            lines.append(f'        "{k}": {json.dumps(v, indent=None)},')
        lines.append("    },")

    lines.append("}")
    lines.append("")

    with open("buildings_db.py", "w") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    main()
