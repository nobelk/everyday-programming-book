# Chapter 2 — Problem Solving: Worked Examples

Chapter 2 teaches a method rather than a language feature: break a problem into steps small enough that each one is obvious, put the steps in order, solve them one at a time. The chapter writes its examples in **pseudocode** — plain words with the shape of a program — so that you can think about the steps before worrying about punctuation.

Each example below shows the pseudocode from the chapter and the Python it becomes. Read the pseudocode first and try to write the Python yourself; the point of the chapter is the translation, not the answer.

**7 examples.** The programs are also available as runnable files under [`code/`](code).

## Al-Khwarizmi's golden principle

Every example here follows the five steps the chapter takes from al-Khwarizmi, the ninth-century mathematician whose Latinised name gave us the word *algorithm*:

1. Break the problem into elemental steps — steps that cannot be simplified any further.
2. Arrange the steps in an order, so that each can be solved on its own without disturbing the others.
3. Find a way to solve each step separately. A step simplified as far as it goes usually has an easy solution.
4. Solve the steps, in the right order.
5. When every step is solved, the original problem is solved too.

### Example 1 — Add two numbers

Read two numbers and print their sum. This is the smallest possible example of the three ideas every program is built from — input, a step, output.

**Pseudocode.**

```text
START
  INPUT first number
  INPUT second number
  SET sum = first number + second number
  OUTPUT sum
END
```

**Python.**

```python
first = float(input("First number: "))
second = float(input("Second number: "))

total = first + second
print(total)
```

`input()` always hands back text, so each reading is passed through `float()` before it is added. Adding the raw strings would join them instead: `"2" + "3"` is `"23"`.

> This program waits for you to type a value, so run it from a terminal rather than reading its output here.

<sub>[Runnable file](code/we_01_add_two_numbers.py)</sub>

### Example 2 — Even or odd

Read a whole number and say whether it is even or odd.

**Pseudocode.**

```text
START
  INPUT number
  IF number mod 2 = 0 THEN
    OUTPUT "Even"
  ELSE
    OUTPUT "Odd"
  ENDIF
END
```

**Python.**

```python
number = int(input("Number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

`%` is the modulus operator: it gives the remainder. A number is even exactly when dividing it by 2 leaves no remainder. Note the two different operators — `%` for the remainder, `==` to compare.

> This program waits for you to type a value, so run it from a terminal rather than reading its output here.

<sub>[Runnable file](code/we_02_even_or_odd.py)</sub>

### Example 3 — Print the numbers 1 to 5

Print each of the numbers from 1 to 5 on its own line.

**Pseudocode.**

```text
START
  FOR count = 1 TO 5
    OUTPUT count
  ENDFOR
END
```

**Python.**

```python
for count in range(1, 6):
    print(count)
```

`range(1, 6)` stops *before* 6, so it produces 1, 2, 3, 4, 5. The pseudocode's `TO 5` includes 5; Python's second argument excludes it. Off-by-one mistakes usually start here.

<sub>[Runnable file](code/we_03_print_one_to_five.py)</sub>

### Example 4 — Greatest common divisor, Euclid's algorithm

Find the greatest common divisor of two numbers. For 48 and 18 the answer is 6: 48 mod 18 = 12, 18 mod 12 = 6, 12 mod 6 = 0, so the last non-zero remainder is 6.

**Pseudocode.**

```text
START
  INPUT a
  INPUT b

  WHILE b != 0
    SET temp = b
    SET b = a mod b
    SET a = temp
  ENDWHILE

  OUTPUT a
END
```

**Python.**

```python
def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


print(gcd(48, 18))   # 6
print(gcd(60, 48))   # 12
```

The loop keeps replacing the pair `(a, b)` with `(b, a mod b)`. Every step makes the second number smaller, so the loop must end, and it ends holding the greatest common divisor.

<sub>[Runnable file](code/we_04_gcd_iterative.py)</sub>

### Example 5 — Greatest common divisor, written recursively

The same algorithm, expressed as a function that calls itself instead of looping.

**Python.**

```python
def gcd_recursive(a, b):
    if b == 0:
        return abs(a)
    return gcd_recursive(b, a % b)


print(gcd_recursive(60, 48))   # 12
```

The `if b == 0` branch is the base case — the point at which the function stops calling itself. A recursive function without a base case never finishes. Compare it with the loop above: same algorithm, two ways of writing the repetition.

<sub>[Runnable file](code/we_05_gcd_recursive.py)</sub>

### Example 6 — Hottest city in a weather log

Given a log of (city, temperature) readings, report which city was the hottest. This is the running example the book returns to, grown later into a tested program.

**Pseudocode.**

```text
START
  INPUT a list of (city, temperature) readings
  SET hottest = the first reading
  FOR each reading in the list
    IF reading temperature > hottest temperature
      SET hottest = reading
  OUTPUT hottest city
END
```

**Python.**

```python
readings = [
    ("Tokyo", 33.0),
    ("Dhaka", 36.5),
    ("Oslo", 21.0),
    ("Cairo", 35.0),
]

hottest = readings[0]
for reading in readings:
    if reading[1] > hottest[1]:
        hottest = reading

print(f"Hottest city: {hottest[0]} at {hottest[1]} C")
```

The pattern — start with the first item, then replace it whenever a later item beats it — is the same one the book describes for finding the largest number in a list. Starting from `readings[0]` rather than from zero matters: temperatures can be negative.

<sub>[Runnable file](code/we_06_hottest_city.py)</sub>

### Example 7 — Finding a word in the dictionary

Al-Khwarizmi's golden principle says to break a problem into steps that cannot be simplified further, order them, solve each, and the whole problem is solved. Applying it to "find a word in an English dictionary" gives the steps below — which are exactly a binary search.

**Pseudocode.**

```text
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
```

**Python.**

```python
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
```

Halving the range each time is why looking a word up in a 1000-page dictionary takes about ten checks rather than a thousand. `//` is integer division, so `middle` is always a whole page number.

<sub>[Runnable file](code/we_07_dictionary_search.py)</sub>
