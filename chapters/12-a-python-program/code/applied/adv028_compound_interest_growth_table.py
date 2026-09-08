"""Advanced problem 28 — Compound Interest Growth Table (imperative)

Subject: Mathematics. Style: imperative.

Problem
-------
A bank pays 6% interest per year, compounded annually. Print the balance for the first 10 years on an initial deposit of $1,000.

Concepts taught
---------------
Mutating accumulator over a `for` loop, formatted numeric output with width specifiers.

Expected output
---------------
Year  0: $   1000.00
Year  1: $   1060.00
Year  2: $   1123.60
Year  3: $   1191.02
Year  4: $   1262.48
Year  5: $   1338.23
Year  6: $   1418.52
Year  7: $   1503.63
Year  8: $   1593.85
Year  9: $   1689.48
Year 10: $   1790.85
"""


principal = 1000.0
rate = 0.06
years = 10

balance = principal
print(f"Year  0: ${balance:>10.2f}")
for year in range(1, years + 1):
    balance = balance * (1 + rate)
    print(f"Year {year:>2}: ${balance:>10.2f}")
