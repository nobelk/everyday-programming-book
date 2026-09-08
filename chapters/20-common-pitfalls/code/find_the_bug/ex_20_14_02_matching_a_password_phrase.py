"""Exercise 20.14.2 — Matching a password phrase

Chapter 20 (Common Pitfalls), section 20.14: Using is instead of == for value comparison.

Problem
-------
The program should grant access when the typed phrase equals the stored phrase.

Bug type: Logical
-----------------
The built string is a different object from the stored literal, so `is` returns `False` even though the text matches. Compare values with `==`.

The program below is the corrected version.
"""


stored_phrase = "open sesame"
typed_phrase = " ".join(["open", "sesame"])
if typed_phrase == stored_phrase:
    print("Access granted")
else:
    print("Access denied")
