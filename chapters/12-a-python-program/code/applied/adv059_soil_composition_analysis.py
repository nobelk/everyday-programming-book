"""Advanced problem 59 — Soil Composition Analysis (imperative)

Subject: Geology. Style: imperative.

Problem
-------
A soil sample is 40% sand, 35% silt, 25% clay by mass. Use the USDA soil triangle classification rules (simplified) to print whether the sample is classified loam, clay loam, etc.

Concepts taught
---------------
Multi-branch `if/elif/else`, chained comparison (`20 <= sand <= 45`), input validation.

Expected output
---------------
Sand=40% Silt=35% Clay=25% → loam
"""


sand, silt, clay = 40, 35, 25
total = sand + silt + clay

if total != 100:
    print(f"WARNING: percentages sum to {total}, not 100.")

if clay >= 40:
    soil_type = "clay"
elif clay >= 27 and 20 <= sand <= 45:
    soil_type = "clay loam"
elif sand >= 70:
    soil_type = "sandy"
elif silt >= 80:
    soil_type = "silty"
else:
    soil_type = "loam"

print(f"Sand={sand}% Silt={silt}% Clay={clay}% → {soil_type}")
