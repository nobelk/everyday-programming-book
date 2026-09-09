"""Exercise 12.5.1 — nonlocal counter

Chapter 12 (Scoping), section 12.5: Using nonlocal in Nested Functions.

Problem
-------
This program builds a counter with a nested function. `nonlocal` should let `increment()` change the enclosing `count`, so the two calls print 1 then 2.

Bug type: Runtime
-----------------
Assigning `count` inside `increment()` makes it local, so `count + 1` reads a local with no value — `UnboundLocalError`. Declare `nonlocal count` to target the enclosing variable.

The program below is the corrected version.
"""


def make_counter():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        return count

    return increment

counter = make_counter()
print(counter())
print(counter())
