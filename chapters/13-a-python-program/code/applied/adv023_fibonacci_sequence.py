"""Advanced problem 23 — Fibonacci Sequence (functional)

Subject: Mathematics. Style: functional.

Problem
-------
Generate the first 15 Fibonacci numbers — without mutation — using recursion plus memoization.

Concepts taught
---------------
Recursion, base case, decorator-style memoization (`lru_cache`), pure function, list comprehension.

Expected output
---------------
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
"""


from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

sequence = [fib(i) for i in range(15)]
print(sequence)
