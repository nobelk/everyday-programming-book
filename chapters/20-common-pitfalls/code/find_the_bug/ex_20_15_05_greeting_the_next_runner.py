"""Exercise 20.15.5 — Greeting the next runner

Chapter 20 (Common Pitfalls), section 20.15: Forgetting to call a function with parentheses.

Problem
-------
The program should print a greeting for the runner.

Bug type: Logical
-----------------
`message = greet_runner` stores the function, so the print shows a function object. Call it with an argument.

The program below is the corrected version.
"""


def greet_runner(name):
    return "Good luck, " + name + "!"

message = greet_runner("Sam")
print(message)
