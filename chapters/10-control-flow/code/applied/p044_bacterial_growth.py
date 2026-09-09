"""Problem 44 — Bacterial growth

Domain: Biology. Chapter 10 (Control Flow), loops.

Problem
-------
A bacterium divides every 20 min. Starting with 1, how many are there after 6 divisions?

Expected output (final line)
----------------------------
Division 6: 64 bacteria
"""


bacteria = 1
for division in range(1, 7):
    bacteria = bacteria * 2
    print(f"Division {division}: {bacteria} bacteria")
