"""Exercise 10.10.4 — Lambda with filter

Chapter 10 (Functions), section 10.10: Lambdas.

Problem
-------
This should keep only the even numbers, giving `[2, 4]`.

Bug type: Logical
-----------------
`n % 2 == 1` keeps odd numbers, not even ones. Test `n % 2 == 0` to keep the even numbers.

The program below is the corrected version.
"""


numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda n: n % 2 == 0, numbers))
print(evens)  # [2, 4]
