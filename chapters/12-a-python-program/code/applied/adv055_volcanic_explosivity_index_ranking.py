"""Advanced problem 55 — Volcanic Explosivity Index Ranking (imperative)

Subject: Geology. Style: imperative.

Problem
-------
Given a dataset of historical eruptions and their VEI ratings, print them sorted by VEI descending, and report the average VEI.

Concepts taught
---------------
Sorting with key + `reverse`, accumulator, division.

Expected output
---------------
VEI 8: Toba ~74000 BCE
VEI 7: Tambora 1815
VEI 6: Krakatoa 1883
VEI 6: Pinatubo 1991
VEI 5: Mt. St. Helens 1980
VEI 4: Eyjafjallajokull 2010

Average VEI: 6.00
"""


eruptions = [
    ("Krakatoa 1883", 6),
    ("Mt. St. Helens 1980", 5),
    ("Pinatubo 1991", 6),
    ("Tambora 1815", 7),
    ("Eyjafjallajokull 2010", 4),
    ("Toba ~74000 BCE", 8),
]

eruptions_sorted = sorted(eruptions, key=lambda e: e[1], reverse=True)

total = 0
for name, vei in eruptions_sorted:
    print(f"VEI {vei}: {name}")
    total += vei
average = total / len(eruptions_sorted)
print(f"\nAverage VEI: {average:.2f}")
