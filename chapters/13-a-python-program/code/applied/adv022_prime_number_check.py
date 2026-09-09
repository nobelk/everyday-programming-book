"""Advanced problem 22 — Prime Number Check (functional)

Subject: Mathematics. Style: functional.

Problem
-------
Determine whether each of the numbers `[2, 7, 15, 23, 91, 97]` is prime.

Concepts taught
---------------
Lambda, generator expression in `all`, short-circuit boolean evaluation, `map`.

Expected output
---------------
  2: prime
  7: prime
 15: composite
 23: prime
 91: composite
 97: prime
"""


from math import isqrt

is_prime = lambda n: n > 1 and all(n % d != 0
                                   for d in range(2, isqrt(n) + 1))

numbers = [2, 7, 15, 23, 91, 97]
labelled = list(map(lambda n: (n, is_prime(n)), numbers))

for n, p in labelled:
    print(f"{n:>3}: {'prime' if p else 'composite'}")
