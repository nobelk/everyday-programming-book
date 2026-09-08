"""Advanced problem 58 — Erosion Rate Over Time (functional)

Subject: Geology. Style: functional.

Problem
-------
A cliff erodes at varying yearly rates measured each decade: [12, 15, 14, 18, 22, 19, 25, 28, 24, 21] mm/yr. Compute the cumulative erosion at each decade end without using `for` loops with mutation.

Concepts taught
---------------
`itertools.accumulate` (a fold producing each intermediate), `map`, `enumerate` with `start`.

Expected output
---------------
Decade  1 ( 10 yr): 12.0 cm total erosion
Decade  2 ( 20 yr): 27.0 cm total erosion
Decade  3 ( 30 yr): 41.0 cm total erosion
Decade  4 ( 40 yr): 59.0 cm total erosion
Decade  5 ( 50 yr): 81.0 cm total erosion
Decade  6 ( 60 yr): 100.0 cm total erosion
Decade  7 ( 70 yr): 125.0 cm total erosion
Decade  8 ( 80 yr): 153.0 cm total erosion
Decade  9 ( 90 yr): 177.0 cm total erosion
Decade 10 (100 yr): 198.0 cm total erosion
"""


from itertools import accumulate

rates_per_decade = [12, 15, 14, 18, 22, 19, 25, 28, 24, 21]
erosion_per_decade = list(map(lambda r: r * 10, rates_per_decade))
cumulative_mm = list(accumulate(erosion_per_decade))

for decade, total in enumerate(cumulative_mm, start=1):
    print(f"Decade {decade:>2} ({decade*10:>3} yr): {total/10:.1f} cm "
          f"total erosion")
