"""
update_app.py
=============
After running enrich_century.py, run this to:
1. Replace the century buildings list in app.py with the enriched version
2. Commit and push to GitHub automatically

USAGE:
  python update_app.py
"""

import re
import subprocess
import sys
from century_enriched import CENTURY_ENRICHED

APP_FILE = "app.py"

def main():
    print("Reading app.py...")
    with open(APP_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Build the new century list as Python source
    lines = ["    century = ["]
    for rec in CENTURY_ENRICHED:
        lines.append(f"        {repr(rec)},")
    lines.append("    ]")
    new_list = "\n".join(lines)

    # Replace the existing century list in _load_century_buildings()
    # Match from "    century = [" to the closing "    ]"
    pattern = r'(    century = \[)(.*?)(    \])'
    flags = re.DOTALL

    if not re.search(pattern, content, flags):
        print("ERROR: Could not find 'century = [' in app.py")
        print("Make sure you're running this from the boardiq directory.")
        sys.exit(1)

    new_content = re.sub(pattern, new_list, content, count=1, flags=flags)

    print(f"Writing updated app.py with {len(CENTURY_ENRICHED)} enriched buildings...")
    with open(APP_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("Pushing to GitHub...")
    subprocess.run(["git", "add", "app.py"], check=True)
    subprocess.run(["git", "commit", "-m", f"Enrich {len(CENTURY_ENRICHED)} Century buildings with DOF + HPD + compliance data"], check=True)
    subprocess.run(["git", "push"], check=True)

    print("\nDone! Railway will deploy in ~60 seconds.")
    print("All Century buildings will now show real tax, violations, and compliance data.")

if __name__ == "__main__":
    main()
