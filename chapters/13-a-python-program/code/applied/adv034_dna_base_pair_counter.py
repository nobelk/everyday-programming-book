"""Advanced problem 34 — DNA Base-Pair Counter (functional)

Subject: Biology. Style: functional.

Problem
-------
Given a DNA strand string, count each base (A, T, G, C) and compute the GC-content percentage.

Concepts taught
---------------
`reduce` over a string, dict comprehension, lambda with conditional expression.

Expected output
---------------
Counts:     {'A': 5, 'T': 5, 'G': 6, 'C': 6}
GC content: 54.55%
"""


from functools import reduce

strand = "AGCTTAGCGCGTAACGTTAGCC"

count = lambda base: reduce(lambda acc, b: acc + (1 if b == base else 0),
                            strand, 0)
counts = {b: count(b) for b in "ATGC"}
gc_percent = (counts["G"] + counts["C"]) / len(strand) * 100

print("Counts:    ", counts)
print(f"GC content: {gc_percent:.2f}%")
