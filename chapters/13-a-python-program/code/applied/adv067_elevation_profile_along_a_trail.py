"""Advanced problem 67 — Elevation Profile Along a Trail (imperative)

Subject: Geography. Style: imperative.

Problem
-------
A hiking trail's elevations (m) at 1-km intervals are [300, 350, 410, 480, 470, 520, 600, 580, 510, 450]. Compute the total ascent and descent over the trail.

Concepts taught
---------------
Loop with `range(1, n)` for pairwise differences, two parallel accumulators.

Expected output
---------------
Total ascent:  310 m
Total descent: 160 m
Net elevation: 150 m
"""


elevations = [300, 350, 410, 480, 470, 520, 600, 580, 510, 450]

ascent = 0
descent = 0
for i in range(1, len(elevations)):
    diff = elevations[i] - elevations[i - 1]
    if diff > 0:
        ascent += diff
    else:
        descent -= diff   # accumulate as positive

print(f"Total ascent:  {ascent} m")
print(f"Total descent: {descent} m")
print(f"Net elevation: {elevations[-1] - elevations[0]} m")
