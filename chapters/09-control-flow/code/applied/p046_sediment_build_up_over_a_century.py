"""Problem 46 — Sediment build-up over a century

Domain: Geology. Chapter 9 (Control Flow), loops.

Problem
-------
A lake bed gains 2 mm of sediment per year. Total in 100 years?

Expected output
---------------
Total sediment in 100 years: 200 mm
"""


total_mm = 0
for year in range(1, 101):
    total_mm = total_mm + 2
print(f"Total sediment in 100 years: {total_mm} mm")
