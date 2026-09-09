# Chapter 9 — Input and Output: Find the Bug

Part III · Data — *Everyday Programming*

These programs all use Python I/O — reading with `input()`, showing results with `print()` and f-strings, and saving to files with `open()`. Each one below has exactly one bug. Find it.

Read each program, decide what it is supposed to print, and find the one line that stops it. Then check yourself against [the solutions](solutions.md). The corrected programs are also available as runnable files under [`code/find_the_bug/`](code/find_the_bug).

**5 exercises in 1 sections.**

## 8.1 Reading Input and Printing Output

### Exercise 9.1.1 — Doubling a recipe

This program asks how many cookies a recipe makes, then prints double that amount.

```python
# Assume the user types: 12
cookies = input("How many cookies does the recipe make? ")
print(f"Doubled, that is {cookies * 2} cookies.")
```

<sub>[Solution](solutions.md#solution-811--doubling-a-recipe)</sub>

### Exercise 9.1.2 — Average of two test scores

Assuming the user types 80 then 90, this program should print `Your average is 85.0.`.

```python
# Assume the user types: 80  then  90
score1 = float(input("First test score? "))
score2 = float(input("Second test score? "))
average = score1 + score2 / 2
print(f"Your average is {average}.")
```

<sub>[Solution](solutions.md#solution-812--average-of-two-test-scores)</sub>

### Exercise 9.1.3 — Printing a shopping list

This program should print three fruits on one line, separated by commas, like `apple, banana, cherry`.

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0], fruits[1], fruits[2], sep=" ")
```

<sub>[Solution](solutions.md#solution-813--printing-a-shopping-list)</sub>

### Exercise 9.1.4 — Saving a temperature reading

This program writes one weather reading to a file and then prints it back.

```python
with open("reading.txt", "w", encoding="utf-8") as f:
    f.write("Tokyo,36.5\n")

with open("reading.txt", "w", encoding="utf-8") as f:
    contents = f.read()

print(contents)
```

<sub>[Solution](solutions.md#solution-814--saving-a-temperature-reading)</sub>

### Exercise 9.1.5 — Greeting by name

This program asks for a name and prints a greeting.

```python
# Assume the user types: Ava
name = input("What is your name? ")
print(f"Hello, {name}! Welcome aboard.)
```

<sub>[Solution](solutions.md#solution-815--greeting-by-name)</sub>
