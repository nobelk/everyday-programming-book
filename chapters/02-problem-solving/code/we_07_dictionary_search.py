"""Example 7 — Finding a word in the dictionary

Chapter 2 (Problem Solving).

Problem
-------
Al-Khwarizmi's golden principle says to break a problem into steps that cannot be simplified further, order them, solve each, and the whole problem is solved. Applying it to "find a word in an English dictionary" gives the steps below — which are exactly a binary search.

Pseudocode
----------
START
  INPUT the word to find
  SET low = first page, high = last page
  WHILE low <= high
    SET middle = the page halfway between low and high
    IF the word is on the middle page
      OUTPUT the page
    IF the word comes before that page alphabetically
      SET high = middle - 1
    ELSE
      SET low = middle + 1
  ENDWHILE
  OUTPUT "not in the dictionary"
END

Notes
-----
Halving the range each time is why looking a word up in a 1000-page dictionary takes about ten checks rather than a thousand. `//` is integer division, so `middle` is always a whole page number.
"""


def find_page(pages, word):
    """Return the index of the page holding `word`, or -1 if it is absent.

    `pages` is a list of alphabetically sorted page contents; each page is a
    list of the words printed on it.
    """
    low = 0
    high = len(pages) - 1

    while low <= high:
        middle = (low + high) // 2
        if word in pages[middle]:
            return middle
        if word < pages[middle][0]:
            high = middle - 1
        else:
            low = middle + 1

    return -1


dictionary = [
    ["ant", "apple", "arch"],
    ["bell", "bird", "brick"],
    ["cloud", "coin", "crow"],
    ["dust", "dwell"],
]

print(find_page(dictionary, "coin"))    # 2
print(find_page(dictionary, "zebra"))   # -1
