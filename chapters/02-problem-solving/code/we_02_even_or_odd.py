"""Example 2 — Even or odd

Chapter 2 (Problem Solving).

Problem
-------
Read a whole number and say whether it is even or odd.

Pseudocode
----------
START
  INPUT number
  IF number mod 2 = 0 THEN
    OUTPUT "Even"
  ELSE
    OUTPUT "Odd"
  ENDIF
END

Notes
-----
`%` is the modulus operator: it gives the remainder. A number is even exactly when dividing it by 2 leaves no remainder. Note the two different operators — `%` for the remainder, `==` to compare.
"""


number = int(input("Number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
