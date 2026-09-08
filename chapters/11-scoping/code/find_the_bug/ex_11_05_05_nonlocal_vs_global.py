"""Exercise 11.5.5 — nonlocal vs global

Chapter 11 (Scoping), section 11.5: Using nonlocal in Nested Functions.

Problem
-------
This program counts how many times a nested function runs using `nonlocal` on the enclosing `times`, and should print 2.

Bug type: Runtime
-----------------
`times` lives in the enclosing function, not the module, so `global times` cannot find it and raises `NameError` at call time. Use `nonlocal` to target the enclosing scope.

The program below is the corrected version.
"""


def make_logger():
    times = 0

    def log():
        nonlocal times
        times += 1
        return times

    return log

log = make_logger()
log()
print("Times:", log())
