"""Advanced problem 25 — Statistics: Mean, Median, Mode (functional)

Subject: Mathematics. Style: functional.

Problem
-------
Given test scores `[85, 92, 78, 92, 88, 76, 92, 81, 88, 90]`, compute the mean, median, and mode in a pure-functional style.

Concepts taught
---------------
`reduce`, ternary expression, `sorted` (returns a new list — doesn't mutate), `Counter` as a functional helper.

Expected output
---------------
Mean   = 86.2
Median = 88.0
Mode   = 92
"""


from functools import reduce
from collections import Counter

scores = [85, 92, 78, 92, 88, 76, 92, 81, 88, 90]

mean = reduce(lambda acc, x: acc + x, scores, 0) / len(scores)
sorted_scores = sorted(scores)
n = len(sorted_scores)
median = (sorted_scores[n // 2] if n % 2 == 1
          else (sorted_scores[n // 2 - 1] + sorted_scores[n // 2]) / 2)
mode = Counter(scores).most_common(1)[0][0]

print(f"Mean   = {mean}")
print(f"Median = {median}")
print(f"Mode   = {mode}")
