"""Advanced problem 66 — Average Rainfall and Outliers (functional)

Subject: Geography. Style: functional.

Problem
-------
Monthly rainfall (mm) for a year is `[80, 70, 95, 110, 140, 180, 220, 210, 160, 120, 95, 85]`. Compute the annual mean and identify months whose rainfall exceeds 1.25× the mean.

Concepts taught
---------------
`reduce` for the mean, `filter` over `zip`, list-comprehension projection.

Expected output
---------------
Mean rainfall: 130.4 mm
Wettest months: ['Jun', 'Jul', 'Aug']
"""


from functools import reduce

rainfall = [80, 70, 95, 110, 140, 180, 220, 210, 160, 120, 95, 85]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

mean = reduce(lambda acc, x: acc + x, rainfall, 0) / len(rainfall)
threshold = 1.25 * mean
wet_months = list(filter(lambda mp: mp[1] > threshold, zip(months, rainfall)))

print(f"Mean rainfall: {mean:.1f} mm")
print("Wettest months:", [m for m, _ in wet_months])
