"""Exercise 11.9.5 — Order of args and kwargs

Chapter 11 (Functions), section 11.9: *args and **kwargs.

Problem
-------
This should print both the positional tuple and the keyword dictionary.

Bug type: Syntax
----------------
`**kwargs` must come after `*args` in the definition, so `def collect(**kwargs, *args)` is a `SyntaxError`. Put `*args` first.

The program below is the corrected version.
"""


def collect(*args, **kwargs):
    print(args)
    print(kwargs)

collect(1, 2, unit="cm")
