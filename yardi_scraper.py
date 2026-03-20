"""
Yardi Expense Distribution Report Scraper (HTTP-only)
=====================================================
Uses requests to log into Yardi Voyager and download
Expense Distribution (Paid Only) reports for all properties.

Usage:
    python yardi_scraper.py --user USERNAME --password PASSWORD
"""

import os
import sys
import json
import argparse
import re
import time
from html.parser import HTMLParser

import requests
from bs4 import BeautifulSoup

sys.path.insert(0, os.path.dirname(__file__))

YARDI_BASE = "https://www.yardiasp13.com/03578cms"
YARDI_LOGIN_URL = f"{YARDI_BASE}/pages/LoginAdvanced.aspx"
EXPORT_DIR = os.path.join(os.path.dirname(__file__), "yardi_exports")


def save_debug(filename, content):
    """Save debug output to yardi_exports/."""
    path = os.path.join(EXPORT_DIR, filename)
    with open(path, "w") as f:
        f.write(content)
    return path


def create_session():
    """Create a requests session with browser-like headers."""
    s = requests.Session()
    s.headers.update({
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Origin": "https://www.yardiasp13.com",
        "Referer": YARDI_LOGIN_URL,
    })
    return s


def login(session, username, password):
    """Log into Yardi Voyager."""
    print("  Fetching login page...")
    resp = session.get(YARDI_LOGIN_URL)
    resp.raise_for_status()

    save_debug("01_login_page.html", resp.text)
    soup = BeautifulSoup(resp.text, "html.parser")

    # Extract the form and all its fields
    form = soup.find("form")
    if not form:
        raise Exception("No form found on login page")

    form_action = form.get("action", "")
    if form_action and not form_action.startswith("http"):
        form_action = f"{YARDI_BASE}/pages/{form_action}"
    elif not form_action:
        form_action = YARDI_LOGIN_URL

    # Collect all input fields
    post_data = {}
    for inp in soup.find_all("input"):
        name = inp.get("name")
        if name:
            post_data[name] = inp.get("value", "")

    # Collect select fields
    selects = {}
    for sel in soup.find_all("select"):
        name = sel.get("name")
        if name:
            options = []
            for opt in sel.find_all("option"):
                options.append({"value": opt.get("value", ""), "text": opt.get_text(strip=True)})
            selects[name] = options
            # Default to first option
            if options:
                post_data[name] = options[0]["value"]

    print(f"  Form action: {form_action}")
    print(f"  Form fields: {list(post_data.keys())}")
    print(f"  Select fields: {list(selects.keys())}")

    # Show Destination options if present
    for sel_name, opts in selects.items():
        if "dest" in sel_name.lower():
            print(f"  Destination options:")
            for opt in opts:
                print(f"    '{opt['value']}' — {opt['text']}")

    # Set credentials
    post_data["Username"] = username
    post_data["Password"] = password
    post_data["Destination"] = "LIVE"
    post_data["cmdLogin1"] = "Login"
    post_data["__EVENTTARGET"] = ""
    post_data["__EVENTARGUMENT"] = ""

    # Remove the placeholder password text field if it exists
    if "Password_Text" in post_data:
        del post_data["Password_Text"]

    print(f"\n  Posting login to {form_action}...")
    print(f"  Username: {username}")
    print(f"  Destination: LIVE")
    resp = session.post(form_action, data=post_data, allow_redirects=True)

    save_debug("02_login_response.html", resp.text)
    print(f"  Response status: {resp.status_code}")
    print(f"  Response URL: {resp.url}")

    # Check for success indicators
    if resp.status_code == 500:
        print(f"  Got 500 error. Response saved to yardi_exports/02_login_response.html")
        # Try alternate form action
        alt_actions = [
            f"{YARDI_BASE}/pages/LoginAdvanced.aspx",
            f"{YARDI_BASE}/pages/Login.aspx",
            f"{YARDI_BASE}/SYSTEM/login.asp",
            f"{YARDI_BASE}/SYSTEM/wci.asp?WCI=begin",
        ]
        for alt in alt_actions:
            print(f"  Trying alternate: {alt}")
            resp = session.post(alt, data=post_data, allow_redirects=True)
            save_debug(f"02_alt_{alt.split('/')[-1]}.html", resp.text)
            print(f"    Status: {resp.status_code}, URL: {resp.url}")
            if resp.status_code == 200 and "login" not in resp.url.lower():
                print(f"  Login succeeded via {alt}!")
                return True

    if "invalid" in resp.text.lower() or "incorrect" in resp.text.lower():
        raise Exception("Login failed — invalid credentials")

    if "session has ended" in resp.text.lower() or "logged off" in resp.text.lower():
        # Try the classic Yardi WCI login
        print("\n  Trying Yardi WCI login method...")
        wci_url = f"{YARDI_BASE}/SYSTEM/wci.asp"
        wci_data = {
            "WCI": "begin",
            "Username": username,
            "Password": password,
        }
        # Add Destination if found
        for sel_name, opts in selects.items():
            if "dest" in sel_name.lower() and opts:
                wci_data["Destination"] = opts[0]["value"]

        resp = session.post(wci_url, data=wci_data, allow_redirects=True)
        save_debug("02_wci_response.html", resp.text)
        print(f"  WCI status: {resp.status_code}, URL: {resp.url}")

        if resp.status_code == 200 and "logged off" not in resp.text.lower():
            print(f"  WCI login succeeded!")
            return True

        # Try iData.ASP endpoint (seen in the logout form)
        print("\n  Trying iData.ASP login method...")
        idata_url = f"{YARDI_BASE}/SYSTEM/iData.ASP?WCI=begin"
        resp = session.post(idata_url, data=wci_data, allow_redirects=True)
        save_debug("02_idata_response.html", resp.text)
        print(f"  iData status: {resp.status_code}, URL: {resp.url}")

    # Even if we're not sure, continue and see what happens
    print(f"  Login attempt complete. Continuing to discover properties...")
    return True


def discover_and_report(session):
    """Try various Yardi URLs to find properties and reports."""
    # Common Yardi Voyager page URLs to try
    urls_to_try = [
        ("Main page", f"{YARDI_BASE}/pages/Main.aspx"),
        ("Dashboard", f"{YARDI_BASE}/pages/Dashboard.aspx"),
        ("Home", f"{YARDI_BASE}/pages/Home.aspx"),
        ("Menu", f"{YARDI_BASE}/pages/Menu.aspx"),
        ("AP Menu", f"{YARDI_BASE}/pages/AP/APMenu.aspx"),
        ("Reports Menu", f"{YARDI_BASE}/pages/Reports/ReportMenu.aspx"),
        ("Report List", f"{YARDI_BASE}/pages/Reports/ReportList.aspx"),
        ("Expense Dist", f"{YARDI_BASE}/pages/Reports/ExpenseDistribution.aspx"),
        ("Expense Dist 2", f"{YARDI_BASE}/pages/AP/ExpenseDistribution.aspx"),
        ("Expense Dist 3", f"{YARDI_BASE}/pages/Reports/ExpenseDistributionPaidOnly.aspx"),
        ("GL Reports", f"{YARDI_BASE}/pages/GL/Reports.aspx"),
        ("GL Menu", f"{YARDI_BASE}/pages/GL/GLMenu.aspx"),
        ("Property List", f"{YARDI_BASE}/pages/PropertySelection.aspx"),
        ("Entity Selection", f"{YARDI_BASE}/pages/EntitySelection.aspx"),
        ("Yardi Default", f"{YARDI_BASE}/pages/default.aspx"),
        ("SysAdmin", f"{YARDI_BASE}/pages/SysAdmin/Default.aspx"),
        ("Yardi Root", f"{YARDI_BASE}/"),
        ("Start WCI", f"{YARDI_BASE}/SYSTEM/wci.asp?WCI=start"),
    ]

    results = {}
    for label, url in urls_to_try:
        try:
            resp = session.get(url, timeout=15, allow_redirects=True)
            status = resp.status_code
            final_url = resp.url
            size = len(resp.text)
            has_form = "<form" in resp.text.lower()
            has_property = bool(re.search(r'property|entity|prop', resp.text.lower()))
            has_report = bool(re.search(r'report|expense|distribution', resp.text.lower()))
            title_match = re.search(r'<title[^>]*>(.*?)</title>', resp.text, re.IGNORECASE)
            title = title_match.group(1).strip() if title_match else "N/A"

            indicator = ""
            if status == 200 and "login" not in title.lower() and "invalid" not in title.lower() and "logged off" not in resp.text.lower()[:500]:
                indicator = " ✓ AUTHENTICATED"
                save_debug(f"03_{label.replace(' ', '_')}.html", resp.text)

            print(f"  {label:20s} {status} {size:>6} bytes  title='{title}'{indicator}")
            results[label] = {"status": status, "url": final_url, "title": title, "size": size, "authenticated": bool(indicator)}
        except Exception as e:
            print(f"  {label:20s} FAILED — {e}")

    # Show summary of authenticated pages
    auth_pages = {k: v for k, v in results.items() if v.get("authenticated")}
    if auth_pages:
        print(f"\n  Found {len(auth_pages)} authenticated pages:")
        for label, info in auth_pages.items():
            print(f"    {label}: {info['url']}")
    else:
        print(f"\n  No authenticated pages found. Login likely failed.")
        print(f"  Debug files saved to yardi_exports/")

    return results


def main():
    parser = argparse.ArgumentParser(description="Yardi Expense Distribution Scraper")
    parser.add_argument("--user", required=True, help="Yardi username")
    parser.add_argument("--password", required=True, help="Yardi password")
    args = parser.parse_args()

    print("=" * 60)
    print("  YARDI EXPENSE DISTRIBUTION REPORT SCRAPER")
    print("  BoardIQ — Century Management Portfolio")
    print("=" * 60)
    print()

    os.makedirs(EXPORT_DIR, exist_ok=True)

    session = create_session()

    # Step 1: Login
    print("[1/2] Logging into Yardi...")
    try:
        login(session, args.user, args.password)
    except Exception as e:
        print(f"  FAILED: {e}")
        return

    # Step 2: Probe all endpoints to find what's accessible
    print(f"\n[2/2] Probing Yardi endpoints...")
    results = discover_and_report(session)

    print(f"\n  All debug files saved to: {EXPORT_DIR}/")
    print(f"  Share any results and I'll adjust the script for the next step.")


if __name__ == "__main__":
    main()
