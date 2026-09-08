"""Problem 55 — Large-population countries

Domain: Geography. Chapter 9 (Control Flow), loops.

Problem
-------
From a small list, print only countries with more than 100 million people.

Expected output
---------------
India: 1428 million
USA: 334 million
Brazil: 216 million
Japan: 124 million
"""


populations_millions = {
    "India": 1428, "USA": 334, "Sri Lanka": 22,
    "Nepal": 30, "Brazil": 216, "Japan": 124,
}
for country, pop in populations_millions.items():
    if pop > 100:
        print(f"{country}: {pop} million")
