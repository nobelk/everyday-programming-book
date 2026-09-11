"""Problem 35 — Northern or southern hemisphere?

Domain: Geography. Chapter 10 (Control Flow), conditionals.

Problem
-------
Positive latitude → northern; negative → southern; 0 → equator.

Expected output
---------------
Southern hemisphere
"""


latitude = -23.5
if latitude > 0:
    print("Northern hemisphere")
elif latitude < 0:
    print("Southern hemisphere")
else:
    print("On the equator")
