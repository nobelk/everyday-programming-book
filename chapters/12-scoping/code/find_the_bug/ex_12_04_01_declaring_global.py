"""Exercise 12.4.1 — declaring global

Chapter 12 (Scoping), section 12.4: Using global.

Problem
-------
This program should use `global` so `visitors` is increased by the function, and print 1.

Bug type: Runtime
-----------------
Without a `global` declaration, assigning `visitors` makes it local, so reading it on the right-hand side raises `UnboundLocalError`. Declare `global visitors` so the module-level variable is updated.

The program below is the corrected version.
"""


visitors = 0

def arrive():
    global visitors
    visitors = visitors + 1

arrive()
print("Visitors:", visitors)
