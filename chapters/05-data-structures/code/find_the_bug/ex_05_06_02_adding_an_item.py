"""Exercise 5.6.2 — Adding an item

Chapter 5 (Data Structures), section 5.6: Lists.

Problem
-------
The program should add "grape" to the list and print 4 items in total.

Bug type: Runtime
-----------------
Lists have no `add` method, so this raises an `AttributeError`. Use `append` to add to a list.

The program below is the corrected version.
"""


fruits = ["apple", "banana", "orange"]
fruits.append("grape")
print(len(fruits))   # 4
