"""Exercise 7.1.5 — A list method

Chapter 7 (Lists), section 7.1: Lists.

Problem
-------
This program removes a finished task from the to-do list.

Bug type: Runtime
-----------------
`list.remove` deletes by *value*, not by index, so `tasks.remove(1)` looks for the value `1` and raises a `ValueError`. To drop the finished task by value, remove `"report"` (or use `del tasks[1]`).

The program below is the corrected version.
"""


tasks = ["email", "report", "lunch"]
tasks.remove("report")
print(tasks)   # ['email', 'lunch']
