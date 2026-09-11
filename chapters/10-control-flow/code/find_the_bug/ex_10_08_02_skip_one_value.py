"""Exercise 10.8.2 — Skip one value

Chapter 10 (Control Flow), section 10.8: continue.

Problem
-------
This program should print 1, 2, 4, 5, 6, skipping only 3.

Bug type: Logical
-----------------
`pass` does nothing, so 3 is still printed. To actually skip it, use `continue`.

The program below is the corrected version.
"""


for number in range(1, 7):
    if number == 3:
        continue
    print(number)
