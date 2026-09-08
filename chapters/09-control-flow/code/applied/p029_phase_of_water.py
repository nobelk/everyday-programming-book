"""Problem 29 — Phase of water

Domain: Physics. Chapter 9 (Control Flow), conditionals.

Problem
-------
Given a temperature at 1 atm, is the water ice, liquid, or steam?

Expected output
---------------
At 105 C water is steam
"""


temp_c = 105
if temp_c <= 0:
    phase = "ice"
elif temp_c < 100:
    phase = "liquid water"
else:
    phase = "steam"
print(f"At {temp_c} C water is {phase}")
