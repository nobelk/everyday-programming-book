"""Advanced problem 20 — Gas Density at STP (functional)

Subject: Chemistry. Style: functional.

Problem
-------
Compute the density (g/L) at STP for several gases using `ρ = M / 22.4` (M = molar mass, 22.4 L/mol at STP).

Concepts taught
---------------
`map`/`filter` chaining, predicate using a free variable from outer scope (air's molar mass).

Expected output
---------------
  H2: 0.090 g/L
  He: 0.179 g/L
  N2: 1.251 g/L
  O2: 1.428 g/L
 CO2: 1.965 g/L

Heavier than air: ['O2', 'CO2']
"""


gases = [("H2", 2.016), ("He", 4.003), ("N2", 28.014),
         ("O2", 31.998), ("CO2", 44.01)]

density = lambda molar_mass: molar_mass / 22.4
densities = list(map(lambda g: (g[0], density(g[1])), gases))
heavier_than_air = list(filter(lambda d: d[1] > density(28.97), densities))

for name, d in densities:
    print(f"{name:>4}: {d:.3f} g/L")
print("\nHeavier than air:", [n for n, _ in heavier_than_air])
