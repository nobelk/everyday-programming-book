"""Problem 51 — Rabbit population over 8 generations

Domain: Biology. Chapter 10 (Control Flow), loops.

Problem
-------
Each generation triples the rabbits. Start with 2.

Expected output (last line)
---------------------------
Gen 8: 13122 rabbits
"""


rabbits = 2
for gen in range(1, 9):
    rabbits = rabbits * 3
    print(f"Gen {gen}: {rabbits} rabbits")
