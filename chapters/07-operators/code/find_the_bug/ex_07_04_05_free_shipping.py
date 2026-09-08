"""Exercise 7.4.5 — Free shipping

Chapter 7 (Operators), section 7.4: Boolean Operators.

Problem
-------
Shipping is free if the order is over $50 or the customer is a member. This program should print `True` for a $30 order by a member.

Bug type: Logical
-----------------
Free shipping needs the order over $50 *or* the customer to be a member, but `and` requires both, so a $30 member order returns `False`. Use `or`. (Note short-circuiting: with `or`, once `is_member` is true the result is true regardless of the order total.)

The program below is the corrected version.
"""


order_total = 30
is_member = True
free_shipping = order_total > 50 or is_member
print(free_shipping)   # True
