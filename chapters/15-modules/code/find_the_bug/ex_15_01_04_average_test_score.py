"""Exercise 15.1.4 — Average test score

Chapter 15 (Modules), section 15.1: Python Standard Library.

Problem
-------
This program should print the average of four test scores using the statistics module.

Bug type: Runtime
-----------------
The module was imported as `statistics`, but the call uses `statistic` (missing the final `s`), raising `NameError`. Use the same name in the call that you used in the import.

The program below is the corrected version.
"""


import statistics

scores = [80, 90, 100, 70]
average = statistics.mean(scores)
print(statistics.mean(scores))   # 85
