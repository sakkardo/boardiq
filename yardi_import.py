"""
Yardi Expense Distribution Report Parser for BoardIQ
Parses .xlsx exports from Yardi Voyager's "Expense Distribution (Paid Only)" report
and returns structured vendor data for benchmarking.

Supports two Yardi export formats:
  - Original format: separate columns for GL code, payee name, amount (16 cols)
  - Batch export format: GL code and vendor in single column (11 cols)
"""

import re
import os
import csv
from collections import defaultdict

try:
    import pandas as pd
except ImportError:
    pd = None

# ── GL Code → BoardIQ Category Mapping ────────────────────────────────────────

GL_TO_CATEGORY = {
    "5812": "ELEVATOR_MAINTENANCE",
    "5831": "EXTERMINATING",
    "5803": "CLEANING_MAINTENANCE",
    "5852": "WATER_TREATMENT",
    "5810": "HVAC_MAINTENANCE",
    "5806": "AC_MAINTENANCE",
    "5828": "RUBBISH_REMOVAL",
    "5865": "LANDSCAPING",
    "5870": "LANDSCAPING",
    "6105": "INSURANCE_PACKAGE",
    "6120": "INSURANCE_UMBRELLA",
    "6125": "INSURANCE_DO",
    "6510": "MANAGEMENT_FEES",
    "6305": "WATER_SEWER",
    "5837": "SECURITY_ALARM",
    "5639": "ELEVATOR_REPAIRS",
    "5630": "PLUMBING_REPAIRS",
    "5622": "HVAC_REPAIRS",
    "5633": "ELECTRICAL_REPAIRS",
}

CATEGORY_LABELS = {
    "ELEVATOR_MAINTENANCE": "Elevator Maintenance",
    "EXTERMINATING": "Exterminating",
    "CLEANING_MAINTENANCE": "Cleaning & Maintenance",
    "WATER_TREATMENT": "Water Treatment",
    "HVAC_MAINTENANCE": "HVAC Maintenance",
    "AC_MAINTENANCE": "AC Maintenance",
    "RUBBISH_REMOVAL": "Rubbish Removal",
    "LANDSCAPING": "Landscaping",
    "INSURANCE_PACKAGE": "Package Insurance",
    "INSURANCE_UMBRELLA": "Umbrella Insurance",
    "INSURANCE_DO": "D&O Insurance",
    "MANAGEMENT_FEES": "Management Fees",
    "WATER_SEWER": "Water/Sewer",
    "SECURITY_ALARM": "Security/Alarm",
    "ELEVATOR_REPAIRS": "Elevator Repairs",
    "PLUMBING_REPAIRS": "Plumbing Repairs",
    "HVAC_REPAIRS": "HVAC Repairs",
    "ELECTRICAL_REPAIRS": "Electrical Repairs",
}

# Known vendor name merges (duplicates with spelling variations)
VENDOR_MERGE = {
    "We Wire Electric Inc": "We Wire Electric Group Inc",
}

# Regex patterns
GL_PATTERN = re.compile(r"^(\d{4})-\d{4}\s*-\s*(.+)")
TOTAL_PATTERN = re.compile(r"^Total\s+(\d{4})-")
PROP_PATTERN = re.compile(r"Property=(\d+)")


def _safe_float(val):
    """Convert a value to float, returning 0.0 on failure."""
    if val is None:
        return 0.0
    try:
        return float(val)
    except (ValueError, TypeError):
        return 0.0


def _is_notna(val):
    """Check if a value is not NaN/None."""
    if val is None:
        return False
    if isinstance(val, float):
        import math
        return not math.isnan(val)
    return True


def parse_yardi_expense_report(filepath):
    """
    Parse a single Yardi Expense Distribution (Paid Only) .xlsx file.

    Returns dict:
        {
            "property_code": str,
            "building_name": str,
            "period": str,
            "vendor_data": [
                {
                    "vendor": "PS Marcato Elevator Company",
                    "category": "ELEVATOR_MAINTENANCE",
                    "category_label": "Elevator Maintenance",
                    "annual": 23271,
                    "per_unit": 0,        # calculated later with unit count
                    "last_bid_year": None,
                    "months_left": None,
                },
                ...
            ],
            "all_expenses": {category: total, ...},  # totals by category
            "grand_total": float,
        }
    """
    if pd is None:
        raise ImportError("pandas is required for Yardi import")

    df = pd.read_excel(filepath, header=None)

    if len(df) < 4:
        return {"property_code": None, "building_name": None, "period": None,
                "vendor_data": [], "all_expenses": {}, "grand_total": 0}

    # ── Detect format ──────────────────────────────────────────────────────
    row0 = str(df.iloc[0, 0]).strip() if _is_notna(df.iloc[0, 0]) else ""
    row1 = str(df.iloc[1, 0]).strip() if _is_notna(df.iloc[1, 0]) else ""
    row2_col1 = str(df.iloc[2, 1]).strip() if df.shape[1] > 1 and _is_notna(df.iloc[2, 1]) else ""

    is_batch = "Control" in row2_col1  # Batch exports have "Control" in col 1

    # ── Extract metadata ───────────────────────────────────────────────────
    prop_match = PROP_PATTERN.search(row1)
    if prop_match:
        property_code = prop_match.group(1)
    else:
        property_code = row1 if row1.isdigit() else None

    # Extract period
    period = ""
    if is_batch:
        period_match = re.search(r"mm/yy=(\S+)", row1)
        if period_match:
            period = period_match.group(1)
    else:
        if "Period:" in row1:
            period = row1
        elif len(df) > 2:
            row2_str = str(df.iloc[2, 0]) if _is_notna(df.iloc[2, 0]) else ""
            if "Period:" in row2_str:
                period = row2_str

    # Extract building name from filename if available
    building_name = None
    if hasattr(filepath, "name"):
        fname = os.path.basename(filepath.name)
    else:
        fname = os.path.basename(str(filepath))
    fname_match = re.match(r"ExpDist_\d+_(.+)\.xlsx", fname)
    if fname_match:
        building_name = fname_match.group(1)

    # ── Parse line items ───────────────────────────────────────────────────
    # Aggregate: (vendor_name, category) -> total spend
    vendor_cats = defaultdict(float)
    current_gl_main = None
    grand_total = 0.0

    for i in range(3, len(df)):
        row = df.iloc[i]
        col0 = str(row[0]).strip() if _is_notna(row[0]) else ""

        # Check for Grand Total
        if col0 == "Grand Total":
            if is_batch:
                grand_total = _safe_float(row[6])
            else:
                grand_total = _safe_float(row[11]) if df.shape[1] > 11 else 0

        if is_batch:
            # ── Batch format: col 0 = "XXXX-XXXX - Name" or "code - Vendor" ──
            gl_m = GL_PATTERN.match(col0)
            if gl_m:
                current_gl_main = gl_m.group(1)
                continue

            tot_m = TOTAL_PATTERN.match(col0)
            if tot_m:
                current_gl_main = None
                continue

            if (current_gl_main and current_gl_main in GL_TO_CATEGORY
                    and " - " in col0 and not col0.startswith("Total")):
                vendor_name = col0.split(" - ", 1)[1].strip()
                amt = _safe_float(row[6])
                if vendor_name and amt != 0:
                    vendor_name = VENDOR_MERGE.get(vendor_name, vendor_name)
                    category = GL_TO_CATEGORY[current_gl_main]
                    vendor_cats[(vendor_name, category)] += amt
        else:
            # ── Original format: GL in col 0, vendor in col 3, amount in col 11 ──
            # GL codes can be "XXXX-XXXX" (no name) or "XXXX-XXXX - Name"
            gl_m = GL_PATTERN.match(col0) if col0 else None
            if not gl_m and col0 and re.match(r"^\d{4}-\d{4}$", col0):
                # Bare GL code without name suffix
                gl_m_simple = re.match(r"^(\d{4})-\d{4}$", col0)
                if gl_m_simple:
                    current_gl_main = gl_m_simple.group(1)
                    continue
            if gl_m:
                current_gl_main = gl_m.group(1)
                continue

            if col0.startswith("Total"):
                current_gl_main = None
                continue

            payee = str(row[3]).strip() if df.shape[1] > 3 and _is_notna(row[3]) else ""
            amt = _safe_float(row[11]) if df.shape[1] > 11 else 0
            if (payee and amt != 0 and current_gl_main
                    and current_gl_main in GL_TO_CATEGORY):
                payee = VENDOR_MERGE.get(payee, payee)
                category = GL_TO_CATEGORY[current_gl_main]
                vendor_cats[(payee, category)] += amt

    # ── Aggregate: pick primary vendor per category (highest spend) ────────
    cat_vendors = defaultdict(list)
    for (vendor, cat), total in vendor_cats.items():
        cat_vendors[cat].append((vendor, total))

    vendor_data = []
    all_expenses = {}
    for cat, vendors in cat_vendors.items():
        # Sum all vendor spend for this category
        cat_total = sum(t for _, t in vendors)
        all_expenses[cat] = round(cat_total, 2)

        # Primary vendor = highest absolute spend
        primary = max(vendors, key=lambda x: abs(x[1]))
        vendor_data.append({
            "vendor": primary[0],
            "category": cat,
            "category_label": CATEGORY_LABELS.get(cat, cat),
            "annual": round(cat_total, 0),
            "per_unit": 0,
            "last_bid_year": None,
            "months_left": None,
        })

    # Sort by annual spend descending
    vendor_data.sort(key=lambda x: -abs(x["annual"]))

    return {
        "property_code": property_code,
        "building_name": building_name,
        "period": period,
        "vendor_data": vendor_data,
        "all_expenses": all_expenses,
        "grand_total": round(grand_total, 2),
    }


def parse_folder(folder_path):
    """
    Parse all .xlsx files in a folder.
    Returns list of parse results, one per building.
    """
    results = []
    errors = []
    for fname in sorted(os.listdir(folder_path)):
        if not fname.endswith(".xlsx"):
            continue
        fpath = os.path.join(folder_path, fname)
        try:
            result = parse_yardi_expense_report(fpath)
            if result["vendor_data"]:
                results.append(result)
        except Exception as e:
            errors.append({"file": fname, "error": str(e)})
    return results, errors


def load_portfolio_csv(csv_path):
    """
    Load the pre-built consolidated CSV (yardi_portfolio_data.csv)
    and return vendor data grouped by property code.

    Returns dict: {property_code: [vendor_dict, ...]}
    """
    portfolio = defaultdict(list)
    with open(csv_path, "r") as f:
        reader = csv.DictReader(f)
        # Aggregate by (property, vendor, category)
        agg = defaultdict(float)
        meta = {}
        for row in reader:
            key = (row["property_code"], row["vendor"], row["category"])
            agg[key] += float(row["annual_spend"])
            meta[key] = {
                "building_name": row["building_name"],
                "category_label": row["category_label"],
            }

    # Pick primary vendor per (property, category)
    prop_cat = defaultdict(list)
    for (prop, vendor, cat), total in agg.items():
        prop_cat[(prop, cat)].append((vendor, total, meta[(prop, vendor, cat)]))

    for (prop, cat), vendors in prop_cat.items():
        primary = max(vendors, key=lambda x: abs(x[1]))
        cat_total = sum(t for _, t, _ in vendors)
        portfolio[prop].append({
            "vendor": primary[0],
            "category": cat,
            "category_label": primary[2]["category_label"],
            "annual": round(cat_total, 0),
            "per_unit": 0,
            "last_bid_year": None,
            "months_left": None,
        })

    # Sort each building's vendors by spend
    for prop in portfolio:
        portfolio[prop].sort(key=lambda x: -abs(x["annual"]))

    return dict(portfolio)


def compute_portfolio_benchmarks(csv_path):
    """
    Compute portfolio-wide benchmark percentiles from the consolidated CSV.
    Returns dict: {category: {p25, p50, p75, p90, mean, count, total}}
    """
    import statistics

    cat_spends = defaultdict(list)
    with open(csv_path, "r") as f:
        reader = csv.DictReader(f)
        # Aggregate per (property, category) first
        prop_cat = defaultdict(float)
        for row in reader:
            key = (row["property_code"], row["category"])
            prop_cat[key] += float(row["annual_spend"])

    for (prop, cat), total in prop_cat.items():
        if total > 0:
            cat_spends[cat].append(total)

    benchmarks = {}
    for cat, spends in cat_spends.items():
        if len(spends) < 3:
            continue
        s = sorted(spends)
        n = len(s)
        benchmarks[cat] = {
            "p25": s[int(n * 0.25)],
            "p50": s[int(n * 0.50)],
            "p75": s[int(n * 0.75)],
            "p90": s[int(n * 0.90)],
            "mean": round(statistics.mean(s), 0),
            "count": n,
            "total": round(sum(s), 0),
            "label": CATEGORY_LABELS.get(cat, cat),
        }
    return benchmarks
