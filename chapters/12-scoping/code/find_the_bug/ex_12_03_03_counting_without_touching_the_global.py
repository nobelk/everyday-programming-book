"""Exercise 12.3.3 — counting without touching the global

Chapter 12 (Scoping), section 12.3: Assignment Inside a Function Usually Creates a Local Variable.

Problem
-------
This program should count items in a basket using a local tally and print the count, leaving the global `count` at 0.

Bug type: Runtime
-----------------
The local `count` should be increased by 1 per item, but `count + item` adds a string to an integer and raises `TypeError`. Increment by 1 instead.

The program below is the corrected version.
"""


count = 0
basket = ["apple", "pear", "plum"]

def tally():
    count = 0
    for item in basket:
        count = count + 1
    return count

print("Items:", tally())
