"""Advanced problem 62 — Population Density of Countries (functional)

Subject: Geography. Style: functional.

Problem
-------
Compute population density (people / km²) for several countries, then list those above 300 (densely populated).

Concepts taught
---------------
Numeric literals with underscores, `map` + `filter`, list-comprehension projection.

Expected output
---------------
  Singapore:    8104.40 /km²
 Bangladesh:    1111.41 /km²
     Russia:       8.48 /km²
      India:     425.89 /km²
     Canada:       3.81 /km²

Densely populated: ['Singapore', 'Bangladesh', 'India']
"""


countries = [
    ("Singapore",    5_900_000,    728),
    ("Bangladesh", 165_000_000, 148_460),
    ("Russia",     145_000_000, 17_098_242),
    ("India",    1_400_000_000, 3_287_263),
    ("Canada",      38_000_000, 9_984_670),
]

density = lambda c: (c[0], c[1] / c[2])
densities = list(map(density, countries))
dense = list(filter(lambda d: d[1] > 300, densities))

for name, d in densities:
    print(f"{name:>11}: {d:>10.2f} /km²")
print("\nDensely populated:", [n for n, _ in dense])
