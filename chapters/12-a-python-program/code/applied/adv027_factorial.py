"""Advanced problem 27 — Factorial (functional)

Subject: Mathematics. Style: functional.

Problem
-------
Compute the factorial of `n` (up to 10) without loops or mutation.

Concepts taught
---------------
`reduce` to accumulate a product, lambda, identity element (`1`) as the initial accumulator.

Expected output
---------------
0! = 1
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
6! = 720
7! = 5040
8! = 40320
9! = 362880
10! = 3628800
"""


from functools import reduce

factorial = lambda n: reduce(lambda acc, x: acc * x, range(1, n + 1), 1)

for n in range(11):
    print(f"{n}! = {factorial(n)}")
