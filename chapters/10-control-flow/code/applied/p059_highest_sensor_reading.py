"""Problem 59 — Highest sensor reading

Domain: Engineering. Chapter 10 (Control Flow), loops.

Problem
-------
A strain-gauge produced these micro-strain values — find the maximum.

Expected output
---------------
Peak strain: 170 µε
"""


readings = [120, 135, 142, 160, 158, 170, 165]
peak = 0
for r in readings:
    if r > peak:
        peak = r
print(f"Peak strain: {peak} µε")
