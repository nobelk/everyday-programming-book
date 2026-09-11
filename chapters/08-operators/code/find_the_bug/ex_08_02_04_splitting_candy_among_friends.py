"""Exercise 8.2.4 — Splitting candy among friends

Chapter 8 (Operators), section 8.2: Assignment Operator.

Problem
-------
There are 12 pieces of candy to split evenly among 4 friends. This program should update the count to pieces-per-friend and print `3`.

Bug type: Logical
-----------------
`/=` performs true division and produces `3.0`, a float, instead of the whole number 3. Use floor-division assignment `//=` to keep an integer count of pieces per friend.

The program below is the corrected version.
"""


candy = 12
friends = 4
candy //= friends
print(candy)   # 3
