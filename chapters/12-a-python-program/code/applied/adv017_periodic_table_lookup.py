"""Advanced problem 17 — Periodic Table Lookup (imperative)

Subject: Chemistry. Style: imperative.

Problem
-------
Build a mini periodic-table lookup. Given a list of element symbols, print the name and atomic number — and report any symbols that are unknown.

Concepts taught
---------------
Dict-of-tuples, membership test (`in`), tuple unpacking, branching.

Expected output
---------------
H: Hydrogen (Z=1)
Au: Gold (Z=79)
Xx: UNKNOWN
Fe: Iron (Z=26)
C: Carbon (Z=6)
Mg: UNKNOWN
"""


table = {
    "H":  ("Hydrogen", 1),
    "He": ("Helium",   2),
    "Li": ("Lithium",  3),
    "C":  ("Carbon",   6),
    "N":  ("Nitrogen", 7),
    "O":  ("Oxygen",   8),
    "Fe": ("Iron",     26),
    "Au": ("Gold",     79),
}

queries = ["H", "Au", "Xx", "Fe", "C", "Mg"]

for sym in queries:
    if sym in table:
        name, num = table[sym]
        print(f"{sym}: {name} (Z={num})")
    else:
        print(f"{sym}: UNKNOWN")
