"""Advanced problem 32 — Exponential Population Growth (functional)

Subject: Biology. Style: functional.

Problem
-------
A bacterial colony doubles every 30 minutes. Starting with 50 cells, predict the population after 0, 30, 60, …, 300 minutes.

Concepts taught
---------------
Lambda, list comprehension, formatting with thousands separators (`:,`).

Expected output
---------------
t=  0 min →         50 cells
t= 30 min →        100 cells
t= 60 min →        200 cells
t= 90 min →        400 cells
t=120 min →        800 cells
t=150 min →      1,600 cells
t=180 min →      3,200 cells
t=210 min →      6,400 cells
t=240 min →     12,800 cells
t=270 min →     25,600 cells
t=300 min →     51,200 cells
"""


initial = 50
doubling_min = 30

population = lambda t: initial * 2 ** (t / doubling_min)
times = range(0, 301, 30)
table = [(t, population(t)) for t in times]

for t, p in table:
    print(f"t={t:>3} min → {int(p):>10,} cells")
