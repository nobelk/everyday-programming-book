"""Exercise 18.1.5 — Counting change

Chapter 18 (Bugs), section 18.1: Syntax Bugs.

Problem
-------
This program should print each coin value in a small pile of change.

Bug type: Syntax
----------------
The `print` line is not indented under the `for`, so Python raises an `IndentationError` because a loop body is expected. Indenting the line by four spaces puts it inside the loop.

The program below is the corrected version.
"""


coins = [25, 10, 5, 1]
for coin in coins:
    print(coin)
