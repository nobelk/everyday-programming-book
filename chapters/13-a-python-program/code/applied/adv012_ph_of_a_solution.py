"""Advanced problem 12 — pH of a Solution (functional)

Subject: Chemistry. Style: functional.

Problem
-------
Given hydrogen-ion concentrations `[H⁺]` of common substances (stomach acid, lemon juice, milk, blood, soap, bleach), compute their pH and classify each as acidic, neutral, or basic.

Concepts taught
---------------
Lambdas, nested ternary in a lambda, list comprehension that destructures tuples.

Expected output
---------------
stomach acid    pH= 1.00  acidic
lemon juice     pH= 2.00  acidic
milk            pH= 7.00  neutral
blood           pH= 7.40  basic
soap            pH=10.00  basic
bleach          pH=13.00  basic
"""


from math import log10

samples = [
    ("stomach acid", 1e-1),
    ("lemon juice",  1e-2),
    ("milk",         1e-7),
    ("blood",        4e-8),
    ("soap",         1e-10),
    ("bleach",       1e-13),
]

ph = lambda h_plus: -log10(h_plus)
classify = lambda p: "acidic" if p < 7 else ("basic" if p > 7 else "neutral")

results = [(name, ph(c), classify(ph(c))) for name, c in samples]

for name, p, label in results:
    print(f"{name:15s} pH={p:5.2f}  {label}")
