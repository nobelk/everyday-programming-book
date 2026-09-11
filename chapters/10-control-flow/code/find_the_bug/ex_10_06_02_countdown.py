"""Exercise 10.6.2 — Countdown

Chapter 10 (Control Flow), section 10.6: while Loops.

Problem
-------
This program should count down from 3 to 1 and then print `Liftoff`.

Bug type: Runtime
-----------------
`count += 1` moves away from the stop condition, so `count > 0` never becomes false—an infinite loop. Use `count -= 1` to count down.

The program below is the corrected version.
"""


count = 3

while count > 0:
    print(count)
    count -= 1

print("Liftoff")
