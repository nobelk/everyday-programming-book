"""Example 1 — Add two numbers

Chapter 2 (Problem Solving).

Problem
-------
Read two numbers and print their sum. This is the smallest possible example of the three ideas every program is built from — input, a step, output.

Pseudocode
----------
START
  INPUT first number
  INPUT second number
  SET sum = first number + second number
  OUTPUT sum
END

Notes
-----
`input()` always hands back text, so each reading is passed through `float()` before it is added. Adding the raw strings would join them instead: `"2" + "3"` is `"23"`.
"""


first = float(input("First number: "))
second = float(input("Second number: "))

total = first + second
print(total)
