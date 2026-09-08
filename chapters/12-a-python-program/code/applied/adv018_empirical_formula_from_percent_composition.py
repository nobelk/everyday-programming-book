"""Advanced problem 18 — Empirical Formula from Percent Composition (functional)

Subject: Chemistry. Style: functional.

Problem
-------
A compound is 40.0% C, 6.7% H, 53.3% O by mass. Find its empirical formula by dividing each percent by the element's atomic mass and then by the smallest result.

Concepts taught
---------------
Dict comprehension, `reduce` to find a min, `str.join` with a generator expression.

Expected output
---------------
Empirical formula: CH2O
"""


from functools import reduce

percents = {"C": 40.0, "H": 6.7, "O": 53.3}
masses   = {"C": 12.011, "H": 1.008, "O": 15.999}

moles = {el: percents[el] / masses[el] for el in percents}
smallest = reduce(lambda acc, v: min(acc, v), moles.values(), float("inf"))
ratios = {el: round(moles[el] / smallest) for el in moles}

formula = "".join(f"{el}{n if n > 1 else ''}" for el, n in ratios.items())
print("Empirical formula:", formula)
