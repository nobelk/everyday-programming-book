"""Problem 26 — Earthquake severity

Domain: Geology. Chapter 10 (Control Flow), conditionals.

Problem
-------
Classify a Richter magnitude as Minor (<4), Light (<5), Moderate (<6), Strong (<7), Major (<8), or Great (≥8).

Expected output
---------------
Magnitude 6.3: Strong
"""


magnitude = 6.3
if magnitude < 4:
    level = "Minor"
elif magnitude < 5:
    level = "Light"
elif magnitude < 6:
    level = "Moderate"
elif magnitude < 7:
    level = "Strong"
elif magnitude < 8:
    level = "Major"
else:
    level = "Great"
print(f"Magnitude {magnitude}: {level}")
