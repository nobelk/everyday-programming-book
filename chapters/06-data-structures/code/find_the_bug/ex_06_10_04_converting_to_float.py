"""Exercise 6.10.4 — Converting to float

Chapter 6 (Data Structures), section 6.10: Variables and Types.

Problem
-------
The program should turn the text "2.5" into a float and print double it, 5.0.

Bug type: Runtime
-----------------
`int("2.5")` raises a `ValueError` because the text is not a whole number. Use `float()` to convert it.

The program below is the corrected version.
"""


weight_text = "2.5"
weight = float(weight_text)
print(weight * 2)   # 5.0
