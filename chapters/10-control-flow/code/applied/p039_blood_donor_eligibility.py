"""Problem 39 — Blood-donor eligibility

Domain: Biology. Chapter 10 (Control Flow), conditionals.

Problem
-------
Must be at least 17 years old AND weigh at least 50 kg.

Expected output
---------------
Eligible to donate
"""


age_years = 18
mass_kg = 55
if age_years >= 17 and mass_kg >= 50:
    print("Eligible to donate")
else:
    print("Not eligible")
