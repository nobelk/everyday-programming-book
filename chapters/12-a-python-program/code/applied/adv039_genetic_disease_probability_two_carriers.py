"""Advanced problem 39 — Genetic Disease Probability (Two Carriers) (imperative)

Subject: Biology. Style: imperative.

Problem
-------
If both parents are carriers (`Aa`) of a recessive trait, compute the probability that 0, 1, 2, or 3 of their three children show the trait (`aa`, probability 1/4 per child).

Concepts taught
---------------
Binomial distribution, `math.comb`, looping with formatted output.

Expected output
---------------
Both parents are carriers (Aa). With 3 children:
  P(exactly 0 affected) = 0.4219
  P(exactly 1 affected) = 0.4219
  P(exactly 2 affected) = 0.1406
  P(exactly 3 affected) = 0.0156
"""


from math import comb

p_affected = 0.25
n_kids = 3

print(f"Both parents are carriers (Aa). With {n_kids} children:")
for k in range(n_kids + 1):
    prob = comb(n_kids, k) * (p_affected ** k) * ((1 - p_affected) ** (n_kids - k))
    print(f"  P(exactly {k} affected) = {prob:.4f}")
