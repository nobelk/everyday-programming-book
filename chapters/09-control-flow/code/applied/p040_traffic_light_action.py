"""Problem 40 — Traffic-light action

Domain: Engineering. Chapter 9 (Control Flow), conditionals.

Problem
-------
Given the current light, print the instruction for a driver.

Expected output
---------------
Slow down
"""


light = "yellow"
if light == "green":
    print("Go")
elif light == "yellow":
    print("Slow down")
elif light == "red":
    print("Stop")
else:
    print("Unknown signal")
