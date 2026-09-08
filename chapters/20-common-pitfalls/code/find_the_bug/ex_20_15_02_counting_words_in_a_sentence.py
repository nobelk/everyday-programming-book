"""Exercise 20.15.2 — Counting words in a sentence

Chapter 20 (Common Pitfalls), section 20.15: Forgetting to call a function with parentheses.

Problem
-------
The program should report how many words a sentence contains.

Bug type: Logical
-----------------
`word_count` alone is the function object; it was never called with the sentence. Call it as `word_count(note)`.

The program below is the corrected version.
"""


def word_count(sentence):
    return len(sentence.split())

note = "the cat sat on the mat"
print("Words:", word_count(note))
