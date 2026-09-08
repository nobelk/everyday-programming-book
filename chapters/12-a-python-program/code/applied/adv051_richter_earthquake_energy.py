"""Advanced problem 51 — Richter Earthquake Energy (imperative)

Subject: Geology. Style: imperative.

Problem
-------
The energy released by an earthquake of magnitude M is `E = 10^(1.5 M + 4.8)` joules. Print the energy for several quakes and compare each to the magnitude-4 reference.

Concepts taught
---------------
Loop with formatted output, derived comparison multiple.

Expected output
---------------
M=3.0    Tremor: E=2.00e+09 J  (       0× M4)
M=4.0     Light: E=6.31e+10 J  (       1× M4)
M=5.5  Moderate: E=1.12e+13 J  (     178× M4)
M=6.7    Strong: E=7.08e+14 J  (  11,220× M4)
M=8.5     Great: E=3.55e+17 J  (5,623,413× M4)
"""


quakes = [
    ("Tremor",  3.0),
    ("Light",   4.0),
    ("Moderate",5.5),
    ("Strong",  6.7),
    ("Great",   8.5),
]

reference = 10 ** (1.5 * 4.0 + 4.8)
for label, M in quakes:
    energy = 10 ** (1.5 * M + 4.8)
    multiple = energy / reference
    print(f"M={M:>3.1f} {label:>9}: E={energy:.2e} J  ({multiple:>8,.0f}× M4)")
