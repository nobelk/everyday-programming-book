"""Example 6 — Hottest city in a weather log

Chapter 2 (Problem Solving).

Problem
-------
Given a log of (city, temperature) readings, report which city was the hottest. This is the running example the book returns to, grown later into a tested program.

Pseudocode
----------
START
  INPUT a list of (city, temperature) readings
  SET hottest = the first reading
  FOR each reading in the list
    IF reading temperature > hottest temperature
      SET hottest = reading
  OUTPUT hottest city
END

Notes
-----
The pattern — start with the first item, then replace it whenever a later item beats it — is the same one the book describes for finding the largest number in a list. Starting from `readings[0]` rather than from zero matters: temperatures can be negative.
"""


readings = [
    ("Tokyo", 33.0),
    ("Dhaka", 36.5),
    ("Oslo", 21.0),
    ("Cairo", 35.0),
]

hottest = readings[0]
for reading in readings:
    if reading[1] > hottest[1]:
        hottest = reading

print(f"Hottest city: {hottest[0]} at {hottest[1]} C")
