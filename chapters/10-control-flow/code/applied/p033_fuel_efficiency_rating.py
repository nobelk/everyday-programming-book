"""Problem 33 — Fuel efficiency rating

Domain: Engineering. Chapter 10 (Control Flow), conditionals.

Problem
-------
A car's km per litre is rated Poor (<10), Average (<15), Good (<20), or Excellent (≥20).

Expected output
---------------
17 km/L → Good
"""


kmpl = 17
if kmpl < 10:
    rating = "Poor"
elif kmpl < 15:
    rating = "Average"
elif kmpl < 20:
    rating = "Good"
else:
    rating = "Excellent"
print(f"{kmpl} km/L → {rating}")
