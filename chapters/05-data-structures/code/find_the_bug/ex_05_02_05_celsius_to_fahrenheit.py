"""Exercise 5.2.5 — Celsius to Fahrenheit

Chapter 5 (Data Structures), section 5.2: float.

Problem
-------
The program converts 100.0 degrees Celsius to Fahrenheit and should print 212.0.

Bug type: Logical
-----------------
Operator precedence makes `celsius * 9 / 5 - 32` subtract 32 instead of adding it, and the +32 must come after the multiply/divide. Add parentheses or use `+ 32`: the formula is `celsius * 9 / 5 + 32`.

The program below is the corrected version.
"""


celsius = 100.0
fahrenheit = celsius * 9 / 5 + 32
print(fahrenheit)   # 212.0
