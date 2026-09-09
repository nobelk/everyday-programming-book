"""Exercise 6.6.5 — How many items

Chapter 6 (Data Structures), section 6.6: Lists.

Problem
-------
The program should print how many items are in the shopping list: 3.

Bug type: Logical
-----------------
`len(shopping)` already gives 3; subtracting 1 makes it 2. Remove the `- 1`.

The program below is the corrected version.
"""


shopping = ["milk", "eggs", "bread"]
count = len(shopping)
print(count)   # 3
