"""Exercise 5.10.2 — Building a message

Chapter 5 (Data Structures), section 5.10: Variables and Types.

Problem
-------
The program should combine a label and a number into one sentence: "Score: 90".

Bug type: Runtime
-----------------
You cannot concatenate a str and an int, so this raises a `TypeError`. Convert the number with `str()` first.

The program below is the corrected version.
"""


score = 90
message = "Score: " + str(score)
print(message)   # Score: 90
