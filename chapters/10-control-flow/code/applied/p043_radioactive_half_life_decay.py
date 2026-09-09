"""Problem 43 — Radioactive half-life decay

Domain: Chemistry. Chapter 10 (Control Flow), loops.

Problem
-------
Starting with 1000 atoms, print how many remain after each of 5 half-lives.

Expected output
---------------
After 1 half-lives: 500.0 atoms
After 2 half-lives: 250.0 atoms
After 3 half-lives: 125.0 atoms
After 4 half-lives: 62.5 atoms
After 5 half-lives: 31.25 atoms
"""


atoms = 1000
for half_life in range(1, 6):
    atoms = atoms / 2
    print(f"After {half_life} half-lives: {atoms} atoms")
