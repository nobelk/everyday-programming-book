"""Exercise 11.5.5 — Mixing names and positions

Chapter 11 (Functions), section 11.5: Keyword Arguments.

Problem
-------
This should compute simple interest (principal times rate times years) as 60.0.

Bug type: Runtime
-----------------
`time=3` is an unexpected keyword the function does not accept, raising a `TypeError`. Pass only the three real parameters.

The program below is the corrected version.
"""


def interest(principal, rate, years):
    return principal * rate * years

print(interest(1000, years=3, rate=0.02))  # 60.0
