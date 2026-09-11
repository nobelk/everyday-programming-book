"""Advanced problem 45 — Gear Ratio Calculator (imperative)

Subject: Engineering. Style: imperative.

Problem
-------
A bicycle has front sprockets [50, 39, 30] teeth and rear sprockets [11, 13, 17, 21, 26, 32]. For each combination, print the gear ratio and label the gear *high* (≥ 3.0), *medium* (1.5–3.0), or *low*.

Concepts taught
---------------
Nested loops with `if/elif/else`, formatted output with literal padding for alignment.

Expected output
---------------
50T / 11T =  4.55  [HIGH]
50T / 13T =  3.85  [HIGH]
50T / 17T =  2.94  [med ]
50T / 21T =  2.38  [med ]
50T / 26T =  1.92  [med ]
50T / 32T =  1.56  [med ]

39T / 11T =  3.55  [HIGH]
39T / 13T =  3.00  [HIGH]
39T / 17T =  2.29  [med ]
39T / 21T =  1.86  [med ]
39T / 26T =  1.50  [med ]
39T / 32T =  1.22  [low ]

30T / 11T =  2.73  [med ]
30T / 13T =  2.31  [med ]
30T / 17T =  1.76  [med ]
30T / 21T =  1.43  [low ]
30T / 26T =  1.15  [low ]
30T / 32T =  0.94  [low ]
"""


front = [50, 39, 30]
rear  = [11, 13, 17, 21, 26, 32]

for f in front:
    for r in rear:
        ratio = f / r
        if ratio >= 3.0:
            label = "HIGH"
        elif ratio >= 1.5:
            label = "med "
        else:
            label = "low "
        print(f"{f}T / {r}T = {ratio:5.2f}  [{label}]")
    print()
