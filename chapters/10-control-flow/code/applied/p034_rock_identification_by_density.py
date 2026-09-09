"""Problem 34 — Rock identification by density

Domain: Geology. Chapter 10 (Control Flow), conditionals.

Problem
-------
A rock with density <2.5 is likely sedimentary, 2.5–3.0 igneous, above 3.0 metamorphic (very rough rule).

Expected output
---------------
Density 2.8 → Igneous
"""


density = 2.8
if density < 2.5:
    rock = "Sedimentary"
elif density <= 3.0:
    rock = "Igneous"
else:
    rock = "Metamorphic"
print(f"Density {density} → {rock}")
