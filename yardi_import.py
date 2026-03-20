"""
Yardi Expense Distribution Report Parser
==========================================
Parses "Expense Distribution (Paid Only)" .xlsx exports from Yardi
and converts them into BoardIQ vendor_data format for benchmarking.
"""

import re
from collections import defaultdict
import openpyxl


# GL code → BoardIQ category mapping
GL_CATEGORY_MAP = {
    "5812": "ELEVATOR_MAINTENANCE",
    "5831": "EXTERMINATING",
    "5803": "CLEANING",
    "5852": "WATER_TREATMENT",
    "5810": "HVAC_MAINTENANCE",
    "5806": "HVAC_MAINTENANCE",      # AC → HVAC bucket
    "5828": "WASTE_REMOVAL",
    "5865": "LANDSCAPING",
    "5870": "LANDSCAPING",
    "6105": "INSURANCE",
    "6120": "INSURANCE",
    "6125": "INSURANCE",
    "6510": "MANAGEMENT_FEE",
    "6305": "UTILITIES_WATER",
    "5837": "SECURITY",
}


def parse_yardi_expense_report(filepath):
    """Parse a single-property Yardi Expense Distribution (Paid Only) .xlsx file.

    Returns:
        dict with keys:
            property_code (str): e.g. "148"
            period (str): e.g. "From 01/2025 to 12/2025"
            vendors (list[dict]): BoardIQ vendor_data format
    """
    wb = openpyxl.load_workbook(filepath, read_only=True, data_only=True)
    ws = wb.active
    rows = list(ws.iter_rows(values_only=True))
    wb.close()

    if not rows:
        raise ValueError("Empty spreadsheet")

    result = _parse_property_section(rows, 0)
    return result


def parse_multi_building_report(filepath):
    """Parse a Yardi export that may contain multiple properties.

    Each property section starts with "Expense Distribution (Paid Only)" header.

    Returns:
        list[dict]: One result dict per property, same format as parse_yardi_expense_report.
    """
    wb = openpyxl.load_workbook(filepath, read_only=True, data_only=True)
    ws = wb.active
    rows = list(ws.iter_rows(values_only=True))
    wb.close()

    if not rows:
        raise ValueError("Empty spreadsheet")

    # Find all section start indices (rows starting with the report header)
    section_starts = []
    for i, row in enumerate(rows):
        cell0 = str(row[0]).strip() if row[0] else ""
        if "expense distribution" in cell0.lower():
            section_starts.append(i)

    if not section_starts:
        # Try parsing as single property from row 0
        return [_parse_property_section(rows, 0)]

    results = []
    for idx, start in enumerate(section_starts):
        end = section_starts[idx + 1] if idx + 1 < len(section_starts) else len(rows)
        section_rows = rows[start:end]
        try:
            result = _parse_property_section(section_rows, 0)
            results.append(result)
        except Exception as e:
            print(f"[YardiImport] Skipping section at row {start}: {e}")

    return results if results else [_parse_property_section(rows, 0)]


def _parse_property_section(rows, start_offset):
    """Parse one property section from the Yardi report.

    Args:
        rows: List of row tuples (values_only).
        start_offset: Row index where this section starts (0-based).

    Returns:
        dict with property_code, period, vendors
    """
    # Row 0: Header ("Expense Distribution (Paid Only)")
    # Row 1: Property code (e.g. "148")
    # Row 2: Period (e.g. "Period: From 01/2025 to 12/2025")
    # Row 3: Column headers
    # Row 4+: Data

    property_code = str(rows[1][0]).strip() if len(rows) > 1 and rows[1][0] else ""
    period_raw = str(rows[2][0]).strip() if len(rows) > 2 and rows[2][0] else ""
    period = period_raw.replace("Period: ", "").strip() if period_raw else ""

    # Aggregate spend by (category, payee_name)
    # category_payee_totals[category][payee_name] = total_amount
    category_payee_totals = defaultdict(lambda: defaultdict(float))

    current_gl = None

    for i in range(4, len(rows)):
        row = rows[i]
        if not row or all(c is None for c in row):
            continue

        col0 = str(row[0]).strip() if row[0] else ""
        col1 = str(row[1]).strip() if row[1] and len(row) > 1 else ""

        # Skip total/grand total rows
        if col0.lower().startswith("total") or col0.lower().startswith("grand total"):
            current_gl = None
            continue

        # Check if this row has a new GL account code
        gl_match = re.match(r'^(\d{4})', col0)
        if gl_match:
            current_gl = gl_match.group(1)

        # Get payee name (col 3) and amount (col 11)
        payee_name = str(row[3]).strip() if len(row) > 3 and row[3] else ""
        amount = 0
        if len(row) > 11 and row[11] is not None:
            try:
                amount = float(row[11])
            except (ValueError, TypeError):
                continue

        if not payee_name or amount == 0:
            continue

        # Map GL code to BoardIQ category
        if current_gl and current_gl in GL_CATEGORY_MAP:
            category = GL_CATEGORY_MAP[current_gl]
            category_payee_totals[category][payee_name] += amount

    # For each category, pick the primary vendor (highest total spend)
    vendors = []
    for category, payees in sorted(category_payee_totals.items()):
        if not payees:
            continue
        primary_vendor = max(payees.items(), key=lambda x: x[1])
        vendor_name, total_spend = primary_vendor

        vendors.append({
            "vendor": vendor_name,
            "category": category,
            "annual": round(total_spend),
            "per_unit": 0,  # calculated later when unit count is known
            "last_bid_year": None,
            "months_left": None,
        })

    return {
        "property_code": property_code,
        "period": period,
        "vendors": vendors,
    }
