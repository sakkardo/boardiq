"""
BoardIQ - Web Application
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

# -- In-memory database (swap for PostgreSQL in production) ---
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
                "law": "Local Law 11 - FISP Facade Inspection",
                "due_date": "Oct 2026",
                "months_away": 9,
                "urgency": "HIGH",
                "consequence": "DOB violations + fines from $1,000/month",
                "cost_low": 14000,
                "cost_high": 22000,
                "network_comps": 23,
            },
            {
                "law": "Local Law 97 - Carbon Emissions",
                "due_date": "Dec 2026",
                "months_away": 11,
                "urgency": "HIGH",
                "consequence": "Est. $31,000/yr penalty at current emissions",
                "cost_low": 18000,
                "cost_high": 35000,
                "network_comps": 31,
            },
            {
                "law": "Local Law 87 - Energy Audit",
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
                "law": "Local Law 11 - FISP Facade Inspection",
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
                "law": "Local Law 11 - FISP Facade Inspection",
                "due_date": "Dec 2026",
                "months_away": 10,
                "urgency": "HIGH",
                "consequence": "DOB violations + fines from $1,000/month if missed",
                "cost_low": 22000,
                "cost_high": 38000,
                "network_comps": 23,
                "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years. The engineer files a report with the DOB classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately. For a 16-story building like Gramercy Plaza, this typically involves hiring a facade engineering firm, erecting sidewalk sheds or scaffolding if repairs are needed, and filing all documentation with the DOB. The board should hire a qualified facade engineer 12+ months before the deadline to allow time for inspection, report preparation, and any required repairs.",
            },
            {
                "law": "Local Law 97 - Carbon Emissions",
                "due_date": "May 2026",
                "months_away": 3,
                "urgency": "HIGH",
                "consequence": "Est. $58,000/yr penalty at current emissions rate",
                "cost_low": 35000,
                "cost_high": 65000,
                "network_comps": 31,
                "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for large buildings. Buildings over 25,000 sq ft must meet strict emissions limits or pay fines of $268 per metric ton of CO2 over the cap every single year until compliant. Gramercy Plaza at 187,000 sq ft is well above the threshold. The annual compliance report for the prior calendar year must be filed with the DOB by May 1st. Given Con Edison bills of $55,000/month, this building almost certainly has significant carbon exposure. The board should immediately commission an LL97 benchmarking study to determine the penalty exposure and what retrofits would reduce or eliminate the fine.",
            },
            {
                "law": "Local Law 87 - Energy Audit and Retro-commissioning",
                "due_date": "Verify with DOB - may be overdue",
                "months_away": 0,
                "urgency": "HIGH",
                "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                "cost_low": 14000,
                "cost_high": 24000,
                "network_comps": 41,
                "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years, based on the last digit of the building's tax block number. Block 882 ends in 2, meaning compliance was due in years ending in 2 - most recently 2022. If Gramercy Plaza has not filed an LL87 report, the building may already be in violation and accruing fines. The board should immediately check DOB BIS records to confirm filing status.",
            },
            {
                "law": "Elevator Annual Inspection - 2 cabs",
                "due_date": "Apr 2026",
                "months_away": 2,
                "urgency": "HIGH",
                "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                "cost_low": 1600,
                "cost_high": 2800,
                "network_comps": 89,
                "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. Gramercy Plaza has 2 passenger elevator cabs. The inspection covers all mechanical and safety components including brakes, cables, door operations, and emergency systems. The elevator contractor (currently PS Marcato) typically coordinates the inspection and must have the equipment in proper working order beforehand. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately, leaving a 16-story building with one or zero working elevators.",
            },
            {
                "law": "Local Law 152 - Gas Piping Inspection",
                "due_date": "Verify with DOB - 2025 may be due",
                "months_away": 0,
                "urgency": "HIGH",
                "consequence": "DOB violations and fines if inspection not filed on time",
                "cost_low": 3500,
                "cost_high": 7000,
                "network_comps": 67,
                "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. Inspections are scheduled by community district. Manhattan Community District 5 (which includes Gramercy Park) falls in the group due in years ending in 0 or 5, meaning the next inspection was due December 31, 2025. If not yet completed, the building is at risk of a DOB violation. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB.",
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
            {"vendor": "Adriatic Plumbing and Heating", "category": "PLUMBING_REPAIRS",
             "annual": 104953, "per_unit": 366, "last_bid_year": 2021, "months_left": 8},
            {"vendor": "PS Marcato Elevator Company", "category": "ELEVATOR_MAINTENANCE",
             "annual": 23369, "per_unit": 81, "last_bid_year": 2019, "months_left": 5},
            {"vendor": "Metric Consulting and Inspection", "category": "PROFESSIONAL_SERVICES",
             "annual": 45000, "per_unit": 157, "last_bid_year": 2020, "months_left": 0},
            {"vendor": "Elevated Outdoors and Ariston Flowers", "category": "LANDSCAPING",
             "annual": 47883, "per_unit": 167, "last_bid_year": 2022, "months_left": 7},
            {"vendor": "Innovacore Environmental", "category": "ENVIRONMENTAL",
             "annual": 57305, "per_unit": 200, "last_bid_year": 2023, "months_left": 14},
            {"vendor": "Century Management", "category": "MANAGEMENT_FEE",
             "annual": 198000, "per_unit": 690, "last_bid_year": 2018, "months_left": 0},
        ],
    },
}

# -- Auth ---
DEMO_USERS = {
    "board@120w72.com":      {"password": "demo1234", "buildings": ["bbl_1022150001"], "name": "Margaret Chen"},
    "board@740park.com":     {"password": "demo1234", "buildings": ["bbl_1012660001"], "name": "Robert Steinberg"},
    "board@gramercyplaza.com": {"password": "demo1234", "buildings": ["bbl_1009270001"], "name": "Gramercy Plaza Board"},
    "admin@boardiq.com":     {"password": "admin", "buildings": list(BUILDINGS_DB.keys()), "name": "BoardIQ Admin", "is_admin": True},
}

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


# -- ROUTES --

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
            session["active_building"] = user["buildings"][0]
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
    benchmarks = compute_benchmarks(building)
    return render_template_string(DASHBOARD_HTML,
        building=building,
        benchmarks=benchmarks,
        user_name=session.get("user_name"),
        all_buildings=[BUILDINGS_DB[b] for b in
                       DEMO_USERS[session["user_email"]]["buildings"]],
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
    building = get_current_building()
    if not building:
        return jsonify({"error": "No active building"}), 400
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400
    f = request.files["file"]
    content = f.read().decode("utf-8-sig")
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv',
                                     delete=False, newline='') as tmp:
        tmp.write(content)
        tmp_path = tmp.name
    try:
        processor = InvoiceProcessor()
        summary = processor.process_file(tmp_path, building["id"], building["units"])
        os.remove(tmp_path)
        return jsonify({"success": True, "summary": summary,
                        "records": len(processor.processed),
                        "classification_rate": summary["classification_rate"]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/sample-csv")
@login_required
def get_sample_csv():
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


# -- HTML TEMPLATES --

LOGIN_HTML = """<!DOCTYPE html>
<html>
<head>
<title>BoardIQ - Sign In</title>
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
    <input type="password" name="password" placeholder="..." required>
    <button type="submit">Sign In</button>
  </form>
  <div class="demo-hint">
    <strong>Demo accounts:</strong><br>
    board@120w72.com / demo1234<br>
    board@740park.com / demo1234<br>
    admin@boardiq.com / admin
  </div>
</div>
</body>
</html>"""


DASHBOARD_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>BoardIQ - {{ building.address }}</title>
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
.sidebar{position:fixed;left:0;top:0;bottom:0;width:220px;background:var(--ink);display:flex;flex-direction:column;z-index:100}
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
.main{margin-left:220px;padding:30px 34px 48px}
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
.action-box{background:linear-gradient(135deg,#fdf6ec 0%,var(--surface) 100%);border:1px solid var(--yellow-border);border-radius:6px;padding:16px;margin-top:18px}
.action-title{font-family:'Playfair Display',serif;font-size:17px;color:var(--gold);margin-bottom:5px}
.action-desc{font-size:12px;color:var(--dim);line-height:1.6;margin-bottom:12px}
.btn-full{width:100%;background:var(--ink);color:#fff;font-family:inherit;font-size:13px;font-weight:600;padding:10px;border:none;border-radius:4px;cursor:pointer;margin-bottom:7px}
.btn-full-out{width:100%;background:transparent;color:var(--dim);font-family:inherit;font-size:12px;padding:8px;border:1px solid var(--border2);border-radius:4px;cursor:pointer}
.upload-result{padding:14px 20px;background:var(--green-light);border:1px solid var(--green-border);border-radius:6px;margin:12px 20px;font-size:12.5px;color:var(--green);display:none}
</style>
</head>
<body>

<nav class="sidebar">
  <div class="logo">
    <div class="logo-mark">Board<span>IQ</span></div>
    <div class="logo-sub">Property Intelligence</div>
  </div>
  <div class="nav">
    <div class="nav-label">Intelligence</div>
    <div class="nav-item active">Dashboard</div>
    <div class="nav-item">Savings
      {% if benchmarks.above_market_count > 0 %}
      <span class="nav-badge">{{ benchmarks.above_market_count }}</span>{% endif %}
    </div>
    <div class="nav-item">BidBoard</div>
    <div class="nav-label">Compliance</div>
    <div class="nav-item">Compliance Calendar
      <span class="nav-badge">{{ building.compliance_deadlines|selectattr('urgency','eq','HIGH')|list|length }}</span>
    </div>
    <div class="nav-item">Contracts</div>
    <div class="nav-label">Building</div>
    <div class="nav-item">Tax and Assessment</div>
    <div class="nav-item">Violations</div>
    <div class="nav-item">Data Upload</div>
  </div>
  {% if all_buildings|length > 1 %}
  <div class="switch-links">
    {% for b in all_buildings %}
    <a href="/switch-building/{{ b.id }}"
       class="switch-link {% if b.id == active_bbl %}active-link{% endif %}">
      {% if b.id == active_bbl %}* {% endif %}{{ b.address[:28] }}
    </a>
    {% endfor %}
  </div>
  {% endif %}
  <div class="bldg-block">
    <div class="bldg-tag">Active Building</div>
    <div class="bldg-name">{{ building.address }}</div>
    <div class="bldg-meta">{{ building.units }} units - {{ building.neighborhood }}</div>
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
      <div class="page-sub">{{ building.address }} - {{ building.managing_agent }} - Data from 187 comparable NYC buildings</div>
    </div>
    <div class="header-badge">Refreshed {{ building.last_data_refresh }}</div>
  </div>

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
        {% if comp_cost_low > 0 %}${{ "{:,.0f}".format(comp_cost_low/1000)|int }}K-${{ "{:,.0f}".format(comp_cost_high/1000)|int }}K{% else %}None due{% endif %}
      </div>
      <div class="strip-sub">plan and budget now</div>
    </div>
  </div>

  <div class="grid">

    <div class="card">
      <div class="ch">
        <div><div class="ct">Vendor Intelligence</div><div class="csub">Benchmarked against 187 comparable NYC buildings</div></div>
        <a href="#" class="ca">View All</a>
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
              <div class="vcat">{{ bm.category_label[:30] }}{% if bm.last_bid_year %} - Last bid {{ bm.last_bid_year }}{% endif %}</div>
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
                {% if status == 'red' %}<span class="pill pill-red">Above Market</span>
                {% elif status == 'yellow' %}<span class="pill pill-yellow">Slightly Above</span>
                {% else %}<span class="pill pill-green">{% if pct < 40 %}Below{% else %}At{% endif %} Market</span>{% endif %}
              </div>
            </td>
          </tr>
          {% endif %}
          {% endfor %}
        </tbody>
      </table>
    </div>

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
        <div class="opp-rank">Priority {{ "%02d"|format(loop.index) }} - {{ opp.category_label[:25] }}</div>
        <div class="opp-name">
          {% if opp.years_since_bid %}No competitive bid in {{ opp.years_since_bid }} years
          {% else %}{{ opp.percentile }}th percentile - above network median{% endif %}
        </div>
        <div class="opp-desc">
          You pay ${{ opp.per_unit }}/unit vs. network median ${{ opp.network_median }}/unit.
          {% if opp.years_since_bid and opp.years_since_bid > 3 %}Market has shifted significantly since last bid.{% endif %}
        </div>
        <div class="opp-row">
          <span class="opp-amt" style="color:var(--{{ opp.status.color }})">${{ "{:,.0f}".format(opp.savings_opportunity_annual) }}/yr</span>
          <span class="opp-cta">Initiate Rebid via BidBoard</span>
        </div>
      </div>
      {% else %}
      <div style="padding:24px;text-align:center;color:var(--muted);font-size:13px">
        All contracts at or below market. No action needed.
      </div>
      {% endfor %}

      <div class="upload-zone" onclick="document.getElementById('csvInput').click()">
        <div class="upload-label">Upload Invoice Data</div>
        <div class="upload-sub">CSV or Excel from Yardi / AvidXchange / manual export</div>
        <input type="file" id="csvInput" accept=".csv,.xlsx,.xls" style="display:none" onchange="uploadInvoices(this)">
      </div>
      <div class="upload-result" id="uploadResult"></div>
      <div style="padding:0 20px 14px;text-align:center">
        <a href="/api/sample-csv" style="font-size:11px;color:var(--muted)">Download sample CSV format</a>
      </div>
    </div>

    <div class="card full">
      <div class="ch">
        <div><div class="ct">Compliance Calendar and Cost Intelligence</div>
        <div class="csub">Deadlines with projected costs from comparable building data</div></div>
        <a href="#" class="ca">Full Calendar</a>
      </div>
      {% for d in building.compliance_deadlines %}
      <div class="comp-item" onclick="openPanel('compliance', '{{ loop.index0 }}')">
        <div>
          <div class="comp-urg" style="color:var(--{% if d.urgency == 'HIGH' %}red{% else %}yellow{% endif %})">
            <div class="comp-dot" style="background:var(--{% if d.urgency == 'HIGH' %}red{% else %}yellow{% endif %})"></div>
            Due in {{ d.months_away }} months - {% if d.urgency == 'HIGH' %}Act now{% else %}Budget now{% endif %}
          </div>
          <div class="comp-law">{{ d.law }}</div>
          <div class="comp-desc">Network benchmark based on {{ d.network_comps }} comparable NYC buildings.</div>
          <div class="comp-consequence">{{ d.consequence }}</div>
          <div class="comp-actions">
            <button class="btn-bid" onclick="event.stopPropagation()">Start BidBoard</button>
            <button class="btn-out" onclick="event.stopPropagation()">View Requirements</button>
          </div>
        </div>
        <div class="comp-cost-box">
          <div class="comp-cost-lbl">Network Cost Range</div>
          <div class="comp-cost-range">${{ "{:,.0f}".format(d.cost_low) }}-${{ "{:,.0f}".format(d.cost_high) }}</div>
          <div class="comp-cost-src">Based on {{ d.network_comps }} comparable filings</div>
          <div class="comp-due">Due {{ d.due_date }}</div>
        </div>
      </div>
      {% endfor %}
    </div>

    <div class="card full">
      <div class="ch"><div><div class="ct">Building Record</div><div class="csub">Public data from NYC agencies - refreshed quarterly</div></div></div>
      <div class="two-mini">
        <div class="mini">
          <div class="mini-title">Tax and Assessment - DOF</div>
          <div class="tax-val">${{ "{:,.0f}".format(building.tax_assessment.assessed_value) }}</div>
          <div class="tax-sub">Assessed Value - {{ building.tax_assessment.fiscal_year }}</div>
          {% if building.tax_assessment.certiorari_recommended %}
          <div class="tax-alert">Assessment up {{ building.tax_assessment.trend_pct_2yr }}% in 2 years. Tax certiorari review recommended - comparable buildings achieve reductions averaging $28,000/yr.</div>
          {% endif %}
        </div>
        <div class="mini">
          <div class="mini-title">Violations Summary - HPD / DOB</div>
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
          <div class="viol-flag">Open HPD Class C violation - Immediately Hazardous. Requires urgent attention.</div>
          {% endif %}
        </div>
      </div>
    </div>

  </div>
</main>

<div class="overlay" id="overlay" onclick="if(event.target===this)closePanel()">
  <div class="panel" id="panel">
    <button class="close-btn" onclick="closePanel()">X</button>
    <div id="panelContent"></div>
  </div>
</div>

<script>
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
        <div class="nbar-caption">You are at the <strong>${bm.percentile}th percentile</strong> - paying more than ${bm.percentile}% of comparable buildings</div>
      </div>
      <div class="panel-section">Key Factors Affecting Price</div>
      <div style="font-size:12px;color:var(--dim);line-height:1.8;background:var(--surface2);padding:12px;border-radius:5px;border:1px solid var(--border)">
        ${(bm.factors||[]).map(f => '- ' + f).join('<br>')}
      </div>
      ${savings > 0 ? `
      <div class="action-box">
        <div class="action-title">Take Action</div>
        <div class="action-desc">Initiate a competitive bid through BidBoard. Your managing agent will be notified and compensated for executing the process.</div>
        <button class="btn-full">Start BidBoard Rebid Process</button>
        <button class="btn-full-out">Send Analysis to Managing Agent</button>
      </div>` : `
      <div style="background:var(--green-light);border:1px solid var(--green-border);border-radius:6px;padding:14px;margin-top:16px;font-size:13px;color:var(--green)">
        This contract is at or below market. No action required at this time.
      </div>`}`;
  } else {
    const d = complianceItems[idx];
    if (!d) return;
    const urgColor = d.urgency === 'HIGH' ? 'red' : 'yellow';
    content.innerHTML = `
      <div class="panel-title">${d.law}</div>
      <div class="panel-sub">Due ${d.due_date} - ${d.months_away} months away</div>
      <div class="stat-grid">
        <div class="stat-box"><div class="stat-lbl">Due Date</div><div class="stat-val">${d.due_date}</div></div>
        <div class="stat-box"><div class="stat-lbl">Time Remaining</div><div class="stat-val ${urgColor}">${d.months_away} months</div></div>
        <div class="stat-box"><div class="stat-lbl">Cost Range (Low)</div><div class="stat-val gold">$${d.cost_low.toLocaleString()}</div></div>
        <div class="stat-box"><div class="stat-lbl">Cost Range (High)</div><div class="stat-val gold">$${d.cost_high.toLocaleString()}</div></div>
      </div>
      <div class="panel-section">Consequence of Non-Compliance</div>
      <div style="background:var(--red-light);border:1px solid var(--red-border);border-radius:5px;padding:12px;font-size:12.5px;color:var(--red);font-weight:500">${d.consequence}</div>
      ${d.context ? `
      <div class="panel-section">What the Board Needs to Know</div>
      <div style="font-size:12.5px;color:var(--dim);line-height:1.8;background:var(--surface2);padding:14px;border-radius:5px;border:1px solid var(--border)">${d.context}</div>` : ''}
      <div class="panel-section">Cost Data - ${d.network_comps} Comparable Buildings</div>
      <div class="nbar-wrap">
        <div class="nbar-labels"><span>$${d.cost_low.toLocaleString()}</span><span>Typical Range</span><span>$${d.cost_high.toLocaleString()}</span></div>
        <div class="nbar-track"><div class="nbar-fill" style="width:100%"></div></div>
        <div class="nbar-caption">Based on ${d.network_comps} comparable NYC buildings that completed this work in the past 24 months</div>
      </div>
      <div class="action-box">
        <div class="action-title">Start BidBoard</div>
        <div class="action-desc">A pre-filled scope of work will be generated based on your building profile. Qualified vendors from the network will be invited to submit competitive bids.</div>
        <button class="btn-full">Start BidBoard - ${d.law.split('-')[0].trim()}</button>
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
  resultEl.textContent = 'Processing invoices...';
  try {
    const resp = await fetch('/api/upload-invoices', {method:'POST', body:formData});
    const data = await resp.json();
    if (data.success) {
      resultEl.textContent = `Processed ${data.records} invoice records - ${data.classification_rate}% classified - Dashboard updated`;
    } else {
      resultEl.style.background = 'var(--red-light)';
      resultEl.style.color = 'var(--red)';
      resultEl.textContent = `Error: ${data.error}`;
    }
  } catch(e) {
    resultEl.textContent = 'Upload failed - check console.';
  }
}
</script>
</body>
</html>"""


if __name__ == "__main__":
    print("=" * 55)
    print("  BoardIQ - Starting Web Application")
    print("=" * 55)
    print("  URL:      http://localhost:5001")
    print("  admin@boardiq.com / admin")
    print("=" * 55)
    app.run(debug=True, port=5001, host="0.0.0.0")
