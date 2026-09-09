"""Problem 23 — Acid, base or neutral?

Domain: Chemistry. Chapter 10 (Control Flow), conditionals.

Problem
-------
Given a pH, print "Acidic", "Neutral", or "Basic".

Expected output
---------------
Basic
"""


ph = 8.2
if ph < 7:
    print("Acidic")
elif ph == 7:
    print("Neutral")
else:
    print("Basic")
