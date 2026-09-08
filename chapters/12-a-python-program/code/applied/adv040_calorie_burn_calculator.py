"""Advanced problem 40 — Calorie Burn Calculator (functional)

Subject: Biology. Style: functional.

Problem
-------
Given a person of 65 kg doing several activities (walking 3.5 MET, cycling 8 MET, running 9.8 MET, swimming 6 MET) for 30 minutes each, compute total calories burned. Formula: `kcal = MET × weight_kg × hours`.

Concepts taught
---------------
`map` + `reduce` pipeline, lambda capturing constants by closure.

Expected output
---------------
  walking:  113.8 kcal
  cycling:  260.0 kcal
  running:  318.5 kcal
 swimming:  195.0 kcal
    TOTAL:  887.2 kcal
"""


from functools import reduce

weight_kg = 65
duration_hr = 0.5
activities = [("walking", 3.5), ("cycling", 8.0),
              ("running", 9.8), ("swimming", 6.0)]

burn = lambda met: met * weight_kg * duration_hr
per_activity = list(map(lambda a: (a[0], burn(a[1])), activities))
total = reduce(lambda acc, x: acc + x[1], per_activity, 0.0)

for name, kcal in per_activity:
    print(f"{name:>9}: {kcal:6.1f} kcal")
print(f"{'TOTAL':>9}: {total:6.1f} kcal")
