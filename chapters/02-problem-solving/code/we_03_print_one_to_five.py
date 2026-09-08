"""Example 3 — Print the numbers 1 to 5

Chapter 2 (Problem Solving).

Problem
-------
Print each of the numbers from 1 to 5 on its own line.

Pseudocode
----------
START
  FOR count = 1 TO 5
    OUTPUT count
  ENDFOR
END

Notes
-----
`range(1, 6)` stops *before* 6, so it produces 1, 2, 3, 4, 5. The pseudocode's `TO 5` includes 5; Python's second argument excludes it. Off-by-one mistakes usually start here.
"""


for count in range(1, 6):
    print(count)
