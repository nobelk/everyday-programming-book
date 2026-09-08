"""Advanced problem 33 — Punnett Square (imperative)

Subject: Biology. Style: imperative.

Problem
-------
Build a Punnett square for a cross between two heterozygous parents (Aa × Aa) and report the genotype ratio.

Concepts taught
---------------
Nested loops, sorting for normalization, dict-counter idiom with `dict.get`.

Expected output
---------------
Children: ['AA', 'aA', 'aA', 'aa']
Ratio:    {'AA': 1, 'aA': 2, 'aa': 1}
"""


parent1 = ["A", "a"]
parent2 = ["A", "a"]

children = []
for g1 in parent1:
    for g2 in parent2:
        # Always put dominant allele first for canonical form
        pair = "".join(sorted([g1, g2], reverse=True))
        children.append(pair)

counts = {}
for c in children:
    counts[c] = counts.get(c, 0) + 1

print("Children:", children)
print("Ratio:   ", counts)
