"""Advanced problem 53 — Mohs Hardness Comparison (imperative)

Subject: Geology. Style: imperative.

Problem
-------
Given a list of mineral hardnesses, sort them and identify which can scratch the others (any mineral can scratch one with strictly lower hardness).

Concepts taught
---------------
`sorted` with key, generator expression with `next`, list comprehension as a filter.

Expected output
---------------
Hardness ranking (soft → hard):
   1  Talc
   2  Gypsum
   3  Calcite
   4  Fluorite
   5  Apatite
   7  Quartz
   8  Topaz
  10  Diamond

Calcite can scratch: ['Talc', 'Gypsum']
"""


minerals = [("Talc", 1), ("Gypsum", 2), ("Calcite", 3),
            ("Fluorite", 4), ("Apatite", 5), ("Quartz", 7),
            ("Topaz", 8), ("Diamond", 10)]

minerals_sorted = sorted(minerals, key=lambda m: m[1])

print("Hardness ranking (soft → hard):")
for name, h in minerals_sorted:
    print(f"  {h:>2}  {name}")

target = "Calcite"
target_h = next(h for n, h in minerals_sorted if n == target)
scratched_by_target = [n for n, h in minerals_sorted if h < target_h]
print(f"\n{target} can scratch: {scratched_by_target}")
