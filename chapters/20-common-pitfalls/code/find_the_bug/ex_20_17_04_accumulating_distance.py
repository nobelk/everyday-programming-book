"""Exercise 20.17.4 — Accumulating distance

Chapter 20 (Common Pitfalls), section 20.17: Changing a global variable inside a function by accident.

Problem
-------
This program should add a new leg of a trip to the total distance traveled.

Bug type: Runtime
-----------------
Assigning `distance_km` inside `drive` makes it local, so the read raises `UnboundLocalError`. Add `global distance_km`.

The program below is the corrected version.
"""


distance_km = 0

def drive(leg):
    global distance_km
    distance_km = distance_km + leg

drive(45)
print("Distance:", distance_km)
