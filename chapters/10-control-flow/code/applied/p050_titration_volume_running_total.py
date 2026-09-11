"""Problem 50 — Titration volume running total

Domain: Chemistry. Chapter 10 (Control Flow), loops.

Problem
-------
Add drops of base (0.05 mL each) until 25 drops are added; report volume after every 5 drops.

Expected output
---------------
After 5 drops: 0.25 mL
After 10 drops: 0.50 mL
After 15 drops: 0.75 mL
After 20 drops: 1.00 mL
After 25 drops: 1.25 mL
"""


volume_ml = 0
for drop in range(1, 26):
    volume_ml = volume_ml + 0.05
    if drop % 5 == 0:
        print(f"After {drop} drops: {volume_ml:.2f} mL")
