"""Exercise 20.15.3 — Rolling for a starting number

Chapter 20 (Common Pitfalls), section 20.15: Forgetting to call a function with parentheses.

Problem
-------
The program should print a fixed starting score produced by a helper.

Bug type: Logical
-----------------
`score = starting_score` stores the function itself, not its result. Add `()` to call it.

The program below is the corrected version.
"""


def starting_score():
    return 100

score = starting_score()
print("You begin with", score, "points")
