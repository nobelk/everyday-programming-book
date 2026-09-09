"""Problem 5 — Electrical power of a bulb

Domain: Engineering. Chapter 6 (Data Structures), variables.

Problem
-------
A bulb runs at 230 V and draws 0.26 A. Compute power using `P = V × I`.

Expected output
---------------
Power: 59.80 W
"""


voltage_v = 230
current_a = 0.26
power_w = voltage_v * current_a
print(f"Power: {power_w:.2f} W")
