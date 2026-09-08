"""Exercise 10.10.1 — Lambda syntax

Chapter 10 (Functions), section 10.10: Lambdas.

Problem
-------
This program should make a one-line function that squares a number and print 25.

Bug type: Syntax
----------------
A lambda body is a single expression and cannot contain `return`, so `lambda x: return x * x` is a `SyntaxError`. Drop the `return`.

The program below is the corrected version.
"""


square = lambda x: x * x

print(square(5))  # 25
