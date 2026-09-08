"""Example 4 — Greatest common divisor, Euclid's algorithm

Chapter 2 (Problem Solving).

Problem
-------
Find the greatest common divisor of two numbers. For 48 and 18 the answer is 6: 48 mod 18 = 12, 18 mod 12 = 6, 12 mod 6 = 0, so the last non-zero remainder is 6.

Pseudocode
----------
START
  INPUT a
  INPUT b

  WHILE b != 0
    SET temp = b
    SET b = a mod b
    SET a = temp
  ENDWHILE

  OUTPUT a
END

Notes
-----
The loop keeps replacing the pair `(a, b)` with `(b, a mod b)`. Every step makes the second number smaller, so the loop must end, and it ends holding the greatest common divisor.
"""


def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


print(gcd(48, 18))   # 6
print(gcd(60, 48))   # 12
