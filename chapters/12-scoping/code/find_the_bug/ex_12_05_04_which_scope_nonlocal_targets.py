"""Exercise 12.5.4 — which scope nonlocal targets

Chapter 12 (Scoping), section 12.5: Using nonlocal in Nested Functions.

Problem
-------
This program steps a value upward by 5 each call using `nonlocal`, and should print 5 then 10.

Bug type: Runtime
-----------------
The first call uses `steper()`, a misspelling of `stepper`, so Python raises `NameError`. Use the correct name.

The program below is the corrected version.
"""


def make_stepper():
    position = 0

    def step():
        nonlocal position
        position += 5
        return position

    return step

stepper = make_stepper()
print(stepper())
print(stepper())
