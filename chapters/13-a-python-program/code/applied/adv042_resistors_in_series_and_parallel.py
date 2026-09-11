"""Advanced problem 42 — Resistors in Series and Parallel (functional)

Subject: Engineering. Style: functional.

Problem
-------
Given resistor values `[10, 22, 47, 100]` Ω, compute the total resistance if they are wired in series, and again if wired in parallel.

Concepts taught
---------------
Two different folds over the same list (sum vs. reciprocal-sum), lambda.

Expected output
---------------
Series:   179 Ω
Parallel: 5.658 Ω
"""


from functools import reduce

resistors = [10, 22, 47, 100]

series = reduce(lambda acc, r: acc + r, resistors, 0)
parallel = 1 / reduce(lambda acc, r: acc + 1.0 / r, resistors, 0.0)

print(f"Series:   {series} Ω")
print(f"Parallel: {parallel:.3f} Ω")
