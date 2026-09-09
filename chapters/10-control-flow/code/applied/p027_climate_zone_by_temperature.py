"""Problem 27 — Climate zone by temperature

Domain: Geography. Chapter 10 (Control Flow), conditionals.

Problem
-------
Given an average annual temperature, label the climate as Polar (<0), Cold (<10), Temperate (<20), or Tropical (≥20).

Expected output
---------------
14 C → Temperate
"""


temp_c = 14
if temp_c < 0:
    zone = "Polar"
elif temp_c < 10:
    zone = "Cold"
elif temp_c < 20:
    zone = "Temperate"
else:
    zone = "Tropical"
print(f"{temp_c} C → {zone}")
