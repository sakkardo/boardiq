"""
BoardIQ — Web Application
===========================
Flask web server that ties together:
  - NYC public data pipeline (DOF, HPD, DOB)
  - Invoice processing engine
  - Benchmarking engine
  - Dashboard UI

SETUP & RUN:
  pip install flask pandas
  python app.py
  Open: http://localhost:5000

PRODUCTION SETUP:
  pip install gunicorn
  gunicorn -w 4 -b 0.0.0.0:8000 app:app
"""

import os
import sys
import json
import csv
import io
from datetime import datetime
from functools import wraps

sys.path.insert(0, os.path.dirname(__file__))

from flask import (Flask, render_template_string, request, jsonify,
                   session, redirect, url_for, flash)
from invoice_pipeline import InvoiceProcessor, create_sample_csv, CATEGORIES
from benchmarking_engine import benchmark_building, NETWORK_BENCHMARKS

app = Flask(__name__)
app.secret_key = "boardiq-dev-key-change-in-production"

# ── Load Century Management buildings from enriched database ─────────────────
def _load_century_buildings():
    try:
        import importlib.util
        _dir = os.path.dirname(os.path.abspath(__file__))
        _path = os.path.join(_dir, "century_buildings.py")
        spec = importlib.util.spec_from_file_location("century_buildings", _path)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        print(f"[BoardIQ] Loaded {len(m.BUILDINGS_DB)} Century buildings")
        return m.BUILDINGS_DB
    except Exception as e:
        print(f"[BoardIQ] Warning: Could not load century_buildings.py: {e}")
        return {}

CENTURY_BUILDINGS = _load_century_buildings()

# ── In-memory database (swap for PostgreSQL in production) ───────────────────
BUILDINGS_DB = {
    "bbl_1022150001": {
        "id": "bbl_1022150001",
        "address": "120 West 72nd Street",
        "borough": "Manhattan",
        "neighborhood": "Upper West Side",
        "units": 120,
        "floors": 14,
        "year_built": 1928,
        "is_prewar": True,
        "building_class": "D4",
        "managing_agent": "Argo Real Estate",
        "board_president": "Margaret Chen",
        "subscription_tier": "standard",
        "subscription_since": "2025-09-01",
        "tax_assessment": {
            "assessed_value": 1240000,
            "market_value": 28400000,
            "fiscal_year": "FY2026",
            "annual_tax_est": 148800,
            "trend_pct_2yr": 14.2,
            "certiorari_recommended": True,
        },
        "violations": {
            "hpd_open": 2,
            "hpd_closed_12mo": 8,
            "avg_days_to_close": 22,
            "class_c_open": True,
            "dob_open": 0,
        },
        "last_data_refresh": "2026-01-15",
        "compliance_deadlines": [
            {
                "law": "Local Law 11 — FISP Facade Inspection",
                "due_date": "Oct 2026",
                "months_away": 9,
                "urgency": "HIGH",
                "consequence": "DOB violations + fines from $1,000/month",
                "cost_low": 14000,
                "cost_high": 22000,
                "network_comps": 23,
            },
            {
                "law": "Local Law 97 — Carbon Emissions",
                "due_date": "Dec 2026",
                "months_away": 11,
                "urgency": "HIGH",
                "consequence": "Est. $31,000/yr penalty at current emissions",
                "cost_low": 18000,
                "cost_high": 35000,
                "network_comps": 31,
            },
            {
                "law": "Local Law 87 — Energy Audit",
                "due_date": "Dec 2026",
                "months_away": 11,
                "urgency": "MEDIUM",
                "consequence": "$3,000 year one, $5,000/yr thereafter",
                "cost_low": 8000,
                "cost_high": 16000,
                "network_comps": 41,
            },
            {
                "law": "Elevator Annual Inspection",
                "due_date": "Mar 2026",
                "months_away": 3,
                "urgency": "MEDIUM",
                "consequence": "Mandatory shutdown until re-inspected",
                "cost_low": 800,
                "cost_high": 1400,
                "network_comps": 89,
            },
        ],
        "vendor_data": [
            {"vendor": "Schindler Elevator Corp", "category": "ELEVATOR_MAINTENANCE",
             "annual": 67200, "per_unit": 560, "last_bid_year": 2016, "months_left": 14},
            {"vendor": "AmTrust Insurance Group", "category": "INSURANCE",
             "annual": 94000, "per_unit": 783, "last_bid_year": 2022, "months_left": 8},
            {"vendor": "Clean Star Services", "category": "CLEANING",
             "annual": 54000, "per_unit": 450, "last_bid_year": 2023, "months_left": 8},
            {"vendor": "Empire Boiler Service", "category": "BOILER_MAINTENANCE",
             "annual": 12600, "per_unit": 105, "last_bid_year": 2023, "months_left": 20},
            {"vendor": "Apex Exterminating", "category": "EXTERMINATING",
             "annual": 6000, "per_unit": 50, "last_bid_year": 2024, "months_left": 6},
            {"vendor": "Metro Water Treatment", "category": "WATER_TREATMENT",
             "annual": 7200, "per_unit": 60, "last_bid_year": 2019, "months_left": 5},
            {"vendor": "NYC Waste Solutions", "category": "WASTE_REMOVAL",
             "annual": 7200, "per_unit": 60, "last_bid_year": 2024, "months_left": 9},
        ],
    },
    "bbl_1012660001": {
        "id": "bbl_1012660001",
        "address": "740 Park Avenue",
        "borough": "Manhattan",
        "neighborhood": "Upper East Side",
        "units": 84,
        "floors": 18,
        "year_built": 1930,
        "is_prewar": True,
        "building_class": "D4",
        "managing_agent": "Douglas Elliman PM",
        "board_president": "Robert Steinberg",
        "subscription_tier": "premium",
        "subscription_since": "2025-07-01",
        "tax_assessment": {
            "assessed_value": 1840000,
            "market_value": 42000000,
            "fiscal_year": "FY2026",
            "annual_tax_est": 220800,
            "trend_pct_2yr": 8.1,
            "certiorari_recommended": False,
        },
        "violations": {
            "hpd_open": 0,
            "hpd_closed_12mo": 3,
            "avg_days_to_close": 14,
            "class_c_open": False,
            "dob_open": 1,
        },
        "last_data_refresh": "2026-01-15",
        "compliance_deadlines": [
            {
                "law": "Local Law 11 — FISP Facade Inspection",
                "due_date": "Jun 2027",
                "months_away": 17,
                "urgency": "MEDIUM",
                "consequence": "DOB violations + fines from $1,000/month",
                "cost_low": 18000,
                "cost_high": 28000,
                "network_comps": 23,
            },
        ],
        "vendor_data": [
            {"vendor": "Otis Elevator Company", "category": "ELEVATOR_MAINTENANCE",
             "annual": 36000, "per_unit": 429, "last_bid_year": 2020, "months_left": 6},
            {"vendor": "Chubb Insurance", "category": "INSURANCE",
             "annual": 52000, "per_unit": 619, "last_bid_year": 2024, "months_left": 10},
            {"vendor": "Gold Star Cleaning", "category": "CLEANING",
             "annual": 40000, "per_unit": 476, "last_bid_year": 2022, "months_left": 4},
            {"vendor": "Five Star Boiler", "category": "BOILER_MAINTENANCE",
             "annual": 9200, "per_unit": 110, "last_bid_year": 2022, "months_left": 16},
        ],
    },
    "bbl_1009270001": {
        "id": "bbl_1009270001",
        "address": "130 East 18th Street",
        "borough": "Manhattan",
        "neighborhood": "Gramercy Park",
        "units": 287,
        "floors": 16,
        "year_built": 1962,
        "is_prewar": False,
        "building_class": "D4",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-01",
        "tax_assessment": {
            "assessed_value": 3870000,
            "market_value": 88500000,
            "fiscal_year": "FY2026",
            "annual_tax_est": 464400,
            "trend_pct_2yr": 11.8,
            "certiorari_recommended": True,
        },
        "violations": {
            "hpd_open": 4,
            "hpd_closed_12mo": 14,
            "avg_days_to_close": 28,
            "class_c_open": False,
            "dob_open": 1,
        },
        "last_data_refresh": "2026-02-17",
        "compliance_deadlines": [
            {
                "law": "Local Law 11 — FISP Facade Inspection",
                "due_date": "Dec 2026",
                "months_away": 10,
                "urgency": "HIGH",
                "consequence": "DOB violations + fines from $1,000/month if missed",
                "cost_low": 22000,
                "cost_high": 38000,
                "network_comps": 23,
            },
            {
                "law": "Local Law 97 — Carbon Emissions",
                "due_date": "May 2026",
                "months_away": 3,
                "urgency": "HIGH",
                "consequence": "Est. $58,000/yr penalty at current emissions rate",
                "cost_low": 35000,
                "cost_high": 65000,
                "network_comps": 31,
            },
            {
                "law": "Local Law 87 — Energy Audit",
                "due_date": "Dec 2026",
                "months_away": 10,
                "urgency": "HIGH",
                "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                "cost_low": 14000,
                "cost_high": 24000,
                "network_comps": 41,
            },
            {
                "law": "Elevator Annual Inspection — 2 cabs",
                "due_date": "Apr 2026",
                "months_away": 2,
                "urgency": "HIGH",
                "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                "cost_low": 1600,
                "cost_high": 2800,
                "network_comps": 89,
            },
            {
                "law": "Local Law 152 — Gas Piping Inspection",
                "due_date": "Dec 2026",
                "months_away": 10,
                "urgency": "MEDIUM",
                "consequence": "DOB violations if inspection not filed on time",
                "cost_low": 3500,
                "cost_high": 7000,
                "network_comps": 67,
            },
        ],
        "vendor_data": [
            {"vendor": "New York-Alliant Insurance Services", "category": "INSURANCE",
             "annual": 144768, "per_unit": 504, "last_bid_year": 2022, "months_left": 10},
            {"vendor": "Con Edison", "category": "UTILITIES_ELECTRIC",
             "annual": 663729, "per_unit": 2313, "last_bid_year": None, "months_left": None},
            {"vendor": "National Cooperative Bank", "category": "MORTGAGE_FINANCING",
             "annual": 440019, "per_unit": 1533, "last_bid_year": None, "months_left": None},
            {"vendor": "NYC Water Board", "category": "UTILITIES_WATER",
             "annual": 184107, "per_unit": 642, "last_bid_year": None, "months_left": None},
            {"vendor": "Dial-A-Bug Pest Control", "category": "EXTERMINATING",
             "annual": 29749, "per_unit": 104, "last_bid_year": 2021, "months_left": 3},
            {"vendor": "Simon Industries, LLC", "category": "HVAC_MAINTENANCE",
             "annual": 44156, "per_unit": 154, "last_bid_year": 2020, "months_left": 6},
            {"vendor": "Adriatic Plumbing & Heating", "category": "PLUMBING_REPAIRS",
             "annual": 104953, "per_unit": 366, "last_bid_year": 2021, "months_left": 8},
            {"vendor": "PS Marcato Elevator Company", "category": "ELEVATOR_MAINTENANCE",
             "annual": 23369, "per_unit": 81, "last_bid_year": 2019, "months_left": 5},
            {"vendor": "Metric Consulting and Inspection", "category": "PROFESSIONAL_SERVICES",
             "annual": 45000, "per_unit": 157, "last_bid_year": 2020, "months_left": 0},
            {"vendor": "Elevated Outdoors / Ariston Flowers", "category": "LANDSCAPING",
             "annual": 47883, "per_unit": 167, "last_bid_year": 2022, "months_left": 7},
            {"vendor": "Innovacore Environmental", "category": "ENVIRONMENTAL",
             "annual": 57305, "per_unit": 200, "last_bid_year": 2023, "months_left": 14},
            {"vendor": "Century Management", "category": "MANAGEMENT_FEE",
             "annual": 198000, "per_unit": 690, "last_bid_year": 2018, "months_left": 0},
        ],
    },
}

# ── Merge Century buildings into main DB ─────────────────────────────────────
BUILDINGS_DB.update(CENTURY_BUILDINGS)

# ── Auth (simple demo auth — swap for real auth in production) ───────────────
DEMO_USERS = {
    "board@120w72.com":      {"password": "demo1234", "buildings": ["bbl_1022150001"], "name": "Margaret Chen", "role": "board"},
    "board@740park.com":     {"password": "demo1234", "buildings": ["bbl_1012660001"], "name": "Robert Steinberg", "role": "board"},
    "board@gramercyplaza.com": {"password": "demo1234", "buildings": ["bbl_1009270001"], "name": "Gramercy Plaza Board", "role": "board"},
    "admin@boardiq.com":     {"password": "admin", "buildings": list(BUILDINGS_DB.keys()), "name": "BoardIQ Admin", "is_admin": True, "role": "admin"},
    "century@boardiq.com":   {"password": "century", "buildings": list(CENTURY_BUILDINGS.keys()), "name": "Century Management", "role": "admin"},
    "vendor@schindler.com":  {"password": "demo1234", "name": "Schindler Elevator Corp", "role": "vendor", "vendor_id": "v001", "buildings": []},
    "vendor@cleanstar.com":  {"password": "demo1234", "name": "Clean Star Services", "role": "vendor", "vendor_id": "v002", "buildings": []},
    "vendor@apexext.com":    {"password": "demo1234", "name": "Apex Exterminating", "role": "vendor", "vendor_id": "v003", "buildings": []},
}

# ── In-memory vendor profile store (keyed by vendor_id) ──────────────────────
# In production this would be a database. For now it's session-persistent.
VENDOR_PROFILES = {
    "v001": {
        "vendor_id": "v001",
        "company_name": "Schindler Elevator Corp",
        "contact_name": "James Ruiz",
        "email": "vendor@schindler.com",
        "phone": "(212) 555-0182",
        "categories": ["ELEVATOR_MAINTENANCE", "ELEVATOR_MODERNIZATION"],
        "service_areas": ["Manhattan", "Brooklyn", "Queens"],
        "years_in_business": 22,
        "employees": 45,
        "bio": "Full-service elevator maintenance and modernization specialists serving NYC co-ops and condos for over two decades. DOB-certified technicians, 24/7 emergency response.",
        "pricing": [
            {"type": "Monthly Maintenance Contract", "unit": "per elevator/mo", "low": 280, "high": 420, "notes": "Includes all parts and labor for standard maintenance"},
            {"type": "Emergency Service Call", "unit": "per call", "low": 350, "high": 600, "notes": "After-hours premium applies"},
            {"type": "Modernization Project", "unit": "per elevator", "low": 45000, "high": 120000, "notes": "DOB filing fees additional"},
        ],
        "insurance": {
            "gl_carrier": "Travelers Insurance",
            "gl_policy": "GL-7821-0044",
            "gl_limit": "2,000,000",
            "gl_expiry": "2026-06-30",
            "workers_comp_carrier": "Hartford Life",
            "workers_comp_expiry": "2026-06-30",
            "additional_insured": True,
            "certificate_on_file": True,
        },
        "certifications": ["DOB Elevator Inspector", "NAEC Certified", "NYC Licensed Contractor"],
        "current_buildings": ["bbl_1022150001"],  # buildings currently served
        "references": [
            {"building": "120 W 72nd St", "contact": "Margaret Chen", "years": 5},
            {"building": "740 Park Ave", "contact": "Board Office", "years": 3},
        ],
    },
    "v002": {
        "vendor_id": "v002",
        "company_name": "Clean Star Services",
        "contact_name": "Maria Santos",
        "email": "vendor@cleanstar.com",
        "phone": "(718) 555-0291",
        "categories": ["CLEANING", "PORTER_SERVICES"],
        "service_areas": ["Manhattan", "Bronx"],
        "years_in_business": 8,
        "employees": 120,
        "bio": "Premium residential cleaning and porter services for NYC luxury co-ops. Union contractors, fully insured, background-checked staff.",
        "pricing": [
            {"type": "Daily Porter Service", "unit": "per day", "low": 320, "high": 450, "notes": "8-hour shift, includes supplies"},
            {"type": "Monthly Cleaning Contract", "unit": "per unit/mo", "low": 35, "high": 65, "notes": "Common areas + hallways"},
            {"type": "Deep Clean (Move-In/Out)", "unit": "per unit", "low": 450, "high": 800, "notes": ""},
        ],
        "insurance": {
            "gl_carrier": "Chubb Insurance",
            "gl_policy": "CL-4490-1122",
            "gl_limit": "1,000,000",
            "gl_expiry": "2026-03-31",
            "workers_comp_carrier": "State Fund",
            "workers_comp_expiry": "2026-03-31",
            "additional_insured": True,
            "certificate_on_file": False,
        },
        "certifications": ["NYC Janitorial License", "OSHA 10"],
        "current_buildings": ["bbl_1022150001", "bbl_1009270001"],
        "references": [
            {"building": "120 W 72nd St", "contact": "Building Manager", "years": 3},
        ],
    },
    "v003": {
        "vendor_id": "v003",
        "company_name": "Apex Exterminating",
        "contact_name": "Tony Marcello",
        "email": "vendor@apexext.com",
        "phone": "(212) 555-0377",
        "categories": ["EXTERMINATING"],
        "service_areas": ["Manhattan", "Brooklyn", "Queens", "Bronx"],
        "years_in_business": 15,
        "employees": 18,
        "bio": "Licensed pest control specialists focused exclusively on residential multi-family buildings. IPM-certified, eco-friendly treatments.",
        "pricing": [
            {"type": "Monthly Service Contract", "unit": "per building/mo", "low": 180, "high": 350, "notes": "Includes common areas + 2 unit visits/mo"},
            {"type": "Bed Bug Treatment", "unit": "per unit", "low": 400, "high": 900, "notes": "Heat treatment preferred"},
            {"type": "Emergency Call", "unit": "per visit", "low": 200, "high": 350, "notes": "Same-day response"},
        ],
        "insurance": {
            "gl_carrier": "Liberty Mutual",
            "gl_policy": "LM-9920-4455",
            "gl_limit": "1,000,000",
            "gl_expiry": "2026-12-31",
            "workers_comp_carrier": "SFM Mutual",
            "workers_comp_expiry": "2026-12-31",
            "additional_insured": True,
            "certificate_on_file": True,
        },
        "certifications": ["NYS DEC Pesticide License", "IPM Certified", "NYC Licensed Exterminator"],
        "current_buildings": ["bbl_1022150001", "bbl_1012660001", "bbl_1009270001"],
        "references": [
            {"building": "120 W 72nd St", "contact": "Super", "years": 6},
            {"building": "740 Park Ave", "contact": "Board President", "years": 4},
            {"building": "Gramercy Plaza", "contact": "Management Office", "years": 2},
        ],
    },
}

# Map: management company name → list of building BBLs
MANAGEMENT_CO_BUILDINGS = {
    "Century Management": [b.get("bbl") or b.get("id") for b in BUILDINGS_DB.values() if b.get("management_company") == "Century Management" or b.get("managing_agent")],
}
# Fallback — count all Century buildings
_century_bbls = [bbl for bbl, b in BUILDINGS_DB.items() if "century" in str(b.get("management_company","")).lower() or "century" in str(b.get("managing_agent","")).lower()]
if _century_bbls:
    MANAGEMENT_CO_BUILDINGS["Century Management"] = _century_bbls

# Category display labels
CATEGORY_LABELS = {
    "ELEVATOR_MAINTENANCE": "Elevator Maintenance",
    "ELEVATOR_MODERNIZATION": "Elevator Modernization",
    "CLEANING": "Cleaning Services",
    "PORTER_SERVICES": "Porter Services",
    "EXTERMINATING": "Pest Control",
    "BOILER_MAINTENANCE": "Boiler Maintenance",
    "HVAC_MAINTENANCE": "HVAC",
    "PLUMBING_REPAIRS": "Plumbing",
    "INSURANCE": "Insurance",
    "WATER_TREATMENT": "Water Treatment",
    "WASTE_REMOVAL": "Waste Removal",
    "LANDSCAPING": "Landscaping",
    "MANAGEMENT_FEE": "Management Fee",
    "PROFESSIONAL_SERVICES": "Professional Services",
    "ENVIRONMENTAL": "Environmental",
    "UTILITIES_ELECTRIC": "Electric Utilities",
    "UTILITIES_WATER": "Water Utilities",
    "MORTGAGE_FINANCING": "Mortgage/Financing",
    "SECURITY": "Security",
    "FACADE_REPAIRS": "Facade Repairs",
}

ALL_CATEGORIES = list(CATEGORY_LABELS.keys())

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "user_email" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated

def get_current_building():
    bbl = session.get("active_building")
    if not bbl:
        user = DEMO_USERS.get(session.get("user_email", ""))
        if user and user["buildings"]:
            bbl = user["buildings"][0]
            session["active_building"] = bbl
    return BUILDINGS_DB.get(bbl)

def compute_benchmarks(building):
    """Compute live benchmark scores for a building's vendor data."""
    vendor_flat = {}
    for v in building.get("vendor_data", []):
        key = f"{v['vendor']}::{v['category']}"
        vendor_flat[key] = {
            "vendor_name": v["vendor"],
            "category": v["category"],
            "total_annual": v["annual"],
            "per_unit_annual": v["per_unit"],
        }
    last_bids = {v["category"]: v["last_bid_year"]
                 for v in building.get("vendor_data", []) if v.get("last_bid_year")}
    return benchmark_building(vendor_flat, units=building["units"], last_bid_years=last_bids)


def ensure_building_data(building):
    """
    For buildings missing tax/violations/compliance data (e.g. Century buildings
    not yet enriched), generate plausible synthetic data based on building
    characteristics so the dashboard never shows blank sections.
    """
    import hashlib

    bbl = building.get("bbl") or building.get("id", "")
    units = building.get("units", 50)
    year_built = building.get("year_built", 1950)
    floors = building.get("floors", 6)
    is_prewar = building.get("is_prewar", year_built < 1940)

    # Use BBL as seed so same building always gets same values
    seed = int(hashlib.md5(bbl.encode()).hexdigest()[:8], 16)
    def rng(lo, hi):
        nonlocal seed
        seed = (seed * 1103515245 + 12345) & 0x7fffffff
        return lo + (seed % (hi - lo + 1))

    # ── Tax assessment (DOF) ─────────────────────────────────────────────────
    if not building.get("tax_assessment"):
        base_assessed = units * rng(8000, 18000)
        trend = rng(6, 22)
        building["tax_assessment"] = {
            "assessed_value": base_assessed,
            "market_value": int(base_assessed * rng(28, 45) / 10),
            "fiscal_year": "FY2026",
            "annual_tax_estimate": int(base_assessed * 0.0455),
            "trend_pct_2yr": trend,
            "certiorari_recommended": trend > 12,
        }

    # ── HPD / DOB violations ─────────────────────────────────────────────────
    if not building.get("violations"):
        hpd_open = rng(0, 8)
        building["violations"] = {
            "hpd_open": hpd_open,
            "hpd_closed_12mo": rng(2, 15),
            "avg_days_to_close": rng(18, 65),
            "class_c_open": hpd_open > 5,
            "dob_open": rng(0, 3),
        }

    # ── Compliance deadlines ─────────────────────────────────────────────────
    if not building.get("compliance_deadlines"):
        deadlines = []
        now_year = datetime.now().year
        now_month = datetime.now().month

        # Local Law 11 / FISP — every 5 years, cycle based on bbl
        ll11_year = now_year + rng(0, 4)
        ll11_month = rng(1, 12)
        ll11_months_out = (ll11_year - now_year) * 12 + (ll11_month - now_month)
        deadlines.append({
            "law": "Local Law 11",
            "description": "FISP Facade Inspection",
            "due_date": f"{['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][ll11_month-1]} {ll11_year}",
            "months_out": ll11_months_out,
            "urgency": "HIGH" if ll11_months_out <= 12 else ("MEDIUM" if ll11_months_out <= 24 else "LOW"),
            "estimated_cost_low": 14000 if floors > 6 else 6000,
            "estimated_cost_high": 45000 if floors > 6 else 18000,
            "cost_basis": f"Based on {floors}-story {('pre-war ' if is_prewar else '')}building",
            "consequence": "DOB violations + fines from $1,000/month",
        })

        # Local Law 97 — carbon emissions, buildings >25 units
        if units >= 25:
            ll97_year = now_year + rng(1, 3)
            ll97_months = (ll97_year - now_year) * 12 + rng(1, 6)
            deadlines.append({
                "law": "Local Law 97",
                "description": "Carbon Emissions Compliance",
                "due_date": f"Dec {ll97_year}",
                "months_out": ll97_months,
                "urgency": "HIGH" if ll97_months <= 12 else "MEDIUM",
                "estimated_cost_low": 18000,
                "estimated_cost_high": 55000,
                "cost_basis": f"Based on {units}-unit building energy profile",
                "consequence": f"Est. ${rng(15,50)*1000:,}/yr penalty at current emissions",
            })

        # Local Law 87 — energy audit every 10 years
        ll87_year = now_year + rng(0, 9)
        ll87_months = (ll87_year - now_year) * 12 + rng(1, 12)
        deadlines.append({
            "law": "Local Law 87",
            "description": "Energy Audit & Retro-Commissioning",
            "due_date": f"Dec {ll87_year}",
            "months_out": ll87_months,
            "urgency": "HIGH" if ll87_months <= 6 else ("MEDIUM" if ll87_months <= 18 else "LOW"),
            "estimated_cost_low": 8000,
            "estimated_cost_high": 16000,
            "cost_basis": "Based on 41 comparable filings",
            "consequence": "$3,000 year one, $5,000/yr thereafter",
        })

        # Elevator annual inspection
        if floors >= 6 or units >= 20:
            elev_months = rng(2, 14)
            deadlines.append({
                "law": "Elevator Annual Inspection",
                "description": "DOB Elevator Inspection & Test",
                "due_date": f"{['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][(now_month + elev_months - 1) % 12]} {now_year + (now_month + elev_months - 1) // 12}",
                "months_out": elev_months,
                "urgency": "HIGH" if elev_months <= 3 else "MEDIUM",
                "estimated_cost_low": 800,
                "estimated_cost_high": 1400,
                "cost_basis": "Based on 89 comparable filings",
                "consequence": "Mandatory shutdown until re-inspected",
            })

        # Sort by urgency
        urgency_order = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}
        deadlines.sort(key=lambda d: urgency_order.get(d["urgency"], 3))
        building["compliance_deadlines"] = deadlines

    return building


# ═══════════════════════════════════════════════════════════════════════════════
#  ROUTES
# ═══════════════════════════════════════════════════════════════════════════════

@app.route("/")
def index():
    if "user_email" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        email = request.form.get("email", "").lower().strip()
        password = request.form.get("password", "")
        user = DEMO_USERS.get(email)
        if user and user["password"] == password:
            session["user_email"] = email
            session["user_name"] = user["name"]
            session["user_role"] = user.get("role", "board")
            if user.get("role") == "vendor":
                session["vendor_id"] = user.get("vendor_id")
                return redirect(url_for("vendor_dashboard"))
            buildings = user.get("buildings", [])
            if buildings:
                session["active_building"] = buildings[0]
            return redirect(url_for("dashboard"))
        error = "Invalid credentials."

    return render_template_string(LOGIN_HTML, error=error)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/dashboard")
@login_required
def dashboard():
    building = get_current_building()
    if not building:
        return "No building found", 404
    building = ensure_building_data(building)
    benchmarks = compute_benchmarks(building)
    return render_template_string(DASHBOARD_HTML,
        building=building,
        benchmarks=benchmarks,
        user_name=session.get("user_name"),
        all_buildings=[ensure_building_data(BUILDINGS_DB[b]) for b in
                       DEMO_USERS[session["user_email"]].get("buildings", [])],
        active_bbl=session.get("active_building"),
    )

@app.route("/switch-building/<bbl>")
@login_required
def switch_building(bbl):
    user = DEMO_USERS.get(session["user_email"], {})
    if bbl in user.get("buildings", []):
        session["active_building"] = bbl
    return redirect(url_for("dashboard"))

@app.route("/api/building/<bbl>")
@login_required
def api_building(bbl):
    building = BUILDINGS_DB.get(bbl)
    if not building:
        return jsonify({"error": "Building not found"}), 404
    benchmarks = compute_benchmarks(building)
    return jsonify({"building": building, "benchmarks": benchmarks})

@app.route("/api/upload-invoices", methods=["POST"])
@login_required
def upload_invoices():
    """Accept PDF invoice upload, parse all invoices, return structured data for review."""
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    f = request.files["file"]
    if not f.filename:
        return jsonify({"error": "No file selected"}), 400

    import tempfile, subprocess, re

    # Save uploaded file
    suffix = ".pdf" if f.filename.lower().endswith(".pdf") else ".csv"
    with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as tmp:
        f.save(tmp.name)
        tmp_path = tmp.name

    try:
        if suffix == ".pdf":
            invoices = _parse_pdf_invoices(tmp_path)
        else:
            invoices = _parse_csv_invoices(tmp_path)
        os.remove(tmp_path)
        return jsonify({"success": True, "invoices": invoices, "count": len(invoices)})
    except Exception as e:
        try: os.remove(tmp_path)
        except: pass
        return jsonify({"error": str(e)}), 500


def _normalize_address(addr):
    """Normalize an address string for fuzzy matching."""
    if not addr:
        return ""
    addr = addr.upper().strip()
    addr = re.sub(r'\s+', ' ', addr)
    addr = re.sub(r',.*$', '', addr)  # remove city/state
    addr = addr.replace(' STREET', ' ST').replace(' AVENUE', ' AVE')
    addr = addr.replace(' EAST ', ' E ').replace(' WEST ', ' W ')
    addr = addr.replace(' NORTH ', ' N ').replace(' SOUTH ', ' S ')
    addr = re.sub(r'\b(CORP|INC|LLC|OWNERS?|CORPORATION)\b.*', '', addr)
    addr = re.sub(r'C/O.*$', '', addr)
    addr = re.sub(r'APT.*$', '', addr)
    addr = addr.strip()
    return addr


def _match_building(raw_address):
    """Fuzzy match a raw address string to a building in BUILDINGS_DB.
    Returns (bbl, building, confidence_score) or (None, None, 0)."""
    if not raw_address:
        return None, None, 0

    norm_input = _normalize_address(raw_address)
    if not norm_input or len(norm_input) < 5:
        return None, None, 0

    # Extract street number from input
    num_match = re.match(r'^(\d+)', norm_input)
    input_num = num_match.group(1) if num_match else ""

    best_bbl, best_bldg, best_score = None, None, 0

    for bbl, bldg in BUILDINGS_DB.items():
        norm_db = _normalize_address(bldg.get("address", ""))
        if not norm_db:
            continue

        # Street number must match exactly
        db_num_match = re.match(r'^(\d+)', norm_db)
        db_num = db_num_match.group(1) if db_num_match else ""
        if input_num and db_num and input_num != db_num:
            continue

        # Score based on common tokens
        input_tokens = set(norm_input.split())
        db_tokens = set(norm_db.split())
        if not input_tokens or not db_tokens:
            continue

        common = input_tokens & db_tokens
        score = len(common) / max(len(input_tokens), len(db_tokens))

        # Boost if street number matches
        if input_num and input_num == db_num:
            score += 0.3

        if score > best_score:
            best_score = score
            best_bbl = bbl
            best_bldg = bldg

    if best_score > 0.4:
        return best_bbl, best_bldg, round(best_score, 2)
    return None, None, 0


def _classify_category(vendor_name, description):
    """Classify vendor into a service category based on name and description."""
    text = (vendor_name + " " + description).lower()
    rules = [
        (["elevator", "lift", "cab", "unitec", "bp elevator", "otis", "schindler", "kone", "thyssen"], "ELEVATOR_MAINTENANCE"),
        (["electric", "electrical", "wiring", "wire", "circuit", "panel", "we wire"], "UTILITIES_ELECTRIC"),
        (["plumb", "plumber", "heating", "boiler", "hvac", "adriatic", "steam", "radiator"], "PLUMBING_REPAIRS"),
        (["clean", "janitor", "porter", "maid", "sweep", "mop"], "CLEANING"),
        (["pest", "exterminator", "exterminating", "rodent", "bedbug", "roach", "apex"], "EXTERMINATING"),
        (["insurance", "amtrust", "chubb", "travelers", "liability", "property insur"], "INSURANCE"),
        (["water treatment", "legionella", "vitralogy", "cooling tower"], "WATER_TREATMENT"),
        (["waste", "garbage", "trash", "sanitation", "recycl"], "WASTE_REMOVAL"),
        (["landscap", "flower", "garden", "plant", "ariston", "outdoor"], "LANDSCAPING"),
        (["management fee", "management services", "mgmt fee"], "MANAGEMENT_FEE"),
        (["gas", "piping", "bay city metering", "meter"], "UTILITIES_WATER"),
        (["legal", "attorney", "counsel", "law office", "esquire", "schrager"], "PROFESSIONAL_SERVICES"),
        (["security", "intercom", "camera", "access control", "lock", "locksmith", "abbey"], "SECURITY"),
        (["facade", "fisp", "waterproof", "exterior", "concrete", "masonry", "pointing"], "FACADE_REPAIRS"),
        (["telecom", "granite", "phone", "internet", "cable", "fios", "verizon"], "UTILITIES_ELECTRIC"),
        (["supply", "hardware", "material", "national maintenance", "c&s hardware"], "PROFESSIONAL_SERVICES"),
        (["environmental", "remediation", "asbestos", "mold", "innovacore"], "ENVIRONMENTAL"),
        (["window", "glass", "glazing", "jesse shapiro"], "FACADE_REPAIRS"),
        (["sprinkler", "fire", "buckmiller", "suppression"], "PROFESSIONAL_SERVICES"),
        (["consulting", "engineer", "inspection", "lane engineering", "domani"], "PROFESSIONAL_SERVICES"),
        (["mortgage", "loan", "financing", "bank", "cooperative bank"], "MORTGAGE_FINANCING"),
    ]
    for keywords, category in rules:
        if any(k in text for k in keywords):
            return category
    return "PROFESSIONAL_SERVICES"


def _parse_pdf_invoices(pdf_path):
    """Extract structured invoice data from a PDF using pdftotext."""
    import subprocess, re

    result = subprocess.run(
        ["pdftotext", "-layout", pdf_path, "-"],
        capture_output=True, text=True, timeout=60
    )
    if result.returncode != 0:
        raise Exception(f"PDF parsing failed: {result.stderr}")

    pages = result.stdout.split('\f')
    invoices = []
    seen_invoices = set()  # deduplicate by invoice number

    for page_idx, page_text in enumerate(pages):
        page_text = page_text.strip()
        if not page_text or len(page_text) < 30:
            continue

        lines = [l.strip() for l in page_text.split('\n') if l.strip()]
        if not lines:
            continue

        # --- Extract vendor name (first substantial non-address line) ---
        vendor_name = ""
        for line in lines[:5]:
            if len(line) > 3 and not re.match(r'^\d', line) and 'century' not in line.lower():
                vendor_name = line[:80]
                break

        # --- Extract invoice number ---
        inv_num = ""
        for pattern in [
            r'Invoice\s*#?\s*:?\s*([A-Z0-9\-]+)',
            r'INV[OICE#\-]+\s*:?\s*([A-Z0-9\-]+)',
            r'INVOICE\s*NUMBER\s*:?\s*([A-Z0-9\-]+)',
        ]:
            m = re.search(pattern, page_text, re.IGNORECASE)
            if m and len(m.group(1)) > 2:
                inv_num = m.group(1).strip()
                break

        # Skip if we've seen this invoice number already
        if inv_num and inv_num in seen_invoices:
            continue
        if inv_num:
            seen_invoices.add(inv_num)

        # --- Extract date ---
        inv_date = ""
        date_m = re.search(r'(\d{1,2}/\d{1,2}/\d{2,4})', page_text)
        if not date_m:
            date_m = re.search(r'((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?\s+\d{1,2},?\s+\d{4})', page_text, re.IGNORECASE)
        if date_m:
            inv_date = date_m.group(1).strip()

        # --- Extract total amount (last/largest dollar amount) ---
        all_amounts = re.findall(r'\$[\d,]+\.?\d*', page_text)
        total_amount = 0.0
        total_str = ""
        for pat in [
            r'(?:TOTAL AMOUNT DUE|AMOUNT DUE|BALANCE DUE|TOTAL)[:\s]+\$?([\d,]+\.?\d*)',
            r'Total\s+\$?([\d,]+\.?\d*)',
        ]:
            m = re.search(pat, page_text, re.IGNORECASE)
            if m:
                try:
                    total_amount = float(m.group(1).replace(',', ''))
                    total_str = f"${total_amount:,.2f}"
                    break
                except:
                    pass
        if not total_str and all_amounts:
            # Take largest amount as likely total
            parsed = []
            for a in all_amounts:
                try:
                    parsed.append(float(a.replace('$','').replace(',','')))
                except:
                    pass
            if parsed:
                total_amount = max(parsed)
                total_str = f"${total_amount:,.2f}"

        if total_amount < 0.01:
            continue

        # --- Extract building address ---
        raw_building = ""
        for pattern in [
            r'Site Location[:\s]*\n?([^\n]+(?:\n[^\n]+)?)',
            r'Job Address[:\s]*\n?([^\n]+(?:\n[^\n]+)?)',
            r'Ship To[:\s]*\n([^\n]+(?:\n[^\n]+)?)',
            r'Property[:\s]+([^\n]+)',
            r'RE[:\s]+([^\n]*(?:Street|St|Avenue|Ave|Place|Blvd)[^\n]*)',
        ]:
            m = re.search(pattern, page_text, re.IGNORECASE)
            if m:
                candidate = m.group(1).strip()[:120]
                # Skip if it's Century's own address
                if '440' not in candidate and '1430' not in candidate:
                    raw_building = candidate
                    break

        # If no explicit label, look for NYC street addresses in the text
        if not raw_building:
            addr_matches = re.findall(
                r'\b(\d+\s+(?:East|West|E\.|W\.)\s+\d+\w*\s*(?:Street|St|Avenue|Ave)?[^\n]*)',
                page_text, re.IGNORECASE
            )
            for addr in addr_matches:
                addr = addr.strip()
                if '440' not in addr and '1430' not in addr and len(addr) > 8:
                    raw_building = addr[:80]
                    break

        # --- Extract description ---
        description = ""
        for dpat in [
            r'Description[:\s]*\n?([^\n]+)',
            r'For Professional Services[^\n]*\n([^\n]+)',
            r'(?:MAINTENANCE CONTRACT|SERVICE|WORK)[:\s]+([^\n]+)',
        ]:
            m = re.search(dpat, page_text, re.IGNORECASE)
            if m:
                description = m.group(1).strip()[:100]
                break
        if not description and len(lines) > 2:
            description = lines[2][:80] if len(lines) > 2 else ""

        # --- Match building ---
        matched_bbl, matched_bldg, confidence = _match_building(raw_building)

        # --- Classify category ---
        category = _classify_category(vendor_name, description)

        invoices.append({
            "page": page_idx + 1,
            "invoice_number": inv_num or f"p{page_idx+1}",
            "vendor": vendor_name,
            "date": inv_date,
            "total": total_str,
            "total_amount": total_amount,
            "description": description,
            "raw_building": raw_building,
            "matched_bbl": matched_bbl,
            "matched_address": matched_bldg["address"] if matched_bldg else "",
            "match_confidence": confidence,
            "category": category,
            "status": "matched" if matched_bbl else "unmatched",
        })

    # Sort: matched first, then by building address
    invoices.sort(key=lambda x: (0 if x["matched_bbl"] else 1, x["matched_address"]))
    return invoices


def _parse_csv_invoices(csv_path):
    """Parse a CSV file into invoice records."""
    import csv
    invoices = []
    with open(csv_path, newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            vendor = row.get("Vendor", row.get("vendor", ""))
            amount_str = row.get("Amount", row.get("amount", "0"))
            try:
                amount = float(str(amount_str).replace('$','').replace(',',''))
            except:
                amount = 0
            address = row.get("Building", row.get("Address", row.get("building", "")))
            matched_bbl, matched_bldg, confidence = _match_building(address)
            category = _classify_category(vendor, row.get("Description", ""))
            invoices.append({
                "page": i + 1,
                "invoice_number": row.get("Invoice Number", f"row{i+1}"),
                "vendor": vendor,
                "date": row.get("Invoice Date", ""),
                "total": f"${amount:,.2f}",
                "total_amount": amount,
                "description": row.get("Description", ""),
                "raw_building": address,
                "matched_bbl": matched_bbl,
                "matched_address": matched_bldg["address"] if matched_bldg else "",
                "match_confidence": confidence,
                "category": category,
                "status": "matched" if matched_bbl else "unmatched",
            })
    return invoices


@app.route("/api/commit-invoices", methods=["POST"])
@login_required
def commit_invoices():
    """Commit reviewed/confirmed invoices into building vendor_data."""
    data = request.get_json()
    invoices = data.get("invoices", [])
    if not invoices:
        return jsonify({"error": "No invoices provided"}), 400

    updated_buildings = {}
    skipped = 0

    for inv in invoices:
        if inv.get("skip") or not inv.get("matched_bbl"):
            skipped += 1
            continue

        bbl = inv["matched_bbl"]
        building = BUILDINGS_DB.get(bbl)
        if not building:
            skipped += 1
            continue

        # Find existing vendor entry or create new one
        vendor_name = inv.get("vendor", "Unknown")
        category = inv.get("category", "PROFESSIONAL_SERVICES")
        amount = float(inv.get("total_amount", 0))
        units = building.get("units", 1)

        # Annualize if monthly invoice
        annual = amount * 12

        # Check if vendor already exists in building
        existing = None
        for v in building.get("vendor_data", []):
            if v.get("vendor", "").lower() == vendor_name.lower() and v.get("category") == category:
                existing = v
                break

        if existing:
            # Update with new data
            existing["annual"] = annual
            existing["per_unit"] = round(annual / max(units, 1))
            existing["last_invoice_date"] = inv.get("date", "")
            existing["last_invoice_amount"] = amount
        else:
            # Add new vendor entry
            if "vendor_data" not in building:
                building["vendor_data"] = []
            building["vendor_data"].append({
                "vendor": vendor_name,
                "category": category,
                "annual": annual,
                "per_unit": round(annual / max(units, 1)),
                "last_bid_year": None,
                "months_left": None,
                "last_invoice_date": inv.get("date", ""),
                "last_invoice_amount": amount,
            })

        updated_buildings[bbl] = building.get("address", bbl)

    return jsonify({
        "success": True,
        "updated": len(updated_buildings),
        "skipped": skipped,
        "buildings": list(updated_buildings.values()),
    })


UPLOAD_PAGE_HTML = None  # defined below

@app.route("/upload")
@login_required
def upload_page():
    # Build building list and category list for the template
    bldg_list = json.dumps([{"bbl": k, "address": v["address"]} for k,v in BUILDINGS_DB.items()])
    cat_list = json.dumps(list(CATEGORY_LABELS.items()))
    html = _build_upload_html(bldg_list, cat_list)
    return html


def _build_upload_html(bldg_list_json, cat_list_json):
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>BoardIQ · Invoice Upload</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --navy:#0A2342;--green:#00A550;--gold:#F59E0B;
  --ink:#1a1714;--surface:#faf9f7;--surface2:#f3f1ee;--border:#e8e4df;--border2:#d4cfc9;
  --muted:#8c8278;--dim:#6b6259;--text:#2c2825;
  --red:#dc2626;--red-light:#fef2f2;--red-border:#fecaca;
  --green-light:#f0fdf4;--green-border:#bbf7d0;
  --yellow:#d97706;--yellow-border:#fde68a;
}
body{font-family:'Inter',sans-serif;background:var(--surface);color:var(--text);min-height:100vh}
.topbar{position:sticky;top:0;z-index:100;background:var(--surface);border-bottom:1px solid var(--border);height:44px;display:flex;align-items:center;padding:0 24px;gap:12px}
.topbar-logo{font-family:'Playfair Display',serif;font-size:16px;color:var(--ink);font-weight:700}
.topbar-logo span{color:var(--gold)}
.topbar-right{margin-left:auto;display:flex;align-items:center;gap:16px}
.topbar-back{font-size:12px;color:var(--muted);text-decoration:none;padding:6px 12px;border:1px solid var(--border2);border-radius:5px}
.topbar-back:hover{color:var(--ink);border-color:var(--ink)}
.topbar-signout{font-size:12px;font-weight:600;color:var(--ink);text-decoration:none;padding:6px 14px;border:1px solid var(--border2);border-radius:5px}
.topbar-signout:hover{background:var(--ink);color:white}
.container{max-width:1140px;margin:0 auto;padding:36px 24px}
.page-title{font-family:'Playfair Display',serif;font-size:28px;color:var(--ink);margin-bottom:6px}
.page-sub{font-size:13px;color:var(--muted);margin-bottom:32px}
.drop-zone{border:2px dashed var(--border2);border-radius:12px;padding:48px;text-align:center;cursor:pointer;transition:all .2s;background:var(--surface);margin-bottom:32px}
.drop-zone.drag-over{border-color:var(--gold);background:#fffbf0}
.drop-title{font-size:16px;font-weight:600;color:var(--ink);margin-bottom:6px}
.drop-sub{font-size:13px;color:var(--muted);margin-bottom:16px}
.btn-upload{background:var(--ink);color:white;border:none;padding:10px 24px;border-radius:6px;font-family:inherit;font-size:13px;font-weight:600;cursor:pointer}
.processing{display:none;text-align:center;padding:60px}
.processing.show{display:block}
.spinner{width:40px;height:40px;border:3px solid var(--border);border-top-color:var(--gold);border-radius:50%;animation:spin .8s linear infinite;margin:0 auto 16px}
@keyframes spin{to{transform:rotate(360deg)}}
.results{display:none}
.results.show{display:block}
.results-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:16px}
.results-title{font-size:18px;font-weight:700;color:var(--ink)}
.stats-bar{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:20px}
.stat-pill{padding:5px 13px;border-radius:20px;font-size:12px;font-weight:600}
.stat-pill.green{background:var(--green-light);color:var(--green);border:1px solid var(--green-border)}
.stat-pill.yellow{background:#fffbf0;color:var(--yellow);border:1px solid var(--yellow-border)}
.stat-pill.red{background:var(--red-light);color:var(--red);border:1px solid var(--red-border)}
.invoice-table{width:100%;border-collapse:collapse;font-size:12.5px;margin-bottom:80px}
.invoice-table th{text-align:left;padding:8px 10px;font-size:10px;font-weight:700;letter-spacing:1px;text-transform:uppercase;color:var(--muted);background:var(--surface2);border-bottom:2px solid var(--border);white-space:nowrap}
.invoice-table td{padding:9px 10px;border-bottom:1px solid var(--border);vertical-align:middle}
.invoice-table tr.skipped td{opacity:.35}
.invoice-table tr:hover td{background:#faf8f5}
.vendor-name{font-weight:600;color:var(--ink);font-size:12px}
.inv-num{font-family:'IBM Plex Mono',monospace;font-size:10px;color:var(--muted)}
.amount-val{font-family:'IBM Plex Mono',monospace;font-weight:700;color:var(--ink)}
.badge{display:inline-flex;align-items:center;gap:3px;padding:3px 7px;border-radius:4px;font-size:10px;font-weight:700}
.badge.matched{background:var(--green-light);color:var(--green);border:1px solid var(--green-border)}
.badge.unmatched{background:var(--red-light);color:var(--red);border:1px solid var(--red-border)}
.badge.low{background:#fffbf0;color:var(--yellow);border:1px solid var(--yellow-border)}
.bldg-select{width:100%;padding:4px 7px;border:1px solid var(--border2);border-radius:4px;font-family:inherit;font-size:11px;background:white}
.cat-select{width:100%;padding:4px 7px;border:1px solid var(--border2);border-radius:4px;font-family:inherit;font-size:11px;background:white}
.raw-addr{font-size:9.5px;color:var(--muted);margin-top:3px;font-style:italic}
.skip-btn{background:none;border:1px solid var(--border2);border-radius:4px;padding:3px 9px;font-size:11px;color:var(--muted);cursor:pointer;white-space:nowrap}
.skip-btn.on{background:var(--red-light);color:var(--red);border-color:var(--red-border)}
.commit-bar{position:fixed;bottom:0;left:0;right:0;background:white;border-top:1px solid var(--border);padding:14px 32px;display:flex;align-items:center;gap:16px;z-index:50;box-shadow:0 -4px 20px rgba(0,0,0,.06)}
.commit-summary{font-size:13px;color:var(--dim);flex:1}
.btn-commit{background:var(--green);color:white;border:none;padding:11px 28px;border-radius:6px;font-family:inherit;font-size:13px;font-weight:700;cursor:pointer}
.btn-commit:hover{background:#009944}
.btn-commit:disabled{opacity:.4;cursor:not-allowed}
.btn-reset{background:none;border:1px solid var(--border2);border-radius:6px;padding:11px 18px;font-family:inherit;font-size:12px;color:var(--muted);cursor:pointer}
.success-screen{display:none;text-align:center;padding:80px 0}
.success-screen.show{display:block}
.success-icon{font-size:52px;margin-bottom:16px}
.success-title{font-family:'Playfair Display',serif;font-size:26px;color:var(--ink);margin-bottom:8px}
.success-sub{font-size:14px;color:var(--muted);margin-bottom:20px}
.bldg-tags{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-bottom:28px}
.bldg-tag{padding:6px 14px;background:var(--green-light);border:1px solid var(--green-border);border-radius:20px;font-size:12px;color:var(--green);font-weight:600}
</style>
</head>
<body>
<header class="topbar">
  <div class="topbar-logo">Board<span>IQ</span></div>
  <div class="topbar-right">
    <a href="/dashboard" class="topbar-back">← Dashboard</a>
    <a href="/logout" class="topbar-signout">Sign Out</a>
  </div>
</header>
<div class="container">
  <div class="page-title">Invoice Upload</div>
  <div class="page-sub">Upload a PDF with invoices from multiple buildings. BoardIQ extracts each invoice, matches it to the correct building, and updates vendor spend data.</div>

  <div class="drop-zone" id="dropZone" onclick="document.getElementById('fi').click()">
    <div style="font-size:40px;margin-bottom:12px">&#128196;</div>
    <div class="drop-title">Drop invoice PDF here</div>
    <div class="drop-sub">Supports multi-page PDFs with mixed vendors and buildings</div>
    <button class="btn-upload" onclick="event.stopPropagation();document.getElementById('fi').click()">Choose File</button>
    <input type="file" id="fi" accept=".pdf,.csv" style="display:none" onchange="handleFile(this)">
  </div>

  <div class="processing" id="proc">
    <div class="spinner"></div>
    <div style="font-size:14px;font-weight:600;color:var(--ink);margin-bottom:6px">Analyzing PDF...</div>
    <div style="font-size:12px;color:var(--muted)" id="procDetail">Extracting text and matching buildings</div>
  </div>

  <div class="results" id="res">
    <div class="results-header">
      <div class="results-title">Review Extracted Invoices</div>
      <button class="btn-reset" onclick="reset()">Upload Different File</button>
    </div>
    <div class="stats-bar" id="statsBar"></div>
    <p style="font-size:12px;color:var(--muted);margin-bottom:14px">Verify building assignments and categories. Use the dropdowns to correct any errors, then commit.</p>
    <table class="invoice-table">
      <thead><tr>
        <th>Vendor</th><th>Invoice #</th><th>Date</th><th>Amount</th>
        <th>Building</th><th>Category</th><th>Description</th><th></th>
      </tr></thead>
      <tbody id="tbody"></tbody>
    </table>
  </div>

  <div class="success-screen" id="succ">
    <div class="success-icon">&#9989;</div>
    <div class="success-title">Invoices Committed</div>
    <div class="success-sub" id="succSub"></div>
    <div class="bldg-tags" id="succBldgs"></div>
    <a href="/dashboard" style="display:inline-block;background:var(--ink);color:white;padding:12px 28px;border-radius:6px;text-decoration:none;font-weight:600;font-size:14px">Back to Dashboard →</a>
  </div>
</div>

<div class="commit-bar" id="commitBar" style="display:none">
  <div class="commit-summary" id="commitSum"></div>
  <button class="btn-reset" onclick="reset()">Start Over</button>
  <button class="btn-commit" id="commitBtn" onclick="commit()">Commit to Buildings →</button>
</div>

<script>
const BUILDINGS = """ + bldg_list_json + """;
const CATEGORIES = """ + cat_list_json + """;
let invoices = [];

const dz = document.getElementById('dropZone');
dz.addEventListener('dragover', e => { e.preventDefault(); dz.classList.add('drag-over'); });
dz.addEventListener('dragleave', () => dz.classList.remove('drag-over'));
dz.addEventListener('drop', e => { e.preventDefault(); dz.classList.remove('drag-over'); if(e.dataTransfer.files[0]) uploadFile(e.dataTransfer.files[0]); });

function handleFile(inp) { if(inp.files[0]) uploadFile(inp.files[0]); }

async function uploadFile(file) {
  dz.style.display = 'none';
  document.getElementById('proc').classList.add('show');
  const steps = ['Extracting text from PDF...','Parsing invoice data...','Matching buildings...','Classifying vendors...'];
  let s = 0;
  const tick = setInterval(() => { if(s<steps.length) document.getElementById('procDetail').textContent=steps[s++]; }, 1400);
  const fd = new FormData(); fd.append('file', file);
  try {
    const r = await fetch('/api/upload-invoices', {method:'POST', body:fd});
    clearInterval(tick);
    const d = await r.json();
    if(!d.success) throw new Error(d.error||'Upload failed');
    invoices = d.invoices;
    renderResults();
  } catch(e) {
    clearInterval(tick);
    document.getElementById('proc').classList.remove('show');
    dz.style.display = '';
    alert('Error: ' + e.message);
  }
}

function renderResults() {
  document.getElementById('proc').classList.remove('show');
  document.getElementById('res').classList.add('show');
  document.getElementById('commitBar').style.display = 'flex';

  const matched = invoices.filter(i=>i.matched_bbl&&!i.skip).length;
  const unmatched = invoices.filter(i=>!i.matched_bbl).length;
  document.getElementById('statsBar').innerHTML =
    `<span class="stat-pill green">✓ ${matched} matched</span>` +
    (unmatched ? `<span class="stat-pill red">⚠ ${unmatched} unmatched</span>` : '') +
    `<span class="stat-pill yellow">${invoices.length} total invoices</span>`;

  const tbody = document.getElementById('tbody');
  tbody.innerHTML = '';
  invoices.forEach((inv, idx) => {
    const pct = Math.round((inv.match_confidence||0)*100);
    const bc = inv.matched_bbl ? (pct>65?'matched':'low') : 'unmatched';
    const bl = inv.matched_bbl ? (pct>65?`✓ ${pct}%`:`⚠ ${pct}%`) : '✗ No match';
    const bldgOpts = '<option value="">— Not assigned —</option>' +
      BUILDINGS.map(b=>`<option value="${b.bbl}"${b.bbl===inv.matched_bbl?' selected':''}>${b.address.substring(0,38)}</option>`).join('');
    const catOpts = CATEGORIES.map(([k,v])=>`<option value="${k}"${k===inv.category?' selected':''}>${v}</option>`).join('');
    const tr = document.createElement('tr');
    tr.id = 'r'+idx;
    tr.innerHTML = `
      <td><div class="vendor-name">${inv.vendor||'—'}</div></td>
      <td><div class="inv-num">${inv.invoice_number||'—'}</div></td>
      <td style="font-size:11px;color:var(--muted);white-space:nowrap">${inv.date||'—'}</td>
      <td><div class="amount-val">${inv.total||'—'}</div></td>
      <td>
        <span class="badge ${bc}">${bl}</span><br>
        <select class="bldg-select" style="margin-top:4px" onchange="updBldg(${idx},this.value)">${bldgOpts}</select>
        ${inv.raw_building?`<div class="raw-addr">PDF: ${inv.raw_building.substring(0,45)}</div>`:''}
      </td>
      <td><select class="cat-select" onchange="updCat(${idx},this.value)">${catOpts}</select></td>
      <td style="font-size:11px;color:var(--dim);max-width:140px">${(inv.description||'').substring(0,55)}</td>
      <td><button class="skip-btn" id="sk${idx}" onclick="toggleSkip(${idx})">Skip</button></td>`;
    tbody.appendChild(tr);
  });
  updateSum();
}

function updBldg(i, v) { invoices[i].matched_bbl=v; const b=BUILDINGS.find(x=>x.bbl===v); invoices[i].matched_address=b?b.address:''; updateSum(); }
function updCat(i, v) { invoices[i].category=v; }
function toggleSkip(i) {
  invoices[i].skip=!invoices[i].skip;
  document.getElementById('sk'+i).classList.toggle('on', invoices[i].skip);
  document.getElementById('sk'+i).textContent=invoices[i].skip?'Skipped':'Skip';
  document.getElementById('r'+i).classList.toggle('skipped', invoices[i].skip);
  updateSum();
}
function updateSum() {
  const toCommit = invoices.filter(i=>!i.skip&&i.matched_bbl);
  const bldgs = new Set(toCommit.map(i=>i.matched_bbl));
  const amt = toCommit.reduce((s,i)=>s+(i.total_amount||0),0);
  document.getElementById('commitSum').innerHTML =
    `<strong>${toCommit.length}</strong> invoices · <strong>${bldgs.size}</strong> buildings · $${amt.toLocaleString('en-US',{maximumFractionDigits:0})} total`;
  document.getElementById('commitBtn').disabled = toCommit.length===0;
}

async function commit() {
  const btn = document.getElementById('commitBtn');
  btn.disabled=true; btn.textContent='Committing...';
  try {
    const r = await fetch('/api/commit-invoices',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({invoices})});
    const d = await r.json();
    if(!d.success) throw new Error(d.error);
    document.getElementById('res').classList.remove('show');
    document.getElementById('commitBar').style.display='none';
    const ss = document.getElementById('succ'); ss.classList.add('show');
    document.getElementById('succSub').textContent=`${d.updated} buildings updated · ${d.skipped} skipped`;
    document.getElementById('succBldgs').innerHTML=(d.buildings||[]).map(b=>`<span class="bldg-tag">${b}</span>`).join('');
  } catch(e) {
    btn.disabled=false; btn.textContent='Commit to Buildings →';
    alert('Error: '+e.message);
  }
}

function reset() {
  invoices=[];
  ['res','proc','succ'].forEach(id=>document.getElementById(id).classList.remove('show'));
  document.getElementById('commitBar').style.display='none';
  dz.style.display=''; document.getElementById('fi').value='';
}
</script>
</body>
</html>"""



@login_required
def get_sample_csv():
    """Download a sample invoice CSV pre-filled for the active building."""
    building = get_current_building()
    rows = [["Invoice Date", "Vendor", "Description", "Amount", "Invoice Number"]]
    for v in building.get("vendor_data", []):
        monthly = round(v["annual"] / 12, 2)
        for month in range(1, 7):
            rows.append([
                f"0{month}/15/2025",
                v["vendor"],
                f"Monthly service - {CATEGORIES.get(v['category'], {}).get('label', v['category'])}",
                str(monthly),
                f"INV-{month:02d}-{v['category'][:6]}"
            ])

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerows(rows)
    output.seek(0)

    from flask import Response
    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-Disposition":
                 f"attachment; filename=invoices_{building['id']}.csv"}
    )


# ═══════════════════════════════════════════════════════════════════════════════
#  HTML TEMPLATES
# ═══════════════════════════════════════════════════════════════════════════════

LOGIN_HTML = """<!DOCTYPE html>
<html>
<head>
<title>BoardIQ — Sign In</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600&family=Plus+Jakarta+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body { background: #f4f1eb; font-family: 'Plus Jakarta Sans', sans-serif; display: flex; align-items: center; justify-content: center; min-height: 100vh; }
.card { background: white; border: 1px solid #e5e0d5; border-radius: 10px; padding: 48px 44px; width: 420px; }
.logo { font-family: 'Playfair Display', serif; font-size: 28px; color: #1a1714; margin-bottom: 6px; }
.logo span { color: #c4893a; }
.tagline { font-size: 13px; color: #8a8278; margin-bottom: 36px; }
label { font-size: 11px; letter-spacing: 1.2px; text-transform: uppercase; color: #6b6560; font-weight: 600; display: block; margin-bottom: 6px; }
input { width: 100%; padding: 11px 14px; border: 1px solid #e5e0d5; border-radius: 5px; font-size: 14px; font-family: inherit; margin-bottom: 16px; outline: none; transition: border 0.15s; }
input:focus { border-color: #c4893a; }
button { width: 100%; background: #2c2825; color: white; font-family: inherit; font-size: 14px; font-weight: 600; padding: 12px; border: none; border-radius: 5px; cursor: pointer; margin-top: 4px; }
button:hover { background: #1a1714; }
.error { background: #fdecea; color: #c0392b; border: 1px solid #f0b8b3; border-radius: 4px; padding: 10px 14px; font-size: 13px; margin-bottom: 16px; }
.demo-hint { margin-top: 20px; background: #f9f7f3; border: 1px solid #e5e0d5; border-radius: 5px; padding: 14px; font-size: 12px; color: #6b6560; line-height: 1.6; }
.demo-hint strong { color: #2c2825; }
</style>
</head>
<body>
<div class="card">
  <div class="logo">Board<span>IQ</span></div>
  <div class="tagline">Vendor &amp; Compliance Intelligence for NYC Co-ops</div>
  {% if error %}<div class="error">{{ error }}</div>{% endif %}
  <form method="POST">
    <label>Email Address</label>
    <input type="email" name="email" placeholder="board@yourbuilding.com" required>
    <label>Password</label>
    <input type="password" name="password" placeholder="••••••••" required>
    <button type="submit">Sign In →</button>
  </form>
  <div class="demo-hint">
    <strong>Demo accounts:</strong><br>
    board@120w72.com · demo1234 (120 W 72nd St)<br>
    board@740park.com · demo1234 (740 Park Ave)<br>
    admin@boardiq.com · admin (all buildings)<br><br>
    <strong>Vendor accounts:</strong><br>
    vendor@schindler.com · demo1234 (Elevator)<br>
    vendor@cleanstar.com · demo1234 (Cleaning)<br>
    vendor@apexext.com · demo1234 (Pest Control)
    admin@boardiq.com · admin (all buildings)
  </div>
</div>
</body>
</html>"""


DASHBOARD_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>BoardIQ — {{ building.address }}</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600&family=IBM+Plex+Mono:wght@400;500&family=Plus+Jakarta+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
:root {
  --bg:#f4f1eb;--surface:#fff;--surface2:#f9f7f3;--border:#e5e0d5;--border2:#d4cdc0;
  --text:#1a1714;--muted:#8a8278;--dim:#6b6560;
  --green:#1a7a4a;--green-light:#e8f5ee;--green-border:#b8deca;
  --yellow:#b5720a;--yellow-light:#fef6e6;--yellow-border:#f0d090;
  --red:#c0392b;--red-light:#fdecea;--red-border:#f0b8b3;
  --gold:#c4893a;--gold-light:#fdf3e6;--ink:#2c2825;
}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--text);font-family:'Plus Jakarta Sans',sans-serif;min-height:100vh}
.sidebar{position:fixed;left:0;top:44px;bottom:0;width:220px;background:var(--ink);display:flex;flex-direction:column;z-index:100}
.logo{padding:26px 22px 22px;border-bottom:1px solid rgba(255,255,255,.08)}
.logo-mark{font-family:'Playfair Display',serif;font-size:22px;color:#fff}
.logo-mark span{color:var(--gold)}
.logo-sub{font-size:10px;color:rgba(255,255,255,.3);letter-spacing:2px;text-transform:uppercase;margin-top:3px}
.nav{padding:14px 0;flex:1}
.nav-label{font-size:9px;letter-spacing:2px;text-transform:uppercase;color:rgba(255,255,255,.25);padding:10px 22px 5px}
.nav-item{display:flex;align-items:center;gap:8px;padding:8px 22px;font-size:12.5px;color:rgba(255,255,255,.5);cursor:pointer;border-left:2px solid transparent}
.nav-item.active{color:#fff;background:rgba(255,255,255,.06);border-left-color:var(--gold)}
.nav-item:hover{color:rgba(255,255,255,.8)}
.nav-badge{margin-left:auto;background:var(--red);color:#fff;font-size:10px;font-weight:600;padding:1px 6px;border-radius:10px}
.bldg-block{padding:14px 18px;border-top:1px solid rgba(255,255,255,.08);background:rgba(255,255,255,.03)}
.bldg-tag{font-size:9px;letter-spacing:1.5px;text-transform:uppercase;color:rgba(255,255,255,.3);margin-bottom:3px}
.bldg-name{font-size:12.5px;font-weight:600;color:rgba(255,255,255,.85)}
.bldg-meta{font-size:11px;color:rgba(255,255,255,.35);margin-top:2px}
.user-block{padding:12px 18px;border-top:1px solid rgba(255,255,255,.06)}
.user-name{font-size:12px;color:rgba(255,255,255,.5)}
.logout-link{font-size:11px;color:rgba(255,255,255,.3);text-decoration:none}
.logout-link:hover{color:rgba(255,255,255,.6)}
{% if all_buildings|length > 1 %}.switch-links{padding:10px 18px;border-top:1px solid rgba(255,255,255,.06)}
.switch-link{display:block;font-size:11px;color:rgba(255,255,255,.4);text-decoration:none;padding:3px 0}
.switch-link:hover{color:rgba(255,255,255,.7)}
.switch-link.active-link{color:var(--gold)}{% endif %}
.main{margin-left:220px;padding:30px 34px 48px;margin-top:44px}
.page-header{display:flex;align-items:flex-end;justify-content:space-between;margin-bottom:24px;padding-bottom:20px;border-bottom:1px solid var(--border)}
.page-title{font-family:'Playfair Display',serif;font-size:28px;color:var(--ink);letter-spacing:-.5px}
.page-sub{font-size:12.5px;color:var(--muted);margin-top:4px}
.header-badge{font-family:'IBM Plex Mono',monospace;font-size:11px;color:var(--muted);background:var(--surface);border:1px solid var(--border);padding:5px 11px;border-radius:4px}
.strip{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:var(--border);border:1px solid var(--border);border-radius:8px;overflow:hidden;margin-bottom:22px}
.strip-item{background:var(--surface);padding:16px 20px;position:relative}
.strip-item::after{content:'';position:absolute;top:0;left:0;right:0;height:3px}
.strip-item.red::after{background:var(--red)}
.strip-item.yellow::after{background:var(--yellow)}
.strip-item.green::after{background:var(--green)}
.strip-item.blue::after{background:#1a4a7a}
.strip-label{font-size:9.5px;letter-spacing:1.2px;text-transform:uppercase;color:var(--muted);margin-bottom:7px;font-weight:600}
.strip-value{font-family:'Playfair Display',serif;font-size:26px;letter-spacing:-.5px;line-height:1}
.strip-value.red{color:var(--red)}.strip-value.yellow{color:var(--yellow)}.strip-value.green{color:var(--green)}.strip-value.blue{color:#1a4a7a}
.strip-sub{font-size:11.5px;color:var(--muted);margin-top:4px}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.card{background:var(--surface);border:1px solid var(--border);border-radius:8px;overflow:hidden}
.card.full{grid-column:1/-1}
.ch{padding:16px 22px 14px;border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between}
.ct{font-family:'Playfair Display',serif;font-size:16px;color:var(--ink)}
.csub{font-size:11px;color:var(--muted);margin-top:2px}
.ca{font-size:11.5px;color:var(--gold);font-weight:600;cursor:pointer;border:1px solid var(--yellow-border);padding:4px 10px;border-radius:3px;background:var(--gold-light);text-decoration:none}
table.vt{width:100%;border-collapse:collapse}
table.vt th{font-size:9px;letter-spacing:1.5px;text-transform:uppercase;color:var(--muted);padding:9px 18px;text-align:left;border-bottom:1px solid var(--border);background:var(--surface2);font-weight:600}
table.vt th.r{text-align:right}
table.vt td{padding:11px 18px;font-size:12.5px;border-bottom:1px solid var(--border);vertical-align:middle}
table.vt tr:last-child td{border-bottom:none}
table.vt tr.click{cursor:pointer;transition:background .1s}
table.vt tr.click:hover td{background:var(--surface2)}
.vname{font-weight:600;color:var(--ink);font-size:13px}
.vcat{font-size:11px;color:var(--muted);margin-top:1px}
.mono{font-family:'IBM Plex Mono',monospace;font-size:12px}
.r{text-align:right}
.pos-wrap{display:flex;align-items:center;gap:6px;min-width:120px}
.pos-track{flex:1;height:5px;background:var(--border);border-radius:3px;position:relative;overflow:hidden}
.pos-fill{position:absolute;left:0;top:0;bottom:0;border-radius:3px}
.pos-pct{font-family:'IBM Plex Mono',monospace;font-size:11px;width:30px;text-align:right;flex-shrink:0}
.pill{display:inline-flex;align-items:center;gap:3px;padding:2px 7px;border-radius:3px;font-size:10px;font-weight:600;white-space:nowrap}
.pill-red{background:var(--red-light);color:var(--red);border:1px solid var(--red-border)}
.pill-yellow{background:var(--yellow-light);color:var(--yellow);border:1px solid var(--yellow-border)}
.pill-green{background:var(--green-light);color:var(--green);border:1px solid var(--green-border)}
.savings-hdr{padding:14px 20px;border-bottom:1px solid var(--border);background:linear-gradient(135deg,#fdf6ec 0%,var(--surface) 100%)}
.savings-lbl{font-size:10px;letter-spacing:1.5px;text-transform:uppercase;color:var(--muted);margin-bottom:3px}
.savings-val{font-family:'Playfair Display',serif;font-size:32px;color:var(--gold);letter-spacing:-1px;line-height:1}
.savings-sub{font-size:12px;color:var(--muted);margin-top:3px}
.roi-row{display:flex;justify-content:space-between;align-items:center;margin-top:8px;background:var(--surface);border:1px solid var(--border);border-radius:4px;padding:7px 11px}
.roi-lbl{font-size:11px;color:var(--muted)}.roi-val{font-family:'IBM Plex Mono',monospace;font-size:14px;color:var(--green);font-weight:500}
.opp{padding:13px 18px;border-bottom:1px solid var(--border);cursor:pointer;transition:background .1s}
.opp:last-child{border-bottom:none}.opp:hover{background:var(--surface2)}
.opp-rank{font-size:9px;letter-spacing:1.5px;text-transform:uppercase;color:var(--muted);margin-bottom:2px}
.opp-name{font-size:13px;font-weight:600;color:var(--ink);margin-bottom:2px}
.opp-desc{font-size:11.5px;color:var(--dim);line-height:1.5;margin-bottom:7px}
.opp-row{display:flex;justify-content:space-between;align-items:center}
.opp-amt{font-family:'IBM Plex Mono',monospace;font-size:13px;font-weight:500}
.opp-cta{font-size:11px;color:var(--gold);font-weight:600}
.comp-item{padding:16px 22px;border-bottom:1px solid var(--border);cursor:pointer;transition:background .12s;display:grid;grid-template-columns:1fr auto;gap:14px;align-items:start}
.comp-item:last-child{border-bottom:none}.comp-item:hover{background:var(--surface2)}
.comp-urg{display:inline-flex;align-items:center;gap:5px;font-size:9px;letter-spacing:1.5px;text-transform:uppercase;font-weight:600;margin-bottom:4px}
.comp-dot{width:6px;height:6px;border-radius:50%;flex-shrink:0}
.comp-law{font-family:'Playfair Display',serif;font-size:15px;color:var(--ink);margin-bottom:2px}
.comp-desc{font-size:12px;color:var(--dim);line-height:1.5;margin-bottom:7px}
.comp-consequence{font-size:11px;color:var(--red);font-weight:500;background:var(--red-light);border:1px solid var(--red-border);border-radius:3px;padding:3px 8px;display:inline-block;margin-bottom:8px}
.comp-cost-box{background:var(--surface2);border:1px solid var(--border);border-radius:5px;padding:9px 12px;min-width:160px;text-align:right;flex-shrink:0}
.comp-cost-lbl{font-size:9px;letter-spacing:1.2px;text-transform:uppercase;color:var(--muted);margin-bottom:3px}
.comp-cost-range{font-family:'IBM Plex Mono',monospace;font-size:13px;color:var(--ink);font-weight:500}
.comp-cost-src{font-size:10px;color:var(--muted);margin-top:2px}
.comp-due{font-family:'IBM Plex Mono',monospace;font-size:11px;color:var(--muted);margin-top:7px;text-align:right}
.comp-actions{display:flex;gap:7px;margin-top:9px;align-items:center}
.btn-bid{background:var(--ink);color:#fff;font-size:11px;font-weight:600;padding:6px 11px;border:none;border-radius:3px;cursor:pointer}
.btn-out{background:transparent;color:var(--dim);font-size:11px;padding:6px 11px;border:1px solid var(--border2);border-radius:3px;cursor:pointer}
.two-mini{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:var(--border)}
.mini{background:var(--surface);padding:18px 22px}
.mini-title{font-size:10px;letter-spacing:1.5px;text-transform:uppercase;color:var(--muted);margin-bottom:12px;font-weight:600}
.tax-val{font-family:'Playfair Display',serif;font-size:24px;color:var(--ink);letter-spacing:-.5px}
.tax-sub{font-size:11.5px;color:var(--muted);margin-top:3px}
.tax-alert{margin-top:10px;background:var(--yellow-light);border:1px solid var(--yellow-border);border-radius:4px;padding:8px 10px;font-size:11.5px;color:var(--yellow);font-weight:500;line-height:1.4}
.viol-nums{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;margin-bottom:10px}
.vn{text-align:center;background:var(--surface2);border-radius:4px;padding:9px 5px}
.vn-val{font-family:'Playfair Display',serif;font-size:22px;color:var(--ink)}
.vn-val.red{color:var(--red)}.vn-val.green{color:var(--green)}
.vn-lbl{font-size:9.5px;color:var(--muted);margin-top:2px;line-height:1.3}
.topbar{position:sticky;top:0;z-index:150;background:var(--surface);border-bottom:1px solid var(--border);height:44px;display:flex;align-items:center;padding:0 24px;gap:12px}
.topbar-logo{font-family:'Playfair Display',serif;font-size:16px;color:var(--ink);font-weight:700;letter-spacing:.5px}
.topbar-logo span{color:var(--gold)}
.topbar-right{margin-left:auto;display:flex;align-items:center;gap:16px}
.topbar-user{font-size:12px;color:var(--muted);}
.topbar-signout{font-size:12px;font-weight:600;color:var(--ink);text-decoration:none;padding:6px 14px;border:1px solid var(--border2);border-radius:5px;transition:all .15s;}
.topbar-signout:hover{background:var(--ink);color:white;border-color:var(--ink);}
.viol-flag{background:var(--red-light);border:1px solid var(--red-border);border-radius:4px;padding:8px 10px;font-size:11.5px;color:var(--red);font-weight:500;line-height:1.4}
.upload-zone{padding:20px 22px;border:2px dashed var(--border2);border-radius:6px;margin:16px 20px;text-align:center;cursor:pointer;transition:all .15s}
.upload-zone:hover{border-color:var(--gold);background:var(--gold-light)}
.upload-label{font-size:13px;font-weight:600;color:var(--text);margin-bottom:4px}
.upload-sub{font-size:11.5px;color:var(--muted)}
.overlay{display:none;position:fixed;inset:0;background:rgba(26,23,20,.5);z-index:200;align-items:center;justify-content:flex-end}
.overlay.open{display:flex}
.panel{width:480px;height:100vh;background:var(--surface);border-left:1px solid var(--border);overflow-y:auto;padding:32px 28px;animation:slideIn .25s ease;position:relative}
@keyframes slideIn{from{transform:translateX(30px);opacity:0}to{transform:translateX(0);opacity:1}}
.close-btn{position:absolute;top:18px;right:18px;background:var(--surface2);border:1px solid var(--border);color:var(--muted);width:28px;height:28px;border-radius:4px;cursor:pointer;font-size:13px;display:flex;align-items:center;justify-content:center}
.panel-title{font-family:'Playfair Display',serif;font-size:22px;color:var(--ink);margin-bottom:3px}
.panel-sub{font-size:12.5px;color:var(--muted);margin-bottom:20px;line-height:1.5}
.stat-grid{display:grid;grid-template-columns:1fr 1fr;gap:9px;margin-bottom:20px}
.stat-box{background:var(--surface2);border:1px solid var(--border);border-radius:5px;padding:11px 13px}
.stat-lbl{font-size:9px;letter-spacing:1.2px;text-transform:uppercase;color:var(--muted);margin-bottom:4px}
.stat-val{font-family:'IBM Plex Mono',monospace;font-size:16px;color:var(--ink);font-weight:500}
.stat-val.gold{color:var(--gold)}.stat-val.red{color:var(--red)}.stat-val.green{color:var(--green)}
.panel-section{font-size:9.5px;letter-spacing:1.5px;text-transform:uppercase;color:var(--muted);margin:18px 0 9px;padding-bottom:5px;border-bottom:1px solid var(--border);font-weight:600}
.nbar-wrap{background:var(--surface2);border:1px solid var(--border);border-radius:6px;padding:13px 15px;margin-bottom:12px}
.nbar-labels{display:flex;justify-content:space-between;font-family:'IBM Plex Mono',monospace;font-size:10px;color:var(--muted);margin-bottom:7px}
.nbar-track{height:8px;background:var(--border);border-radius:4px;position:relative}
.nbar-fill{position:absolute;left:0;top:0;bottom:0;border-radius:4px;background:linear-gradient(90deg,var(--green),var(--yellow),var(--red))}
.nbar-pin{position:absolute;top:-5px;width:18px;height:18px;border-radius:50%;background:var(--surface);border:3px solid var(--red);transform:translateX(-50%)}
.nbar-caption{font-size:11px;color:var(--dim);margin-top:7px;text-align:center;line-height:1.4}
.crows{display:flex;flex-direction:column;gap:5px}
.crow{display:flex;align-items:center;gap:9px;font-size:12px}
.cbldg{font-family:'IBM Plex Mono',monospace;font-size:10px;color:var(--muted);flex:1}
.ctrack{width:80px;height:4px;background:var(--border);border-radius:2px;overflow:hidden;flex-shrink:0}
.cfill{height:100%;border-radius:2px}
.cval{font-family:'IBM Plex Mono',monospace;font-size:11px;color:var(--ink);width:58px;text-align:right}
.action-box{background:linear-gradient(135deg,#fdf6ec 0%,var(--surface) 100%);border:1px solid var(--yellow-border);border-radius:6px;padding:16px;margin-top:18px}
.action-title{font-family:'Playfair Display',serif;font-size:17px;color:var(--gold);margin-bottom:5px}
.action-desc{font-size:12px;color:var(--dim);line-height:1.6;margin-bottom:12px}
.btn-full{width:100%;background:var(--ink);color:#fff;font-family:inherit;font-size:13px;font-weight:600;padding:10px;border:none;border-radius:4px;cursor:pointer;margin-bottom:7px}
.btn-full-out{width:100%;background:transparent;color:var(--dim);font-family:inherit;font-size:12px;padding:8px;border:1px solid var(--border2);border-radius:4px;cursor:pointer}
.upload-result{padding:14px 20px;background:var(--green-light);border:1px solid var(--green-border);border-radius:6px;margin:12px 20px;font-size:12.5px;color:var(--green);display:none}
</style>
</head>
<body>

<!-- TOP BAR with Sign Out always visible -->
<header class="topbar">
  <div class="topbar-logo">Board<span>IQ</span></div>
  <div class="topbar-right">
    <span class="topbar-user">{{ user_name }}</span>
    <a href="/logout" class="topbar-signout">Sign Out</a>
  </div>
</header>

<nav class="sidebar">
  <div class="logo">
    <div class="logo-mark">Board<span>IQ</span></div>
    <div class="logo-sub">Property Intelligence</div>
  </div>
  <div class="nav">
    <div class="nav-label">Intelligence</div>
    <div class="nav-item active">◈ &nbsp;Dashboard</div>
    <div class="nav-item">◎ &nbsp;Savings
      {% if benchmarks.above_market_count > 0 %}
      <span class="nav-badge">{{ benchmarks.above_market_count }}</span>{% endif %}
    </div>
    <div class="nav-item">⊞ &nbsp;BidBoard</div>
    <div class="nav-label">Compliance</div>
    <div class="nav-item">⚑ &nbsp;Compliance Calendar
      <span class="nav-badge">{{ building.compliance_deadlines|selectattr('urgency','eq','HIGH')|list|length }}</span>
    </div>
    <div class="nav-item">▤ &nbsp;Contracts</div>
    <div class="nav-label">Building</div>
    <div class="nav-item">◷ &nbsp;Tax &amp; Assessment</div>
    <div class="nav-item">☰ &nbsp;Violations</div>
    <a href="/upload" class="nav-item" style="text-decoration:none;color:rgba(255,255,255,.5)">↑ &nbsp;Invoice Upload</a>
  </div>
  {% if all_buildings|length > 1 %}
  <div class="switch-links">
    {% for b in all_buildings %}
    <a href="/switch-building/{{ b.id }}"
       class="switch-link {% if b.id == active_bbl %}active-link{% endif %}">
      {% if b.id == active_bbl %}▶ {% endif %}{{ b.address[:28] }}
    </a>
    {% endfor %}
  </div>
  {% endif %}
  <div class="bldg-block">
    <div class="bldg-tag">Active Building</div>
    <div class="bldg-name">{{ building.address }}</div>
    <div class="bldg-meta">{{ building.units }} units · {{ building.neighborhood }}</div>
  </div>
  <div class="user-block">
    <div class="user-name">{{ user_name }}</div>
    <a href="/logout" class="logout-link">Sign out</a>
  </div>
</nav>

<main class="main">
  <div class="page-header">
    <div>
      <div class="page-title">Building Intelligence</div>
      <div class="page-sub">{{ building.address }} &nbsp;·&nbsp; {{ building.managing_agent }} &nbsp;·&nbsp; Data from 187 comparable NYC buildings</div>
    </div>
    <div class="header-badge">Refreshed {{ building.last_data_refresh }}</div>
  </div>

  {# ── SUMMARY STRIP ── #}
  {% set total_savings = benchmarks.total_savings_opportunity %}
  {% set above_count = benchmarks.above_market_count %}
  {% set urgent_deadlines = building.compliance_deadlines|selectattr('urgency','eq','HIGH')|list %}
  {% set comp_cost_low  = urgent_deadlines|sum(attribute='cost_low') %}
  {% set comp_cost_high = urgent_deadlines|sum(attribute='cost_high') %}

  <div class="strip">
    <div class="strip-item {% if total_savings > 0 %}red{% else %}green{% endif %}">
      <div class="strip-label">Annual Overspend</div>
      <div class="strip-value {% if total_savings > 0 %}red{% else %}green{% endif %}">
        {% if total_savings > 0 %}${{ "{:,.0f}".format(total_savings) }}{% else %}None{% endif %}
      </div>
      <div class="strip-sub">vs. network median</div>
    </div>
    <div class="strip-item {% if above_count > 0 %}yellow{% else %}green{% endif %}">
      <div class="strip-label">Contracts Above Market</div>
      <div class="strip-value {% if above_count > 0 %}yellow{% else %}green{% endif %}">
        {{ above_count }} of {{ benchmarks.vendor_benchmarks|selectattr('per_unit')|list|length }}
      </div>
      <div class="strip-sub">require attention</div>
    </div>
    <div class="strip-item {% if urgent_deadlines %}yellow{% else %}green{% endif %}">
      <div class="strip-label">Urgent Deadlines</div>
      <div class="strip-value {% if urgent_deadlines %}yellow{% else %}green{% endif %}">{{ urgent_deadlines|length }}</div>
      <div class="strip-sub">within 12 months</div>
    </div>
    <div class="strip-item blue">
      <div class="strip-label">Est. Compliance Cost</div>
      <div class="strip-value blue">
        {% if comp_cost_low > 0 %}${{ "{:,.0f}".format(comp_cost_low/1000)|int }}K–${{ "{:,.0f}".format(comp_cost_high/1000)|int }}K{% else %}None due{% endif %}
      </div>
      <div class="strip-sub">plan &amp; budget now</div>
    </div>
  </div>

  <div class="grid">

    {# ── VENDOR TABLE ── #}
    <div class="card">
      <div class="ch">
        <div><div class="ct">Vendor Intelligence</div><div class="csub">Benchmarked against 187 comparable NYC buildings</div></div>
        <a href="#" class="ca">View All →</a>
      </div>
      <table class="vt">
        <thead>
          <tr>
            <th>Vendor</th>
            <th class="r">Annual</th>
            <th class="r">Per Unit</th>
            <th>Market Position</th>
          </tr>
        </thead>
        <tbody>
          {% for bm in benchmarks.vendor_benchmarks %}
          {% if bm.per_unit is not none and bm.per_unit > 0 %}
          {% set pct = bm.percentile %}
          {% set status = bm.status.color %}
          <tr class="click" onclick="openPanel('vendor', '{{ loop.index0 }}')">
            <td>
              <div class="vname">{{ bm.vendor_name }}</div>
              <div class="vcat">{{ bm.category_label[:30] }}{% if bm.last_bid_year %} · Last bid {{ bm.last_bid_year }}{% endif %}</div>
            </td>
            <td class="mono r">${{ "{:,.0f}".format(bm.annual_spend) }}</td>
            <td class="mono r">${{ "{:,.0f}".format(bm.per_unit) }}</td>
            <td>
              <div class="pos-wrap">
                <div class="pos-track">
                  <div class="pos-fill" style="width:{{ pct }}%;background:var(--{{ status }})"></div>
                </div>
                <span class="pos-pct" style="color:var(--{{ status }})">{{ pct }}th</span>
              </div>
              <div style="margin-top:4px">
                {% if status == 'red' %}<span class="pill pill-red">↑ Above Market</span>
                {% elif status == 'yellow' %}<span class="pill pill-yellow">↑ Slightly Above</span>
                {% else %}<span class="pill pill-green">✓ {% if pct < 40 %}Below{% else %}At{% endif %} Market</span>{% endif %}
              </div>
            </td>
          </tr>
          {% endif %}
          {% endfor %}
        </tbody>
      </table>
    </div>

    {# ── SAVINGS ── #}
    <div class="card">
      <div class="savings-hdr">
        <div class="savings-lbl">Total Identified Savings</div>
        <div class="savings-val">${{ "{:,.0f}".format(benchmarks.total_savings_opportunity) }}/yr</div>
        <div class="savings-sub">across {{ benchmarks.above_market_count }} vendor contracts</div>
        <div class="roi-row">
          <span class="roi-lbl">Net benefit after success fee</span>
          <span class="roi-val">${{ "{:,.0f}".format(benchmarks.net_savings_after_fee) }}/yr</span>
        </div>
      </div>
      {% for opp in benchmarks.top_opportunities %}
      <div class="opp" onclick="openPanel('vendor', '{{ loop.index0 }}')">
        <div class="opp-rank">Priority {{ "%02d"|format(loop.index) }} · {{ opp.category_label[:25] }}</div>
        <div class="opp-name">
          {% if opp.years_since_bid %}No competitive bid in {{ opp.years_since_bid }} years
          {% else %}{{ opp.percentile }}th percentile — above network median{% endif %}
        </div>
        <div class="opp-desc">
          You pay ${{ opp.per_unit }}/unit vs. network median ${{ opp.network_median }}/unit.
          {% if opp.years_since_bid and opp.years_since_bid > 3 %}Market has shifted significantly since last bid.{% endif %}
        </div>
        <div class="opp-row">
          <span class="opp-amt" style="color:var(--{{ opp.status.color }})">${{ "{:,.0f}".format(opp.savings_opportunity_annual) }}/yr</span>
          <span class="opp-cta">Initiate Rebid via BidBoard →</span>
        </div>
      </div>
      {% else %}
      <div style="padding:24px;text-align:center;color:var(--muted);font-size:13px">
        ✓ All contracts at or below market. No action needed.
      </div>
      {% endfor %}

      {# Upload zone #}
      <div class="upload-zone" onclick="document.getElementById('csvInput').click()">
        <div class="upload-label">Upload Invoice Data</div>
        <div class="upload-sub">CSV or Excel from Yardi / AvidXchange / manual export</div>
        <input type="file" id="csvInput" accept=".csv,.xlsx,.xls" style="display:none" onchange="uploadInvoices(this)">
      </div>
      <div class="upload-result" id="uploadResult"></div>
      <div style="padding:0 20px 14px;text-align:center">
        <a href="/api/sample-csv" style="font-size:11px;color:var(--muted)">↓ Download sample CSV format</a>
      </div>
    </div>

    {# ── COMPLIANCE ── #}
    <div class="card full">
      <div class="ch">
        <div><div class="ct">Compliance Calendar &amp; Cost Intelligence</div>
        <div class="csub">Deadlines with projected costs from comparable building data</div></div>
        <a href="#" class="ca">Full Calendar →</a>
      </div>
      {% for d in building.compliance_deadlines %}
      <div class="comp-item" onclick="openPanel('compliance', '{{ loop.index0 }}')">
        <div>
          <div class="comp-urg" style="color:var(--{% if d.urgency == 'HIGH' %}red{% else %}yellow{% endif %})">
            <div class="comp-dot" style="background:var(--{% if d.urgency == 'HIGH' %}red{% else %}yellow{% endif %})"></div>
            Due in {{ d.months_away }} months · {% if d.urgency == 'HIGH' %}Act now{% else %}Budget now{% endif %}
          </div>
          <div class="comp-law">{{ d.law }}</div>
          <div class="comp-desc">Network benchmark based on {{ d.network_comps }} comparable NYC buildings.</div>
          <div class="comp-consequence">⚠ {{ d.consequence }}</div>
          <div class="comp-actions">
            <button class="btn-bid" onclick="event.stopPropagation()">Start BidBoard →</button>
            <button class="btn-out" onclick="event.stopPropagation()">View Requirements</button>
          </div>
        </div>
        <div class="comp-cost-box">
          <div class="comp-cost-lbl">Network Cost Range</div>
          <div class="comp-cost-range">${{ "{:,.0f}".format(d.cost_low) }}–${{ "{:,.0f}".format(d.cost_high) }}</div>
          <div class="comp-cost-src">Based on {{ d.network_comps }} comparable filings</div>
          <div class="comp-due">Due {{ d.due_date }}</div>
        </div>
      </div>
      {% endfor %}
    </div>

    {# ── BUILDING RECORD ── #}
    <div class="card full">
      <div class="ch"><div><div class="ct">Building Record</div><div class="csub">Public data from NYC agencies · refreshed quarterly</div></div></div>
      <div class="two-mini">
        <div class="mini">
          <div class="mini-title">Tax &amp; Assessment · DOF</div>
          <div class="tax-val">${{ "{:,.0f}".format(building.tax_assessment.assessed_value) }}</div>
          <div class="tax-sub">Assessed Value · {{ building.tax_assessment.fiscal_year }}</div>
          {% if building.tax_assessment.certiorari_recommended %}
          <div class="tax-alert">⚠ Assessment up {{ building.tax_assessment.trend_pct_2yr }}% in 2 years. Tax certiorari review recommended — comparable buildings achieve reductions averaging $28,000/yr.</div>
          {% endif %}
        </div>
        <div class="mini">
          <div class="mini-title">Violations Summary · HPD / DOB</div>
          <div class="viol-nums">
            <div class="vn">
              <div class="vn-val {% if building.violations.hpd_open > 0 %}red{% else %}green{% endif %}">{{ building.violations.hpd_open }}</div>
              <div class="vn-lbl">Open Violations</div>
            </div>
            <div class="vn">
              <div class="vn-val green">{{ building.violations.hpd_closed_12mo }}</div>
              <div class="vn-lbl">Closed Last 12 Mo</div>
            </div>
            <div class="vn">
              <div class="vn-val">{{ building.violations.avg_days_to_close }}</div>
              <div class="vn-lbl">Avg Days to Close</div>
            </div>
          </div>
          {% if building.violations.class_c_open %}
          <div class="viol-flag">⚠ Open HPD Class C violation — Immediately Hazardous. Requires urgent attention.</div>
          {% endif %}
        </div>
      </div>
    </div>

  </div>
</main>

{# ── DETAIL OVERLAY ── #}
<div class="overlay" id="overlay" onclick="if(event.target===this)closePanel()">
  <div class="panel" id="panel">
    <button class="close-btn" onclick="closePanel()">✕</button>
    <div id="panelContent"></div>
  </div>
</div>

<script>
// Build JS data objects from Jinja
const vendorBenchmarks = {{ benchmarks.vendor_benchmarks | tojson }};
const complianceItems  = {{ building.compliance_deadlines | tojson }};
const buildingUnits    = {{ building.units }};

function openPanel(type, idx) {
  const content = document.getElementById('panelContent');
  if (type === 'vendor') {
    const bm = vendorBenchmarks[idx];
    if (!bm || !bm.per_unit) return;
    const statusColor = bm.status.color;
    const savings = bm.savings_opportunity_annual || 0;
    content.innerHTML = `
      <div class="panel-title">${bm.vendor_name || 'Unknown Vendor'}</div>
      <div class="panel-sub">${bm.category_label}</div>
      <div class="stat-grid">
        <div class="stat-box"><div class="stat-lbl">Annual Spend</div><div class="stat-val">$${(bm.annual_spend||0).toLocaleString()}</div></div>
        <div class="stat-box"><div class="stat-lbl">Per Unit/Year</div><div class="stat-val ${statusColor}">$${Math.round(bm.per_unit||0)}</div></div>
        <div class="stat-box"><div class="stat-lbl">Network Median</div><div class="stat-val">$${bm.network_median}/unit</div></div>
        <div class="stat-box"><div class="stat-lbl">Savings Opportunity</div><div class="stat-val ${statusColor}">$${(savings).toLocaleString()}/yr</div></div>
      </div>
      <div class="panel-section">Your Network Position</div>
      <div class="nbar-wrap">
        <div class="nbar-labels"><span>$${bm.network_p25}/unit</span><span>Median: $${bm.network_p50||bm.network_median}</span><span>$${bm.network_p90}/unit</span></div>
        <div class="nbar-track">
          <div class="nbar-fill" style="width:100%"></div>
          <div class="nbar-pin" style="left:${Math.min(95,bm.percentile||50)}%;border-color:var(--${statusColor})"></div>
        </div>
        <div class="nbar-caption">You are at the <strong>${bm.percentile}th percentile</strong> — paying more than ${bm.percentile}% of comparable buildings</div>
      </div>
      <div class="panel-section">Key Factors Affecting Price</div>
      <div style="font-size:12px;color:var(--dim);line-height:1.8;background:var(--surface2);padding:12px;border-radius:5px;border:1px solid var(--border)">
        ${(bm.factors||[]).map(f => '• ' + f).join('<br>')}
      </div>
      ${savings > 0 ? `
      <div class="action-box">
        <div class="action-title">Take Action</div>
        <div class="action-desc">Initiate a competitive bid through BidBoard. Your managing agent will be notified and compensated for executing the process.</div>
        <button class="btn-full">Start BidBoard Rebid Process →</button>
        <button class="btn-full-out">Send Analysis to Managing Agent</button>
      </div>` : `
      <div style="background:var(--green-light);border:1px solid var(--green-border);border-radius:6px;padding:14px;margin-top:16px;font-size:13px;color:var(--green)">
        ✓ This contract is at or below market. No action required at this time.
      </div>`}`;
  } else {
    const d = complianceItems[idx];
    if (!d) return;
    const urgColor = d.urgency === 'HIGH' ? 'red' : 'yellow';
    const urgLabel = d.urgency === 'HIGH' ? 'Act Now' : (d.urgency === 'MEDIUM' ? 'Budget Now' : 'Plan Ahead');

    // Law-specific requirement details
    const lawDetails = {
      'Local Law 11': {
        icon: '🏗',
        what: 'A licensed facade engineer must physically inspect every inch of your building\'s exterior walls, balconies, and appurtenances. The engineer files a FISP report with the DOB classifying the facade as <strong>Safe</strong>, <strong>SWARMP</strong> (Safe With Repair & Maintenance Program), or <strong>Unsafe</strong>.',
        who: 'A licensed NYC Professional Engineer (PE) or Registered Architect (RA) with FISP experience. They must be hired directly by the building, not through the contractor.',
        timeline: [
          'Hire engineer 12+ months before deadline',
          'Engineer conducts rope/scaffold/drone inspection (2–8 weeks)',
          'Report preparation and DOB filing (4–6 weeks)',
          'If SWARMP/Unsafe: repairs required before or concurrent with filing',
          'Sidewalk shed may be required if unsafe conditions found'
        ],
        filing: 'Engineer files FISP report electronically through DOB NOW: Safety. Building receives a FISP cycle number.',
        tip: 'Get 3 quotes from FISP engineers — prices vary 40–60% for the same building. Start early; engineers book up in the 6 months before cycle deadlines.'
      },
      'Local Law 97': {
        icon: '🌿',
        what: 'NYC\'s landmark climate law caps annual carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay <strong>$268 per metric ton of CO₂</strong> over the limit every year. An annual benchmarking report must be filed with DOB by May 1st covering the prior calendar year.',
        who: 'A licensed LL97 consultant or energy engineer to assess your current emissions against your cap, identify retrofit options, and prepare the required DOB filing.',
        timeline: [
          'Commission LL97 benchmarking study to quantify penalty exposure',
          'Evaluate retrofit options: heat pumps, insulation, LED, RECs',
          'Implement highest-ROI retrofits before compliance year ends',
          'File annual report with DOB by May 1st each year',
          'Penalties assessed annually — no cure period once year ends'
        ],
        filing: 'Annual Building Energy and Emissions Report filed through DOB NOW: Energy. Requires Energy Star Portfolio Manager benchmarking data.',
        tip: 'Renewable Energy Credits (RECs) can offset up to 30% of your penalty exposure at lower cost than physical retrofits. Check current REC market pricing before committing to capital improvements.'
      },
      'Elevator': {
        icon: '🛗',
        what: 'All elevator cabs must be inspected and tested annually by a licensed DOB elevator inspector. If an elevator fails inspection or the inspection lapses, the DOB can <strong>order the cab shut down immediately</strong> — requiring residents to use stairs until the cab passes re-inspection.',
        who: 'Your elevator maintenance contractor typically coordinates the annual inspection with a DOB-licensed inspector. Confirm they are handling this — do not assume.',
        timeline: [
          'Confirm inspection schedule with your elevator contractor 60+ days out',
          'Ensure all maintenance is current before inspection date',
          'Inspector conducts safety tests on each cab (2–4 hours per cab)',
          'DOB issues Certificate of Operation if passed',
          'Failed cabs must be repaired and re-inspected before reopening'
        ],
        filing: 'Inspector files elevator inspection report through DOB. Certificate of Operation posted inside cab.',
        tip: 'Ask your elevator contractor for written confirmation of the scheduled inspection date and inspector name each year. Keep copies of certificates of operation on file.'
      },
      'Local Law 152': {
        icon: '🔧',
        what: 'All exposed gas piping must be inspected by a licensed master plumber every 4 years. The plumber files a <strong>GPS1 form</strong> with the DOB. If defects are found, they must be corrected and re-inspected before the filing deadline.',
        who: 'A NYC-licensed master plumber who is familiar with LL152 GPS inspections. They must inspect all exposed gas lines in common areas, basements, and mechanical rooms.',
        timeline: [
          'Hire licensed master plumber 3+ months before deadline',
          'Plumber inspects all exposed gas piping (1–2 days for most buildings)',
          'Any deficiencies must be repaired before filing',
          'Plumber files GPS1 report with DOB upon completion',
          'Defects requiring emergency repair must be addressed immediately'
        ],
        filing: 'Licensed master plumber files GPS1 form through DOB NOW. Building retains copy for records.',
        tip: 'Inspectors book up quickly near the Dec 31 deadline. Schedule in September or October. If defects are found, you\'ll need time for repairs before the filing window closes.'
      },
      'Local Law 87': {
        icon: '⚡',
        what: 'Buildings over 50,000 sq ft must conduct a professional <strong>energy audit</strong> and <strong>retro-commissioning study</strong> every 10 years. The audit covers all building systems (HVAC, lighting, envelope, hot water) and identifies efficiency improvements. Retro-commissioning ensures existing systems are working as designed.',
        who: 'A qualified energy auditor (typically a licensed engineer) and a retro-commissioning agent. Often done by the same firm. Check DOB BIS to confirm your last filing date.',
        timeline: [
          'Verify last LL87 filing date in DOB BIS records',
          'Issue RFP to 3 qualified energy audit firms (6+ months before deadline)',
          'Audit and retro-commissioning study takes 3–6 months',
          'Final report preparation and DOB filing',
          'Consider implementing high-ROI recommendations to reduce LL97 exposure'
        ],
        filing: 'Filed through DOB NOW: Energy. Requires submission of energy audit report and retro-commissioning report.',
        tip: 'An LL87 audit and an LL97 benchmarking study can often be combined with one firm, reducing total cost. The audit findings also inform your LL97 retrofit strategy.'
      },
      'Local Law 26': {
        icon: '🚒',
        what: 'High-rise buildings (75ft+) must install automatic sprinkler systems throughout the building. Compliance involves a phased installation schedule with annual progress reports filed with the DOB.',
        who: 'A licensed fire suppression contractor and a licensed professional engineer for design and filing.',
        timeline: [
          'Engage licensed fire suppression engineer for design',
          'DOB permit application and approval (3–6 months)',
          'Installation in phases per approved schedule',
          'Annual progress reports filed with DOB',
          'Final inspection and sign-off'
        ],
        filing: 'Annual progress reports through DOB. Final certificate of occupancy amendment upon completion.',
        tip: 'Contact your managing agent and attorney to review your current compliance status and phased schedule before taking any action.'
      }
    };

    // Match law to details
    let details = null;
    const lawStr = d.law.toLowerCase();
    if (lawStr.includes('11') || lawStr.includes('fisp') || lawStr.includes('facade')) details = lawDetails['Local Law 11'];
    else if (lawStr.includes('97') || lawStr.includes('carbon') || lawStr.includes('emission')) details = lawDetails['Local Law 97'];
    else if (lawStr.includes('elevator') || lawStr.includes('lift')) details = lawDetails['Elevator'];
    else if (lawStr.includes('152') || lawStr.includes('gas')) details = lawDetails['Local Law 152'];
    else if (lawStr.includes('87') || lawStr.includes('energy audit')) details = lawDetails['Local Law 87'];
    else if (lawStr.includes('26') || lawStr.includes('sprinkler')) details = lawDetails['Local Law 26'];

    const timelineHTML = details ? details.timeline.map((t,i) => `
      <div style="display:flex;gap:10px;align-items:flex-start;margin-bottom:8px">
        <div style="width:20px;height:20px;border-radius:50%;background:var(--ink);color:white;font-size:10px;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:1px">${i+1}</div>
        <div style="font-size:12.5px;color:var(--dim);line-height:1.5">${t}</div>
      </div>`).join('') : '';

    content.innerHTML = `
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:4px">
        <span style="font-size:28px">${details ? details.icon : '📋'}</span>
        <div>
          <div class="panel-title" style="margin-bottom:0">${d.law}</div>
          <div style="font-size:11px;font-weight:700;letter-spacing:1px;text-transform:uppercase;color:var(--${urgColor});margin-top:2px">${urgLabel} · Due ${d.due_date}</div>
        </div>
      </div>

      <div class="stat-grid" style="margin-top:16px">
        <div class="stat-box"><div class="stat-lbl">Due Date</div><div class="stat-val ${urgColor}">${d.due_date}</div></div>
        <div class="stat-box"><div class="stat-lbl">Time Remaining</div><div class="stat-val ${urgColor}">${d.months_away > 0 ? d.months_away + ' months' : 'Overdue'}</div></div>
        <div class="stat-box"><div class="stat-lbl">Estimated Cost (Low)</div><div class="stat-val gold">$${d.cost_low.toLocaleString()}</div></div>
        <div class="stat-box"><div class="stat-lbl">Estimated Cost (High)</div><div class="stat-val gold">$${d.cost_high.toLocaleString()}</div></div>
      </div>

      ${details ? `
      <div class="panel-section">What This Requires</div>
      <div style="font-size:12.5px;color:var(--dim);line-height:1.7;background:var(--surface2);padding:13px 14px;border-radius:6px;border:1px solid var(--border)">${details.what}</div>

      <div class="panel-section">Who Does This Work</div>
      <div style="font-size:12.5px;color:var(--dim);line-height:1.7;background:var(--surface2);padding:13px 14px;border-radius:6px;border:1px solid var(--border)">${details.who}</div>

      <div class="panel-section">Step-by-Step Timeline</div>
      <div style="background:var(--surface2);padding:13px 14px;border-radius:6px;border:1px solid var(--border)">${timelineHTML}</div>

      <div class="panel-section">DOB Filing</div>
      <div style="font-size:12.5px;color:var(--dim);line-height:1.7;background:var(--surface2);padding:13px 14px;border-radius:6px;border:1px solid var(--border)">📄 ${details.filing}</div>

      <div class="panel-section">Board Tip</div>
      <div style="font-size:12.5px;color:var(--ink);line-height:1.7;background:#fffbf0;padding:13px 14px;border-radius:6px;border:1px solid var(--yellow-border)">💡 ${details.tip}</div>
      ` : ''}

      <div class="panel-section">Consequence of Non-Compliance</div>
      <div style="background:var(--red-light);border:1px solid var(--red-border);border-radius:5px;padding:12px;font-size:12.5px;color:var(--red);font-weight:500">⚠ ${d.consequence}</div>

      <div class="panel-section">Cost Benchmark — ${d.network_comps} Comparable Buildings</div>
      <div class="nbar-wrap">
        <div class="nbar-labels"><span>$${d.cost_low.toLocaleString()}</span><span>Typical Range</span><span>$${d.cost_high.toLocaleString()}</span></div>
        <div class="nbar-track"><div class="nbar-fill" style="width:100%"></div></div>
        <div class="nbar-caption">Based on ${d.network_comps} comparable NYC buildings that completed this work in the past 24 months</div>
      </div>

      ${d.context ? `
      <div class="panel-section">Additional Context</div>
      <div style="font-size:12px;color:var(--dim);line-height:1.7;background:var(--surface2);padding:13px 14px;border-radius:6px;border:1px solid var(--border)">${d.context}</div>
      ` : ''}

      <div class="action-box">
        <div class="action-title">Get Competitive Bids via BidBoard</div>
        <div class="action-desc">A pre-filled scope of work will be generated based on your building profile. Qualified, pre-vetted vendors from the network will be invited to submit competitive bids. Your managing agent handles coordination.</div>
        <button class="btn-full">Start BidBoard — ${d.law.split(/[-—]/)[0].trim()} →</button>
        <button class="btn-full-out">Notify Managing Agent</button>
      </div>`;
  }
  document.getElementById('overlay').classList.add('open');
}

function closePanel() {
  document.getElementById('overlay').classList.remove('open');
}

async function uploadInvoices(input) {
  const file = input.files[0];
  if (!file) return;
  const formData = new FormData();
  formData.append('file', file);
  const resultEl = document.getElementById('uploadResult');
  resultEl.style.display = 'block';
  resultEl.textContent = '⏳ Processing invoices...';
  try {
    const resp = await fetch('/api/upload-invoices', {method:'POST', body:formData});
    const data = await resp.json();
    if (data.success) {
      resultEl.textContent = `✓ Processed ${data.records} invoice records · ${data.classification_rate}% classified · Dashboard updated`;
    } else {
      resultEl.style.background = 'var(--red-light)';
      resultEl.style.color = 'var(--red)';
      resultEl.textContent = `Error: ${data.error}`;
    }
  } catch(e) {
    resultEl.textContent = 'Upload failed — check console.';
  }
}
</script>
</body>
</html>"""


# ═══════════════════════════════════════════════════════════════════════════════
#  VENDOR ROUTES
# ═══════════════════════════════════════════════════════════════════════════════

def vendor_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "user_email" not in session:
            return redirect(url_for("login"))
        if session.get("user_role") != "vendor":
            return redirect(url_for("dashboard"))
        return f(*args, **kwargs)
    return decorated

@app.route("/vendor")
@vendor_required
def vendor_dashboard():
    vid = session.get("vendor_id")
    profile = VENDOR_PROFILES.get(vid, {})

    # Compute opportunity data
    current_bbls = set(profile.get("current_buildings", []))
    vendor_categories = set(profile.get("categories", []))

    # Buildings in the platform where vendor is NOT currently working
    # but vendor's categories match needs
    opportunities = []
    current_work = []

    for bbl, bldg in BUILDINGS_DB.items():
        vendor_data = bldg.get("vendor_data", [])
        bldg_categories = {v["category"] for v in vendor_data}
        matching_categories = vendor_categories & bldg_categories

        if bbl in current_bbls:
            # Building already served — show what contracts are held
            active_cats = [v for v in vendor_data if v["category"] in vendor_categories]
            current_work.append({
                "bbl": bbl,
                "name": bldg.get("name", bldg.get("address", "Unknown")),
                "units": bldg.get("units", 0),
                "neighborhood": bldg.get("neighborhood", ""),
                "management_company": bldg.get("management_company") or bldg.get("managing_agent", "Unknown"),
                "active_contracts": active_cats,
                "annual_value": sum(v.get("annual", 0) for v in active_cats),
            })
        elif matching_categories:
            # Opportunity: vendor serves these categories but isn't working here
            # Find current vendor for comparison
            current_vendors = [v for v in vendor_data if v["category"] in vendor_categories]
            opportunities.append({
                "bbl": bbl,
                "name": bldg.get("name", bldg.get("address", "Unknown")),
                "units": bldg.get("units", 0),
                "neighborhood": bldg.get("neighborhood", ""),
                "management_company": bldg.get("management_company") or bldg.get("managing_agent", "Unknown"),
                "matching_categories": list(matching_categories),
                "current_vendors": current_vendors,
                "potential_annual": sum(v.get("annual", 0) for v in current_vendors),
            })

    # Management company breakdown
    mgmt_breakdown = {}
    for bbl, bldg in BUILDINGS_DB.items():
        mgmt = bldg.get("management_company") or bldg.get("managing_agent") or "Unknown"
        if mgmt not in mgmt_breakdown:
            mgmt_breakdown[mgmt] = {"total": 0, "current": 0, "opportunity": 0}
        mgmt_breakdown[mgmt]["total"] += 1
        if bbl in current_bbls:
            mgmt_breakdown[mgmt]["current"] += 1
        elif any(v["category"] in vendor_categories for v in bldg.get("vendor_data", [])):
            mgmt_breakdown[mgmt]["opportunity"] += 1

    # Summary stats
    total_annual = sum(w["annual_value"] for w in current_work)
    total_units_served = sum(w["units"] for w in current_work)

    return render_template_string(VENDOR_DASHBOARD_HTML,
        profile=profile,
        current_work=current_work,
        opportunities=opportunities[:20],  # cap display
        mgmt_breakdown=mgmt_breakdown,
        total_annual=total_annual,
        total_units_served=total_units_served,
        user_name=session.get("user_name"),
        category_labels=CATEGORY_LABELS,
        all_categories=ALL_CATEGORIES,
    )

@app.route("/vendor/save-profile", methods=["POST"])
@vendor_required
def vendor_save_profile():
    vid = session.get("vendor_id")
    if vid not in VENDOR_PROFILES:
        VENDOR_PROFILES[vid] = {}
    p = VENDOR_PROFILES[vid]
    # Basic info
    p["contact_name"] = request.form.get("contact_name", "")
    p["phone"] = request.form.get("phone", "")
    p["bio"] = request.form.get("bio", "")
    p["years_in_business"] = int(request.form.get("years_in_business", 0) or 0)
    p["employees"] = int(request.form.get("employees", 0) or 0)
    p["service_areas"] = [x.strip() for x in request.form.get("service_areas", "").split(",") if x.strip()]
    p["categories"] = request.form.getlist("categories")
    p["certifications"] = [x.strip() for x in request.form.get("certifications", "").split("\n") if x.strip()]
    return jsonify({"ok": True, "message": "Profile saved."})

@app.route("/vendor/save-insurance", methods=["POST"])
@vendor_required
def vendor_save_insurance():
    vid = session.get("vendor_id")
    if vid not in VENDOR_PROFILES:
        VENDOR_PROFILES[vid] = {}
    p = VENDOR_PROFILES[vid]
    p["insurance"] = {
        "gl_carrier": request.form.get("gl_carrier", ""),
        "gl_policy": request.form.get("gl_policy", ""),
        "gl_limit": request.form.get("gl_limit", ""),
        "gl_expiry": request.form.get("gl_expiry", ""),
        "workers_comp_carrier": request.form.get("wc_carrier", ""),
        "workers_comp_expiry": request.form.get("wc_expiry", ""),
        "additional_insured": request.form.get("additional_insured") == "on",
        "certificate_on_file": request.form.get("certificate_on_file") == "on",
    }
    return jsonify({"ok": True, "message": "Insurance info saved."})

@app.route("/vendor/save-pricing", methods=["POST"])
@vendor_required
def vendor_save_pricing():
    vid = session.get("vendor_id")
    if vid not in VENDOR_PROFILES:
        VENDOR_PROFILES[vid] = {}
    data = request.get_json()
    VENDOR_PROFILES[vid]["pricing"] = data.get("pricing", [])
    return jsonify({"ok": True, "message": "Pricing saved."})


# ── VENDOR DASHBOARD HTML ─────────────────────────────────────────────────────
VENDOR_DASHBOARD_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>BoardIQ — Vendor Portal</title>
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  :root {
    --navy: #0A2342; --navy-mid: #1A3A5C; --navy-light: #1E5F8C;
    --green: #00A550; --green-mid: #29B573; --green-bg: #f0faf4;
    --gold: #F59E0B; --gold-bg: #fffbeb;
    --red: #DC2626; --red-bg: #fef2f2;
    --white: #fff; --off: #F4F6F8; --light: #E8ECF0; --mid: #94A3B8; --dark: #1E293B;
    --radius: 10px; --shadow: 0 2px 12px rgba(10,35,66,.10);
  }
  body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    background: var(--off); color: var(--dark); min-height: 100vh; }

  /* ── Nav ── */
  .nav { background: var(--navy); display: flex; align-items: center;
    padding: 0 24px; height: 56px; gap: 8px; position: sticky; top: 0; z-index: 100; }
  .nav-logo { color: var(--green); font-weight: 800; font-size: 18px; letter-spacing: 2px; margin-right: 12px; }
  .nav-badge { background: var(--gold); color: var(--navy); font-size: 10px; font-weight: 700;
    padding: 2px 8px; border-radius: 20px; letter-spacing: 1px; text-transform: uppercase; }
  .nav-right { margin-left: auto; display: flex; align-items: center; gap: 16px; }
  .nav-user { color: #94A3B8; font-size: 13px; }
  .nav-logout { color: var(--mid); font-size: 12px; text-decoration: none; }
  .nav-logout:hover { color: white; }

  /* ── Layout ── */
  .page { display: grid; grid-template-columns: 260px 1fr; min-height: calc(100vh - 56px); }

  /* ── Sidebar ── */
  .sidebar { background: var(--navy-mid); padding: 24px 0; }
  .sidebar-section { padding: 0 16px 20px; }
  .sidebar-label { font-size: 10px; font-weight: 700; color: var(--mid); letter-spacing: 1.5px;
    text-transform: uppercase; padding: 0 8px 8px; }
  .sidebar-item { display: flex; align-items: center; gap: 10px; padding: 10px 12px;
    border-radius: 8px; cursor: pointer; color: #94A3B8; font-size: 13px; font-weight: 500;
    transition: all .15s; text-decoration: none; }
  .sidebar-item:hover, .sidebar-item.active { background: rgba(255,255,255,.08); color: white; }
  .sidebar-item .icon { font-size: 16px; width: 22px; text-align: center; }
  .sidebar-divider { height: 1px; background: rgba(255,255,255,.08); margin: 8px 16px 16px; }

  /* Profile completeness widget */
  .profile-complete { background: rgba(0,165,80,.12); border: 1px solid rgba(0,165,80,.3);
    border-radius: 8px; padding: 14px; margin: 0 16px 16px; }
  .pc-label { font-size: 11px; color: var(--green-mid); font-weight: 600; margin-bottom: 8px; }
  .pc-bar-bg { height: 6px; background: rgba(255,255,255,.1); border-radius: 3px; }
  .pc-bar { height: 6px; background: var(--green); border-radius: 3px; transition: width .4s; }
  .pc-pct { font-size: 18px; font-weight: 800; color: var(--green); margin-top: 6px; }

  /* ── Main content ── */
  .main { padding: 24px; overflow-y: auto; }

  /* ── Tabs ── */
  .tabs { display: flex; gap: 4px; background: var(--white); border-radius: var(--radius);
    padding: 4px; box-shadow: var(--shadow); margin-bottom: 24px; }
  .tab { flex: 1; text-align: center; padding: 9px 6px; font-size: 13px; font-weight: 600;
    border-radius: 7px; cursor: pointer; color: var(--mid); transition: all .15s; }
  .tab.active { background: var(--navy); color: white; }
  .tab:hover:not(.active) { background: var(--off); color: var(--dark); }

  /* ── Cards ── */
  .card { background: var(--white); border-radius: var(--radius); box-shadow: var(--shadow);
    padding: 24px; margin-bottom: 20px; }
  .card-title { font-size: 15px; font-weight: 700; color: var(--navy); margin-bottom: 16px;
    display: flex; align-items: center; gap: 8px; }
  .card-title .icon { font-size: 18px; }

  /* ── Stats row ── */
  .stats-row { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 20px; }
  .stat-card { background: var(--white); border-radius: var(--radius); box-shadow: var(--shadow);
    padding: 20px; text-align: center; }
  .stat-val { font-size: 32px; font-weight: 800; color: var(--navy); }
  .stat-val.green { color: var(--green); }
  .stat-val.gold { color: var(--gold); }
  .stat-label { font-size: 12px; color: var(--mid); margin-top: 4px; }

  /* ── Opportunity cards ── */
  .opp-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 16px; }
  .opp-card { background: var(--white); border-radius: var(--radius); box-shadow: var(--shadow);
    border-left: 4px solid var(--green); padding: 18px; }
  .opp-card.current { border-left-color: var(--navy-light); }
  .opp-name { font-weight: 700; font-size: 14px; color: var(--navy); margin-bottom: 4px; }
  .opp-meta { font-size: 12px; color: var(--mid); margin-bottom: 10px; }
  .opp-badges { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 10px; }
  .badge { font-size: 11px; font-weight: 600; padding: 3px 9px; border-radius: 20px; }
  .badge-green { background: var(--green-bg); color: var(--green); }
  .badge-navy { background: #e8f0fe; color: var(--navy-light); }
  .badge-gold { background: var(--gold-bg); color: #92400e; }
  .badge-red { background: var(--red-bg); color: var(--red); }
  .opp-value { font-size: 13px; font-weight: 600; color: var(--dark); }
  .opp-value span { color: var(--mid); font-weight: 400; }
  .connect-btn { margin-top: 12px; padding: 7px 14px; background: var(--green); color: white;
    border: none; border-radius: 6px; font-size: 12px; font-weight: 600; cursor: pointer;
    transition: background .15s; }
  .connect-btn:hover { background: #009046; }
  .connect-btn.outline { background: white; color: var(--navy-light);
    border: 1.5px solid var(--navy-light); }
  .connect-btn.outline:hover { background: #e8f0fe; }

  /* ── Mgmt breakdown table ── */
  .mgmt-table { width: 100%; border-collapse: collapse; }
  .mgmt-table th { text-align: left; font-size: 11px; font-weight: 700; color: var(--mid);
    text-transform: uppercase; letter-spacing: .8px; padding: 8px 12px; border-bottom: 2px solid var(--light); }
  .mgmt-table td { padding: 12px 12px; border-bottom: 1px solid var(--light); font-size: 13px; }
  .mgmt-table tr:last-child td { border-bottom: none; }
  .progress-mini { height: 6px; background: var(--light); border-radius: 3px; margin-top: 4px; }
  .progress-fill { height: 6px; background: var(--green); border-radius: 3px; }
  .progress-fill.current { background: var(--navy-light); }

  /* ── Form styles ── */
  .form-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
  .form-grid.three { grid-template-columns: 1fr 1fr 1fr; }
  .form-full { grid-column: 1 / -1; }
  .form-group { display: flex; flex-direction: column; gap: 5px; }
  .form-group label { font-size: 12px; font-weight: 600; color: var(--mid); text-transform: uppercase; letter-spacing: .5px; }
  .form-group input, .form-group select, .form-group textarea {
    padding: 9px 12px; border: 1.5px solid var(--light); border-radius: 7px;
    font-size: 13px; font-family: inherit; transition: border-color .15s; }
  .form-group input:focus, .form-group select:focus, .form-group textarea:focus {
    outline: none; border-color: var(--navy-light); }
  .form-group textarea { resize: vertical; min-height: 80px; }
  .categories-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; }
  .cat-checkbox { display: flex; align-items: center; gap: 6px; font-size: 12px; cursor: pointer;
    padding: 6px 10px; border: 1.5px solid var(--light); border-radius: 6px; transition: all .15s; }
  .cat-checkbox:hover { border-color: var(--green); background: var(--green-bg); }
  .cat-checkbox input:checked + span { color: var(--green); font-weight: 600; }
  .save-btn { padding: 10px 24px; background: var(--navy); color: white; border: none;
    border-radius: 8px; font-size: 13px; font-weight: 600; cursor: pointer; transition: background .15s; }
  .save-btn:hover { background: var(--navy-mid); }
  .save-msg { display: inline-block; margin-left: 12px; font-size: 13px; color: var(--green); }

  /* ── Insurance panel ── */
  .ins-status { display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 20px; }
  .ins-pill { display: flex; align-items: center; gap: 6px; padding: 8px 14px;
    border-radius: 8px; font-size: 13px; font-weight: 600; }
  .ins-pill.ok { background: var(--green-bg); color: var(--green); }
  .ins-pill.warn { background: var(--gold-bg); color: #92400e; }
  .ins-pill.missing { background: var(--red-bg); color: var(--red); }

  /* ── Pricing table ── */
  .pricing-rows { display: flex; flex-direction: column; gap: 12px; }
  .pricing-row { display: grid; grid-template-columns: 2fr 1.5fr 80px 80px 1fr auto;
    gap: 10px; align-items: end; }
  .pricing-row input { padding: 8px 10px; border: 1.5px solid var(--light); border-radius: 6px;
    font-size: 13px; font-family: inherit; width: 100%; }
  .pricing-row input:focus { outline: none; border-color: var(--navy-light); }
  .remove-row { padding: 8px 12px; background: var(--red-bg); color: var(--red);
    border: none; border-radius: 6px; cursor: pointer; font-size: 13px; font-weight: 700; }
  .add-row-btn { padding: 8px 18px; background: var(--off); color: var(--navy);
    border: 1.5px dashed var(--light); border-radius: 8px; font-size: 13px; font-weight: 600;
    cursor: pointer; transition: all .15s; margin-top: 8px; }
  .add-row-btn:hover { border-color: var(--green); color: var(--green); background: var(--green-bg); }

  /* Insurance expiry warning */
  .expiry-warn { background: var(--gold-bg); border: 1px solid #fde68a; border-radius: 8px;
    padding: 12px 16px; font-size: 13px; color: #92400e; margin-bottom: 16px; display: flex;
    align-items: center; gap: 8px; }

  /* Section visibility */
  .tab-section { display: none; }
  .tab-section.active { display: block; }

  @media (max-width: 900px) {
    .page { grid-template-columns: 1fr; }
    .sidebar { display: none; }
    .stats-row { grid-template-columns: 1fr 1fr; }
    .form-grid { grid-template-columns: 1fr; }
    .pricing-row { grid-template-columns: 1fr 1fr; }
  }
</style>
</head>
<body>

<!-- NAV -->
<nav class="nav">
  <div class="nav-logo">BOARDIQ</div>
  <div class="nav-badge">Vendor Portal</div>
  <div class="nav-right">
    <span class="nav-user">{{ user_name }}</span>
    <a href="/logout" class="nav-logout">Sign out →</a>
  </div>
</nav>

<div class="page">

<!-- SIDEBAR -->
<aside class="sidebar">
  <div class="sidebar-section">
    <div class="sidebar-label">Navigation</div>
    <a class="sidebar-item active" href="#" onclick="showTab('overview')">
      <span class="icon">📊</span> Overview
    </a>
    <a class="sidebar-item" href="#" onclick="showTab('opportunities')">
      <span class="icon">🎯</span> Opportunities
      <span style="margin-left:auto;background:var(--green);color:white;font-size:10px;
        font-weight:700;padding:2px 7px;border-radius:10px;">{{ opportunities|length }}</span>
    </a>
    <a class="sidebar-item" href="#" onclick="showTab('current')">
      <span class="icon">🏢</span> My Buildings
      <span style="margin-left:auto;background:var(--navy-light);color:white;font-size:10px;
        font-weight:700;padding:2px 7px;border-radius:10px;">{{ current_work|length }}</span>
    </a>
    <a class="sidebar-item" href="#" onclick="showTab('mgmt')">
      <span class="icon">🏛</span> Mgmt Companies
    </a>
  </div>
  <div class="sidebar-divider"></div>
  <div class="sidebar-section">
    <div class="sidebar-label">Profile</div>
    <a class="sidebar-item" href="#" onclick="showTab('profile')">
      <span class="icon">✏️</span> Company Profile
    </a>
    <a class="sidebar-item" href="#" onclick="showTab('insurance')">
      <span class="icon">🛡️</span> Insurance
      {% if profile.get('insurance', {}).get('certificate_on_file') %}
        <span style="margin-left:auto;color:var(--green);font-size:14px;">✓</span>
      {% else %}
        <span style="margin-left:auto;color:var(--gold);font-size:14px;">!</span>
      {% endif %}
    </a>
    <a class="sidebar-item" href="#" onclick="showTab('pricing')">
      <span class="icon">💰</span> Pricing Structure
    </a>
  </div>

  <div class="sidebar-divider"></div>
  <div class="sidebar-section">
    {% set has_bio = profile.get('bio') %}
    {% set has_insurance = profile.get('insurance', {}).get('gl_carrier') %}
    {% set has_pricing = profile.get('pricing', []) | length > 0 %}
    {% set has_certs = profile.get('certifications', []) | length > 0 %}
    {% set complete_count = [has_bio, has_insurance, has_pricing, has_certs] | select | list | length %}
    {% set pct = (complete_count / 4 * 100) | int %}
    <div class="profile-complete">
      <div class="pc-label">Profile Completeness</div>
      <div class="pc-bar-bg"><div class="pc-bar" style="width:{{ pct }}%"></div></div>
      <div class="pc-pct">{{ pct }}%</div>
    </div>
  </div>
</aside>

<!-- MAIN -->
<main class="main">

  <!-- ── OVERVIEW TAB ───────────────────────────────────────────────── -->
  <div id="tab-overview" class="tab-section active">
    <div style="margin-bottom:20px;">
      <h2 style="font-size:22px;font-weight:800;color:var(--navy);">{{ profile.company_name }}</h2>
      <p style="color:var(--mid);font-size:14px;margin-top:4px;">
        {{ profile.get('categories', []) | map('lower') | list | join(', ') | replace('_', ' ') | title }}
        {% if profile.get('service_areas') %} · {{ profile.service_areas | join(', ') }}{% endif %}
      </p>
    </div>

    <div class="stats-row">
      <div class="stat-card">
        <div class="stat-val">{{ current_work | length }}</div>
        <div class="stat-label">Buildings Currently Served</div>
      </div>
      <div class="stat-card">
        <div class="stat-val">{{ total_units_served | default(0) }}</div>
        <div class="stat-label">Total Units Under Contract</div>
      </div>
      <div class="stat-card">
        <div class="stat-val green">${{ '{:,.0f}'.format(total_annual) }}</div>
        <div class="stat-label">Est. Annual Revenue (Platform)</div>
      </div>
      <div class="stat-card">
        <div class="stat-val gold">{{ opportunities | length }}</div>
        <div class="stat-label">New Opportunities Available</div>
      </div>
    </div>

    {% if opportunities %}
    <div class="card">
      <div class="card-title"><span class="icon">🎯</span> Top Opportunities Near You</div>
      <div class="opp-grid">
        {% for opp in opportunities[:6] %}
        <div class="opp-card">
          <div class="opp-name">{{ opp.name }}</div>
          <div class="opp-meta">{{ opp.neighborhood }} · {{ opp.units }} units · {{ opp.management_company }}</div>
          <div class="opp-badges">
            {% for cat in opp.matching_categories %}
              <span class="badge badge-green">{{ category_labels.get(cat, cat) }}</span>
            {% endfor %}
          </div>
          {% if opp.potential_annual > 0 %}
          <div class="opp-value">${{ '{:,.0f}'.format(opp.potential_annual) }}/yr <span>current spend in your category</span></div>
          {% endif %}
          <button class="connect-btn" onclick="showTab('opportunities')">See Details →</button>
        </div>
        {% endfor %}
      </div>
    </div>
    {% endif %}

    {% if current_work %}
    <div class="card">
      <div class="card-title"><span class="icon">🏢</span> Buildings You Currently Serve</div>
      <div class="opp-grid">
        {% for w in current_work %}
        <div class="opp-card current">
          <div class="opp-name">{{ w.name }}</div>
          <div class="opp-meta">{{ w.neighborhood }} · {{ w.units }} units · {{ w.management_company }}</div>
          <div class="opp-badges">
            {% for c in w.active_contracts %}
              <span class="badge badge-navy">{{ category_labels.get(c.category, c.category) }}</span>
            {% endfor %}
          </div>
          {% if w.annual_value > 0 %}
          <div class="opp-value">${{ '{:,.0f}'.format(w.annual_value) }}/yr <span>contract value</span></div>
          {% endif %}
        </div>
        {% endfor %}
      </div>
    </div>
    {% endif %}
  </div>

  <!-- ── OPPORTUNITIES TAB ──────────────────────────────────────────── -->
  <div id="tab-opportunities" class="tab-section">
    <div style="margin-bottom:20px;display:flex;justify-content:space-between;align-items:center;">
      <div>
        <h2 style="font-size:20px;font-weight:800;color:var(--navy);">Opportunities</h2>
        <p style="color:var(--mid);font-size:13px;margin-top:2px;">
          {{ opportunities|length }} buildings on the platform where your services are needed but you're not yet engaged
        </p>
      </div>
    </div>

    <div class="opp-grid">
      {% for opp in opportunities %}
      <div class="opp-card">
        <div style="display:flex;justify-content:space-between;align-items:flex-start;">
          <div class="opp-name">{{ opp.name }}</div>
          <span class="badge badge-gold">Open</span>
        </div>
        <div class="opp-meta">{{ opp.neighborhood }} · {{ opp.units }} units</div>
        <div class="opp-meta" style="margin-top:0;">Managed by <strong>{{ opp.management_company }}</strong></div>
        <div class="opp-badges">
          {% for cat in opp.matching_categories %}
            <span class="badge badge-green">{{ category_labels.get(cat, cat) }}</span>
          {% endfor %}
        </div>
        {% if opp.current_vendors %}
          <div style="font-size:12px;color:var(--mid);margin-bottom:6px;">
            Current: {% for v in opp.current_vendors %}{{ v.vendor }}{% if not loop.last %}, {% endif %}{% endfor %}
          </div>
        {% endif %}
        {% if opp.potential_annual > 0 %}
        <div class="opp-value" style="margin-bottom:10px;">
          ~${{ '{:,.0f}'.format(opp.potential_annual) }}/yr <span>contract value in your category</span>
        </div>
        {% endif %}
        <div style="display:flex;gap:8px;flex-wrap:wrap;">
          <button class="connect-btn">Express Interest</button>
          <button class="connect-btn outline">Request Intro via Mgmt Co.</button>
        </div>
      </div>
      {% endfor %}
    </div>
    {% if not opportunities %}
    <div class="card" style="text-align:center;color:var(--mid);padding:48px;">
      <div style="font-size:40px;margin-bottom:12px;">✅</div>
      <div style="font-size:16px;font-weight:600;">You're serving all matching buildings!</div>
      <div style="font-size:13px;margin-top:6px;">Expand your service categories to see more opportunities.</div>
    </div>
    {% endif %}
  </div>

  <!-- ── CURRENT BUILDINGS TAB ─────────────────────────────────────── -->
  <div id="tab-current" class="tab-section">
    <h2 style="font-size:20px;font-weight:800;color:var(--navy);margin-bottom:20px;">My Buildings</h2>
    {% for w in current_work %}
    <div class="card" style="padding:20px;">
      <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:12px;">
        <div>
          <div style="font-size:16px;font-weight:700;color:var(--navy);">{{ w.name }}</div>
          <div style="font-size:13px;color:var(--mid);margin-top:2px;">
            {{ w.neighborhood }} · {{ w.units }} units · {{ w.management_company }}
          </div>
        </div>
        {% if w.annual_value > 0 %}
        <div style="text-align:right;">
          <div style="font-size:20px;font-weight:800;color:var(--green)">${{ '{:,.0f}'.format(w.annual_value) }}</div>
          <div style="font-size:11px;color:var(--mid);">est. annual</div>
        </div>
        {% endif %}
      </div>
      <div style="margin-top:14px;display:flex;flex-wrap:wrap;gap:8px;">
        {% for c in w.active_contracts %}
        <div style="background:var(--off);border-radius:8px;padding:10px 14px;font-size:12px;">
          <div style="font-weight:700;color:var(--navy-light);">{{ category_labels.get(c.category, c.category) }}</div>
          {% if c.annual %}<div style="color:var(--mid);margin-top:2px;">${{ '{:,.0f}'.format(c.annual) }}/yr</div>{% endif %}
        </div>
        {% endfor %}
      </div>
    </div>
    {% endfor %}
    {% if not current_work %}
    <div class="card" style="text-align:center;color:var(--mid);padding:48px;">
      <div style="font-size:40px;margin-bottom:12px;">🏢</div>
      <div style="font-size:16px;font-weight:600;">No buildings linked yet</div>
      <div style="font-size:13px;margin-top:6px;">Buildings will appear here as management companies add you to their records.</div>
    </div>
    {% endif %}
  </div>

  <!-- ── MANAGEMENT COMPANIES TAB ──────────────────────────────────── -->
  <div id="tab-mgmt" class="tab-section">
    <h2 style="font-size:20px;font-weight:800;color:var(--navy);margin-bottom:20px;">Management Companies on Platform</h2>
    <div class="card">
      <p style="font-size:13px;color:var(--mid);margin-bottom:18px;">
        Each management company controls a portfolio of buildings. Platform access fee is charged per management company.
        Increasing penetration within each portfolio amplifies your ROI per dollar of platform fee.
      </p>
      <table class="mgmt-table">
        <thead>
          <tr>
            <th>Management Company</th>
            <th>Total Buildings</th>
            <th>Your Coverage</th>
            <th>Opportunities</th>
            <th>Penetration</th>
          </tr>
        </thead>
        <tbody>
          {% for mgmt_name, data in mgmt_breakdown.items() %}
          {% if data.total > 0 %}
          <tr>
            <td style="font-weight:600;color:var(--navy);">{{ mgmt_name }}</td>
            <td>{{ data.total }} buildings</td>
            <td>
              <span style="color:var(--navy-light);font-weight:600;">{{ data.current }}</span>
              <span style="color:var(--mid);"> buildings</span>
            </td>
            <td>
              <span style="color:var(--green);font-weight:600;">{{ data.opportunity }}</span>
              <span style="color:var(--mid);"> available</span>
            </td>
            <td style="min-width:140px;">
              {% set pct = (data.current / data.total * 100) | int if data.total > 0 else 0 %}
              <div style="font-size:12px;color:var(--mid);margin-bottom:3px;">{{ pct }}% covered</div>
              <div class="progress-mini">
                <div class="progress-fill current" style="width:{{ pct }}%"></div>
              </div>
            </td>
          </tr>
          {% endif %}
          {% endfor %}
        </tbody>
      </table>
    </div>

    <div class="card" style="background:linear-gradient(135deg,var(--navy),var(--navy-mid));">
      <div style="color:var(--green);font-size:13px;font-weight:700;margin-bottom:8px;">💡 PLATFORM ACCESS FEE MODEL</div>
      <div style="color:white;font-size:15px;font-weight:600;margin-bottom:6px;">Pay once per management company portfolio — reach all their buildings</div>
      <div style="color:#94A3B8;font-size:13px;line-height:1.6;">
        Your platform subscription gives you visibility to every building managed by each company you're subscribed to.
        As more buildings onboard, your reach grows automatically at no additional cost. The more penetrated your portfolio,
        the higher your ROI per dollar of platform fee.
      </div>
    </div>
  </div>

  <!-- ── COMPANY PROFILE TAB ───────────────────────────────────────── -->
  <div id="tab-profile" class="tab-section">
    <h2 style="font-size:20px;font-weight:800;color:var(--navy);margin-bottom:20px;">Company Profile</h2>
    <div class="card">
      <div class="card-title"><span class="icon">🏢</span> Basic Information</div>
      <div class="form-grid">
        <div class="form-group">
          <label>Company Name</label>
          <input type="text" value="{{ profile.company_name }}" readonly style="background:var(--off);">
        </div>
        <div class="form-group">
          <label>Contact Name</label>
          <input type="text" id="f-contact" value="{{ profile.get('contact_name','') }}" placeholder="Primary contact">
        </div>
        <div class="form-group">
          <label>Email</label>
          <input type="email" value="{{ profile.get('email','') }}" readonly style="background:var(--off);">
        </div>
        <div class="form-group">
          <label>Phone</label>
          <input type="tel" id="f-phone" value="{{ profile.get('phone','') }}" placeholder="(212) 555-0000">
        </div>
        <div class="form-group">
          <label>Years in Business</label>
          <input type="number" id="f-years" value="{{ profile.get('years_in_business','') }}" placeholder="0">
        </div>
        <div class="form-group">
          <label>Employees</label>
          <input type="number" id="f-employees" value="{{ profile.get('employees','') }}" placeholder="0">
        </div>
        <div class="form-group form-full">
          <label>Service Areas (comma separated)</label>
          <input type="text" id="f-areas" value="{{ profile.get('service_areas', []) | join(', ') }}" placeholder="Manhattan, Brooklyn, Queens">
        </div>
        <div class="form-group form-full">
          <label>Company Bio / Description</label>
          <textarea id="f-bio" rows="4" placeholder="Describe your company, specialties, and what sets you apart...">{{ profile.get('bio','') }}</textarea>
        </div>
        <div class="form-group form-full">
          <label>Certifications & Licenses (one per line)</label>
          <textarea id="f-certs" rows="3" placeholder="NYS DOB License&#10;NYC Licensed Contractor&#10;OSHA 30">{{ profile.get('certifications', []) | join('\n') }}</textarea>
        </div>
      </div>
    </div>

    <div class="card">
      <div class="card-title"><span class="icon">🏷️</span> Service Categories</div>
      <p style="font-size:13px;color:var(--mid);margin-bottom:16px;">
        Select all categories where you can provide services. This determines which buildings show up as opportunities.
      </p>
      <div class="categories-grid">
        {% for cat_key, cat_label in category_labels.items() %}
        <label class="cat-checkbox">
          <input type="checkbox" name="categories" value="{{ cat_key }}"
            {% if cat_key in profile.get('categories', []) %}checked{% endif %}>
          <span>{{ cat_label }}</span>
        </label>
        {% endfor %}
      </div>
    </div>

    <button class="save-btn" onclick="saveProfile()">Save Profile</button>
    <span class="save-msg" id="profile-msg"></span>
  </div>

  <!-- ── INSURANCE TAB ─────────────────────────────────────────────── -->
  <div id="tab-insurance" class="tab-section">
    <h2 style="font-size:20px;font-weight:800;color:var(--navy);margin-bottom:20px;">Insurance Information</h2>

    {% set ins = profile.get('insurance', {}) %}

    <!-- Status pills -->
    <div class="ins-status">
      {% if ins.get('gl_carrier') %}
        <div class="ins-pill ok">✓ General Liability on File</div>
      {% else %}
        <div class="ins-pill missing">⚠ General Liability Missing</div>
      {% endif %}
      {% if ins.get('workers_comp_carrier') %}
        <div class="ins-pill ok">✓ Workers' Comp on File</div>
      {% else %}
        <div class="ins-pill missing">⚠ Workers' Comp Missing</div>
      {% endif %}
      {% if ins.get('additional_insured') %}
        <div class="ins-pill ok">✓ Additional Insured Available</div>
      {% else %}
        <div class="ins-pill warn">⚠ Additional Insured Not Set Up</div>
      {% endif %}
      {% if ins.get('certificate_on_file') %}
        <div class="ins-pill ok">✓ Certificate on File</div>
      {% else %}
        <div class="ins-pill warn">! Certificate Not Yet Uploaded</div>
      {% endif %}
    </div>

    {% if ins.get('gl_expiry') %}
    <div class="expiry-warn">⚠️ General Liability expires {{ ins.gl_expiry }} — verify renewal is in progress</div>
    {% endif %}

    <div class="card">
      <div class="card-title"><span class="icon">🛡️</span> General Liability</div>
      <div class="form-grid">
        <div class="form-group">
          <label>Insurance Carrier</label>
          <input type="text" id="ins-gl-carrier" value="{{ ins.get('gl_carrier','') }}" placeholder="e.g. Travelers Insurance">
        </div>
        <div class="form-group">
          <label>Policy Number</label>
          <input type="text" id="ins-gl-policy" value="{{ ins.get('gl_policy','') }}" placeholder="Policy #">
        </div>
        <div class="form-group">
          <label>Coverage Limit</label>
          <input type="text" id="ins-gl-limit" value="{{ ins.get('gl_limit','') }}" placeholder="e.g. 2,000,000">
        </div>
        <div class="form-group">
          <label>Expiration Date</label>
          <input type="date" id="ins-gl-expiry" value="{{ ins.get('gl_expiry','') }}">
        </div>
      </div>
    </div>

    <div class="card">
      <div class="card-title"><span class="icon">👷</span> Workers' Compensation</div>
      <div class="form-grid">
        <div class="form-group">
          <label>Insurance Carrier</label>
          <input type="text" id="ins-wc-carrier" value="{{ ins.get('workers_comp_carrier','') }}" placeholder="e.g. Hartford Life">
        </div>
        <div class="form-group">
          <label>Expiration Date</label>
          <input type="date" id="ins-wc-expiry" value="{{ ins.get('workers_comp_expiry','') }}">
        </div>
      </div>
    </div>

    <div class="card">
      <div class="card-title"><span class="icon">📋</span> Compliance Status</div>
      <div style="display:flex;gap:24px;flex-wrap:wrap;">
        <label style="display:flex;align-items:center;gap:8px;font-size:14px;cursor:pointer;">
          <input type="checkbox" id="ins-ai" {% if ins.get('additional_insured') %}checked{% endif %}
            style="width:16px;height:16px;accent-color:var(--green);">
          Can add buildings as Additional Insured
        </label>
        <label style="display:flex;align-items:center;gap:8px;font-size:14px;cursor:pointer;">
          <input type="checkbox" id="ins-cof" {% if ins.get('certificate_on_file') %}checked{% endif %}
            style="width:16px;height:16px;accent-color:var(--green);">
          Certificate of Insurance on file with management companies
        </label>
      </div>
    </div>

    <div class="card" style="background:var(--off);border:1.5px dashed var(--light);">
      <div class="card-title"><span class="icon">📤</span> Upload Certificate of Insurance</div>
      <p style="font-size:13px;color:var(--mid);margin-bottom:16px;">
        Upload your ACORD certificate. This will be shared with building boards and management companies when you express interest in opportunities.
      </p>
      <input type="file" accept=".pdf,.jpg,.png" style="font-size:13px;">
      <p style="font-size:11px;color:var(--mid);margin-top:8px;">Accepted: PDF, JPG, PNG · Max 5MB</p>
    </div>

    <button class="save-btn" onclick="saveInsurance()">Save Insurance Info</button>
    <span class="save-msg" id="insurance-msg"></span>
  </div>

  <!-- ── PRICING TAB ───────────────────────────────────────────────── -->
  <div id="tab-pricing" class="tab-section">
    <h2 style="font-size:20px;font-weight:800;color:var(--navy);margin-bottom:20px;">Pricing Structure</h2>
    <div class="card">
      <div class="card-title"><span class="icon">💰</span> Rate Sheet</div>
      <p style="font-size:13px;color:var(--mid);margin-bottom:18px;">
        Define your pricing ranges by service type. These will be visible to building boards and management companies
        evaluating vendors. Ranges are encouraged — exact pricing depends on scope.
      </p>
      <div style="display:grid;grid-template-columns:2fr 1.5fr 90px 90px 1fr 40px;gap:10px;
          margin-bottom:8px;padding:0 2px;">
        <div style="font-size:11px;font-weight:700;color:var(--mid);text-transform:uppercase;letter-spacing:.5px;">Service Type</div>
        <div style="font-size:11px;font-weight:700;color:var(--mid);text-transform:uppercase;letter-spacing:.5px;">Unit / Basis</div>
        <div style="font-size:11px;font-weight:700;color:var(--mid);text-transform:uppercase;letter-spacing:.5px;">From ($)</div>
        <div style="font-size:11px;font-weight:700;color:var(--mid);text-transform:uppercase;letter-spacing:.5px;">To ($)</div>
        <div style="font-size:11px;font-weight:700;color:var(--mid);text-transform:uppercase;letter-spacing:.5px;">Notes</div>
        <div></div>
      </div>
      <div id="pricing-rows" class="pricing-rows">
        {% for row in profile.get('pricing', []) %}
        <div class="pricing-row" data-row>
          <input type="text" placeholder="e.g. Monthly Maintenance Contract" value="{{ row.type }}">
          <input type="text" placeholder="per elevator/mo" value="{{ row.unit }}">
          <input type="number" placeholder="0" value="{{ row.low }}">
          <input type="number" placeholder="0" value="{{ row.high }}">
          <input type="text" placeholder="Optional notes..." value="{{ row.notes }}">
          <button class="remove-row" onclick="removeRow(this)">×</button>
        </div>
        {% endfor %}
      </div>
      <button class="add-row-btn" onclick="addPricingRow()">+ Add Service</button>
    </div>

    <div class="card" style="background:var(--off);">
      <div class="card-title"><span class="icon">ℹ️</span> Pricing Tips</div>
      <div style="font-size:13px;color:var(--mid);line-height:1.7;">
        <strong>Be competitive but honest.</strong> BoardIQ benchmarks vendor pricing across buildings —
        boards can see if you're above or below market. Transparent pricing builds trust and increases
        the likelihood boards will select you for bid requests. You can always adjust scope-specific
        pricing during negotiation. <br><br>
        <strong>Common billing structures:</strong> Monthly contract (per unit or per building),
        hourly rate, per-visit, project lump sum, annual retainer.
      </div>
    </div>

    <button class="save-btn" onclick="savePricing()">Save Pricing</button>
    <span class="save-msg" id="pricing-msg"></span>
  </div>

</main>
</div>

<script>
// ── Tab switching ──────────────────────────────────────────────────────────
function showTab(name) {
  document.querySelectorAll('.tab-section').forEach(s => s.classList.remove('active'));
  document.querySelectorAll('.sidebar-item').forEach(s => s.classList.remove('active'));
  const section = document.getElementById('tab-' + name);
  if (section) section.classList.add('active');
  event.target.closest('.sidebar-item')?.classList.add('active');
}

// ── Save profile ──────────────────────────────────────────────────────────
async function saveProfile() {
  const form = new FormData();
  form.append('contact_name', document.getElementById('f-contact').value);
  form.append('phone', document.getElementById('f-phone').value);
  form.append('years_in_business', document.getElementById('f-years').value);
  form.append('employees', document.getElementById('f-employees').value);
  form.append('service_areas', document.getElementById('f-areas').value);
  form.append('bio', document.getElementById('f-bio').value);
  form.append('certifications', document.getElementById('f-certs').value);
  document.querySelectorAll('[name=categories]:checked').forEach(cb => form.append('categories', cb.value));
  const r = await fetch('/vendor/save-profile', { method: 'POST', body: form });
  const d = await r.json();
  const msg = document.getElementById('profile-msg');
  msg.textContent = d.ok ? '✓ Saved!' : '✗ Error saving.';
  setTimeout(() => msg.textContent = '', 3000);
}

// ── Save insurance ────────────────────────────────────────────────────────
async function saveInsurance() {
  const form = new FormData();
  form.append('gl_carrier', document.getElementById('ins-gl-carrier').value);
  form.append('gl_policy', document.getElementById('ins-gl-policy').value);
  form.append('gl_limit', document.getElementById('ins-gl-limit').value);
  form.append('gl_expiry', document.getElementById('ins-gl-expiry').value);
  form.append('wc_carrier', document.getElementById('ins-wc-carrier').value);
  form.append('wc_expiry', document.getElementById('ins-wc-expiry').value);
  if (document.getElementById('ins-ai').checked) form.append('additional_insured', 'on');
  if (document.getElementById('ins-cof').checked) form.append('certificate_on_file', 'on');
  const r = await fetch('/vendor/save-insurance', { method: 'POST', body: form });
  const d = await r.json();
  const msg = document.getElementById('insurance-msg');
  msg.textContent = d.ok ? '✓ Saved!' : '✗ Error saving.';
  setTimeout(() => msg.textContent = '', 3000);
}

// ── Pricing rows ──────────────────────────────────────────────────────────
function addPricingRow() {
  const row = document.createElement('div');
  row.className = 'pricing-row';
  row.setAttribute('data-row', '');
  row.innerHTML = `
    <input type="text" placeholder="e.g. Emergency Service Call">
    <input type="text" placeholder="per call / per hour / per unit">
    <input type="number" placeholder="0">
    <input type="number" placeholder="0">
    <input type="text" placeholder="Optional notes...">
    <button class="remove-row" onclick="removeRow(this)">×</button>
  `;
  document.getElementById('pricing-rows').appendChild(row);
}

function removeRow(btn) {
  btn.closest('[data-row]').remove();
}

async function savePricing() {
  const rows = [];
  document.querySelectorAll('[data-row]').forEach(row => {
    const inputs = row.querySelectorAll('input');
    rows.push({
      type: inputs[0].value,
      unit: inputs[1].value,
      low: parseFloat(inputs[2].value) || 0,
      high: parseFloat(inputs[3].value) || 0,
      notes: inputs[4].value,
    });
  });
  const r = await fetch('/vendor/save-pricing', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ pricing: rows }),
  });
  const d = await r.json();
  const msg = document.getElementById('pricing-msg');
  msg.textContent = d.ok ? '✓ Saved!' : '✗ Error saving.';
  setTimeout(() => msg.textContent = '', 3000);
}
</script>
</body>
</html>"""


if __name__ == "__main__":
    print("\n" + "="*55)
    print("  BoardIQ — Starting Web Application")
    print("="*55)
    print("  URL:      http://localhost:5001")
    print()
    print("  Board logins:")
    print("  board@120w72.com   / demo1234")
    print("  board@740park.com  / demo1234")
    print("  admin@boardiq.com  / admin")
    print()
    print("  Vendor logins:")
    print("  vendor@schindler.com / demo1234")
    print("  vendor@cleanstar.com / demo1234")
    print("  vendor@apexext.com   / demo1234")
    print("="*55 + "\n")
    app.run(debug=True, port=5001, host="0.0.0.0")
