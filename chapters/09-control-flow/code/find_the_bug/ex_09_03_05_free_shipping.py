"""Exercise 9.3.5 — Free shipping

Chapter 9 (Control Flow), section 9.3: Logical Operators.

Problem
-------
Free shipping applies when the cart total is at least 50 or the customer is a member. A $30 order from a member should print `Free shipping`.

Bug type: Logical
-----------------
Free shipping should apply when *either* condition holds, but `and` requires both, so a member with a $30 order is wrongly charged. Using `or` matches the rule.

The program below is the corrected version.
"""


total = 30
is_member = True

if total >= 50 or is_member:
    print("Free shipping")
else:
    print("Pay shipping")
# expected: Free shipping
