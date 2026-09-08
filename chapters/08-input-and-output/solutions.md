# Chapter 8 — Input and Output: Find the Bug, Solutions

Each solution names the bug type — **syntax**, **runtime**, or **logical** — explains why the original program misbehaved, and shows the corrected program.

Back to [the exercises](find-the-bug.md).

## 8.1 Reading Input and Printing Output

### Solution 8.1.1 — Doubling a recipe

**Bug type:** Logical

`input()` always returns a string, so `cookies * 2` repeats the text (`"1212"`) instead of computing `24`. Convert the input to an `int` before doing arithmetic.

```python
# Assume the user types: 12
cookies = int(input("How many cookies does the recipe make? "))
print(f"Doubled, that is {cookies * 2} cookies.")
```

<sub>[Exercise](find-the-bug.md#exercise-811--doubling-a-recipe) · [Runnable file](code/find_the_bug/ex_08_01_01_doubling_a_recipe.py)</sub>

### Solution 8.1.2 — Average of two test scores

**Bug type:** Logical

Without parentheses, `score1 + score2 / 2` divides only the second score first (operator precedence), giving 125.0 instead of 85.0. Parenthesize the sum before dividing.

```python
# Assume the user types: 80  then  90
score1 = float(input("First test score? "))
score2 = float(input("Second test score? "))
average = (score1 + score2) / 2
print(f"Your average is {average}.")
```

<sub>[Exercise](find-the-bug.md#exercise-812--average-of-two-test-scores) · [Runnable file](code/find_the_bug/ex_08_01_02_average_of_two_test_scores.py)</sub>

### Solution 8.1.3 — Printing a shopping list

**Bug type:** Logical

The `sep` argument controls what goes between the printed items; a single space produces `apple banana cherry`, not the comma-separated list that was wanted. Set `sep=", "`.

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0], fruits[1], fruits[2], sep=", ")
```

<sub>[Exercise](find-the-bug.md#exercise-813--printing-a-shopping-list) · [Runnable file](code/find_the_bug/ex_08_01_03_printing_a_shopping_list.py)</sub>

### Solution 8.1.4 — Saving a temperature reading

**Bug type:** Runtime

The second `open` uses mode `"w"` again, which opens the file for writing (and erases it); calling `f.read()` on a write-mode file raises `io.UnsupportedOperation`. Open it in read mode `"r"` to read the contents back.

```python
with open("reading.txt", "w", encoding="utf-8") as f:
    f.write("Tokyo,36.5\n")

with open("reading.txt", "r", encoding="utf-8") as f:
    contents = f.read()

print(contents)
```

<sub>[Exercise](find-the-bug.md#exercise-814--saving-a-temperature-reading) · [Runnable file](code/find_the_bug/ex_08_01_04_saving_a_temperature_reading.py)</sub>

### Solution 8.1.5 — Greeting by name

**Bug type:** Syntax

The f-string is missing its closing double quote, so Python never finds the end of the string and reports a syntax error. Add the closing `"` before the parenthesis.

```python
# Assume the user types: Ava
name = input("What is your name? ")
print(f"Hello, {name}! Welcome aboard.")
```

<sub>[Exercise](find-the-bug.md#exercise-815--greeting-by-name) · [Runnable file](code/find_the_bug/ex_08_01_05_greeting_by_name.py)</sub>
