"""Advanced problem 47 — Bridge Load Distribution (imperative)

Subject: Engineering. Style: imperative.

Problem
-------
A simply-supported bridge of span 20 m has loads at distances from the left support: (5 m, 10 kN), (12 m, 15 kN), (18 m, 8 kN). Compute the reactions at the left and right supports using moment balance.

Concepts taught
---------------
Two parallel accumulators inside one loop, simple statics application.

Expected output
---------------
Total load:     33.00 kN
Left reaction:  14.30 kN
Right reaction: 18.70 kN
"""


span = 20.0
loads = [(5.0, 10.0), (12.0, 15.0), (18.0, 8.0)]

moment_about_left = 0.0
total_load = 0.0
for distance, force in loads:
    moment_about_left += distance * force
    total_load += force

R_right = moment_about_left / span
R_left = total_load - R_right

print(f"Total load:     {total_load:.2f} kN")
print(f"Left reaction:  {R_left:.2f} kN")
print(f"Right reaction: {R_right:.2f} kN")
