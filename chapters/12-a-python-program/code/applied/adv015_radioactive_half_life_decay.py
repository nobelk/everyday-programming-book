"""Advanced problem 15 — Radioactive Half-Life Decay (imperative)

Subject: Chemistry. Style: imperative.

Problem
-------
Carbon-14 has a half-life of 5730 years. Given an artifact that starts with 100 g of C-14, print the remaining mass every 5730 years for 6 half-lives, and stop early if less than 1 g remains.

Concepts taught
---------------
`while` loop with multiple counters, `break`, conditional early exit.

Expected output
---------------
Year      0: 100.00 g
Year   5730:  50.00 g
Year  11460:  25.00 g
Year  17190:  12.50 g
Year  22920:   6.25 g
Year  28650:   3.12 g
"""


half_life = 5730
mass = 100.0
year = 0
half_lives_passed = 0

while half_lives_passed < 6:
    print(f"Year {year:>6}: {mass:6.2f} g")
    if mass < 1.0:
        print("Below 1 g — stopping early.")
        break
    mass = mass / 2.0
    year += half_life
    half_lives_passed += 1
