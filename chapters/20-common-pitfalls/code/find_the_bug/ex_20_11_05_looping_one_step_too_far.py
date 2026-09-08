"""Exercise 20.11.5 — Looping one step too far

Chapter 20 (Common Pitfalls), section 20.11: Going past the end of a list.

Problem
-------
This program should print every price in the list.

Bug type: Runtime
-----------------
`index <= len(prices)` lets `index` reach `3`, which is out of range, so the loop raises `IndexError`. Stop with `<` instead of `<=`.

The program below is the corrected version.
"""


prices = [3, 5, 9]
index = 0
while index < len(prices):
    print(prices[index])
    index = index + 1
