"""Exercise 20.18.1 — Saving a shopping list

Chapter 20 (Common Pitfalls), section 20.18: Forgetting to close a file.

Problem
-------
This program should write the shopping list to a file and leave no file handle open.

Bug type: Logical
-----------------
The file is opened but never closed, so the handle leaks and buffered data may not flush. Use a `with` block, which closes automatically.

The program below is the corrected version.
"""


groceries = "milk\neggs\nbread\n"
with open("groceries.txt", "w") as list_file:
    list_file.write(groceries)
print("Shopping list saved")
