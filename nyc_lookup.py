"""
NYC address lookup — resolves an address to BBL and pulls PLUTO / HPD / DOB data
from public NYC OpenData endpoints. No API keys required.

Used by /api/admin/add-building to bootstrap a new building record.

Endpoints:
  GeoSearch  https://geosearch.planninglabs.nyc/v2/search  (address → lat/lon + BBL)
  PLUTO      https://data.cityofnewyork.us/resource/64uk-42ks.json?bbl=X
  HPD viol.  https://data.cityofnewyork.us/resource/wvxf-dwi5.json?bbl=X
  DOB viol.  https://data.cityofnewyork.us/resource/3h2n-5cm9.json?bbl=X
"""
import json
import urllib.parse
import urllib.request
from datetime import datetime, timedelta

GEOSEARCH_URL = "https://geosearch.planninglabs.nyc/v2/search"
PLUTO_URL     = "https://data.cityofnewyork.us/resource/64uk-42ks.json"
HPD_VIOL_URL  = "https://data.cityofnewyork.us/resource/wvxf-dwi5.json"
DOB_VIOL_URL  = "https://data.cityofnewyork.us/resource/3h2n-5cm9.json"

_BOROUGH_NAMES = {
    "1": "Manhattan",
    "2": "Bronx",
    "3": "Brooklyn",
    "4": "Queens",
    "5": "Staten Island",
    "MN": "Manhattan",
    "BX": "Bronx",
    "BK": "Brooklyn",
    "QN": "Queens",
    "SI": "Staten Island",
}


def _fetch_json(url, params=None, timeout=10):
    if params:
        url = url + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "BoardIQ/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _format_bbl(boro, block, lot):
    """NYC BBL is borough(1) + block(5) + lot(4), zero-padded."""
    try:
        boro = str(int(boro))
        block = str(int(block)).zfill(5)
        lot = str(int(lot)).zfill(4)
    except (TypeError, ValueError):
        return None
    return f"bbl_{boro}{block}{lot}"


def _neighborhood_from_pluto(p):
    """PLUTO doesn't have a neighborhood field, but we can infer from zipcode or leave blank."""
    zip_code = p.get("zipcode", "")
    neighborhoods = {
        "10001": "Chelsea", "10002": "Lower East Side", "10003": "East Village",
        "10004": "Financial District", "10005": "Financial District",
        "10006": "Financial District", "10007": "Tribeca",
        "10009": "East Village", "10010": "Gramercy", "10011": "Chelsea",
        "10012": "SoHo", "10013": "Tribeca", "10014": "West Village",
        "10016": "Murray Hill", "10017": "Midtown East", "10018": "Midtown West",
        "10019": "Midtown West", "10021": "Upper East Side", "10022": "Midtown East",
        "10023": "Upper West Side", "10024": "Upper West Side",
        "10025": "Upper West Side", "10026": "Harlem", "10027": "Harlem",
        "10028": "Upper East Side", "10029": "East Harlem",
        "10031": "Hamilton Heights", "10032": "Washington Heights",
        "10033": "Washington Heights", "10034": "Inwood", "10035": "East Harlem",
        "10036": "Midtown West", "10037": "Harlem", "10038": "Financial District",
        "10039": "Harlem", "10040": "Washington Heights",
        "10065": "Upper East Side", "10069": "Upper West Side",
        "10075": "Upper East Side", "10128": "Upper East Side",
        "10280": "Battery Park City", "10282": "Battery Park City",
    }
    return neighborhoods.get(zip_code, "")


def geocode_address(address):
    """Resolve an NYC address to BBL + canonical address via Planning Labs GeoSearch."""
    data = _fetch_json(GEOSEARCH_URL, {"text": address, "size": 1})
    features = data.get("features") or []
    if not features:
        return None
    f = features[0]
    props = f.get("properties", {})
    bbl_num = props.get("pad_bbl") or props.get("addendum", {}).get("pad", {}).get("bbl")
    if not bbl_num:
        return None
    # GeoSearch returns BBL as 10-digit string like "1009270001"
    bbl = f"bbl_{bbl_num}"
    return {
        "bbl": bbl,
        "bbl_num": str(bbl_num),
        "canonical_address": props.get("label") or props.get("name") or address,
        "borough": props.get("borough") or "",
        "house_number": props.get("housenumber", ""),
        "street": props.get("street", ""),
        "postalcode": props.get("postalcode", ""),
    }


def fetch_pluto(bbl_num):
    """Pull building metadata from PLUTO."""
    try:
        rows = _fetch_json(PLUTO_URL, {"bbl": str(bbl_num)})
        if not rows:
            return {}
        p = rows[0]
        year_built = int(p.get("yearbuilt", 0) or 0)
        units = int(float(p.get("unitstotal", 0) or 0))
        units_res = int(float(p.get("unitsres", 0) or 0))
        floors = int(float(p.get("numfloors", 0) or 0))
        bldg_class = (p.get("bldgclass") or "").strip()
        assess_total = int(float(p.get("assesstot", 0) or 0))
        borough = _BOROUGH_NAMES.get(str(p.get("borough", "")).strip(), "")
        return {
            "year_built": year_built or None,
            "is_prewar": bool(year_built and year_built < 1940),
            "units": units or units_res or None,
            "units_res": units_res or None,
            "floors": floors or None,
            "building_class": bldg_class,
            "assessed_value": assess_total,
            "borough": borough,
            "address": (p.get("address") or "").title(),
            "zipcode": p.get("zipcode", ""),
            "neighborhood": _neighborhood_from_pluto(p),
            "lot_area": int(float(p.get("lotarea", 0) or 0)),
            "bldg_area": int(float(p.get("bldgarea", 0) or 0)),
        }
    except Exception as e:
        return {"_pluto_error": str(e)}


def fetch_hpd_violations(bbl_num, limit=500):
    """Return HPD violation summary (open count, closed in last 12mo, etc.)."""
    try:
        # NYC BBL format in HPD is borough-block-lot separated, but a bare 10-digit works too.
        rows = _fetch_json(HPD_VIOL_URL, {"bbl": str(bbl_num), "$limit": limit})
        open_count = 0
        closed_recent = 0
        class_c_open = False
        cutoff = (datetime.utcnow() - timedelta(days=365)).date().isoformat()
        for r in rows:
            status = (r.get("violationstatus") or "").strip().lower()
            klass = (r.get("class") or "").strip().upper()
            if status == "open":
                open_count += 1
                if klass == "C":
                    class_c_open = True
            elif status == "close":
                close_date = (r.get("newcertifybydate") or r.get("originalcertifybydate") or "")[:10]
                if close_date and close_date >= cutoff:
                    closed_recent += 1
        return {
            "hpd_open": open_count,
            "hpd_closed_12mo": closed_recent,
            "class_c_open": class_c_open,
            "avg_days_to_close": None,  # out of scope for MVP
        }
    except Exception as e:
        return {"hpd_open": 0, "hpd_closed_12mo": 0, "class_c_open": False, "_hpd_error": str(e)}


def fetch_dob_violations(bbl_num, limit=500):
    """Count open DOB violations."""
    try:
        rows = _fetch_json(DOB_VIOL_URL, {"bbl": str(bbl_num), "$limit": limit})
        open_count = 0
        for r in rows:
            status = (r.get("violation_category") or r.get("violationcategory") or "").upper()
            # DOB uses "V-ACTIVE" vs "V-DOB VIOLATION DISMISSED" etc.
            if "ACTIVE" in status:
                open_count += 1
        return {"dob_open": open_count}
    except Exception as e:
        return {"dob_open": 0, "_dob_error": str(e)}


def _default_compliance_deadlines(year_built, units, floors):
    """Generate reasonable compliance deadline placeholders for any NYC building.
    These are templates keyed to NYC law thresholds — user can refine later.
    """
    deadlines = []
    now = datetime.utcnow()

    # LL11 / FISP — required every 5 years for buildings >6 stories
    if floors and floors > 6:
        due = now.replace(year=now.year + 1)
        deadlines.append({
            "law": "Local Law 11 — FISP Facade Inspection",
            "due_date": due.strftime("%b %Y"),
            "months_away": 12,
            "urgency": "MEDIUM",
            "consequence": "DOB violations + fines from $1,000/month if missed",
            "cost_low": 45000,
            "cost_high": 75000,
            "network_comps": 20,
            "context": f"NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under FISP. This building has {floors} stories and must file a Technical Façade Report in the next FISP cycle.",
        })

    # LL87 — energy audits for buildings >25,000 sf (proxy: units > 25 or floors > 7)
    sf_proxy = (units or 0) * 900  # rough sf per unit
    if sf_proxy > 25000 or (floors or 0) > 7:
        due = now.replace(year=now.year + 2)
        deadlines.append({
            "law": "Local Law 87 — Energy Audit",
            "due_date": due.strftime("%b %Y"),
            "months_away": 24,
            "urgency": "LOW",
            "consequence": "DOB notices of violation if not filed timely",
            "cost_low": 18000,
            "cost_high": 32000,
            "network_comps": 22,
            "context": "Buildings over 25,000 sf must conduct energy audits and retro-commissioning studies every 10 years.",
        })

    # LL97 — carbon emissions caps for buildings >25,000 sf
    if sf_proxy > 25000 or (floors or 0) > 7:
        deadlines.append({
            "law": "Local Law 97 — Carbon Emissions",
            "due_date": "Dec 2030",
            "months_away": max(1, (datetime(2030, 12, 31) - now).days // 30),
            "urgency": "LOW",
            "consequence": "$150,000–$250,000/yr penalty if over emissions cap",
            "cost_low": 120000,
            "cost_high": 280000,
            "network_comps": 24,
            "context": "Starting 2025, buildings over 25,000 sf must meet progressively stricter carbon emissions caps. Penalties apply if buildings exceed the cap.",
        })

    # CAT1 elevator inspection — annual for any building with elevators (proxy: floors >= 5)
    if (floors or 0) >= 5:
        due = now.replace(year=now.year + 1)
        deadlines.append({
            "law": "Elevator Inspection — CAT1",
            "due_date": due.strftime("%b %Y"),
            "months_away": 12,
            "urgency": "MEDIUM",
            "consequence": "Elevator shutdown order if not compliant",
            "cost_low": 8000,
            "cost_high": 12000,
            "network_comps": 40,
            "context": "Annual Category 1 inspection required for all elevators in NYC. Must be filed with DOB within 90 days of inspection.",
        })

    return deadlines


def lookup_building(address):
    """Full lookup: address → BBL → PLUTO + HPD + DOB → candidate building dict.

    Returns a dict shaped like an MRC_BUILDINGS entry (still needs id, managing_agent,
    subscription_tier, vendor_data added by caller).
    """
    geo = geocode_address(address)
    if not geo:
        return {"error": f"Could not find NYC address: {address}"}

    bbl = geo["bbl"]
    bbl_num = geo["bbl_num"]
    pluto = fetch_pluto(bbl_num)
    hpd = fetch_hpd_violations(bbl_num)
    dob = fetch_dob_violations(bbl_num)

    borough = pluto.get("borough") or geo.get("borough") or ""
    units = pluto.get("units") or pluto.get("units_res") or 0
    floors = pluto.get("floors") or 0
    year_built = pluto.get("year_built")
    building_class = pluto.get("building_class") or ""
    address_clean = pluto.get("address") or geo.get("canonical_address") or address

    assess_total = pluto.get("assessed_value", 0)
    # NYC tax roll: market value ~= assessed / 0.45 for Class 2 residential. Rough estimate.
    market_value = int(assess_total / 0.45) if assess_total else 0
    # Tax rate Class 2 FY2026 ~= 12.502% of assessed (residential)
    annual_tax = int(assess_total * 0.12502) if assess_total else 0

    return {
        "bbl": bbl,
        "id": bbl,
        "address": address_clean,
        "borough": borough,
        "neighborhood": pluto.get("neighborhood", ""),
        "units": units or 0,
        "floors": floors or 0,
        "year_built": year_built,
        "is_prewar": pluto.get("is_prewar", False),
        "building_class": building_class,
        "building_type": _building_type_from_class(building_class),
        "tax_assessment": {
            "assessed_value": assess_total,
            "market_value": market_value,
            "fiscal_year": "FY2026",
            "annual_tax_est": annual_tax,
            "trend_pct_2yr": None,
            "certiorari_recommended": False,
        },
        "violations": {
            "hpd_open": hpd.get("hpd_open", 0),
            "hpd_closed_12mo": hpd.get("hpd_closed_12mo", 0),
            "avg_days_to_close": hpd.get("avg_days_to_close"),
            "class_c_open": hpd.get("class_c_open", False),
            "dob_open": dob.get("dob_open", 0),
        },
        "last_data_refresh": datetime.utcnow().strftime("%Y-%m-%d"),
        "compliance_deadlines": _default_compliance_deadlines(year_built, units, floors),
        "vendor_data": [],
        "_lookup_warnings": [w for w in (
            pluto.get("_pluto_error"),
            hpd.get("_hpd_error"),
            dob.get("_dob_error"),
        ) if w],
    }


def _building_type_from_class(cls):
    """Infer building type from NYC building class code."""
    if not cls:
        return ""
    head = cls[0].upper()
    return {
        "A": "Single-family",
        "B": "Two-family",
        "C": "Walk-up Apartment",
        "D": "Elevator Apartment",
        "R": "Condo",
        "S": "Mixed-Use Residential",
    }.get(head, cls)


if __name__ == "__main__":
    # Quick smoke test — run: python nyc_lookup.py "160 East 48th Street, Manhattan"
    import sys
    addr = " ".join(sys.argv[1:]) or "130 East 18th Street, Manhattan"
    print(f"Looking up: {addr}")
    result = lookup_building(addr)
    print(json.dumps(result, indent=2, default=str))
