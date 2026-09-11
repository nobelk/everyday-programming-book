"""Problem 45 — Resistors in series

Domain: Engineering. Chapter 10 (Control Flow), loops.

Problem
-------
Add up four resistor values.

Expected output
---------------
Total resistance: 179 Ohm
"""


resistors_ohm = [10, 22, 47, 100]
total_r = 0
for r in resistors_ohm:
    total_r = total_r + r
print(f"Total resistance: {total_r} Ohm")
