"""Problem 28 — Blood-pressure category

Domain: Biology. Chapter 9 (Control Flow), conditionals.

Problem
-------
Using systolic pressure, classify as Low (<90), Normal (<120), Elevated (<130), High (<140), or Hypertensive (≥140).

Expected output
---------------
Systolic 135: High
"""


systolic = 135
if systolic < 90:
    category = "Low"
elif systolic < 120:
    category = "Normal"
elif systolic < 130:
    category = "Elevated"
elif systolic < 140:
    category = "High"
else:
    category = "Hypertensive"
print(f"Systolic {systolic}: {category}")
