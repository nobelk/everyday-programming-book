"""Exercise 6.4.1 — First letter

Chapter 6 (Data Structures), section 6.4: Strings.

Problem
-------
The program should print the first letter of a city name: T.

Bug type: Logical
-----------------
String indexing starts at 0, so `city[1]` is the second letter ("o"). Use index `0` for the first letter.

The program below is the corrected version.
"""


city = "Tokyo"
first = city[0]
print(first)   # T
