"""Exercise 20.12.1 — Building a shopping list

Chapter 20 (Common Pitfalls), section 20.12: Using parentheses instead of brackets for lists.

Problem
-------
This program should make a list of groceries and add one more item.

Bug type: Runtime
-----------------
Parentheses create a tuple, which has no `append` method, so the call raises `AttributeError`. Use square brackets to make a list.

The program below is the corrected version.
"""


groceries = ["milk", "bread", "eggs"]
groceries.append("butter")
print(groceries)
