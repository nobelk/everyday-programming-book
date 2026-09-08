"""Problem 62 — Celsius ↔ Fahrenheit

Domain: Chemistry. Chapter 10 (Functions), functions.

Problem
-------
Two functions: `c_to_f` and `f_to_c`.

Expected output
---------------
212.0
0.0
"""


def c_to_f(c):
    return c * 9 / 5 + 32

def f_to_c(f):
    return (f - 32) * 5 / 9

print(c_to_f(100))
print(f_to_c(32))
