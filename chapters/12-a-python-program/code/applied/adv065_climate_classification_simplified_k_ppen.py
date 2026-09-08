"""Advanced problem 65 — Climate Classification (Simplified Köppen) (imperative)

Subject: Geography. Style: imperative.

Problem
-------
Given annual average temperature (°C) and rainfall (mm), assign a simplified climate label.

Concepts taught
---------------
Multi-branch `if/elif/else` with compound conditions using `and`.

Expected output
---------------
     Cairo: T=22°C P=25mm → Hot desert
    Mumbai: T=27°C P=2200mm → Tropical wet
    London: T=10°C P=600mm → Temperate
    Moscow: T=5°C P=700mm → Cold temperate
 Reykjavik: T=4°C P=800mm → Cold temperate
 Singapore: T=27°C P=2500mm → Tropical wet
"""


locations = [
    ("Cairo",    22, 25),
    ("Mumbai",   27, 2200),
    ("London",   10, 600),
    ("Moscow",    5, 700),
    ("Reykjavik", 4, 800),
    ("Singapore",27, 2500),
]

for name, T, P in locations:
    if T >= 18 and P >= 1500:
        label = "Tropical wet"
    elif T >= 18 and P < 250:
        label = "Hot desert"
    elif T < 0:
        label = "Polar"
    elif T < 10:
        label = "Cold temperate"
    elif P < 400:
        label = "Semi-arid"
    else:
        label = "Temperate"
    print(f"{name:>10}: T={T}°C P={P}mm → {label}")
