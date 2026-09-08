"""Problem 71 — Heart-rate training zone

Domain: Biology. Chapter 10 (Functions), functions.

Problem
-------
Zone 2 is 60–70% of max. Return the (low, high) bpm.

Expected output
---------------
(123.0, 143.5)
"""


def zone_2(age_years):
    max_hr = 220 - age_years
    return (0.60 * max_hr, 0.70 * max_hr)

print(zone_2(15))
