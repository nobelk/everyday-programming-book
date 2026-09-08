"""Exercise 9.1.3 — Independent checks that should be alternatives

Chapter 9 (Control Flow), section 9.1: if, elif, else.

Problem
-------
A water sample's pH should be labelled once: acidic, neutral, or basic. With pH 6.0 it should print only `Acidic`.

Bug type: Logical
-----------------
The second test starts a new `if` instead of chaining with `elif`, so its `else` attaches to the second `if` only; an acidic value (pH 6.0) makes the first `if` print `Acidic` and the second `else` also print `Basic`. Using `elif` makes the three cases mutually exclusive.

The program below is the corrected version.
"""


ph = 6.0

if ph < 7:
    print("Acidic")
elif ph == 7:
    print("Neutral")
else:
    print("Basic")
