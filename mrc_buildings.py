"""
Madison Realty Capital NYC Portfolio
8 managed rental buildings in Manhattan and Brooklyn
Data as of 2026-03-15
"""

MRC_BUILDINGS = {
    "mrc_001": {
        "id": "mrc_001",
        "address": "160 East 48th Street",
        "borough": "Manhattan",
        "neighborhood": "Midtown East",
        "units": 299,
        "floors": 16,
        "year_built": 1928,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Rental",
        "managing_agent": "Madison Realty Capital",
        "board_president": "",
        "subscription_tier": "premium",
        "subscription_since": "2026-03-01",
        "tax_assessment": {
            "assessed_value": 52310000,
            "market_value": 754295000,
            "fiscal_year": "FY2026",
            "annual_tax_est": 2615500,
            "trend_pct_2yr": 12.3,
            "certiorari_recommended": True
        },
        "violations": {
            "hpd_open": 6,
            "hpd_closed_12mo": 18,
            "avg_days_to_close": 32,
            "class_c_open": True,
            "dob_open": 2
        },
        "last_data_refresh": "2026-03-15",
        "compliance_deadlines": [
            {
                "law": "Local Law 11 - FISP Facade Inspection",
                "due_date": "Jun 2026",
                "months_away": 3,
                "urgency": "HIGH",
                "consequence": "DOB violations + fines from $1,000/month if missed",
                "cost_low": 45000,
                "cost_high": 75000,
                "network_comps": 19,
                "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The Buchanan last filed in June 2021; inspection due within 3 months."
            },
            {
                "law": "Local Law 87 - Energy Audit",
                "due_date": "Sep 2026",
                "months_away": 6,
                "urgency": "MEDIUM",
                "consequence": "DOB notices of violation if not filed timely",
                "cost_low": 18000,
                "cost_high": 32000,
                "network_comps": 22,
                "context": "Buildings over 25,000 sf must conduct energy audits and retro-commissioning studies every 10 years. The Buchanan (87,000 sf) is due by Sep 2026. A qualified energy auditor must be hired to perform the audit and recommend energy efficiency improvements."
            },
            {
                "law": "Local Law 97 - Carbon Emissions",
                "due_date": "Dec 2030",
                "months_away": 57,
                "urgency": "LOW",
                "consequence": "$150,000-$250,000/yr penalty if over emissions cap",
                "cost_low": 120000,
                "cost_high": 280000,
                "network_comps": 24,
                "context": "Starting 2025, buildings over 25,000 sf must meet progressively stricter carbon emissions caps. Penalties apply if buildings exceed the cap. The Buchanan will need to evaluate electrification, HVAC upgrades, or renewable energy to meet 2030-2031 targets."
            },
            {
                "law": "Elevator Inspection - CAT1",
                "due_date": "Jul 2026",
                "months_away": 4,
                "urgency": "HIGH",
                "consequence": "Elevator shutdown order if not compliant",
                "cost_low": 8000,
                "cost_high": 12000,
                "network_comps": 16,
                "context": "Category 1 elevators require annual inspection and testing by certified elevator inspector. The Buchanan has 6 passenger elevators + 2 service. Last CAT1 inspection was July 2025; due for renewal by July 2026."
            },
            {
                "law": "Boiler Inspection - Annual",
                "due_date": "May 2026",
                "months_away": 2,
                "urgency": "HIGH",
                "consequence": "Building cannot operate without valid boiler certificate",
                "cost_low": 3500,
                "cost_high": 5500,
                "network_comps": 12,
                "context": "Annual boiler inspection and certification required by NYC Department of Environmental Protection. The Buchanan's boiler was inspected May 2025; renewal inspection needed by May 2026. Certificate is critical for heating system operation."
            }
        ],
        "vendor_data": [
            {"vendor": "Schindler Elevator Corp", "category": "ELEVATOR_MAINTENANCE", "annual": 89400, "per_unit": 299, "last_bid_year": 2020, "months_left": 8},
            {"vendor": "New York-Alliant Insurance Services", "category": "INSURANCE", "annual": 186000, "per_unit": 622, "last_bid_year": 2022, "months_left": 14},
            {"vendor": "Metropolitan Cleaning Services", "category": "CLEANING", "annual": 142000, "per_unit": 475, "last_bid_year": 2023, "months_left": 9},
            {"vendor": "Empire Boiler Service", "category": "BOILER_MAINTENANCE", "annual": 21450, "per_unit": 72, "last_bid_year": 2024, "months_left": 18},
            {"vendor": "Apex Exterminating", "category": "EXTERMINATING", "annual": 12000, "per_unit": 40, "last_bid_year": 2024, "months_left": 6},
            {"vendor": "Con Edison", "category": "UTILITIES_ELECTRIC", "annual": 847200, "per_unit": 2832, "last_bid_year": None, "months_left": None},
            {"vendor": "Gotham Water Treatment", "category": "UTILITIES_WATER", "annual": 54000, "per_unit": 181, "last_bid_year": None, "months_left": None},
            {"vendor": "NYC Waste Solutions", "category": "WASTE_REMOVAL", "annual": 18000, "per_unit": 60, "last_bid_year": 2024, "months_left": 12},
            {"vendor": "Turner Plumbing NYC", "category": "PLUMBING_REPAIRS", "annual": 28000, "per_unit": 94, "last_bid_year": 2023, "months_left": 11},
            {"vendor": "Guardian Fire Safety", "category": "FIRE_SAFETY_SPRINKLER", "annual": 16800, "per_unit": 56, "last_bid_year": 2024, "months_left": 10}
        ]
    },
    "mrc_002": {
        "id": "mrc_002",
        "address": "361 East 50th Street",
        "borough": "Manhattan",
        "neighborhood": "Midtown East",
        "units": 44,
        "floors": 7,
        "year_built": 1940,
        "is_prewar": True,
        "building_class": "C6",
        "building_type": "Rental",
        "managing_agent": "Madison Realty Capital",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-03-01",
        "tax_assessment": {
            "assessed_value": 8800000,
            "market_value": 138600000,
            "fiscal_year": "FY2026",
            "annual_tax_est": 440000,
            "trend_pct_2yr": 8.7,
            "certiorari_recommended": False
        },
        "violations": {
            "hpd_open": 3,
            "hpd_closed_12mo": 12,
            "avg_days_to_close": 28,
            "class_c_open": False,
            "dob_open": 1
        },
        "last_data_refresh": "2026-03-15",
        "compliance_deadlines": [
            {
                "law": "Local Law 11 - FISP Facade Inspection",
                "due_date": "Oct 2027",
                "months_away": 19,
                "urgency": "LOW",
                "consequence": "DOB violations + fines from $1,000/month if missed",
                "cost_low": 28000,
                "cost_high": 48000,
                "network_comps": 14,
                "context": "Last facade inspection filed in October 2022; next inspection due October 2027. Current status is Safe with SWARMP program for minor masonry repairs in progress."
            },
            {
                "law": "Local Law 87 - Energy Audit",
                "due_date": "Apr 2027",
                "months_away": 13,
                "urgency": "LOW",
                "consequence": "DOB notices of violation if not filed timely",
                "cost_low": 12000,
                "cost_high": 20000,
                "network_comps": 11,
                "context": "Energy audit required for buildings over 25,000 sf. The Fields is 18,500 sf and is exempt from this requirement but should consider audit for sustainability planning."
            },
            {
                "law": "Boiler Inspection - Annual",
                "due_date": "Mar 2026",
                "months_away": 0,
                "urgency": "HIGH",
                "consequence": "Building cannot operate without valid boiler certificate",
                "cost_low": 2500,
                "cost_high": 4000,
                "network_comps": 8,
                "context": "Annual boiler inspection due immediately (March 2026). Boiler certificate renewal is critical for heating season compliance."
            },
            {
                "law": "Elevator Inspection - CAT1",
                "due_date": "Aug 2026",
                "months_away": 5,
                "urgency": "MEDIUM",
                "consequence": "Elevator shutdown order if not compliant",
                "cost_low": 4000,
                "cost_high": 6000,
                "network_comps": 7,
                "context": "The Fields has 1 passenger elevator + 1 service elevator. Annual CAT1 inspection and certification required by August 2026."
            }
        ],
        "vendor_data": [
            {"vendor": "Otis Elevator Company", "category": "ELEVATOR_MAINTENANCE", "annual": 12000, "per_unit": 273, "last_bid_year": 2021, "months_left": 6},
            {"vendor": "Chubb Insurance", "category": "INSURANCE", "annual": 32000, "per_unit": 727, "last_bid_year": 2024, "months_left": 10},
            {"vendor": "Gold Star Cleaning", "category": "CLEANING", "annual": 21000, "per_unit": 477, "last_bid_year": 2023, "months_left": 7},
            {"vendor": "Five Star Boiler", "category": "BOILER_MAINTENANCE", "annual": 3600, "per_unit": 82, "last_bid_year": 2024, "months_left": 16},
            {"vendor": "Consolidated Exterminating", "category": "EXTERMINATING", "annual": 2200, "per_unit": 50, "last_bid_year": 2023, "months_left": 8},
            {"vendor": "Con Edison", "category": "UTILITIES_ELECTRIC", "annual": 84000, "per_unit": 1909, "last_bid_year": None, "months_left": None},
            {"vendor": "Gotham Water Treatment", "category": "UTILITIES_WATER", "annual": 8400, "per_unit": 191, "last_bid_year": None, "months_left": None},
            {"vendor": "Metro Waste Management", "category": "WASTE_REMOVAL", "annual": 5600, "per_unit": 127, "last_bid_year": 2024, "months_left": 14},
            {"vendor": "Hudson River Plumbing", "category": "PLUMBING_REPAIRS", "annual": 8000, "per_unit": 182, "last_bid_year": 2023, "months_left": 9}
        ]
    },
    "mrc_003": {
        "id": "mrc_003",
        "address": "504 Myrtle Avenue",
        "borough": "Brooklyn",
        "neighborhood": "Clinton Hill",
        "units": 143,
        "floors": 8,
        "year_built": 2017,
        "is_prewar": False,
        "building_class": "D1",
        "building_type": "Rental",
        "managing_agent": "Madison Realty Capital",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-03-01",
        "tax_assessment": {
            "assessed_value": 28600000,
            "market_value": 345000000,
            "fiscal_year": "FY2026",
            "annual_tax_est": 1430000,
            "trend_pct_2yr": 6.2,
            "certiorari_recommended": False
        },
        "violations": {
            "hpd_open": 1,
            "hpd_closed_12mo": 4,
            "avg_days_to_close": 18,
            "class_c_open": False,
            "dob_open": 0
        },
        "last_data_refresh": "2026-03-15",
        "compliance_deadlines": [
            {
                "law": "Local Law 11 - FISP Facade Inspection",
                "due_date": "Feb 2032",
                "months_away": 71,
                "urgency": "LOW",
                "consequence": "DOB violations + fines from $1,000/month if missed",
                "cost_low": 32000,
                "cost_high": 52000,
                "network_comps": 17,
                "context": "New building (2017) - first facade inspection was filed in February 2022. Next inspection due February 2032. Building is in excellent condition with no structural concerns."
            },
            {
                "law": "Local Law 97 - Carbon Emissions",
                "due_date": "Dec 2030",
                "months_away": 57,
                "urgency": "LOW",
                "consequence": "$80,000-$140,000/yr penalty if over emissions cap",
                "cost_low": 60000,
                "cost_high": 120000,
                "network_comps": 20,
                "context": "Modern building built to higher energy standards; already exceeds base year emissions targets. Will need minor HVAC upgrades or renewable energy sourcing by 2030."
            },
            {
                "law": "Boiler Inspection - Annual",
                "due_date": "Apr 2026",
                "months_away": 1,
                "urgency": "HIGH",
                "consequence": "Building cannot operate without valid boiler certificate",
                "cost_low": 3000,
                "cost_high": 4500,
                "network_comps": 9,
                "context": "Annual inspection of modern boiler system required by April 2026. System was installed 2017 and is in excellent condition."
            },
            {
                "law": "Window Guard Installation (LL57)",
                "due_date": "Sep 2026",
                "months_away": 6,
                "urgency": "MEDIUM",
                "consequence": "DOB violations and fines for non-compliance",
                "cost_low": 18000,
                "cost_high": 28000,
                "network_comps": 13,
                "context": "Annual window guard inspection and maintenance required on all low-rise residential buildings. The Posthouse has 108 residential windows requiring guards or compliant alternatives. Testing and documentation due September 2026."
            }
        ],
        "vendor_data": [
            {"vendor": "Schindler Elevator Corp", "category": "ELEVATOR_MAINTENANCE", "annual": 32400, "per_unit": 226, "last_bid_year": 2022, "months_left": 12},
            {"vendor": "Liberty Insurance Partners", "category": "INSURANCE", "annual": 78000, "per_unit": 545, "last_bid_year": 2023, "months_left": 18},
            {"vendor": "Clean Star Services", "category": "CLEANING", "annual": 51600, "per_unit": 361, "last_bid_year": 2023, "months_left": 8},
            {"vendor": "Modern Boiler Systems", "category": "BOILER_MAINTENANCE", "annual": 8600, "per_unit": 60, "last_bid_year": 2024, "months_left": 20},
            {"vendor": "Apex Exterminating", "category": "EXTERMINATING", "annual": 5000, "per_unit": 35, "last_bid_year": 2024, "months_left": 8},
            {"vendor": "Con Edison", "category": "UTILITIES_ELECTRIC", "annual": 285600, "per_unit": 1998, "last_bid_year": None, "months_left": None},
            {"vendor": "Brooklyn Water Department", "category": "UTILITIES_WATER", "annual": 32200, "per_unit": 225, "last_bid_year": None, "months_left": None},
            {"vendor": "EcoWaste Services", "category": "WASTE_REMOVAL", "annual": 12000, "per_unit": 84, "last_bid_year": 2024, "months_left": 10},
            {"vendor": "Turner Plumbing NYC", "category": "PLUMBING_REPAIRS", "annual": 18000, "per_unit": 126, "last_bid_year": 2024, "months_left": 15}
        ]
    },
    "mrc_004": {
        "id": "mrc_004",
        "address": "644 East 14th Street",
        "borough": "Manhattan",
        "neighborhood": "East Village",
        "units": 196,
        "floors": 24,
        "year_built": 2026,
        "is_prewar": False,
        "building_class": "D1",
        "building_type": "Rental",
        "managing_agent": "Madison Realty Capital",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-03-01",
        "tax_assessment": {
            "assessed_value": 78400000,
            "market_value": 862000000,
            "fiscal_year": "FY2026",
            "annual_tax_est": 3920000,
            "trend_pct_2yr": 0,
            "certiorari_recommended": False
        },
        "violations": {
            "hpd_open": 0,
            "hpd_closed_12mo": 0,
            "avg_days_to_close": 0,
            "class_c_open": False,
            "dob_open": 0
        },
        "last_data_refresh": "2026-03-15",
        "compliance_deadlines": [
            {
                "law": "Local Law 11 - FISP Facade Inspection",
                "due_date": "Mar 2031",
                "months_away": 60,
                "urgency": "LOW",
                "consequence": "DOB violations + fines from $1,000/month if missed",
                "cost_low": 48000,
                "cost_high": 68000,
                "network_comps": 21,
                "context": "Brand new building (2026) - first facade inspection due March 2031. Building certified fully compliant with current NYC building code. No immediate facade concerns expected."
            },
            {
                "law": "Local Law 97 - Carbon Emissions",
                "due_date": "Dec 2030",
                "months_away": 57,
                "urgency": "LOW",
                "consequence": "$120,000-$180,000/yr penalty if over emissions cap",
                "cost_low": 50000,
                "cost_high": 100000,
                "network_comps": 22,
                "context": "New construction (2026) built to highest energy standards including heat pumps and solar-ready roof. Expected to exceed carbon emissions targets through 2030-2031 compliance period."
            },
            {
                "law": "Boiler Inspection - Annual",
                "due_date": "Mar 2027",
                "months_away": 12,
                "urgency": "LOW",
                "consequence": "Building cannot operate without valid boiler certificate",
                "cost_low": 3000,
                "cost_high": 4500,
                "network_comps": 10,
                "context": "Building uses modern electric heat pump system, first annual inspection due March 2027. Cutting-edge HVAC system was commissioned in March 2026."
            },
            {
                "law": "Window Guard Installation (LL57)",
                "due_date": "Mar 2027",
                "months_away": 12,
                "urgency": "LOW",
                "consequence": "DOB violations and fines for non-compliance",
                "cost_low": 24000,
                "cost_high": 35000,
                "network_comps": 15,
                "context": "Annual testing of window guards and rails on all residential units required by March 2027. Building has 176 residential windows with modern guard systems compliant with LL57."
            }
        ],
        "vendor_data": [
            {"vendor": "Otis Elevator Company", "category": "ELEVATOR_MAINTENANCE", "annual": 98800, "per_unit": 504, "last_bid_year": 2026, "months_left": 24},
            {"vendor": "AIG Insurance", "category": "INSURANCE", "annual": 142000, "per_unit": 724, "last_bid_year": 2026, "months_left": 22},
            {"vendor": "Metropolitan Cleaning Services", "category": "CLEANING", "annual": 78400, "per_unit": 400, "last_bid_year": 2026, "months_left": 18},
            {"vendor": "Modern Boiler Systems", "category": "BOILER_MAINTENANCE", "annual": 12000, "per_unit": 61, "last_bid_year": 2026, "months_left": 23},
            {"vendor": "Apex Exterminating", "category": "EXTERMINATING", "annual": 7840, "per_unit": 40, "last_bid_year": 2026, "months_left": 20},
            {"vendor": "Con Edison", "category": "UTILITIES_ELECTRIC", "annual": 392000, "per_unit": 2000, "last_bid_year": None, "months_left": None},
            {"vendor": "NYC Water Department", "category": "UTILITIES_WATER", "annual": 58800, "per_unit": 300, "last_bid_year": None, "months_left": None},
            {"vendor": "EcoWaste Services", "category": "WASTE_REMOVAL", "annual": 19600, "per_unit": 100, "last_bid_year": 2026, "months_left": 20},
            {"vendor": "Turner Plumbing NYC", "category": "PLUMBING_REPAIRS", "annual": 16000, "per_unit": 82, "last_bid_year": 2026, "months_left": 18},
            {"vendor": "Guardian Fire Safety", "category": "FIRE_SAFETY_SPRINKLER", "annual": 28000, "per_unit": 143, "last_bid_year": 2026, "months_left": 22}
        ]
    },
    "mrc_005": {
        "id": "mrc_005",
        "address": "65 Dupont Street",
        "borough": "Brooklyn",
        "neighborhood": "Greenpoint",
        "units": 473,
        "floors": 8,
        "year_built": 2024,
        "is_prewar": False,
        "building_class": "D1",
        "building_type": "Rental",
        "managing_agent": "Madison Realty Capital",
        "board_president": "",
        "subscription_tier": "premium",
        "subscription_since": "2026-03-01",
        "tax_assessment": {
            "assessed_value": 118250000,
            "market_value": 1308000000,
            "fiscal_year": "FY2026",
            "annual_tax_est": 5912500,
            "trend_pct_2yr": 14.1,
            "certiorari_recommended": False
        },
        "violations": {
            "hpd_open": 2,
            "hpd_closed_12mo": 3,
            "avg_days_to_close": 12,
            "class_c_open": False,
            "dob_open": 0
        },
        "last_data_refresh": "2026-03-15",
        "compliance_deadlines": [
            {
                "law": "Local Law 11 - FISP Facade Inspection",
                "due_date": "Feb 2029",
                "months_away": 35,
                "urgency": "LOW",
                "consequence": "DOB violations + fines from $1,000/month if missed",
                "cost_low": 45000,
                "cost_high": 68000,
                "network_comps": 23,
                "context": "First facade inspection was filed in February 2024 for new construction. Next inspection due February 2029. Building has premium exterior envelope with minimal maintenance expected."
            },
            {
                "law": "Local Law 97 - Carbon Emissions",
                "due_date": "Dec 2030",
                "months_away": 57,
                "urgency": "LOW",
                "consequence": "$200,000-$300,000/yr penalty if over emissions cap",
                "cost_low": 90000,
                "cost_high": 180000,
                "network_comps": 26,
                "context": "Large modern rental (473 units) built in 2024 with high-efficiency systems. Expected to meet or exceed carbon targets through 2030-2031 compliance period with minimal retrofits needed."
            },
            {
                "law": "Boiler Inspection - Annual",
                "due_date": "Mar 2026",
                "months_away": 0,
                "urgency": "HIGH",
                "consequence": "Building cannot operate without valid boiler certificate",
                "cost_low": 4500,
                "cost_high": 6500,
                "network_comps": 11,
                "context": "Annual inspection of district heating system serving entire building required immediately (March 2026). System was installed 2024 and is in pristine condition."
            },
            {
                "law": "Backflow Prevention Test",
                "due_date": "May 2026",
                "months_away": 2,
                "urgency": "HIGH",
                "consequence": "Building water system shutdown if not compliant",
                "cost_low": 2400,
                "cost_high": 3800,
                "network_comps": 9,
                "context": "Annual backflow prevention device testing required on all domestic water lines serving 473 units. Test must be completed by licensed NYC plumber by May 2026."
            }
        ],
        "vendor_data": [
            {"vendor": "Schindler Elevator Corp", "category": "ELEVATOR_MAINTENANCE", "annual": 189200, "per_unit": 400, "last_bid_year": 2024, "months_left": 16},
            {"vendor": "New York-Alliant Insurance Services", "category": "INSURANCE", "annual": 256000, "per_unit": 541, "last_bid_year": 2024, "months_left": 20},
            {"vendor": "Clean Star Services", "category": "CLEANING", "annual": 126000, "per_unit": 266, "last_bid_year": 2024, "months_left": 14},
            {"vendor": "Modern Boiler Systems", "category": "BOILER_MAINTENANCE", "annual": 28400, "per_unit": 60, "last_bid_year": 2024, "months_left": 21},
            {"vendor": "Apex Exterminating", "category": "EXTERMINATING", "annual": 14200, "per_unit": 30, "last_bid_year": 2024, "months_left": 9},
            {"vendor": "Con Edison", "category": "UTILITIES_ELECTRIC", "annual": 945800, "per_unit": 2000, "last_bid_year": None, "months_left": None},
            {"vendor": "Brooklyn Water Department", "category": "UTILITIES_WATER", "annual": 126000, "per_unit": 266, "last_bid_year": None, "months_left": None},
            {"vendor": "EcoWaste Services", "category": "WASTE_REMOVAL", "annual": 47300, "per_unit": 100, "last_bid_year": 2024, "months_left": 12},
            {"vendor": "Turner Plumbing NYC", "category": "PLUMBING_REPAIRS", "annual": 42400, "per_unit": 90, "last_bid_year": 2024, "months_left": 17},
            {"vendor": "Guardian Fire Safety", "category": "FIRE_SAFETY_SPRINKLER", "annual": 52000, "per_unit": 110, "last_bid_year": 2024, "months_left": 19}
        ]
    },
    "mrc_006": {
        "id": "mrc_006",
        "address": "219 East 42nd Street",
        "borough": "Manhattan",
        "neighborhood": "Midtown East",
        "units": 1602,
        "floors": 32,
        "year_built": 2027,
        "is_prewar": False,
        "building_class": "D1",
        "building_type": "Rental",
        "managing_agent": "Madison Realty Capital",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-03-01",
        "tax_assessment": {
            "assessed_value": 640800000,
            "market_value": 6408000000,
            "fiscal_year": "FY2026",
            "annual_tax_est": 32040000,
            "trend_pct_2yr": 0,
            "certiorari_recommended": False
        },
        "violations": {
            "hpd_open": 0,
            "hpd_closed_12mo": 0,
            "avg_days_to_close": 0,
            "class_c_open": False,
            "dob_open": 0
        },
        "last_data_refresh": "2026-03-15",
        "compliance_deadlines": [
            {
                "law": "Local Law 11 - FISP Facade Inspection",
                "due_date": "Sep 2032",
                "months_away": 78,
                "urgency": "LOW",
                "consequence": "DOB violations + fines from $1,000/month if missed",
                "cost_low": 85000,
                "cost_high": 120000,
                "network_comps": 28,
                "context": "Under construction (due completion 2027) - first facade inspection will be due September 2032. State-of-the-art curtain wall system with automated maintenance protocols in place."
            },
            {
                "law": "Local Law 97 - Carbon Emissions",
                "due_date": "Dec 2030",
                "months_away": 57,
                "urgency": "MEDIUM",
                "consequence": "$600,000-$900,000/yr penalty if over emissions cap",
                "cost_low": 200000,
                "cost_high": 450000,
                "network_comps": 32,
                "context": "Massive mixed-use development (1,602 units) under construction will include district geothermal system and rooftop solar. Expected to exceed carbon targets; however, large portfolio size means careful energy monitoring required."
            },
            {
                "law": "Boiler Inspection - Annual",
                "due_date": "Sep 2027",
                "months_away": 18,
                "urgency": "LOW",
                "consequence": "Building cannot operate without valid boiler certificate",
                "cost_low": 8000,
                "cost_high": 12000,
                "network_comps": 14,
                "context": "Building completion expected September 2026; first annual boiler inspection and certification due September 2027. Advanced district heating system will be tested and commissioned during construction."
            },
            {
                "law": "Window Guard Installation (LL57)",
                "due_date": "Sep 2027",
                "months_away": 18,
                "urgency": "LOW",
                "consequence": "DOB violations and fines for non-compliance",
                "cost_low": 60000,
                "cost_high": 90000,
                "network_comps": 24,
                "context": "New construction with integrated window safety systems. First annual LL57 compliance testing due September 2027 for all 1,440 residential windows with integrated guard systems."
            }
        ],
        "vendor_data": [
            {"vendor": "Otis Elevator Company", "category": "ELEVATOR_MAINTENANCE", "annual": 576000, "per_unit": 360, "last_bid_year": 2026, "months_left": 22},
            {"vendor": "AIG Insurance", "category": "INSURANCE", "annual": 960000, "per_unit": 599, "last_bid_year": 2026, "months_left": 24},
            {"vendor": "Metropolitan Cleaning Services", "category": "CLEANING", "annual": 480000, "per_unit": 300, "last_bid_year": 2026, "months_left": 16},
            {"vendor": "Enterprise Boiler Services", "category": "BOILER_MAINTENANCE", "annual": 96000, "per_unit": 60, "last_bid_year": 2026, "months_left": 20},
            {"vendor": "Apex Exterminating", "category": "EXTERMINATING", "annual": 48000, "per_unit": 30, "last_bid_year": 2026, "months_left": 18},
            {"vendor": "Con Edison", "category": "UTILITIES_ELECTRIC", "annual": 3200000, "per_unit": 1998, "last_bid_year": None, "months_left": None},
            {"vendor": "NYC Water Department", "category": "UTILITIES_WATER", "annual": 480000, "per_unit": 300, "last_bid_year": None, "months_left": None},
            {"vendor": "Metro Waste Management", "category": "WASTE_REMOVAL", "annual": 160000, "per_unit": 100, "last_bid_year": 2026, "months_left": 19},
            {"vendor": "Turner Plumbing NYC", "category": "PLUMBING_REPAIRS", "annual": 128000, "per_unit": 80, "last_bid_year": 2026, "months_left": 21},
            {"vendor": "Guardian Fire Safety", "category": "FIRE_SAFETY_SPRINKLER", "annual": 160000, "per_unit": 100, "last_bid_year": 2026, "months_left": 23}
        ]
    },
    "mrc_007": {
        "id": "mrc_007",
        "address": "1580 Nostrand Avenue",
        "borough": "Brooklyn",
        "neighborhood": "East Flatbush",
        "units": 93,
        "floors": 6,
        "year_built": 1965,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Rental",
        "managing_agent": "Madison Realty Capital",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-03-01",
        "tax_assessment": {
            "assessed_value": 16740000,
            "market_value": 236000000,
            "fiscal_year": "FY2026",
            "annual_tax_est": 837000,
            "trend_pct_2yr": 9.4,
            "certiorari_recommended": True
        },
        "violations": {
            "hpd_open": 5,
            "hpd_closed_12mo": 14,
            "avg_days_to_close": 26,
            "class_c_open": True,
            "dob_open": 1
        },
        "last_data_refresh": "2026-03-15",
        "compliance_deadlines": [
            {
                "law": "Local Law 11 - FISP Facade Inspection",
                "due_date": "Dec 2025",
                "months_away": -3,
                "urgency": "HIGH",
                "consequence": "Immediate DOB violations and escalating fines",
                "cost_low": 32000,
                "cost_high": 52000,
                "network_comps": 16,
                "context": "OVERDUE - Last facade inspection filed December 2020. Facade inspection was due December 2025 and is now overdue. DOB will issue violations if inspection not filed immediately. Building has visible mortar deterioration and spalling brick on south elevation requiring SWARMP repairs."
            },
            {
                "law": "Local Law 87 - Energy Audit",
                "due_date": "Jun 2026",
                "months_away": 3,
                "urgency": "HIGH",
                "consequence": "DOB notices of violation if not filed timely",
                "cost_low": 14000,
                "cost_high": 24000,
                "network_comps": 13,
                "context": "Energy audit due June 2026 for this 16,400 sf building. Aging HVAC system from 1980s will likely show significant inefficiencies; retrofits recommended for LL97 compliance."
            },
            {
                "law": "Boiler Inspection - Annual",
                "due_date": "Apr 2026",
                "months_away": 1,
                "urgency": "HIGH",
                "consequence": "Building cannot operate without valid boiler certificate",
                "cost_low": 2800,
                "cost_high": 4500,
                "network_comps": 9,
                "context": "Annual boiler inspection due April 2026. Original boiler from 1965 is still in operation; replacement recommended within 2 years for efficiency and compliance."
            },
            {
                "law": "Local Law 97 - Carbon Emissions",
                "due_date": "Dec 2030",
                "months_away": 57,
                "urgency": "MEDIUM",
                "consequence": "$75,000-$125,000/yr penalty if over emissions cap",
                "cost_low": 85000,
                "cost_high": 160000,
                "network_comps": 18,
                "context": "Building currently exceeds carbon emissions cap due to aging HVAC system. Must complete energy efficiency improvements or install renewable energy by 2030. Budget for boiler replacement and ventilation upgrades."
            }
        ],
        "vendor_data": [
            {"vendor": "Thyssenkrupp Elevators", "category": "ELEVATOR_MAINTENANCE", "annual": 18600, "per_unit": 200, "last_bid_year": 2019, "months_left": 4},
            {"vendor": "Chubb Insurance", "category": "INSURANCE", "annual": 54000, "per_unit": 581, "last_bid_year": 2023, "months_left": 12},
            {"vendor": "Gold Star Cleaning", "category": "CLEANING", "annual": 28000, "per_unit": 301, "last_bid_year": 2023, "months_left": 6},
            {"vendor": "Five Star Boiler", "category": "BOILER_MAINTENANCE", "annual": 5600, "per_unit": 60, "last_bid_year": 2023, "months_left": 14},
            {"vendor": "Consolidated Exterminating", "category": "EXTERMINATING", "annual": 3700, "per_unit": 40, "last_bid_year": 2024, "months_left": 10},
            {"vendor": "Con Edison", "category": "UTILITIES_ELECTRIC", "annual": 186000, "per_unit": 2000, "last_bid_year": None, "months_left": None},
            {"vendor": "Brooklyn Water Department", "category": "UTILITIES_WATER", "annual": 18600, "per_unit": 200, "last_bid_year": None, "months_left": None},
            {"vendor": "Metro Waste Management", "category": "WASTE_REMOVAL", "annual": 9300, "per_unit": 100, "last_bid_year": 2024, "months_left": 8},
            {"vendor": "Hudson River Plumbing", "category": "PLUMBING_REPAIRS", "annual": 11000, "per_unit": 118, "last_bid_year": 2023, "months_left": 7}
        ]
    },
    "mrc_008": {
        "id": "mrc_008",
        "address": "2051 Frederick Douglass Boulevard",
        "borough": "Manhattan",
        "neighborhood": "Harlem",
        "units": 78,
        "floors": 7,
        "year_built": 1925,
        "is_prewar": True,
        "building_class": "D1",
        "building_type": "Rental",
        "managing_agent": "Madison Realty Capital",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-03-01",
        "tax_assessment": {
            "assessed_value": 14040000,
            "market_value": 195000000,
            "fiscal_year": "FY2026",
            "annual_tax_est": 702000,
            "trend_pct_2yr": 11.8,
            "certiorari_recommended": True
        },
        "violations": {
            "hpd_open": 4,
            "hpd_closed_12mo": 16,
            "avg_days_to_close": 35,
            "class_c_open": False,
            "dob_open": 2
        },
        "last_data_refresh": "2026-03-15",
        "compliance_deadlines": [
            {
                "law": "Local Law 11 - FISP Facade Inspection",
                "due_date": "May 2026",
                "months_away": 2,
                "urgency": "HIGH",
                "consequence": "DOB violations + fines from $1,000/month if missed",
                "cost_low": 38000,
                "cost_high": 58000,
                "network_comps": 20,
                "context": "Historic prewar (1925) building with ornamental terra cotta facade. Last inspection filed May 2021 identified minor SWARMP items. Next inspection due May 2026. Historical preservation requirements may apply to facade repairs."
            },
            {
                "law": "Local Law 87 - Energy Audit",
                "due_date": "Aug 2026",
                "months_away": 5,
                "urgency": "MEDIUM",
                "consequence": "DOB notices of violation if not filed timely",
                "cost_low": 13000,
                "cost_high": 21000,
                "network_comps": 12,
                "context": "Energy audit due August 2026 for this 14,000 sf historic building. Original windows and poor insulation are significant energy drains. Retrofit options limited by historic preservation regulations."
            },
            {
                "law": "Boiler Inspection - Annual",
                "due_date": "Jul 2026",
                "months_away": 4,
                "urgency": "HIGH",
                "consequence": "Building cannot operate without valid boiler certificate",
                "cost_low": 3000,
                "cost_high": 4800,
                "network_comps": 10,
                "context": "Annual boiler inspection required by July 2026. Building has original cast iron radiator system with original 1925 boiler (replaced 2005). System is reliable but energy-intensive."
            },
            {
                "law": "Local Law 97 - Carbon Emissions",
                "due_date": "Dec 2030",
                "months_away": 57,
                "urgency": "MEDIUM",
                "consequence": "$65,000-$110,000/yr penalty if over emissions cap",
                "cost_low": 95000,
                "cost_high": 175000,
                "network_comps": 17,
                "context": "Building exceeds carbon cap due to poor envelope performance and heating system inefficiency. Historic designation limits major retrofits; will need renewable energy sourcing or alternative compliance strategy by 2030."
            }
        ],
        "vendor_data": [
            {"vendor": "Otis Elevator Company", "category": "ELEVATOR_MAINTENANCE", "annual": 11700, "per_unit": 150, "last_bid_year": 2020, "months_left": 5},
            {"vendor": "Liberty Insurance Partners", "category": "INSURANCE", "annual": 45000, "per_unit": 577, "last_bid_year": 2023, "months_left": 16},
            {"vendor": "Metropolitan Cleaning Services", "category": "CLEANING", "annual": 23400, "per_unit": 300, "last_bid_year": 2024, "months_left": 11},
            {"vendor": "Empire Boiler Service", "category": "BOILER_MAINTENANCE", "annual": 7200, "per_unit": 92, "last_bid_year": 2024, "months_left": 19},
            {"vendor": "Consolidated Exterminating", "category": "EXTERMINATING", "annual": 3100, "per_unit": 40, "last_bid_year": 2024, "months_left": 9},
            {"vendor": "Con Edison", "category": "UTILITIES_ELECTRIC", "annual": 187200, "per_unit": 2400, "last_bid_year": None, "months_left": None},
            {"vendor": "Gotham Water Treatment", "category": "UTILITIES_WATER", "annual": 14400, "per_unit": 185, "last_bid_year": None, "months_left": None},
            {"vendor": "Metro Waste Management", "category": "WASTE_REMOVAL", "annual": 7800, "per_unit": 100, "last_bid_year": 2024, "months_left": 13},
            {"vendor": "Hudson River Plumbing", "category": "PLUMBING_REPAIRS", "annual": 10400, "per_unit": 133, "last_bid_year": 2023, "months_left": 8}
        ]
    }
}
