"""Advanced problem 26 — Pythagorean Triples (imperative)

Subject: Mathematics. Style: imperative.

Problem
-------
Find all Pythagorean triples `(a, b, c)` with `c ≤ 30`.

Concepts taught
---------------
Nested `for` loops, list mutation (`append`), integer-vs-float check trick.

Expected output
---------------
Found 11 triples:
(3, 4, 5)
(5, 12, 13)
(6, 8, 10)
(7, 24, 25)
(8, 15, 17)
(9, 12, 15)
(10, 24, 26)
(12, 16, 20)
(15, 20, 25)
(18, 24, 30)
(20, 21, 29)
"""


triples = []
for a in range(1, 31):
    for b in range(a, 31):
        c_squared = a * a + b * b
        c = int(c_squared ** 0.5)
        if c * c == c_squared and c <= 30:
            triples.append((a, b, c))

print(f"Found {len(triples)} triples:")
for t in triples:
    print(t)
