"""Exercise 11.2.2 — the local shadow should win inside

Chapter 11 (Scoping), section 11.2: A Local Variable Can Hide a Global Variable.

Problem
-------
Inside `convert()`, a local `factor` should shadow the global `factor` so the function multiplies by 1000. The program should print 5000.

Bug type: Logical
-----------------
To convert kilometers to meters you multiply by 1000; the code divides instead, so it shrinks the value. Use multiplication with the local `factor`.

The program below is the corrected version.
"""


factor = 1

def convert(kilometers):
    factor = 1000
    return kilometers * factor

print("Meters:", convert(5))
