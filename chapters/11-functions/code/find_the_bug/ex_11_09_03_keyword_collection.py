"""Exercise 11.9.3 — Keyword collection

Chapter 11 (Functions), section 11.9: *args and **kwargs.

Problem
-------
This program should print the keyword arguments as a dictionary.

Bug type: Runtime
-----------------
A single star collects positional arguments; keyword arguments need two stars. With one star, the keyword call raises a `TypeError`. Use `**kwargs`.

The program below is the corrected version.
"""


def show_options(**kwargs):
    print(kwargs)

show_options(color="blue", size="large")
# {'color': 'blue', 'size': 'large'}
