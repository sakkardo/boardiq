"""
Import all Yardi exports into BoardIQ
======================================
Reads all .xlsx files from yardi_exports/ and updates BUILDINGS_DB vendor_data.

Usage:
    python yardi_import_all.py
"""

import os
import sys
import json
import glob

sys.path.insert(0, os.path.dirname(__file__))

from yardi_import import parse_yardi_expense_report, GL_CATEGORY_MAP

EXPORT_DIR = os.path.join(os.path.dirname(__file__), "yardi_exports")


def main():
    import app as boardiq_app

    xlsx_files = sorted(glob.glob(os.path.join(EXPORT_DIR, "*.xlsx")))
    if not xlsx_files:
        print(f"No .xlsx files found in {EXPORT_DIR}/")
        print("Run yardi_scraper.py first to download reports from Yardi.")
        return

    print(f"Found {len(xlsx_files)} Yardi export files.\n")

    imported_count = 0
    skipped = []

    for filepath in xlsx_files:
        filename = os.path.basename(filepath)
        try:
            result = parse_yardi_expense_report(filepath)
        except Exception as e:
            print(f"  SKIP {filename}: parse error — {e}")
            skipped.append(filename)
            continue

        prop_code = result["property_code"]
        vendors = result["vendors"]

        if not vendors:
            print(f"  SKIP {filename}: no benchmarkable vendors found")
            skipped.append(filename)
            continue

        # Match property code to a building in BUILDINGS_DB
        matched_bbl = None
        matched_building = None

        for bbl, building in boardiq_app.BUILDINGS_DB.items():
            # Match by Yardi property code stored on building, or by bbl suffix
            if building.get("yardi_property_code") == prop_code:
                matched_bbl = bbl
                matched_building = building
                break

        # Fallback: try matching by property code in building ID
        if not matched_building:
            for bbl, building in boardiq_app.BUILDINGS_DB.items():
                if bbl.endswith(prop_code) or building.get("id", "").endswith(prop_code):
                    matched_bbl = bbl
                    matched_building = building
                    break

        if not matched_building:
            print(f"  SKIP {filename}: property code '{prop_code}' not matched to any building")
            skipped.append(filename)
            continue

        # Update vendor_data
        units = matched_building.get("units", 1)
        existing_categories = {v["category"] for v in matched_building.get("vendor_data", [])}

        new_count = 0
        updated_count = 0

        for v in vendors:
            v["per_unit"] = round(v["annual"] / max(units, 1))

            # Check if category already exists
            found = False
            for ev in matched_building.get("vendor_data", []):
                if ev["category"] == v["category"]:
                    ev["vendor"] = v["vendor"]
                    ev["annual"] = v["annual"]
                    ev["per_unit"] = v["per_unit"]
                    updated_count += 1
                    found = True
                    break

            if not found:
                if "vendor_data" not in matched_building:
                    matched_building["vendor_data"] = []
                matched_building["vendor_data"].append(v)
                new_count += 1

        addr = matched_building.get("address", matched_bbl)
        print(f"  OK {addr} (prop {prop_code}): {len(vendors)} vendors ({new_count} new, {updated_count} updated)")
        imported_count += 1

    # Save
    boardiq_app._save_vendor_data()

    print(f"\nDone. Imported {imported_count} buildings, skipped {len(skipped)}.")
    if skipped:
        print(f"Skipped files: {', '.join(skipped)}")


if __name__ == "__main__":
    main()
