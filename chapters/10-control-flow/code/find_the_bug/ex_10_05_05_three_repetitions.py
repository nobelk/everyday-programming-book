"""Exercise 10.5.5 — Three repetitions

Chapter 10 (Control Flow), section 10.5: range.

Problem
-------
This program should print `Hello` exactly three times.

Bug type: Logical
-----------------
`range(3)` runs three times, but the extra `print(count)` also prints the index each pass, which was not intended. Removing that line prints `Hello` three times.

The program below is the corrected version.
"""


for count in range(3):
    print("Hello")
