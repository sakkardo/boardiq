"""
BoardIQ - Building Enricher
============================
Geocodes each building and pulls real DOF + HPD data.
Reads buildings_db.py, enriches each record, writes enriched_buildings_db.py.

USAGE:
  python enrich_buildings.py

No API keys needed - all NYC Open Data (free).
"""

import requests
import json
import time
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from buildings_db import BUILDINGS_DB

GEOSEARCH  = "https://geosearch.planninglabs.nyc/v2/search"
DOF_URL    = "https://data.cityofnewyork.us/resource/8y4t-faws.json"
HPD_URL    = "https://data.cityofnewyork.us/resource/wvxf-dwi5.json"

from datetime import date
TODAY = date.today()


def geocode(address, borough):
    query = f"{address}, {borough}, NY"
    try:
        r = requests.get(GEOSEARCH, params={"text": query, "size": 1}, timeout=10)
        features = r.json().get("features", [])
        if not features:
            return None
        props = features[0]["properties"]
        addendum = props.get("addendum", {}).get("pad", {})
        bbl = addendum.get("bbl", "")
        return {
            "bbl":   bbl,
            "block": bbl[1:6] if len(bbl) >= 6 else "",
            "cd":    "",
        }
    except Exception as e:
        return None


def get_dof(bbl):
    try:
        r = requests.get(DOF_URL, params={"parid": bbl, "$limit": 1}, timeout=10)
        rows = r.json()
        if not rows:
            return {}
        row = rows[0]
        market   = int(float(row.get("curmkttot", 0) or 0))
        assessed = int(float(row.get("curacttot", 0) or 0))
        taxable  = int(float(row.get("curtxbtot", 0) or 0))
        # Prior year for trend
        py_market = int(float(row.get("pymkttot", 0) or 0))
        trend = round(((market - py_market) / py_market * 100), 1) if py_market > 0 else 0
        return {
            "assessed_value": assessed,
            "market_value":   market,
            "fiscal_year":    f"FY{row.get('year', '2026')}",
            "annual_tax_est": round(taxable * 0.1255),
            "trend_pct_2yr":  trend,
            "certiorari_recommended": trend > 8,
        }
    except:
        return {}


def get_hpd(bbl):
    try:
        boro  = bbl[0]
        block = bbl[1:6].lstrip("0") or "0"
        lot   = bbl[6:].lstrip("0")  or "0"
        r = requests.get(HPD_URL, params={"boroid": boro, "block": block, "lot": lot, "$limit": 500}, timeout=10)
        viols = r.json()
        open_v = [v for v in viols if v.get("violationstatus","").upper() == "OPEN"]
        class_c = any(v.get("class","") == "C" for v in open_v)
        closed_12 = []
        cutoff = date(TODAY.year-1, TODAY.month, TODAY.day)
        days = []
        for v in viols:
            if v.get("violationstatus","").upper() == "CLOSE":
                try:
                    cd = date.fromisoformat(v["closedate"][:10])
                    if cd >= cutoff:
                        closed_12.append(v)
                        od = date.fromisoformat(v.get("approveddate","")[:10])
                        days.append((cd - od).days)
                except:
                    pass
        return {
            "hpd_open":          len(open_v),
            "hpd_closed_12mo":   len(closed_12),
            "avg_days_to_close": round(sum(days)/len(days)) if days else 0,
            "class_c_open":      class_c,
            "dob_open":          0,
        }
    except:
        return {}


def main():
    buildings = dict(BUILDINGS_DB)
    total = len(buildings)
    print(f"Enriching {total} buildings...")
    print("This will take about 5-10 minutes.\n")

    enriched = 0
    failed   = []

    for i, (key, rec) in enumerate(buildings.items(), 1):
        address = rec["address"]
        borough = rec["borough"]
        print(f"[{i}/{total}] {address} ({borough})... ", end="", flush=True)

        geo = geocode(address, borough)
        if not geo or not geo.get("bbl"):
            print("GEOCODE FAILED")
            failed.append(address)
            time.sleep(0.3)
            continue

        bbl = geo["bbl"]
        time.sleep(0.2)

        dof = get_dof(bbl)
        time.sleep(0.2)

        hpd = get_hpd(bbl)
        time.sleep(0.2)

        # Merge into record
        if dof:
            buildings[key]["tax_assessment"].update(dof)
        if hpd:
            buildings[key]["violations"].update(hpd)
        buildings[key]["bbl"] = bbl
        buildings[key]["last_data_refresh"] = str(TODAY)

        hpd_open = hpd.get("hpd_open", 0)
        av = dof.get("assessed_value", 0)
        print(f"OK  BBL:{bbl}  HPD open:{hpd_open}  AV:${av:,}")
        enriched += 1

    # Write output
    print(f"\n\nWriting enriched_buildings_db.py...")
    lines = [
        '"""',
        f'Enriched buildings_db - {enriched} buildings with live NYC data',
        f'Generated: {TODAY}',
        '"""',
        '',
        'BUILDINGS_DB = {',
    ]
    for key, rec in buildings.items():
        # Convert to Python-safe repr
        rec_str = repr(rec)
        lines.append(f'    "{key}": {rec_str},')
    lines.append('}')
    lines.append('')

    with open("enriched_buildings_db.py", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"\nDone! {enriched} enriched, {len(failed)} failed.")
    if failed:
        print("\nFailed:")
        for f in failed:
            print(f"  - {f}")
    print("\nNext step: rename enriched_buildings_db.py to buildings_db.py and upload to GitHub.")


if __name__ == "__main__":
    main()
