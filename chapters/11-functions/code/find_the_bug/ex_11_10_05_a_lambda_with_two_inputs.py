"""Exercise 11.10.5 — A lambda with two inputs

Chapter 11 (Functions), section 11.10: Lambdas.

Problem
-------
This should make a one-line function that adds two numbers and print 7.

Bug type: Syntax
----------------
Lambda parameters must be separated by a comma, so `lambda a b: a + b` is a `SyntaxError`. Write `lambda a, b: a + b`.

The program below is the corrected version.
"""


add = lambda a, b: a + b

print(add(3, 4))  # 7
