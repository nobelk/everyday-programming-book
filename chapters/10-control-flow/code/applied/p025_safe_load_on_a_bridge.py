"""Problem 25 — Safe load on a bridge

Domain: Engineering. Chapter 10 (Control Flow), conditionals.

Problem
-------
A footbridge is rated 3 000 kg. Tell a group whether they can cross.

Expected output
---------------
Safe to cross
"""


group_mass_kg = 2750
if group_mass_kg <= 3000:
    print("Safe to cross")
else:
    print("Too heavy")
