"""
Auto-generated buildings_db.py
Buildings: 125
"""

BUILDINGS_DB = {
    "bldg_001": {
        "id": "bldg_001",
        "address": "10 West 15th Street",
        "borough": "Manhattan",
        "neighborhood": "Flatiron",
        "units": 429,
        "floors": 21,
        "year_built": 1965,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 35000,
                        "cost_high": 65000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 3 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 2400,
                        "cost_high": 4200,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 3 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2026",
                        "months_away": 10,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2030",
                        "months_away": 48,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2020 and the next is 2030. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_002": {
        "id": "bldg_002",
        "address": "153 East 87th St",
        "borough": "Manhattan",
        "neighborhood": "Upper East Side",
        "units": 48,
        "floors": 10,
        "year_built": 1960,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2028",
                        "months_away": 24,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 12000,
                        "cost_high": 22000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_003": {
        "id": "bldg_003",
        "address": "29 East 9th St",
        "borough": "Manhattan",
        "neighborhood": "Greenwich Village",
        "units": 90,
        "floors": 12,
        "year_built": 1929,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2025",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2029",
                        "months_away": 36,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2019 and the next is 2029. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_004": {
        "id": "bldg_004",
        "address": "130 East 18th St",
        "borough": "Manhattan",
        "neighborhood": "Gramercy",
        "units": 280,
        "floors": 15,
        "year_built": 1962,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2026",
                        "months_away": 10,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2030",
                        "months_away": 48,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2020 and the next is 2030. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_005": {
        "id": "bldg_005",
        "address": "310 East 49th St",
        "borough": "Manhattan",
        "neighborhood": "Turtle Bay",
        "units": 101,
        "floors": 13,
        "year_built": 1960,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2026",
                        "months_away": 10,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2030",
                        "months_away": 48,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2020 and the next is 2030. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_006": {
        "id": "bldg_006",
        "address": "444 East 86th St",
        "borough": "Manhattan",
        "neighborhood": "Upper East Side",
        "units": 315,
        "floors": 37,
        "year_built": 1974,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2025",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 35000,
                        "cost_high": 65000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 3 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 2400,
                        "cost_high": 4200,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 3 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2028",
                        "months_away": 34,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2034",
                        "months_away": 96,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2024 and the next is 2034. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_007": {
        "id": "bldg_007",
        "address": "77 Bleecker St",
        "borough": "Manhattan",
        "neighborhood": "Greenwich Village",
        "units": 243,
        "floors": 12,
        "year_built": 1930,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2027",
                        "months_away": 12,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2017 and the next is 2027. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                },
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2028",
                        "months_away": 24,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_008": {
        "id": "bldg_008",
        "address": "210 Central Park South",
        "borough": "Manhattan",
        "neighborhood": "Midtown",
        "units": 86,
        "floors": 23,
        "year_built": 1969,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 35000,
                        "cost_high": 65000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 3 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 2400,
                        "cost_high": 4200,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 3 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2026",
                        "months_away": 10,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2030",
                        "months_away": 48,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2020 and the next is 2030. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_009": {
        "id": "bldg_009",
        "address": "225 East 36th St",
        "borough": "Manhattan",
        "neighborhood": "Murray Hill",
        "units": 285,
        "floors": 20,
        "year_built": 1964,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 35000,
                        "cost_high": 65000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 3 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 2400,
                        "cost_high": 4200,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 3 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2035",
                        "months_away": 108,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2025 and the next is 2035. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_010": {
        "id": "bldg_010",
        "address": "529 West 42nd St",
        "borough": "Manhattan",
        "neighborhood": "Hell's Kitchen",
        "units": 165,
        "floors": 10,
        "year_built": 1941,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2025",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 12000,
                        "cost_high": 22000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2029",
                        "months_away": 36,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2019 and the next is 2029. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_011": {
        "id": "bldg_011",
        "address": "315 East 70th St",
        "borough": "Manhattan",
        "neighborhood": "Upper East Side",
        "units": 125,
        "floors": 12,
        "year_built": 1961,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2027",
                        "months_away": 22,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2035",
                        "months_away": 108,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2025 and the next is 2035. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_012": {
        "id": "bldg_012",
        "address": "159 Madison Avenue",
        "borough": "Manhattan",
        "neighborhood": "Murray Hill",
        "units": 119,
        "floors": 12,
        "year_built": 1920,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2025",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2027",
                        "months_away": 22,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2029",
                        "months_away": 36,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2019 and the next is 2029. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_013": {
        "id": "bldg_013",
        "address": "25 West 54th St",
        "borough": "Manhattan",
        "neighborhood": "Midtown",
        "units": 73,
        "floors": 12,
        "year_built": 1939,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2035",
                        "months_away": 108,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2025 and the next is 2035. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_014": {
        "id": "bldg_014",
        "address": "52 Riverside Drive",
        "borough": "Manhattan",
        "neighborhood": "Upper West Side",
        "units": 47,
        "floors": 16,
        "year_built": 1925,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2027",
                        "months_away": 12,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2028",
                        "months_away": 34,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_015": {
        "id": "bldg_015",
        "address": "160 East 22nd St",
        "borough": "Manhattan",
        "neighborhood": "Gramercy",
        "units": 82,
        "floors": 12,
        "year_built": 2000,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$20,000-$45,000/yr penalty if over emissions cap",
                        "cost_low": 20000,
                        "cost_high": 45000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2028",
                        "months_away": 34,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2030",
                        "months_away": 48,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2020 and the next is 2030. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_016": {
        "id": "bldg_016",
        "address": "157 East 72nd St",
        "borough": "Manhattan",
        "neighborhood": "Upper East Side",
        "units": 147,
        "floors": 14,
        "year_built": 1923,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2027",
                        "months_away": 12,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2017 and the next is 2027. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                },
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2028",
                        "months_away": 24,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_017": {
        "id": "bldg_017",
        "address": "31 East 28th St",
        "borough": "Manhattan",
        "neighborhood": "NoMad",
        "units": 22,
        "floors": 12,
        "year_built": 1913,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2027",
                        "months_away": 12,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2027",
                        "months_away": 22,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_018": {
        "id": "bldg_018",
        "address": "240 East 79th St",
        "borough": "Manhattan",
        "neighborhood": "Upper East Side",
        "units": 66,
        "floors": 17,
        "year_built": 1929,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2028",
                        "months_away": 34,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2030",
                        "months_away": 48,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2020 and the next is 2030. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_019": {
        "id": "bldg_019",
        "address": "440 East 79th St",
        "borough": "Manhattan",
        "neighborhood": "Upper East Side",
        "units": 218,
        "floors": 16,
        "year_built": 1956,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2028",
                        "months_away": 34,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2030",
                        "months_away": 48,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2020 and the next is 2030. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_020": {
        "id": "bldg_020",
        "address": "33 Greenwich Avenue",
        "borough": "Manhattan",
        "neighborhood": "West Village",
        "units": 148,
        "floors": 15,
        "year_built": 1962,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2028",
                        "months_away": 24,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2033",
                        "months_away": 84,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2023 and the next is 2033. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_021": {
        "id": "bldg_021",
        "address": "509 East 77th St",
        "borough": "Manhattan",
        "neighborhood": "Upper East Side",
        "units": 384,
        "floors": 6,
        "year_built": 1910,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 1 cab",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 800,
                        "cost_high": 1400,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 1 elevator cab. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2029",
                        "months_away": 36,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2019 and the next is 2029. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_022": {
        "id": "bldg_022",
        "address": "141 East 3rd St",
        "borough": "Manhattan",
        "neighborhood": "East Village",
        "units": 100,
        "floors": 6,
        "year_built": 1937,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 1 cab",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 800,
                        "cost_high": 1400,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 1 elevator cab. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2031",
                        "months_away": 60,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2021 and the next is 2031. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_023": {
        "id": "bldg_023",
        "address": "303 East 33rd St",
        "borough": "Manhattan",
        "neighborhood": "Murray Hill",
        "units": 129,
        "floors": 14,
        "year_built": 1990,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$20,000-$45,000/yr penalty if over emissions cap",
                        "cost_low": 20000,
                        "cost_high": 45000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2027",
                        "months_away": 22,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2028",
                        "months_away": 24,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2033",
                        "months_away": 84,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2023 and the next is 2033. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_024": {
        "id": "bldg_024",
        "address": "142 East 16th St",
        "borough": "Manhattan",
        "neighborhood": "Gramercy",
        "units": 137,
        "floors": 21,
        "year_built": 1964,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2027",
                        "months_away": 12,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 35000,
                        "cost_high": 65000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Elevator Annual Inspection - 3 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 2400,
                        "cost_high": 4200,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 3 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2026",
                        "months_away": 10,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2032",
                        "months_away": 72,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2022 and the next is 2032. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_025": {
        "id": "bldg_025",
        "address": "360 West 21st St",
        "borough": "Manhattan",
        "neighborhood": "Chelsea",
        "units": 53,
        "floors": 5,
        "year_built": 1896,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 1 cab",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 800,
                        "cost_high": 1400,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 1 elevator cab. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2028",
                        "months_away": 34,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_026": {
        "id": "bldg_026",
        "address": "320 West 12th St",
        "borough": "Manhattan",
        "neighborhood": "West Village",
        "units": 9,
        "floors": 6,
        "year_built": 1957,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Elevator Annual Inspection - 1 cab",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 800,
                        "cost_high": 1400,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 1 elevator cab. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2028",
                        "months_away": 34,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_027": {
        "id": "bldg_027",
        "address": "545 West 111th St",
        "borough": "Manhattan",
        "neighborhood": "Morningside Heights",
        "units": 133,
        "floors": 10,
        "year_built": 1911,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 12000,
                        "cost_high": 22000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2035",
                        "months_away": 108,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2025 and the next is 2035. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_028": {
        "id": "bldg_028",
        "address": "125 West 96th St",
        "borough": "Manhattan",
        "neighborhood": "Upper West Side",
        "units": 59,
        "floors": 6,
        "year_built": 1942,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 1 cab",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 800,
                        "cost_high": 1400,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 1 elevator cab. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2035",
                        "months_away": 108,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2025 and the next is 2035. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_029": {
        "id": "bldg_029",
        "address": "172 West 79th St",
        "borough": "Manhattan",
        "neighborhood": "Upper West Side",
        "units": 98,
        "floors": 19,
        "year_built": 1930,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2027",
                        "months_away": 12,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2028",
                        "months_away": 34,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2032",
                        "months_away": 72,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2022 and the next is 2032. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_030": {
        "id": "bldg_030",
        "address": "110 West 86th St",
        "borough": "Manhattan",
        "neighborhood": "Upper West Side",
        "units": 79,
        "floors": 17,
        "year_built": 1928,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2026",
                        "months_away": 10,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2030",
                        "months_away": 48,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2020 and the next is 2030. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_031": {
        "id": "bldg_031",
        "address": "400 Park Avenue South",
        "borough": "Manhattan",
        "neighborhood": "Flatiron",
        "units": 81,
        "floors": 18,
        "year_built": 2003,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$20,000-$45,000/yr penalty if over emissions cap",
                        "cost_low": 20000,
                        "cost_high": 45000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2028",
                        "months_away": 34,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2030",
                        "months_away": 48,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2020 and the next is 2030. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_032": {
        "id": "bldg_032",
        "address": "305 East 24th St",
        "borough": "Manhattan",
        "neighborhood": "Gramercy",
        "units": 388,
        "floors": 20,
        "year_built": 1966,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 35000,
                        "cost_high": 65000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 3 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 2400,
                        "cost_high": 4200,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 3 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2035",
                        "months_away": 108,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2025 and the next is 2035. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_033": {
        "id": "bldg_033",
        "address": "150 West 87th St",
        "borough": "Manhattan",
        "neighborhood": "Upper West Side",
        "units": 41,
        "floors": 10,
        "year_built": 1914,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 12000,
                        "cost_high": 22000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2026",
                        "months_away": 10,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_034": {
        "id": "bldg_034",
        "address": "100 Barrow St",
        "borough": "Manhattan",
        "neighborhood": "West Village",
        "units": 33,
        "floors": 12,
        "year_built": 2018,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$20,000-$45,000/yr penalty if over emissions cap",
                        "cost_low": 20000,
                        "cost_high": 45000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2028",
                        "months_away": 34,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_035": {
        "id": "bldg_035",
        "address": "121 East 22nd St",
        "borough": "Manhattan",
        "neighborhood": "Gramercy",
        "units": 140,
        "floors": 16,
        "year_built": 2014,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$20,000-$45,000/yr penalty if over emissions cap",
                        "cost_low": 20000,
                        "cost_high": 45000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2027",
                        "months_away": 12,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2031",
                        "months_away": 60,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2021 and the next is 2031. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_036": {
        "id": "bldg_036",
        "address": "147 Waverly Place",
        "borough": "Manhattan",
        "neighborhood": "Greenwich Village",
        "units": 18,
        "floors": 13,
        "year_built": 1915,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2027",
                        "months_away": 22,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2028",
                        "months_away": 24,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                }
        ],
        "vendor_data": []
},
    "bldg_037": {
        "id": "bldg_037",
        "address": "41 Fifth Avenue",
        "borough": "Manhattan",
        "neighborhood": "Greenwich Village",
        "units": 88,
        "floors": 16,
        "year_built": 1923,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2027",
                        "months_away": 12,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2031",
                        "months_away": 60,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2021 and the next is 2031. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_038": {
        "id": "bldg_038",
        "address": "91 Leonard St",
        "borough": "Manhattan",
        "neighborhood": "Tribeca",
        "units": 111,
        "floors": 14,
        "year_built": 2006,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$20,000-$45,000/yr penalty if over emissions cap",
                        "cost_low": 20000,
                        "cost_high": 45000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2027",
                        "months_away": 12,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2027",
                        "months_away": 22,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2031",
                        "months_away": 60,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2021 and the next is 2031. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_039": {
        "id": "bldg_039",
        "address": "310 East 46th St",
        "borough": "Manhattan",
        "neighborhood": "Turtle Bay",
        "units": 338,
        "floors": 25,
        "year_built": 1977,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 35000,
                        "cost_high": 65000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 3 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 2400,
                        "cost_high": 4200,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 3 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2026",
                        "months_away": 10,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2030",
                        "months_away": 48,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2020 and the next is 2030. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_040": {
        "id": "bldg_040",
        "address": "245 West 74th St",
        "borough": "Manhattan",
        "neighborhood": "Upper West Side",
        "units": 59,
        "floors": 10,
        "year_built": 1923,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 12000,
                        "cost_high": 22000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2035",
                        "months_away": 108,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2025 and the next is 2035. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_041": {
        "id": "bldg_041",
        "address": "309 East 87th St",
        "borough": "Manhattan",
        "neighborhood": "Upper East Side",
        "units": 122,
        "floors": 12,
        "year_built": 1955,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2025",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2029",
                        "months_away": 36,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2019 and the next is 2029. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_042": {
        "id": "bldg_042",
        "address": "580 West End Avenue",
        "borough": "Manhattan",
        "neighborhood": "Upper West Side",
        "units": 17,
        "floors": 16,
        "year_built": 1928,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2028",
                        "months_away": 34,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_043": {
        "id": "bldg_043",
        "address": "30 East 29th St",
        "borough": "Manhattan",
        "neighborhood": "NoMad",
        "units": 123,
        "floors": 18,
        "year_built": 2017,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$20,000-$45,000/yr penalty if over emissions cap",
                        "cost_low": 20000,
                        "cost_high": 45000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2026",
                        "months_away": 10,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2030",
                        "months_away": 48,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2020 and the next is 2030. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_044": {
        "id": "bldg_044",
        "address": "415 East 80th St",
        "borough": "Manhattan",
        "neighborhood": "Upper East Side",
        "units": 78,
        "floors": 5,
        "year_built": 1959,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 1 cab",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 800,
                        "cost_high": 1400,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 1 elevator cab. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2027",
                        "months_away": 22,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2035",
                        "months_away": 108,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2025 and the next is 2035. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_045": {
        "id": "bldg_045",
        "address": "100 Norfolk St",
        "borough": "Manhattan",
        "neighborhood": "Lower East Side",
        "units": 38,
        "floors": 12,
        "year_built": 2015,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$20,000-$45,000/yr penalty if over emissions cap",
                        "cost_low": 20000,
                        "cost_high": 45000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2028",
                        "months_away": 34,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_046": {
        "id": "bldg_046",
        "address": "150 East 78th St",
        "borough": "Manhattan",
        "neighborhood": "Upper East Side",
        "units": 25,
        "floors": 10,
        "year_built": 1960,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 12000,
                        "cost_high": 22000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2026",
                        "months_away": 10,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_047": {
        "id": "bldg_047",
        "address": "69 West 9th St",
        "borough": "Manhattan",
        "neighborhood": "Greenwich Village",
        "units": 106,
        "floors": 13,
        "year_built": 1959,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2025",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2029",
                        "months_away": 36,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2019 and the next is 2029. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_048": {
        "id": "bldg_048",
        "address": "302 East 96th St",
        "borough": "Manhattan",
        "neighborhood": "Upper East Side",
        "units": 48,
        "floors": 12,
        "year_built": 2005,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$20,000-$45,000/yr penalty if over emissions cap",
                        "cost_low": 20000,
                        "cost_high": 45000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2027",
                        "months_away": 12,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2026",
                        "months_away": 10,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_049": {
        "id": "bldg_049",
        "address": "350 West 42nd St",
        "borough": "Manhattan",
        "neighborhood": "Hell's Kitchen",
        "units": 551,
        "floors": 60,
        "year_built": 2006,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 35000,
                        "cost_high": 65000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$20,000-$45,000/yr penalty if over emissions cap",
                        "cost_low": 20000,
                        "cost_high": 45000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 3 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 2400,
                        "cost_high": 4200,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 3 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2026",
                        "months_away": 10,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2030",
                        "months_away": 48,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2020 and the next is 2030. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_050": {
        "id": "bldg_050",
        "address": "1045 Madison Avenue",
        "borough": "Manhattan",
        "neighborhood": "Upper East Side",
        "units": 15,
        "floors": 12,
        "year_built": 2000,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_051": {
        "id": "bldg_051",
        "address": "1435 Lexington Avenue",
        "borough": "Manhattan",
        "neighborhood": "Upper East Side",
        "units": 64,
        "floors": 12,
        "year_built": 1925,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2027",
                        "months_away": 22,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2035",
                        "months_away": 108,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2025 and the next is 2035. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_052": {
        "id": "bldg_052",
        "address": "100 West 18th St",
        "borough": "Manhattan",
        "neighborhood": "Chelsea",
        "units": 47,
        "floors": 10,
        "year_built": 2000,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 12000,
                        "cost_high": 22000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$20,000-$45,000/yr penalty if over emissions cap",
                        "cost_low": 20000,
                        "cost_high": 45000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2028",
                        "months_away": 34,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_053": {
        "id": "bldg_053",
        "address": "131 East 93rd St",
        "borough": "Manhattan",
        "neighborhood": "Carnegie Hill",
        "units": 35,
        "floors": 9,
        "year_built": 1923,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2027",
                        "months_away": 12,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 12000,
                        "cost_high": 22000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2027",
                        "months_away": 22,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_054": {
        "id": "bldg_054",
        "address": "456 West 19th St",
        "borough": "Manhattan",
        "neighborhood": "Chelsea",
        "units": 22,
        "floors": 8,
        "year_built": 2005,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2027",
                        "months_away": 12,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 12000,
                        "cost_high": 22000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2028",
                        "months_away": 34,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_055": {
        "id": "bldg_055",
        "address": "90 Beekman St",
        "borough": "Manhattan",
        "neighborhood": "Financial District",
        "units": 1651,
        "floors": 27,
        "year_built": 1971,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 35000,
                        "cost_high": 65000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 3 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 2400,
                        "cost_high": 4200,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 3 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2026",
                        "months_away": 10,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2030",
                        "months_away": 48,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2020 and the next is 2030. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_056": {
        "id": "bldg_056",
        "address": "200 East 83rd St",
        "borough": "Manhattan",
        "neighborhood": "Upper East Side",
        "units": 85,
        "floors": 14,
        "year_built": 2000,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$20,000-$45,000/yr penalty if over emissions cap",
                        "cost_low": 20000,
                        "cost_high": 45000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2028",
                        "months_away": 34,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2030",
                        "months_away": 48,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2020 and the next is 2030. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_057": {
        "id": "bldg_057",
        "address": "150 West 82nd St",
        "borough": "Manhattan",
        "neighborhood": "Upper West Side",
        "units": 27,
        "floors": 10,
        "year_built": 1926,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 12000,
                        "cost_high": 22000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2026",
                        "months_away": 10,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_058": {
        "id": "bldg_058",
        "address": "105 West 73rd St",
        "borough": "Manhattan",
        "neighborhood": "Upper West Side",
        "units": 39,
        "floors": 8,
        "year_built": 1920,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 12000,
                        "cost_high": 22000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_059": {
        "id": "bldg_059",
        "address": "260 West Broadway",
        "borough": "Manhattan",
        "neighborhood": "Tribeca",
        "units": 50,
        "floors": 12,
        "year_built": 1894,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2028",
                        "months_away": 34,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_060": {
        "id": "bldg_060",
        "address": "22 Bond St",
        "borough": "Manhattan",
        "neighborhood": "NoHo",
        "units": 6,
        "floors": 6,
        "year_built": 2000,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Elevator Annual Inspection - 1 cab",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 800,
                        "cost_high": 1400,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 1 elevator cab. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2026",
                        "months_away": 10,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_061": {
        "id": "bldg_061",
        "address": "1165 Madison Ave",
        "borough": "Manhattan",
        "neighborhood": "Carnegie Hill",
        "units": 11,
        "floors": 10,
        "year_built": 2000,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 12000,
                        "cost_high": 22000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_062": {
        "id": "bldg_062",
        "address": "200 West 79th St",
        "borough": "Manhattan",
        "neighborhood": "Upper West Side",
        "units": 241,
        "floors": 19,
        "year_built": 1975,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2028",
                        "months_away": 34,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2030",
                        "months_away": 48,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2020 and the next is 2030. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_063": {
        "id": "bldg_063",
        "address": "33 East 74th St",
        "borough": "Manhattan",
        "neighborhood": "Upper East Side",
        "units": 10,
        "floors": 8,
        "year_built": 2000,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2028",
                        "months_away": 24,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 12000,
                        "cost_high": 22000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_064": {
        "id": "bldg_064",
        "address": "169 Hudson St",
        "borough": "Manhattan",
        "neighborhood": "Tribeca",
        "units": 14,
        "floors": 8,
        "year_built": 1915,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2025",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 12000,
                        "cost_high": 22000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_065": {
        "id": "bldg_065",
        "address": "785 Fifth Avenue",
        "borough": "Manhattan",
        "neighborhood": "Upper East Side",
        "units": 54,
        "floors": 18,
        "year_built": 1963,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_066": {
        "id": "bldg_066",
        "address": "233 East 69th St",
        "borough": "Manhattan",
        "neighborhood": "Upper East Side",
        "units": 192,
        "floors": 18,
        "year_built": 1954,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2028",
                        "months_away": 24,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2033",
                        "months_away": 84,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2023 and the next is 2033. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_067": {
        "id": "bldg_067",
        "address": "411 East 53rd St",
        "borough": "Manhattan",
        "neighborhood": "Turtle Bay",
        "units": 191,
        "floors": 21,
        "year_built": 1959,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2027",
                        "months_away": 12,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 35000,
                        "cost_high": 65000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Elevator Annual Inspection - 3 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 2400,
                        "cost_high": 4200,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 3 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2027",
                        "months_away": 22,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2031",
                        "months_away": 60,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2021 and the next is 2031. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_068": {
        "id": "bldg_068",
        "address": "265 Riverside Drive",
        "borough": "Manhattan",
        "neighborhood": "Upper West Side",
        "units": 75,
        "floors": 10,
        "year_built": 1912,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 12000,
                        "cost_high": 22000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2035",
                        "months_away": 108,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2025 and the next is 2035. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_069": {
        "id": "bldg_069",
        "address": "515 West End Avenue",
        "borough": "Manhattan",
        "neighborhood": "Upper West Side",
        "units": 60,
        "floors": 16,
        "year_built": 1926,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2027",
                        "months_away": 22,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2035",
                        "months_away": 108,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2025 and the next is 2035. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_070": {
        "id": "bldg_070",
        "address": "93 Worth Street",
        "borough": "Manhattan",
        "neighborhood": "Tribeca",
        "units": 92,
        "floors": 17,
        "year_built": 2014,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$20,000-$45,000/yr penalty if over emissions cap",
                        "cost_low": 20000,
                        "cost_high": 45000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2028",
                        "months_away": 24,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2033",
                        "months_away": 84,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2023 and the next is 2033. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_071": {
        "id": "bldg_071",
        "address": "130 West 19th Street",
        "borough": "Manhattan",
        "neighborhood": "Chelsea",
        "units": 64,
        "floors": 12,
        "year_built": 2005,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$20,000-$45,000/yr penalty if over emissions cap",
                        "cost_low": 20000,
                        "cost_high": 45000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2026",
                        "months_away": 10,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2030",
                        "months_away": 48,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2020 and the next is 2030. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_072": {
        "id": "bldg_072",
        "address": "343 East 74th Street",
        "borough": "Manhattan",
        "neighborhood": "Upper East Side",
        "units": 148,
        "floors": 16,
        "year_built": 1965,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2027",
                        "months_away": 22,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2028",
                        "months_away": 24,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2033",
                        "months_away": 84,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2023 and the next is 2033. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_073": {
        "id": "bldg_073",
        "address": "116 Pinehurst Ave",
        "borough": "Manhattan",
        "neighborhood": "Washington Heights",
        "units": 353,
        "floors": 6,
        "year_built": 1924,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2016 and the next is 2026. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 1 cab",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 800,
                        "cost_high": 1400,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 1 elevator cab. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2028",
                        "months_away": 34,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_074": {
        "id": "bldg_074",
        "address": "245 Bennett Avenue",
        "borough": "Manhattan",
        "neighborhood": "Washington Heights",
        "units": 352,
        "floors": 5,
        "year_built": 1950,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 1 cab",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 800,
                        "cost_high": 1400,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 1 elevator cab. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2035",
                        "months_away": 108,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2025 and the next is 2035. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_075": {
        "id": "bldg_075",
        "address": "135 West 70th Street",
        "borough": "Manhattan",
        "neighborhood": "Upper West Side",
        "units": 84,
        "floors": 11,
        "year_built": 1926,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 12000,
                        "cost_high": 22000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2027",
                        "months_away": 22,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2035",
                        "months_away": 108,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2025 and the next is 2035. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_076": {
        "id": "bldg_076",
        "address": "125 East 93rd Street",
        "borough": "Manhattan",
        "neighborhood": "Carnegie Hill",
        "units": 29,
        "floors": 9,
        "year_built": 1924,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 12000,
                        "cost_high": 22000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_077": {
        "id": "bldg_077",
        "address": "505 West End Ave",
        "borough": "Manhattan",
        "neighborhood": "Upper West Side",
        "units": 68,
        "floors": 14,
        "year_built": 1922,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2035",
                        "months_away": 108,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2025 and the next is 2035. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_078": {
        "id": "bldg_078",
        "address": "980 Fifth Ave",
        "borough": "Manhattan",
        "neighborhood": "Upper East Side",
        "units": 45,
        "floors": 26,
        "year_built": 1966,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 35000,
                        "cost_high": 65000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 3 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 2400,
                        "cost_high": 4200,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 3 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2028",
                        "months_away": 34,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_079": {
        "id": "bldg_079",
        "address": "162 East 80th Street",
        "borough": "Manhattan",
        "neighborhood": "Upper East Side",
        "units": 26,
        "floors": 10,
        "year_built": 1928,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2027",
                        "months_away": 12,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 12000,
                        "cost_high": 22000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2026",
                        "months_away": 10,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_080": {
        "id": "bldg_080",
        "address": "102 East 22nd Street",
        "borough": "Manhattan",
        "neighborhood": "Gramercy",
        "units": 89,
        "floors": 9,
        "year_built": 1963,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2027",
                        "months_away": 12,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 12000,
                        "cost_high": 22000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2026",
                        "months_away": 10,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2032",
                        "months_away": 72,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2022 and the next is 2032. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_081": {
        "id": "bldg_081",
        "address": "377 Rector Pl",
        "borough": "Manhattan",
        "neighborhood": "Battery Park City",
        "units": 239,
        "floors": 30,
        "year_built": 1986,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$20,000-$45,000/yr penalty if over emissions cap",
                        "cost_low": 20000,
                        "cost_high": 45000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 3 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 2400,
                        "cost_high": 4200,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 3 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2027",
                        "months_away": 12,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2017 and the next is 2027. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                },
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2028",
                        "months_away": 24,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 35000,
                        "cost_high": 65000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_082": {
        "id": "bldg_082",
        "address": "181 Macdougal St",
        "borough": "Manhattan",
        "neighborhood": "Greenwich Village",
        "units": 16,
        "floors": 6,
        "year_built": 1920,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Elevator Annual Inspection - 1 cab",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 800,
                        "cost_high": 1400,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 1 elevator cab. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_083": {
        "id": "bldg_083",
        "address": "45 East 89th Street",
        "borough": "Manhattan",
        "neighborhood": "Carnegie Hill",
        "units": 251,
        "floors": 30,
        "year_built": 1969,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 35000,
                        "cost_high": 65000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 3 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 2400,
                        "cost_high": 4200,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 3 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2035",
                        "months_away": 108,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2025 and the next is 2035. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_084": {
        "id": "bldg_084",
        "address": "105 Norfolk Street",
        "borough": "Manhattan",
        "neighborhood": "Lower East Side",
        "units": 30,
        "floors": 16,
        "year_built": 2006,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$20,000-$45,000/yr penalty if over emissions cap",
                        "cost_low": 20000,
                        "cost_high": 45000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_085": {
        "id": "bldg_085",
        "address": "4 Lexington Ave",
        "borough": "Manhattan",
        "neighborhood": "Gramercy",
        "units": 160,
        "floors": 15,
        "year_built": 1912,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2025",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2028",
                        "months_away": 34,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2034",
                        "months_away": 96,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2024 and the next is 2034. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_086": {
        "id": "bldg_086",
        "address": "212 Warren Street",
        "borough": "Manhattan",
        "neighborhood": "Battery Park City",
        "units": 166,
        "floors": 20,
        "year_built": 2015,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$20,000-$45,000/yr penalty if over emissions cap",
                        "cost_low": 20000,
                        "cost_high": 45000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2027",
                        "months_away": 12,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 35000,
                        "cost_high": 65000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Elevator Annual Inspection - 3 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 2400,
                        "cost_high": 4200,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 3 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2028",
                        "months_away": 34,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2032",
                        "months_away": 72,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2022 and the next is 2032. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_087": {
        "id": "bldg_087",
        "address": "200 East 75th Street",
        "borough": "Manhattan",
        "neighborhood": "Upper East Side",
        "units": 36,
        "floors": 10,
        "year_built": 2000,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 12000,
                        "cost_high": 22000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$20,000-$45,000/yr penalty if over emissions cap",
                        "cost_low": 20000,
                        "cost_high": 45000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2028",
                        "months_away": 34,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_088": {
        "id": "bldg_088",
        "address": "12 E 13th Street",
        "borough": "Manhattan",
        "neighborhood": "Greenwich Village",
        "units": 8,
        "floors": 6,
        "year_built": 2000,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Elevator Annual Inspection - 1 cab",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 800,
                        "cost_high": 1400,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 1 elevator cab. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2028",
                        "months_away": 34,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_089": {
        "id": "bldg_089",
        "address": "771 W End Ave",
        "borough": "Manhattan",
        "neighborhood": "Upper West Side",
        "units": 78,
        "floors": 12,
        "year_built": 1915,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2027",
                        "months_away": 12,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2027",
                        "months_away": 22,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2031",
                        "months_away": 60,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2021 and the next is 2031. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_090": {
        "id": "bldg_090",
        "address": "155 West 18th Street",
        "borough": "Manhattan",
        "neighborhood": "Chelsea",
        "units": 30,
        "floors": 8,
        "year_built": 2010,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 12000,
                        "cost_high": 22000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$20,000-$45,000/yr penalty if over emissions cap",
                        "cost_low": 20000,
                        "cost_high": 45000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2027",
                        "months_away": 22,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_091": {
        "id": "bldg_091",
        "address": "132 East 35th Street",
        "borough": "Manhattan",
        "neighborhood": "Murray Hill",
        "units": 187,
        "floors": 18,
        "year_built": 1960,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2027",
                        "months_away": 12,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2028",
                        "months_away": 34,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2032",
                        "months_away": 72,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2022 and the next is 2032. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_092": {
        "id": "bldg_092",
        "address": "30 West Street",
        "borough": "Manhattan",
        "neighborhood": "Financial District",
        "units": 236,
        "floors": 38,
        "year_built": 1998,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 35000,
                        "cost_high": 65000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$20,000-$45,000/yr penalty if over emissions cap",
                        "cost_low": 20000,
                        "cost_high": 45000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 3 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 2400,
                        "cost_high": 4200,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 3 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2026",
                        "months_away": 10,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2030",
                        "months_away": 48,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2020 and the next is 2030. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_093": {
        "id": "bldg_093",
        "address": "155 East 34th Street",
        "borough": "Manhattan",
        "neighborhood": "Murray Hill",
        "units": 339,
        "floors": 30,
        "year_built": 1985,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 35000,
                        "cost_high": 65000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$20,000-$45,000/yr penalty if over emissions cap",
                        "cost_low": 20000,
                        "cost_high": 45000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 3 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 2400,
                        "cost_high": 4200,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 3 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2027",
                        "months_away": 22,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2035",
                        "months_away": 108,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2025 and the next is 2035. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_094": {
        "id": "bldg_094",
        "address": "21 South End Avenue",
        "borough": "Manhattan",
        "neighborhood": "Battery Park City",
        "units": 181,
        "floors": 20,
        "year_built": 1987,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$20,000-$45,000/yr penalty if over emissions cap",
                        "cost_low": 20000,
                        "cost_high": 45000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2027",
                        "months_away": 12,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 35000,
                        "cost_high": 65000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Elevator Annual Inspection - 3 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 2400,
                        "cost_high": 4200,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 3 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2031",
                        "months_away": 60,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2021 and the next is 2031. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_095": {
        "id": "bldg_095",
        "address": "380 Rector Place",
        "borough": "Manhattan",
        "neighborhood": "Battery Park City",
        "units": 247,
        "floors": 25,
        "year_built": 1989,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 35000,
                        "cost_high": 65000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$20,000-$45,000/yr penalty if over emissions cap",
                        "cost_low": 20000,
                        "cost_high": 45000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 3 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 2400,
                        "cost_high": 4200,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 3 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2028",
                        "months_away": 34,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2030",
                        "months_away": 48,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2020 and the next is 2030. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_096": {
        "id": "bldg_096",
        "address": "2 South End Avenue",
        "borough": "Manhattan",
        "neighborhood": "Battery Park City",
        "units": 165,
        "floors": 18,
        "year_built": 1987,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$20,000-$45,000/yr penalty if over emissions cap",
                        "cost_low": 20000,
                        "cost_high": 45000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2027",
                        "months_away": 12,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2026",
                        "months_away": 10,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2032",
                        "months_away": 72,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2022 and the next is 2032. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_097": {
        "id": "bldg_097",
        "address": "305 West 86th Street",
        "borough": "Manhattan",
        "neighborhood": "Upper West Side",
        "units": 49,
        "floors": 10,
        "year_built": 1930,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 12000,
                        "cost_high": 22000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_098": {
        "id": "bldg_098",
        "address": "370 East 76th Street",
        "borough": "Manhattan",
        "neighborhood": "Upper East Side",
        "units": 364,
        "floors": 20,
        "year_built": 1970,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 35000,
                        "cost_high": 65000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 3 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 2400,
                        "cost_high": 4200,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 3 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2026",
                        "months_away": 10,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2030",
                        "months_away": 48,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2020 and the next is 2030. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_099": {
        "id": "bldg_099",
        "address": "325 West 86th Street",
        "borough": "Manhattan",
        "neighborhood": "Upper West Side",
        "units": 49,
        "floors": 10,
        "year_built": 1930,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 12000,
                        "cost_high": 22000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_100": {
        "id": "bldg_100",
        "address": "40 W 116th Street",
        "borough": "Manhattan",
        "neighborhood": "Harlem",
        "units": 249,
        "floors": 18,
        "year_built": 2008,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$20,000-$45,000/yr penalty if over emissions cap",
                        "cost_low": 20000,
                        "cost_high": 45000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2028",
                        "months_away": 34,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2030",
                        "months_away": 48,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2020 and the next is 2030. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_101": {
        "id": "bldg_101",
        "address": "305 E 51st Street",
        "borough": "Manhattan",
        "neighborhood": "Turtle Bay",
        "units": 123,
        "floors": 14,
        "year_built": 2005,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$20,000-$45,000/yr penalty if over emissions cap",
                        "cost_low": 20000,
                        "cost_high": 45000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2035",
                        "months_away": 108,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2025 and the next is 2035. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_102": {
        "id": "bldg_102",
        "address": "2427 East 29th St",
        "borough": "Brooklyn",
        "neighborhood": "Sheepshead Bay",
        "units": 168,
        "floors": 6,
        "year_built": 1962,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 1 cab",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 800,
                        "cost_high": 1400,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 1 elevator cab. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2027",
                        "months_away": 12,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2017 and the next is 2027. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2027",
                        "months_away": 22,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_103": {
        "id": "bldg_103",
        "address": "205 Water St",
        "borough": "Brooklyn",
        "neighborhood": "DUMBO",
        "units": 64,
        "floors": 8,
        "year_built": 2005,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 12000,
                        "cost_high": 22000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$20,000-$45,000/yr penalty if over emissions cap",
                        "cost_low": 20000,
                        "cost_high": 45000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2035",
                        "months_away": 108,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2025 and the next is 2035. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_104": {
        "id": "bldg_104",
        "address": "2012 Pearson St",
        "borough": "Brooklyn",
        "neighborhood": "Canarsie",
        "units": 340,
        "floors": 2,
        "year_built": 1952,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2028",
                        "months_away": 34,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2032",
                        "months_away": 72,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2022 and the next is 2032. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_105": {
        "id": "bldg_105",
        "address": "90 Furman St",
        "borough": "Brooklyn",
        "neighborhood": "Brooklyn Heights",
        "units": 130,
        "floors": 10,
        "year_built": 2017,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 12000,
                        "cost_high": 22000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$20,000-$45,000/yr penalty if over emissions cap",
                        "cost_low": 20000,
                        "cost_high": 45000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2026",
                        "months_away": 10,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2030",
                        "months_away": 48,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2020 and the next is 2030. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_106": {
        "id": "bldg_106",
        "address": "306 Gold St",
        "borough": "Brooklyn",
        "neighborhood": "Downtown Brooklyn",
        "units": 303,
        "floors": 42,
        "year_built": 2008,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2016 and the next is 2026. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$20,000-$45,000/yr penalty if over emissions cap",
                        "cost_low": 20000,
                        "cost_high": 45000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2027",
                        "months_away": 12,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 35000,
                        "cost_high": 65000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Elevator Annual Inspection - 3 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 2400,
                        "cost_high": 4200,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 3 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2026",
                        "months_away": 10,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_107": {
        "id": "bldg_107",
        "address": "500 Waverly Avenue",
        "borough": "Brooklyn",
        "neighborhood": "Clinton Hill",
        "units": 48,
        "floors": 6,
        "year_built": 2005,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$20,000-$45,000/yr penalty if over emissions cap",
                        "cost_low": 20000,
                        "cost_high": 45000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 1 cab",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 800,
                        "cost_high": 1400,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 1 elevator cab. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2028",
                        "months_away": 34,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_108": {
        "id": "bldg_108",
        "address": "29 Tiffany Place",
        "borough": "Brooklyn",
        "neighborhood": "Cobble Hill",
        "units": 70,
        "floors": 8,
        "year_built": 2005,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2025",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 12000,
                        "cost_high": 22000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$20,000-$45,000/yr penalty if over emissions cap",
                        "cost_low": 20000,
                        "cost_high": 45000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2029",
                        "months_away": 36,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2019 and the next is 2029. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_109": {
        "id": "bldg_109",
        "address": "1 Grand Army Plaza",
        "borough": "Brooklyn",
        "neighborhood": "Prospect Heights",
        "units": 96,
        "floors": 10,
        "year_built": 2005,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$20,000-$45,000/yr penalty if over emissions cap",
                        "cost_low": 20000,
                        "cost_high": 45000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2027",
                        "months_away": 12,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 12000,
                        "cost_high": 22000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2031",
                        "months_away": 60,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2021 and the next is 2031. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_110": {
        "id": "bldg_110",
        "address": "444 12th Street",
        "borough": "Brooklyn",
        "neighborhood": "Park Slope",
        "units": 37,
        "floors": 6,
        "year_built": 2005,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$20,000-$45,000/yr penalty if over emissions cap",
                        "cost_low": 20000,
                        "cost_high": 45000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 1 cab",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 800,
                        "cost_high": 1400,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 1 elevator cab. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2028",
                        "months_away": 34,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_111": {
        "id": "bldg_111",
        "address": "438 12th Street",
        "borough": "Brooklyn",
        "neighborhood": "Park Slope",
        "units": 35,
        "floors": 8,
        "year_built": 1920,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2026",
                        "months_away": 10,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2028",
                        "months_away": 24,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 12000,
                        "cost_high": 22000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                }
        ],
        "vendor_data": []
},
    "bldg_112": {
        "id": "bldg_112",
        "address": "429 Kent Avenue",
        "borough": "Brooklyn",
        "neighborhood": "Williamsburg",
        "units": 216,
        "floors": 8,
        "year_built": 2016,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Condo",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2025",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 12000,
                        "cost_high": 22000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$20,000-$45,000/yr penalty if over emissions cap",
                        "cost_low": 20000,
                        "cost_high": 45000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2029",
                        "months_away": 36,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2019 and the next is 2029. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_113": {
        "id": "bldg_113",
        "address": "315 St Johns Pl",
        "borough": "Brooklyn",
        "neighborhood": "Crown Heights",
        "units": 47,
        "floors": 6,
        "year_built": 1921,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 1 cab",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 800,
                        "cost_high": 1400,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 1 elevator cab. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2027",
                        "months_away": 22,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_114": {
        "id": "bldg_114",
        "address": "35 Prospect Park West",
        "borough": "Brooklyn",
        "neighborhood": "Park Slope",
        "units": 74,
        "floors": 16,
        "year_built": 1928,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2027",
                        "months_away": 22,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2035",
                        "months_away": 108,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2025 and the next is 2035. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_115": {
        "id": "bldg_115",
        "address": "336 Himrod Street",
        "borough": "Brooklyn",
        "neighborhood": "Bushwick",
        "units": 63,
        "floors": 6,
        "year_built": 2015,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Rental",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2016 and the next is 2026. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$20,000-$45,000/yr penalty if over emissions cap",
                        "cost_low": 20000,
                        "cost_high": 45000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 1 cab",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 800,
                        "cost_high": 1400,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 1 elevator cab. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2028",
                        "months_away": 34,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_116": {
        "id": "bldg_116",
        "address": "67-76 Booth St",
        "borough": "Queens",
        "neighborhood": "Forest Hills",
        "units": 128,
        "floors": 8,
        "year_built": 1950,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2016 and the next is 2026. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2027",
                        "months_away": 12,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 12000,
                        "cost_high": 22000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2028",
                        "months_away": 34,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_117": {
        "id": "bldg_117",
        "address": "45 Kew Gardens Road",
        "borough": "Queens",
        "neighborhood": "Kew Gardens",
        "units": 96,
        "floors": 6,
        "year_built": 1939,
        "is_prewar": True,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 1 cab",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 800,
                        "cost_high": 1400,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 1 elevator cab. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2035",
                        "months_away": 108,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2025 and the next is 2035. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_118": {
        "id": "bldg_118",
        "address": "31-85 Crescent St",
        "borough": "Queens",
        "neighborhood": "Astoria",
        "units": 115,
        "floors": 6,
        "year_built": 1960,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 1 cab",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 800,
                        "cost_high": 1400,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 1 elevator cab. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2035",
                        "months_away": 108,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2025 and the next is 2035. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_119": {
        "id": "bldg_119",
        "address": "102-55 67th Drive",
        "borough": "Queens",
        "neighborhood": "Forest Hills",
        "units": 71,
        "floors": 6,
        "year_built": 1952,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 1 cab",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 800,
                        "cost_high": 1400,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 1 elevator cab. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2027",
                        "months_away": 22,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2035",
                        "months_away": 108,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2025 and the next is 2035. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_120": {
        "id": "bldg_120",
        "address": "27110 Grand Central Pkwy",
        "borough": "Queens",
        "neighborhood": "Floral Park",
        "units": 1844,
        "floors": 20,
        "year_built": 1974,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 35000,
                        "cost_high": 65000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 3 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 2400,
                        "cost_high": 4200,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 3 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2026",
                        "months_away": 10,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2030",
                        "months_away": 48,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2020 and the next is 2030. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_121": {
        "id": "bldg_121",
        "address": "2575 Palisade Avenue",
        "borough": "Bronx",
        "neighborhood": "Riverdale",
        "units": 143,
        "floors": 12,
        "year_built": 1957,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2027",
                        "months_away": 22,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2035",
                        "months_away": 108,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2025 and the next is 2035. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_122": {
        "id": "bldg_122",
        "address": "1720 Mayflower Avenue",
        "borough": "Bronx",
        "neighborhood": "Pelham Bay",
        "units": 120,
        "floors": 11,
        "year_built": 1964,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Mitchell Lama",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 12000,
                        "cost_high": 22000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2028",
                        "months_away": 34,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2030",
                        "months_away": 48,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2020 and the next is 2030. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_123": {
        "id": "bldg_123",
        "address": "1041 Pugsley Avenue",
        "borough": "Bronx",
        "neighborhood": "Pelham Bay",
        "units": 132,
        "floors": 15,
        "year_built": 1964,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Mitchell Lama",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2027",
                        "months_away": 12,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2031",
                        "months_away": 60,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2021 and the next is 2031. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
    "bldg_124": {
        "id": "bldg_124",
        "address": "1966 Newbold Avenue",
        "borough": "Bronx",
        "neighborhood": "Parkchester",
        "units": 139,
        "floors": 14,
        "year_built": 1968,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2026",
                        "months_away": 0,
                        "urgency": "HIGH",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2016 and the next is 2026. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                },
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Local Law 11 - FISP Facade Inspection",
                        "due_date": "Feb 2027",
                        "months_away": 12,
                        "urgency": "HIGH",
                        "consequence": "DOB violations + fines from $1,000/month if missed",
                        "cost_low": 22000,
                        "cost_high": 40000,
                        "network_comps": 23,
                        "context": "NYC requires all buildings over 6 stories to have a licensed engineer inspect the exterior facade every 5 years under the Facade Inspection Safety Program (FISP). The engineer files a report classifying the facade as Safe, Safe with Repair and Maintenance Program (SWARMP), or Unsafe. If Unsafe, repairs must begin immediately or the DOB can issue a vacate order. The board should hire a qualified facade engineer at least 12 months before the deadline to allow time for inspection, report preparation, and any required repairs. Sidewalk sheds may be required if unsafe conditions are found, adding significant cost."
                },
                {
                        "law": "Elevator Annual Inspection - 2 cabs",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 1600,
                        "cost_high": 2800,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 2 elevator cabs. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2026",
                        "months_away": 10,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                }
        ],
        "vendor_data": []
},
    "bldg_125": {
        "id": "bldg_125",
        "address": "5601 Riverdale Avenue",
        "borough": "Bronx",
        "neighborhood": "Riverdale",
        "units": 114,
        "floors": 6,
        "year_built": 1954,
        "is_prewar": False,
        "building_class": "D4",
        "building_type": "Coop",
        "managing_agent": "Century Management",
        "board_president": "",
        "subscription_tier": "standard",
        "subscription_since": "2026-02-19",
        "tax_assessment": {
                "assessed_value": 0,
                "market_value": 0,
                "fiscal_year": "FY2026",
                "annual_tax_est": 0,
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
        "last_data_refresh": "2026-02-19",
        "compliance_deadlines": [
                {
                        "law": "Local Law 97 - Carbon Emissions",
                        "due_date": "May 1, 2026",
                        "months_away": 3,
                        "urgency": "HIGH",
                        "consequence": "$45,000-$80,000/yr penalty if over emissions cap",
                        "cost_low": 35000,
                        "cost_high": 75000,
                        "network_comps": 31,
                        "context": "Local Law 97 is NYC's landmark climate legislation that caps carbon emissions for buildings over 25,000 sq ft. Buildings that exceed their cap pay $268 per metric ton of CO2 over the limit every year until compliant. The annual compliance report covering the prior calendar year must be filed with the DOB by May 1st. Buildings should commission an LL97 benchmarking study to determine penalty exposure and what retrofits - better insulation, heat pump upgrades, LED lighting, or renewable energy credits - would reduce or eliminate the fine."
                },
                {
                        "law": "Elevator Annual Inspection - 1 cab",
                        "due_date": "Annual - verify with DOB",
                        "months_away": 6,
                        "urgency": "MEDIUM",
                        "consequence": "Mandatory cab shutdown until re-inspected by DOB",
                        "cost_low": 800,
                        "cost_high": 1400,
                        "network_comps": 89,
                        "context": "NYC requires annual safety inspections of all elevator cabs by a licensed DOB inspector. This building has an estimated 1 elevator cab. If an elevator fails inspection or the inspection lapses, the DOB can order the cab shut down immediately. Confirm inspection dates with your elevator contractor at least 60 days in advance."
                },
                {
                        "law": "Local Law 152 - Gas Piping Inspection",
                        "due_date": "Dec 31, 2029",
                        "months_away": 46,
                        "urgency": "MEDIUM",
                        "consequence": "DOB violations and fines if inspection not filed on time",
                        "cost_low": 2500,
                        "cost_high": 6000,
                        "network_comps": 67,
                        "context": "Local Law 152 requires buildings to have all exposed gas piping inspected by a licensed master plumber every 4 years. The licensed plumber files a Gas Piping System Periodic Inspection Report (GPS1) with the DOB after completing the inspection. If defects are found, they must be corrected and re-inspected before the filing deadline. Boards should hire a licensed master plumber well in advance as inspectors get booked quickly near deadlines."
                },
                {
                        "law": "Local Law 87 - Energy Audit",
                        "due_date": "Dec 2031",
                        "months_away": 60,
                        "urgency": "MEDIUM",
                        "consequence": "$3,000 year one, $5,000/yr thereafter until filed",
                        "cost_low": 12000,
                        "cost_high": 24000,
                        "network_comps": 41,
                        "context": "Local Law 87 requires buildings over 50,000 sq ft to conduct a professional energy audit and retro-commissioning study every 10 years. The last due year was 2021 and the next is 2031. The board should check DOB BIS records to confirm the last filing. The audit covers all building systems and identifies efficiency improvements."
                }
        ],
        "vendor_data": []
},
}
