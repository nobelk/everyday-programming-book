"""Problem 32 — Classify an animal by number of legs

Domain: Biology. Chapter 9 (Control Flow), conditionals.

Problem
-------
Given leg count, label the animal (0 → snake-like, 2 → biped, 4 → quadruped, 6 → insect, 8 → arachnid).

Expected output
---------------
6 legs → insect
"""


legs = 6
if legs == 0:
    kind = "snake-like"
elif legs == 2:
    kind = "biped"
elif legs == 4:
    kind = "quadruped"
elif legs == 6:
    kind = "insect"
elif legs == 8:
    kind = "arachnid"
else:
    kind = "unknown"
print(f"{legs} legs → {kind}")
