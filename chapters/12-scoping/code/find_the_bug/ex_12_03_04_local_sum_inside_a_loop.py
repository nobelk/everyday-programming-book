"""Exercise 12.3.4 — local sum inside a loop

Chapter 12 (Scoping), section 12.3: Assignment Inside a Function Usually Creates a Local Variable.

Problem
-------
This program should add up the distances of three trips using a local running total and print 45.

Bug type: Logical
-----------------
The running total should add each distance, but the loop subtracts, giving a negative total. Use addition.

The program below is the corrected version.
"""


distance = 0
trips = [10, 15, 20]

def trip_total():
    distance = 0
    for d in trips:
        distance = distance + d
    return distance

print("Total distance:", trip_total())
