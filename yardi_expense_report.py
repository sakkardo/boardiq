"""
Yardi Expense Distribution Report Runner (HTTP-only)
====================================================
Logs into Yardi Voyager via HTTP requests (no browser) and runs
Expense Distribution (Paid Only) reports for all Century Management
properties pulled from the Monday.com Building Master List.

Usage:
    python yardi_expense_report.py --password YOUR_PASSWORD
    python yardi_expense_report.py --password YOUR_PASSWORD --entity 148
    python yardi_expense_report.py --password YOUR_PASSWORD --dry-run

Environment:
    YARDI_PASSWORD=xxx python yardi_expense_report.py
"""

import os
import sys
import json
import argparse
import re
import time
import traceback
from datetime import datetime
from urllib.parse import urljoin, urlparse, parse_qs

import requests
from bs4 import BeautifulSoup

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

YARDI_BASE = "https://www.yardiasp13.com/03578cms"
YARDI_LOGIN_URL = f"{YARDI_BASE}/pages/LoginAdvanced.aspx"
YARDI_USERNAME = "sirotkin"
EXPORT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "yardi_exports")

# All 160 current buildings from Monday.com Building Master List (board 3473581362)
# Format: (entity_number, building_name, address)
MONDAY_BUILDINGS = [
    (106, "5 West 14th Owners Corp.", "10 West 15th Street"),
    (123, "Beverly House Co.", "84-51 Beverly Rd"),
    (138, "Morgan House Condominium", "153 East 87th St"),
    (140, "29-45 Tenants Corp.", "29 East 9th St"),
    (148, "130 E. 18 Owners Corp.", "130 East 18th St"),
    (159, "5601 Riverdale Owners Corp.", "5601 Riverdale Avenue"),
    (168, "310 East 49th Owners Corp.", "310 East 49th St"),
    (204, "444 East 86th Street Owners Corp.", "444 East 86th St"),
    (205, "77 Bleecker Commercial Prop", "77 Bleecker St"),
    (206, "77 Bleecker Street Corp.", "77 Bleecker St"),
    (210, "210 Central Park South Inc.", "210 Central Park South"),
    (212, "221 East 36th Owners Corp.", "225 East 36th St"),
    (215, "The Armory Owners Inc.", "529 West 42nd St"),
    (216, "315 East 70th Street Apartment Corp.", "315 East 70th St"),
    (217, "The Armory Condominium", "529 West 42nd St"),
    (224, "159 Madison Owners Corp.", "159 Madison Avenue"),
    (227, "Regent House Tenants Corp.", "25 West 54th St"),
    (228, "52 Riverside Drive Owners Corp.", "52 Riverside Drive"),
    (301, "Sheepshead Terrace Coop, Inc.", "2427 East 29th St"),
    (302, "205 Water Street Condo", "205 Water St"),
    (308, "Fillmore Gardens Cooperative", "2012 Pearson St"),
    (309, "Jsignal LLC", "76 North 4th St"),
    (340, "Pierhouse Condominium", "90 Furman St"),
    (342, "Lincoln Sponsor LLC", "31-33 Lincoln Rd"),
    (343, "The 306 Gold Street Condominium", "306 Gold St"),
    (344, "234 Starr Street Developers LLC", "234 Starr St"),
    (345, "H & L Broadway Holding LLC", "29-10 Broadway"),
    (347, "500 Waverly Condominium", "500 Waverly Avenue"),
    (348, "Ariana Condominium", "29 Tiffany Place"),
    (352, "One Grand Army Plaza", "1 Grand Army Plaza"),
    (354, "Ansonia Muse Condominium", "444 12th Street"),
    (355, "Glassworks at 336 Himrod", "336 Himrod street"),
    (357, "315 St.John's Owners Inc", "315 St Johns Pl"),
    (358, "35 Prospect Park West", "35 Prospect Park West"),
    (359, "Ansonia Clockworks Condominium", "438 12th Street"),
    (360, "The Oosten Condominium", "429 Kent"),
    (410, "Booth Street Owners Corp.", "67-76 Booth St"),
    (434, "45 Kew Gardens Owners Inc.", "45 Kew Gardens Road"),
    (437, "Crescent Tenants Corp.", "31-85 Crescent St"),
    (438, "B.G. Apartments", "102-55 67th Drive"),
    (440, "Kenwood Gardens", "160 Middle Neck Road"),
    (442, "North Shore Towers", "27110 Grand Central Parkway"),
    (500, "2575 Owners Corp.", "2575 Palisade Avenue"),
    (501, "Mayflower Terrace Inc", "1720 Mayflower Avenue"),
    (507, "Chatterton Terrace Inc", "1041 Puglsey Avenue"),
    (510, "Hugh Grant Gardens HDFC", "1966 Newbold Avenue"),
    (703, "The 160 East 22nd Street Condominium", "160 East 22nd St"),
    (710, "157 East 72nd Street Condominium", "157 East 72nd St"),
    (715, "The Parkwood Condominium", "31 East 28th St"),
    (717, "240-79 Owners Corp.", "240 East 79th St"),
    (718, "440 East 79th Street Owners Corp.", "440 East 79th St"),
    (719, "33 Greenwich Owners Corp.", "33 Greenwich Avenue"),
    (724, "Cherokee Owners Corp.", "509 East 77th St"),
    (727, "141 East Third Owners Corp.", "141 East 3rd St"),
    (732, "303 East 33rd Street Condominium", "303 East 33rd St"),
    (733, "142 E 16 Cooperative Owners' Inc.", "142 East 16th St"),
    (738, "Cheltoncort", "360 West 21st St"),
    (743, "323-325-327 West 11th St Owners Corp", "323 West 11th St"),
    (745, "The Abingdon Condominium", "320 West 12th St"),
    (746, "545 West Corp.", "545 West 111th St"),
    (747, "545 W 111th Street Condominium", "545 West 111th St"),
    (749, "125 West 96th Street Owners Corp.", "125 West 96th St"),
    (805, "The Hopkins Condominium", "172 West 79th St"),
    (806, "110 West 86th Street Condominium", "110 West 86th St"),
    (808, "400 Park Avenue South", "400 Park Avenue South"),
    (809, "305 East 24th Owners Corp (NY Towers)", "305 East 24th St"),
    (810, "150 West 87th Owners Corp.", "150 West 87th St"),
    (813, "100 Barrow Street Apartment Corp.", "100 Barrow St"),
    (818, "175 West 10th Street Condominium", "130 Seventh Avenue South"),
    (823, "121 East 22nd Street Condominium", "121 East 22nd St"),
    (824, "10 Provost Square Condominium", "10 Provost St"),
    (826, "147 Waverly Place Condominium", "147 Waverly Place"),
    (829, "41 Fifth Owners Corp", "41 Fifth Avenue"),
    (831, "91 Leonard Street Condominium", "91 Leonard St"),
    (834, "Turtle Bay Towers Corp.", "310 East 46th St"),
    (835, "Alfie Arms Corp.", "245 West 74th St"),
    (836, "309 East 87th Tenants' Corp.", "309 East 87th St"),
    (837, "580 West End Avenue Corp.", "580 West End Avenue"),
    (838, "Rose Hill Condominium", "30 East 29th St"),
    (839, "415 East 80th Street Housing Corp.", "415 East 80th St"),
    (840, "100 Norfolk Street Condominium", "100 Norfolk St"),
    (841, "150 East 78th Street Condominium", "150 East 78th St"),
    (842, "69 West 9 Street Owners Corp.", "69 West 9th St"),
    (846, "Vitre Condominium", "302 East 96th St"),
    (847, "The Orion", "350 West 42nd St"),
    (848, "1045 Madison Condominium (The Benson)", "1045 Madison Avenue"),
    (849, "1435 Tenants Corp.", "1435 Lexington Avenue"),
    (850, "LL 141 East 26th Street LLC", "141 East 26th St"),
    (851, "LL 218 East 81st Street LLC", "218 East 81st St"),
    (852, "LL 216 East 83rd Street LLC", "216 East 83rd St"),
    (853, "LL 1324 Lexington Avenue LLC", "1324 Lexington Avenue"),
    (854, "LL 1371 First Avenue LLC", "1371 1st Avenue"),
    (855, "LL 204 East 84th Street LLC", "204 East 84th St"),
    (856, "LL 505 East 88th Street LLC", "505 East 88th St"),
    (857, "LL 410 East 78th Street LLC", "410 East 78th St"),
    (858, "LL 1361 Lexington Avenue LLC", "1361 Lexington Avenue"),
    (859, "LL 1592 Second Avenue LLC", "1592 2nd Avenue"),
    (860, "LL 450 East 81st Street LLC", "450 East 81st St"),
    (861, "LL 305 East 78th Street LLC", "305 East 78th St"),
    (862, "LL 204 East 25th Street LLC", "204 East 25th St"),
    (863, "LL 205-215 East 88th Street LLC", "205-215 East 88th St"),
    (864, "LL 7 Jones Street LLC", "7 Jones St"),
    (865, "Lemle Master (204 East 83rd)", "204 East 83rd St"),
    (867, "205215 Owners LTD", "205 East 88th St"),
    (869, "100 West 18th Street Condominium", "100 West 18th St"),
    (870, "13193 Owners Corp.", "131 East 93rd St"),
    (871, "The 456 West 19th Street Condominium", "456 West 19th St"),
    (872, "SouthBridge Towers", "90 Beekman St"),
    (874, "200 East 83rd Street Condominium", "200 East 83rd St"),
    (875, "150 West 82nd Street Condominium", "150 West 82nd St"),
    (876, "105 West 73rd Owners Corp", "105 West 73rd St"),
    (878, "260 West Broadway Condominium", "260 West Broadway"),
    (879, "The 22 Bond Street Condominium", "22 Bond St"),
    (880, "1165 Madison Avenue", "1165 Madison Ave"),
    (881, "200 West 79th Street Owners, Inc", "200 West 79th St"),
    (882, "200 West 79th Street Condominium", "200 West 79th St"),
    (883, "33 East 74th Street Condominium", "33 East 74th St"),
    (884, "169 Hudson Street Condominium", "169 Hudson St"),
    (885, "Fifth Avenue and 60th Street Corp.", "785 Fifth Avenue"),
    (886, "233 East 69th Street Owners Corp.", "233 East 69th St"),
    (901, "233 East 69th Street Condominium", "233 East 69th St"),
    (902, "411 East 53rd Street Condominium", "411 East 53rd St"),
    (903, "265 River Owners Corp.", "265 Riverside Drive"),
    (904, "151 Bay Street Condominium", "151 Bay St"),
    (905, "515 Tenants Corp", "515 West End Avenue"),
    (906, "93 Worth Street Condominium", "93 Worth Street"),
    (907, "The Chelsea House", "130 West 19th Street"),
    (908, "Forum Owners Corp", "343 East 74th Street"),
    (909, "Hudson View Gardens", "116 Pinehurst Ave"),
    (910, "Fort Tryon Apartments", "245 Bennett Avenue"),
    (912, "The 176 East 82nd Street Condominium", "176 East 82nd Street"),
    (913, "The Pythian Condominium", "135 West 70th Street"),
    (915, "93rd Street Owners Corp", "125 East 93rd Street"),
    (916, "505 WE Owners Corp.", "505 West End Ave"),
    (917, "980 Fifth Avenue Corp", "980 Fifth Ave"),
    (918, "162 East 80th Street Tenants, Inc", "162 East 80th Street"),
    (919, "980 Fifth Avenue Corp. - Garage", "980 Fifth Ave"),
    (920, "Gramercy Arms Corp", "102 East 22nd Street"),
    (921, "The Liberty House", "377 Rector Pl."),
    (922, "181 MacDougal Street Condominium", "181 Macdougal St"),
    (923, "89th & Madison Owners Corp", "45 East 89th Street"),
    (924, "The 45 East 89th Street Condominium", "45 East 89th Street"),
    (925, "Blue Condominium", "105 Norfolk Street"),
    (926, "Gramercy Towers Owners Corp", "4 Lexington Ave"),
    (927, "River and Warren Condominium", "212 Warren Street"),
    (929, "200 E 75th Street Condominium", "200 East 75th Street"),
    (930, "12 E 13th Street Condominium", "12 E 13th Street"),
    (931, "771 West End Avenue, Inc", "771 W End Ave"),
    (932, "155 West 18th St. Condo (The Flynn)", "155 West 18th Street"),
    (933, "132 East 35th Street Owners, Inc.", "132 East 35th Street"),
    (934, "The Millennium Tower Residences", "30 West Street"),
    (935, "The Warren House Condominium", "155 East 34th Street"),
    (936, "The Regatta Condominium", "21 South End Avenue"),
    (937, "Liberty Terrace Condominium", "380 Rector"),
    (938, "The Cove Club Condominium", "2 South End Avenue"),
    (939, "305 Equites Corp", "305 West 86th Street"),
    (940, "Newport East, Inc.", "370 East 76th Street"),
    (941, "325 West 86th Corp", "325 West 86th Street"),
    (942, "The Kalahari Condominium", "40 W 116th Street"),
    (943, "The Halcyon Condominium", "305 E 51st Street"),
]


# ---------------------------------------------------------------------------
# HTTP Session & Yardi Auth
# ---------------------------------------------------------------------------

def create_session():
    """Create a requests session with browser-like headers."""
    s = requests.Session()
    s.headers.update({
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    })
    return s


def extract_asp_fields(soup):
    """Extract all hidden ASP.NET form fields (__VIEWSTATE, etc.)."""
    fields = {}
    for inp in soup.find_all("input", {"type": "hidden"}):
        name = inp.get("name")
        if name:
            fields[name] = inp.get("value", "")
    return fields


def save_debug(filename, content):
    """Save debug output to yardi_exports/."""
    os.makedirs(EXPORT_DIR, exist_ok=True)
    path = os.path.join(EXPORT_DIR, filename)
    with open(path, "w", encoding="utf-8", errors="replace") as f:
        f.write(content if isinstance(content, str) else str(content))
    return path


def login_yardi(session, password):
    """
    Log into Yardi Voyager via HTTP POST.
    Handles ASP.NET WebForms authentication with ViewState.
    """
    print("  [1] Fetching login page...")
    resp = session.get(YARDI_LOGIN_URL, timeout=30)
    resp.raise_for_status()
    save_debug("01_login_page.html", resp.text)

    soup = BeautifulSoup(resp.text, "html.parser")

    # Extract ASP.NET hidden fields
    asp_fields = extract_asp_fields(soup)
    print(f"      ASP.NET fields: {list(asp_fields.keys())}")

    # Build login POST data
    post_data = dict(asp_fields)
    post_data.update({
        "Username": YARDI_USERNAME,
        "Password": password,
        "Destination": "LIVE",
        "cmdLogin1": "LOGIN",
        "__EVENTTARGET": "",
        "__EVENTARGUMENT": "",
    })

    # Remove password placeholder if present
    post_data.pop("Password_Text", None)

    print(f"  [2] Posting login (user={YARDI_USERNAME}, dest=LIVE)...")
    resp = session.post(
        YARDI_LOGIN_URL,
        data=post_data,
        allow_redirects=True,
        timeout=30,
    )
    save_debug("02_login_response.html", resp.text)
    print(f"      Status: {resp.status_code}, URL: {resp.url}")

    # Check for login failure
    body_lower = resp.text.lower()
    if "invalid" in body_lower and "credential" in body_lower:
        print("      ERROR: Invalid credentials")
        return False, resp
    if "incorrect" in body_lower and ("password" in body_lower or "user" in body_lower):
        print("      ERROR: Incorrect password/username")
        return False, resp

    # Check for successful redirect away from login page
    if "login" not in resp.url.lower().split("/")[-1]:
        print("      Login appears successful (redirected away from login page)")
        return True, resp

    # Check if we got a session cookie
    cookies = dict(session.cookies)
    asp_cookie = any("asp" in k.lower() or "session" in k.lower() for k in cookies)
    if asp_cookie:
        print(f"      Got session cookies: {list(cookies.keys())}")
        return True, resp

    # If still on login page, try alternate login methods
    print("      Still on login page, trying alternate methods...")

    # Method 2: Try the SYSTEM/wci.asp endpoint
    wci_url = f"{YARDI_BASE}/SYSTEM/wci.asp"
    wci_data = {
        "WCI": "begin",
        "Username": YARDI_USERNAME,
        "Password": password,
        "Destination": "LIVE",
    }
    print(f"  [2b] Trying WCI login: {wci_url}")
    resp = session.post(wci_url, data=wci_data, allow_redirects=True, timeout=30)
    save_debug("02b_wci_response.html", resp.text)
    print(f"       Status: {resp.status_code}, URL: {resp.url}")

    if resp.status_code == 200 and "logged off" not in resp.text.lower()[:500]:
        return True, resp

    # Method 3: Try iData.ASP
    idata_url = f"{YARDI_BASE}/SYSTEM/iData.ASP?WCI=begin"
    print(f"  [2c] Trying iData login: {idata_url}")
    resp = session.post(idata_url, data=wci_data, allow_redirects=True, timeout=30)
    save_debug("02c_idata_response.html", resp.text)
    print(f"       Status: {resp.status_code}, URL: {resp.url}")

    if resp.status_code == 200:
        return True, resp

    return False, resp


# ---------------------------------------------------------------------------
# Report discovery & generation
# ---------------------------------------------------------------------------

# Common Yardi Voyager report page URL patterns
REPORT_URLS = [
    ("ReportViewer", f"{YARDI_BASE}/pages/Shared/ReportViewer.aspx"),
    ("ReportMenu", f"{YARDI_BASE}/pages/Reports/ReportMenu.aspx"),
    ("ReportList", f"{YARDI_BASE}/pages/Reporting/ReportList.aspx"),
    ("GLReports", f"{YARDI_BASE}/pages/GL/GLReportList.aspx"),
    ("APReports", f"{YARDI_BASE}/pages/AP/APReportList.aspx"),
    ("APExpDist", f"{YARDI_BASE}/pages/AP/ExpenseDistribution.aspx"),
    ("ExpDist2", f"{YARDI_BASE}/pages/Reports/ExpenseDistribution.aspx"),
    ("ExpDistPaid", f"{YARDI_BASE}/pages/Reports/ExpenseDistributionPaidOnly.aspx"),
    ("ExpDistPaid2", f"{YARDI_BASE}/pages/AP/ExpenseDistributionPaidOnly.aspx"),
]

# Yardi Voyager 7/8 REST-ish API patterns
API_URLS = [
    ("API Reports", f"{YARDI_BASE}/api/reports"),
    ("API GL", f"{YARDI_BASE}/api/gl"),
    ("API Properties", f"{YARDI_BASE}/api/properties"),
    ("Webservices", f"{YARDI_BASE}/Webservices/Reports.asmx"),
]


def discover_pages(session):
    """Probe Yardi endpoints to find report pages and property selectors."""
    print("\n  [3] Discovering Yardi report pages...")
    found = {}

    # Also check the main entry points
    entry_urls = [
        ("Main", f"{YARDI_BASE}/pages/Main.aspx"),
        ("Default", f"{YARDI_BASE}/pages/default.aspx"),
        ("Dashboard", f"{YARDI_BASE}/pages/Dashboard.aspx"),
        ("Home", f"{YARDI_BASE}/pages/Home.aspx"),
        ("PropertySel", f"{YARDI_BASE}/pages/PropertySelection.aspx"),
        ("EntitySel", f"{YARDI_BASE}/pages/EntitySelection.aspx"),
    ]

    all_urls = entry_urls + REPORT_URLS + API_URLS

    for label, url in all_urls:
        try:
            resp = session.get(url, timeout=15, allow_redirects=True)
            title_match = re.search(r'<title[^>]*>(.*?)</title>', resp.text, re.IGNORECASE)
            title = title_match.group(1).strip() if title_match else "N/A"

            is_login = "login" in resp.url.lower().split("?")[0].split("/")[-1]
            is_error = resp.status_code >= 400
            is_logged_off = "logged off" in resp.text.lower()[:500] or "session has ended" in resp.text.lower()[:500]

            status_icon = "X" if (is_login or is_error or is_logged_off) else "OK"

            print(f"      [{status_icon}] {label:18s} {resp.status_code} {len(resp.text):>6} bytes  title='{title}'")

            if status_icon == "OK":
                found[label] = {
                    "url": resp.url,
                    "status": resp.status_code,
                    "title": title,
                    "size": len(resp.text),
                    "text": resp.text,
                }
                save_debug(f"03_{label.replace(' ', '_')}.html", resp.text)

        except Exception as e:
            print(f"      [!] {label:18s} FAILED - {e}")

    return found


def find_property_selector(session, pages):
    """Look for a property/entity selector dropdown or API in discovered pages."""
    print("\n  [4] Looking for property selector...")

    for label, info in pages.items():
        html = info.get("text", "")
        soup = BeautifulSoup(html, "html.parser")

        # Look for <select> elements that might be property selectors
        for select in soup.find_all("select"):
            sel_id = select.get("id", "") or select.get("name", "")
            options = select.find_all("option")
            if len(options) > 5:  # likely a property list
                print(f"      Found select '{sel_id}' on {label} with {len(options)} options")
                opt_samples = [(o.get("value", ""), o.get_text(strip=True)) for o in options[:5]]
                print(f"      Sample: {opt_samples}")
                return {
                    "page": label,
                    "url": info["url"],
                    "select_id": sel_id,
                    "options": [(o.get("value", ""), o.get_text(strip=True)) for o in options],
                }

        # Look for frames/iframes that might contain the report interface
        for frame in soup.find_all(["frame", "iframe"]):
            src = frame.get("src", "")
            if src:
                print(f"      Found frame on {label}: {src}")

    print("      No property selector found in discovered pages")
    return None


def try_run_report(session, pages, entity_code, start_date="01/2025", end_date="12/2025"):
    """
    Attempt to navigate Yardi's report system and run the Expense Distribution
    (Paid Only) report for a given entity/property code.
    """
    # Strategy 1: Direct URL with query params (some Yardi configs support this)
    direct_urls = [
        f"{YARDI_BASE}/pages/AP/ExpenseDistribution.aspx?Entity={entity_code}&FromPeriod={start_date}&ToPeriod={end_date}&PaidOnly=Y",
        f"{YARDI_BASE}/pages/Reports/ExpenseDistribution.aspx?PropertyCode={entity_code}&From={start_date}&To={end_date}",
        f"{YARDI_BASE}/pages/Shared/ReportViewer.aspx?ReportName=ExpenseDistribution&Entity={entity_code}",
    ]

    for url in direct_urls:
        try:
            resp = session.get(url, timeout=20, allow_redirects=True)
            if resp.status_code == 200 and "login" not in resp.url.lower().split("/")[-1]:
                # Check if we got actual report content
                if "expense" in resp.text.lower() and len(resp.text) > 5000:
                    print(f"      Direct URL hit for entity {entity_code}!")
                    return resp
        except Exception:
            pass

    # Strategy 2: POST to a report page with form data
    for label in ["APExpDist", "ExpDist2", "ExpDistPaid", "ExpDistPaid2"]:
        if label not in pages:
            continue

        page_info = pages[label]
        soup = BeautifulSoup(page_info["text"], "html.parser")
        asp_fields = extract_asp_fields(soup)

        post_data = dict(asp_fields)
        # Try common Yardi form field names for the report parameters
        post_data.update({
            "Entity": str(entity_code),
            "PropertyCode": str(entity_code),
            "txtEntity": str(entity_code),
            "txtProperty": str(entity_code),
            "FromPeriod": start_date,
            "ToPeriod": end_date,
            "txtFromPeriod": start_date,
            "txtToPeriod": end_date,
            "chkPaidOnly": "on",
            "btnRun": "Run Report",
            "btnSubmit": "Submit",
            "__EVENTTARGET": "",
            "__EVENTARGUMENT": "",
        })

        try:
            resp = session.post(
                page_info["url"],
                data=post_data,
                allow_redirects=True,
                timeout=30,
            )
            if resp.status_code == 200 and len(resp.text) > 5000:
                content_type = resp.headers.get("Content-Type", "")
                if "spreadsheet" in content_type or "excel" in content_type or "octet" in content_type:
                    print(f"      Got spreadsheet response for entity {entity_code}!")
                    return resp
                if "expense" in resp.text.lower():
                    return resp
        except Exception:
            pass

    return None


def download_report_xlsx(session, resp, entity_code):
    """Save report response as .xlsx file."""
    filename = f"expense_dist_{entity_code}_{datetime.now().strftime('%Y%m%d')}.xlsx"
    filepath = os.path.join(EXPORT_DIR, filename)

    content_type = resp.headers.get("Content-Type", "")
    if "spreadsheet" in content_type or "excel" in content_type or "octet" in content_type:
        with open(filepath, "wb") as f:
            f.write(resp.content)
        print(f"      Saved: {filepath}")
        return filepath

    # If HTML response, check for an export/download link
    soup = BeautifulSoup(resp.text, "html.parser")
    export_links = []
    for a in soup.find_all("a", href=True):
        href = a["href"].lower()
        text = a.get_text(strip=True).lower()
        if any(kw in href or kw in text for kw in ["export", "excel", "xlsx", "download", "csv"]):
            export_links.append(a["href"])

    for link in export_links:
        if not link.startswith("http"):
            link = urljoin(resp.url, link)
        try:
            dl_resp = session.get(link, timeout=30)
            if dl_resp.status_code == 200 and len(dl_resp.content) > 100:
                with open(filepath, "wb") as f:
                    f.write(dl_resp.content)
                print(f"      Exported: {filepath}")
                return filepath
        except Exception:
            pass

    # Save HTML as debug
    debug_path = save_debug(f"report_{entity_code}.html", resp.text)
    print(f"      No xlsx export found, saved HTML: {debug_path}")
    return None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Run Yardi Expense Distribution reports for all Century buildings"
    )
    parser.add_argument("--password", default=os.environ.get("YARDI_PASSWORD"),
                        help="Yardi password (or set YARDI_PASSWORD env var)")
    parser.add_argument("--entity", type=int, default=None,
                        help="Run for a single entity number only (for testing)")
    parser.add_argument("--from-period", default="01/2025",
                        help="Report start period (default: 01/2025)")
    parser.add_argument("--to-period", default="12/2025",
                        help="Report end period (default: 12/2025)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Just list buildings, don't connect to Yardi")
    args = parser.parse_args()

    print("=" * 70)
    print("  YARDI EXPENSE DISTRIBUTION REPORT RUNNER")
    print("  Century Management - All Properties from Monday.com")
    print(f"  {len(MONDAY_BUILDINGS)} buildings | Period: {args.from_period} to {args.to_period}")
    print(f"  Run time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)

    # Filter to single entity if specified
    buildings = MONDAY_BUILDINGS
    if args.entity:
        buildings = [(e, n, a) for e, n, a in MONDAY_BUILDINGS if e == args.entity]
        if not buildings:
            print(f"\n  ERROR: Entity {args.entity} not found in Monday.com list")
            sys.exit(1)
        print(f"\n  Filtered to entity {args.entity}: {buildings[0][1]}")

    if args.dry_run:
        print(f"\n  DRY RUN - listing {len(buildings)} buildings:\n")
        for entity, name, addr in sorted(buildings):
            print(f"    Entity {entity:>4}  {name:50s}  {addr}")
        print(f"\n  Total: {len(buildings)} buildings")
        sys.exit(0)

    if not args.password:
        print("\n  ERROR: No password provided.")
        print("  Usage: python yardi_expense_report.py --password YOUR_PASSWORD")
        print("     or: YARDI_PASSWORD=xxx python yardi_expense_report.py")
        sys.exit(1)

    os.makedirs(EXPORT_DIR, exist_ok=True)

    # Step 1: Login
    print("\n--- LOGIN ---")
    session = create_session()
    success, resp = login_yardi(session, args.password)

    if not success:
        print("\n  LOGIN FAILED. Debug files saved to yardi_exports/")
        print("  Check yardi_exports/02_login_response.html for details.")
        sys.exit(1)

    # Step 2: Discover report pages
    print("\n--- DISCOVERY ---")
    pages = discover_pages(session)

    if not pages:
        print("\n  No authenticated pages found. Login may have failed silently.")
        print("  Check debug files in yardi_exports/")
        sys.exit(1)

    # Step 3: Look for property selector
    prop_selector = find_property_selector(session, pages)

    # Step 4: Run reports
    print(f"\n--- RUNNING REPORTS ({len(buildings)} buildings) ---")
    results = {"success": [], "failed": [], "skipped": []}

    for i, (entity, name, addr) in enumerate(sorted(buildings)):
        print(f"\n  [{i+1}/{len(buildings)}] Entity {entity}: {name}")

        try:
            resp = try_run_report(session, pages, entity, args.from_period, args.to_period)
            if resp:
                filepath = download_report_xlsx(session, resp, entity)
                if filepath:
                    results["success"].append((entity, name, filepath))
                else:
                    results["failed"].append((entity, name, "No xlsx export"))
            else:
                results["failed"].append((entity, name, "No report page accessible"))
        except Exception as e:
            results["failed"].append((entity, name, str(e)))
            traceback.print_exc()

        # Rate limit - don't hammer the server
        time.sleep(1)

    # Summary
    print("\n" + "=" * 70)
    print("  SUMMARY")
    print("=" * 70)
    print(f"  Success: {len(results['success'])}")
    print(f"  Failed:  {len(results['failed'])}")
    print(f"  Total:   {len(buildings)}")

    if results["success"]:
        print(f"\n  Successfully downloaded:")
        for entity, name, path in results["success"]:
            print(f"    Entity {entity}: {name}")

    if results["failed"]:
        print(f"\n  Failed:")
        for entity, name, reason in results["failed"]:
            print(f"    Entity {entity}: {name} - {reason}")

    # Save results JSON
    results_path = os.path.join(EXPORT_DIR, f"run_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
    with open(results_path, "w") as f:
        json.dump({
            "timestamp": datetime.now().isoformat(),
            "total_buildings": len(buildings),
            "success_count": len(results["success"]),
            "failed_count": len(results["failed"]),
            "success": [(e, n) for e, n, _ in results["success"]],
            "failed": [(e, n, r) for e, n, r in results["failed"]],
        }, f, indent=2)
    print(f"\n  Results saved to: {results_path}")


if __name__ == "__main__":
    main()
