"""Problem 60 — Rainwater collected by a row of cylinders

Domain: Physics / Geography. Chapter 10 (Control Flow), loops.

Problem
-------
Five rain gauges hold different volumes. Print the running total as you empty them.

Expected output
---------------
After gauge 1: total = 120 mL
After gauge 2: total = 205 mL
After gauge 3: total = 345 mL
After gauge 4: total = 440 mL
After gauge 5: total = 550 mL
"""


gauges_ml = [120, 85, 140, 95, 110]
total_ml = 0
for i, v in enumerate(gauges_ml, start=1):
    total_ml = total_ml + v
    print(f"After gauge {i}: total = {total_ml} mL")
