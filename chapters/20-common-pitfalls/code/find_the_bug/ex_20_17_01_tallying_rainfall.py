"""Exercise 20.17.1 — Tallying rainfall

Chapter 20 (Common Pitfalls), section 20.17: Changing a global variable inside a function by accident.

Problem
-------
The program should add today's rainfall to the running total and print it.

Bug type: Runtime
-----------------
Assigning to `total_rain` inside the function makes it local, so reading it on the right raises `UnboundLocalError`. Declare it `global`.

The program below is the corrected version.
"""


total_rain = 0.0

def add_rain(today):
    global total_rain
    total_rain = total_rain + today

add_rain(1.2)
print("Total rainfall:", total_rain)
