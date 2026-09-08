# Chapter 20 — Common Pitfalls: Find the Bug, Solutions

Each solution names the bug type — **syntax**, **runtime**, or **logical** — explains why the original program misbehaved, and shows the corrected program.

Back to [the exercises](find-the-bug.md).

## 20.1 Forgetting the `:` after `if`, `for`, `while`, or `def`

### Solution 20.1.1 — Missing colon after `if`

**Bug type:** Syntax

The `if` header is missing the trailing `:`, so Python cannot tell where the condition ends and the block begins. Adding the colon fixes the parse error.

```python
temperature = 39
if temperature >= 38:
    print("Fever")
```

<sub>[Exercise](find-the-bug.md#exercise-2011--missing-colon-after-if) · [Runnable file](code/find_the_bug/ex_20_01_01_missing_colon_after_if.py)</sub>

### Solution 20.1.2 — Missing colon after `for`

**Bug type:** Syntax

A `for` loop header must end with `:`. Without it the program will not run; adding the colon resolves it.

```python
distances = [58, 108, 150]
for distance in distances:
    print(distance)
```

<sub>[Exercise](find-the-bug.md#exercise-2012--missing-colon-after-for) · [Runnable file](code/find_the_bug/ex_20_01_02_missing_colon_after_for.py)</sub>

### Solution 20.1.3 — Missing colon after `while`

**Bug type:** Syntax

The `while` header needs a colon before its block. Adding `:` lets the countdown loop parse and run.

```python
seconds = 3
while seconds > 0:
    print(seconds)
    seconds = seconds - 1
```

<sub>[Exercise](find-the-bug.md#exercise-2013--missing-colon-after-while) · [Runnable file](code/find_the_bug/ex_20_01_03_missing_colon_after_while.py)</sub>

### Solution 20.1.4 — Missing colon after `def`

**Bug type:** Syntax

A function definition must end with `:` after the parameter list. Adding the colon makes the definition valid.

```python
def rectangle_area(width, height):
    return width * height

print(rectangle_area(4, 5))  # 20
```

<sub>[Exercise](find-the-bug.md#exercise-2014--missing-colon-after-def) · [Runnable file](code/find_the_bug/ex_20_01_04_missing_colon_after_def.py)</sub>

### Solution 20.1.5 — Missing colon after `elif`

**Bug type:** Syntax

Like `if`, an `elif` header requires a trailing `:`. Adding it lets the three-way branch parse.

```python
score = 55
if score >= 60:
    print("Pass")
elif score >= 50:
    print("Borderline")
else:
    print("Fail")
```

<sub>[Exercise](find-the-bug.md#exercise-2015--missing-colon-after-elif) · [Runnable file](code/find_the_bug/ex_20_01_05_missing_colon_after_elif.py)</sub>

## 20.2 Using the wrong indentation

### Solution 20.2.1 — Body not indented

**Bug type:** Syntax

The `print` after the `if` must be indented to form the block. Indenting it by four spaces fixes the `IndentationError`.

```python
member = "Alex"
if member == "Alex":
    print("Welcome back")
```

<sub>[Exercise](find-the-bug.md#exercise-2021--body-not-indented) · [Runnable file](code/find_the_bug/ex_20_02_01_body_not_indented.py)</sub>

### Solution 20.2.2 — Inconsistent indentation in a loop

**Bug type:** Syntax

The final `print` is indented more deeply than the loop body, which Python reads as an unexpected indent. Aligning it at the outer level (after the loop) fixes it.

```python
rainfall = [12, 8, 15]
total = 0
for amount in rainfall:
    total = total + amount
print(total)  # 35
```

<sub>[Exercise](find-the-bug.md#exercise-2022--inconsistent-indentation-in-a-loop) · [Runnable file](code/find_the_bug/ex_20_02_02_inconsistent_indentation_in_a_loop.py)</sub>

### Solution 20.2.3 — Function body not indented

**Bug type:** Syntax

The `return` statement must be indented inside the function. Indenting it four spaces makes the definition valid.

```python
def square_perimeter(side):
    return 4 * side

print(square_perimeter(6))  # 24
```

<sub>[Exercise](find-the-bug.md#exercise-2023--function-body-not-indented) · [Runnable file](code/find_the_bug/ex_20_02_03_function_body_not_indented.py)</sub>

### Solution 20.2.4 — Over-indented statement

**Bug type:** Syntax

The second `print` is indented inconsistently relative to the `if` block, causing an `IndentationError`. Matching the block's indentation (here, dedenting it to the top level) fixes it.

```python
temperature = 100
if temperature >= 100:
    print("Boiling")
print("Done checking")
```

<sub>[Exercise](find-the-bug.md#exercise-2024--over-indented-statement) · [Runnable file](code/find_the_bug/ex_20_02_04_over_indented_statement.py)</sub>

### Solution 20.2.5 — Indentation mixing two blocks

**Bug type:** Syntax

The closing `print` is indented two spaces, matching neither the loop body nor the top level, so Python raises an `IndentationError`. Dedenting it to the top level fixes it.

```python
grades = [88, 91, 79]
for grade in grades:
    print(grade)
print("Report complete")
```

<sub>[Exercise](find-the-bug.md#exercise-2025--indentation-mixing-two-blocks) · [Runnable file](code/find_the_bug/ex_20_02_05_indentation_mixing_two_blocks.py)</sub>

## 20.3 Confusing assignment with equality

### Solution 20.3.1 — Assignment inside an `if`

**Bug type:** Syntax

`=` assigns and cannot appear as a condition; comparing requires `==`. Using `==` makes the test valid.

```python
thermostat = 20
if thermostat == 20:
    print("Comfortable")
```

<sub>[Exercise](find-the-bug.md#exercise-2031--assignment-inside-an-if) · [Runnable file](code/find_the_bug/ex_20_03_01_assignment_inside_an_if.py)</sub>

### Solution 20.3.2 — Assignment when comparing a password length

**Bug type:** Syntax

A condition must compare with `==`, not assign with `=`. Switching to `==` fixes the error.

```python
length = 8
if length == 8:
    print("Valid length")
```

<sub>[Exercise](find-the-bug.md#exercise-2032--assignment-when-comparing-a-password-length) · [Runnable file](code/find_the_bug/ex_20_03_02_assignment_when_comparing_a_password_length.py)</sub>

### Solution 20.3.3 — Equality used where assignment is meant

**Bug type:** Runtime

`balance == 100` compares instead of assigning, so `balance` is never created and the `print` raises `NameError`. Use a single `=` to assign.

```python
balance = 100
print(balance)  # 100
```

<sub>[Exercise](find-the-bug.md#exercise-2033--equality-used-where-assignment-is-meant) · [Runnable file](code/find_the_bug/ex_20_03_03_equality_used_where_assignment_is_meant.py)</sub>

### Solution 20.3.4 — Assignment inside a `while`

**Bug type:** Syntax

A `while` condition cannot use `=`; it needs a comparison. The intended loop continues while the count is below 50, so use `<`.

```python
count = 5
while count < 50:
    count = count * 2
    print(count)
```

<sub>[Exercise](find-the-bug.md#exercise-2034--assignment-inside-a-while) · [Runnable file](code/find_the_bug/ex_20_03_04_assignment_inside_a_while.py)</sub>

### Solution 20.3.5 — Equality used for assignment

**Bug type:** Runtime

`speed == 60` does not create `speed`; the later `print` raises `NameError`. A single `=` assigns the value.

```python
speed = 60
print("Speed:", speed)  # Speed: 60
```

<sub>[Exercise](find-the-bug.md#exercise-2035--equality-used-for-assignment) · [Runnable file](code/find_the_bug/ex_20_03_05_equality_used_for_assignment.py)</sub>

## 20.4 Using a variable before it is created

### Solution 20.4.1 — Printing before assigning

**Bug type:** Runtime

`students` is used on the first line but assigned on the second, raising `NameError`. Assign before using.

```python
students = 30
print(students)
```

<sub>[Exercise](find-the-bug.md#exercise-2041--printing-before-assigning) · [Runnable file](code/find_the_bug/ex_20_04_01_printing_before_assigning.py)</sub>

### Solution 20.4.2 — Using a sum before it exists

**Bug type:** Runtime

`total` is printed before it is computed, causing `NameError`. Move the assignment above the `print`.

```python
first = 70
second = 85
total = first + second
print(total)
```

<sub>[Exercise](find-the-bug.md#exercise-2042--using-a-sum-before-it-exists) · [Runnable file](code/find_the_bug/ex_20_04_02_using_a_sum_before_it_exists.py)</sub>

### Solution 20.4.3 — Using a result before computing it

**Bug type:** Runtime

`area` is referenced before it is assigned, raising `NameError`. Compute `area` first, then print it.

```python
radius = 3
area = 3.14159 * radius * radius
print(area)
```

<sub>[Exercise](find-the-bug.md#exercise-2043--using-a-result-before-computing-it) · [Runnable file](code/find_the_bug/ex_20_04_03_using_a_result_before_computing_it.py)</sub>

### Solution 20.4.4 — Reading a counter that is set later

**Bug type:** Runtime

`laps` is used before it is created, so the `print` raises `NameError`. Assign `laps` before printing it.

```python
laps = 4
print("Laps:", laps)
```

<sub>[Exercise](find-the-bug.md#exercise-2044--reading-a-counter-that-is-set-later) · [Runnable file](code/find_the_bug/ex_20_04_04_reading_a_counter_that_is_set_later.py)</sub>

### Solution 20.4.5 — Using a price before defining it

**Bug type:** Runtime

`price` is multiplied before it is assigned, raising `NameError`. Define `price` before the calculation.

```python
quantity = 3
price = 2
print(quantity * price)
```

<sub>[Exercise](find-the-bug.md#exercise-2045--using-a-price-before-defining-it) · [Runnable file](code/find_the_bug/ex_20_04_05_using_a_price_before_defining_it.py)</sub>

## 20.5 Misspelling variable names

### Solution 20.5.1 — Misspelled variable in a print

**Bug type:** Runtime

`greting` is a different name from `greeting`, so Python raises `NameError`. Use the correct spelling.

```python
greeting = "Good morning"
print(greeting)
```

<sub>[Exercise](find-the-bug.md#exercise-2051--misspelled-variable-in-a-print) · [Runnable file](code/find_the_bug/ex_20_05_01_misspelled_variable_in_a_print.py)</sub>

### Solution 20.5.2 — Misspelled variable in a calculation

**Bug type:** Runtime

`sped` was never defined; only `speed` exists, so the line raises `NameError`. Fix the spelling.

```python
speed = 60
hours = 2
distance = speed * hours
print(distance)  # 120
```

<sub>[Exercise](find-the-bug.md#exercise-2052--misspelled-variable-in-a-calculation) · [Runnable file](code/find_the_bug/ex_20_05_02_misspelled_variable_in_a_calculation.py)</sub>

### Solution 20.5.3 — Inconsistent capitalization

**Bug type:** Runtime

Python is case-sensitive: `Temperature` and `temperature` are different names, so the `print` raises `NameError`. Match the case used at assignment.

```python
Temperature = 31
print(Temperature)
```

<sub>[Exercise](find-the-bug.md#exercise-2053--inconsistent-capitalization) · [Runnable file](code/find_the_bug/ex_20_05_03_inconsistent_capitalization.py)</sub>

### Solution 20.5.4 — Misspelled variable when updating

**Bug type:** Runtime

`bil` is a misspelling of `bill`, so the calculation raises `NameError`. Use the correct name.

```python
bill = 40
tip = 6
total = bill + tip
print(total)  # 46
```

<sub>[Exercise](find-the-bug.md#exercise-2054--misspelled-variable-when-updating) · [Runnable file](code/find_the_bug/ex_20_05_04_misspelled_variable_when_updating.py)</sub>

### Solution 20.5.5 — Misspelled list name

**Bug type:** Runtime

`score` (singular) was never defined; the list is named `scores`, so `sum(score)` raises `NameError`. Pass the correct list name.

```python
scores = [80, 90, 100]
average = sum(scores) / len(scores)
print(average)  # 90.0
```

<sub>[Exercise](find-the-bug.md#exercise-2055--misspelled-list-name) · [Runnable file](code/find_the_bug/ex_20_05_05_misspelled_list_name.py)</sub>

## 20.6 Mixing strings and numbers without converting types

### Solution 20.6.1 — Joining text and a number

**Bug type:** Runtime

You cannot add a string to an integer; `"Steps today: " + steps` raises `TypeError`. Convert the number with `str()`.

```python
steps = 8000
print("Steps today: " + str(steps))
```

<sub>[Exercise](find-the-bug.md#exercise-2061--joining-text-and-a-number) · [Runnable file](code/find_the_bug/ex_20_06_01_joining_text_and_a_number.py)</sub>

### Solution 20.6.2 — Adding a number to a string label

**Bug type:** Runtime

Mixing `str` and `int` with `+` raises `TypeError`. Convert `liters` to a string before concatenating.

```python
liters = 2
print("Drink " + str(liters) + " liters")
```

<sub>[Exercise](find-the-bug.md#exercise-2062--adding-a-number-to-a-string-label) · [Runnable file](code/find_the_bug/ex_20_06_02_adding_a_number_to_a_string_label.py)</sub>

### Solution 20.6.3 — Concatenating a price into a message

**Bug type:** Runtime

`"...$" + price` adds a string and an int, raising `TypeError`. Wrap `price` in `str()`.

```python
price = 15
message = "Ticket costs $" + str(price)
print(message)
```

<sub>[Exercise](find-the-bug.md#exercise-2063--concatenating-a-price-into-a-message) · [Runnable file](code/find_the_bug/ex_20_06_03_concatenating_a_price_into_a_message.py)</sub>

### Solution 20.6.4 — Combining a count with text

**Bug type:** Runtime

`books + " books..."` adds an int to a string, raising `TypeError`. Convert `books` to a string first.

```python
books = 12
print(str(books) + " books on the shelf")
```

<sub>[Exercise](find-the-bug.md#exercise-2064--combining-a-count-with-text) · [Runnable file](code/find_the_bug/ex_20_06_04_combining_a_count_with_text.py)</sub>

### Solution 20.6.5 — Treating a string as a number

**Bug type:** Runtime/Logical

`score` holds the text `"75"`, so `score + 10` mixes a string and an int and raises `TypeError`. Convert `score` to an integer (or store it as one) before adding.

```python
score = int("75")
print(score + 10)
```

<sub>[Exercise](find-the-bug.md#exercise-2065--treating-a-string-as-a-number) · [Runnable file](code/find_the_bug/ex_20_06_05_treating_a_string_as_a_number.py)</sub>

## 20.7 Forgetting to convert `input()` to a number

### Solution 20.7.1 — Adding to raw input

**Bug type:** Runtime

`input()` returns text, so `year + 1` adds a string and an int, raising `TypeError`. Wrap the input in `int()`.

```python
year = int(input("Enter the year: "))
print(year + 1)
```

<sub>[Exercise](find-the-bug.md#exercise-2071--adding-to-raw-input) · [Runnable file](code/find_the_bug/ex_20_07_01_adding_to_raw_input.py)</sub>

### Solution 20.7.2 — Doubling a typed quantity

**Bug type:** Logical

`cookies` is text, so `cookies * 2` repeats the string (e.g. `"1212"`) instead of doubling the number. Convert the input to `int` first.

```python
cookies = int(input("How many cookies? "))
print(cookies * 2 == 24)  # for input 12
```

<sub>[Exercise](find-the-bug.md#exercise-2072--doubling-a-typed-quantity) · [Runnable file](code/find_the_bug/ex_20_07_02_doubling_a_typed_quantity.py)</sub>

### Solution 20.7.3 — Summing two typed numbers

**Bug type:** Runtime

`second` is left as text, so `first + second` adds an int and a string, raising `TypeError`. Convert `second` with `int()` as well.

```python
first = int(input("First price: "))
second = int(input("Second price: "))
print(first + second)
```

<sub>[Exercise](find-the-bug.md#exercise-2073--summing-two-typed-numbers) · [Runnable file](code/find_the_bug/ex_20_07_03_summing_two_typed_numbers.py)</sub>

### Solution 20.7.4 — Comparing typed age to a limit

**Bug type:** Runtime

`age` is a string, so `age >= 18` compares a string with an int and raises `TypeError`. Convert the input to `int` before comparing.

```python
age = int(input("Your age: "))
if age >= 18:
    print("Adult")
```

<sub>[Exercise](find-the-bug.md#exercise-2074--comparing-typed-age-to-a-limit) · [Runnable file](code/find_the_bug/ex_20_07_04_comparing_typed_age_to_a_limit.py)</sub>

### Solution 20.7.5 — Averaging a typed temperature

**Bug type:** Runtime

`temperature` is text, so `temperature / 2` raises `TypeError`. Convert the input to a number first (`float` allows decimals).

```python
temperature = float(input("Temperature: "))
print(temperature / 2)
```

<sub>[Exercise](find-the-bug.md#exercise-2075--averaging-a-typed-temperature) · [Runnable file](code/find_the_bug/ex_20_07_05_averaging_a_typed_temperature.py)</sub>

## 20.8 Using `/` when you want a whole-number result

### Solution 20.8.1 — Splitting students into teams

**Bug type:** Logical

`/` gives `7.5`, but full teams need integer division. Use `//` to get `7`.

```python
students = 30
team_size = 4
print(students // team_size)  # 7
```

<sub>[Exercise](find-the-bug.md#exercise-2081--splitting-students-into-teams) · [Runnable file](code/find_the_bug/ex_20_08_01_splitting_students_into_teams.py)</sub>

### Solution 20.8.2 — Pages per chapter

**Bug type:** Logical

`52 / 5` is `10.4`; the program wants whole pages. Use `//` for the integer quotient `10`.

```python
pages = 52
chapters = 5
print(pages // chapters)  # 10
```

<sub>[Exercise](find-the-bug.md#exercise-2082--pages-per-chapter) · [Runnable file](code/find_the_bug/ex_20_08_02_pages_per_chapter.py)</sub>

### Solution 20.8.3 — Counting full boxes

**Bug type:** Logical

`40 / 6` is `6.66...`, but you can only fill whole boxes. `//` gives the correct `6`.

```python
eggs = 40
per_box = 6
full_boxes = eggs // per_box
print(full_boxes)  # 6
```

<sub>[Exercise](find-the-bug.md#exercise-2083--counting-full-boxes) · [Runnable file](code/find_the_bug/ex_20_08_03_counting_full_boxes.py)</sub>

### Solution 20.8.4 — Whole minutes from seconds

**Bug type:** Logical

`200 / 60` is `3.33...`; whole minutes need `//`, giving `3`.

```python
seconds = 200
minutes = seconds // 60
print(minutes)  # 3
```

<sub>[Exercise](find-the-bug.md#exercise-2084--whole-minutes-from-seconds) · [Runnable file](code/find_the_bug/ex_20_08_04_whole_minutes_from_seconds.py)</sub>

### Solution 20.8.5 — Sharing marbles evenly

**Bug type:** Logical

`25 / 3` is `8.33...`; each child gets a whole number of marbles. `//` yields `8`.

```python
marbles = 25
children = 3
print(marbles // children)  # 8
```

<sub>[Exercise](find-the-bug.md#exercise-2085--sharing-marbles-evenly) · [Runnable file](code/find_the_bug/ex_20_08_05_sharing_marbles_evenly.py)</sub>

## 20.9 Using `^` for powers instead of `**`

### Solution 20.9.1 — Area of a square

**Bug type:** Logical

`^` is bitwise XOR, not exponent, so `5 ^ 2` is `7`, not `25`. Use `**` for powers.

```python
side = 5
print(side ** 2)  # 25
```

<sub>[Exercise](find-the-bug.md#exercise-2091--area-of-a-square) · [Runnable file](code/find_the_bug/ex_20_09_01_area_of_a_square.py)</sub>

### Solution 20.9.2 — Cube of a number

**Bug type:** Logical

`4 ^ 3` computes XOR (`7`), not `4` cubed. Use `**`.

```python
base = 4
print(base ** 3)  # 64
```

<sub>[Exercise](find-the-bug.md#exercise-2092--cube-of-a-number) · [Runnable file](code/find_the_bug/ex_20_09_02_cube_of_a_number.py)</sub>

### Solution 20.9.3 — Compound growth

**Bug type:** Logical

`2 ^ 10` is XOR (`8`), not `2` to the tenth. Use `**` for exponentiation.

```python
print(2 ** 10)  # 1024
```

<sub>[Exercise](find-the-bug.md#exercise-2093--compound-growth) · [Runnable file](code/find_the_bug/ex_20_09_03_compound_growth.py)</sub>

### Solution 20.9.4 — Volume of a cube

**Bug type:** Logical

`3 ^ 3` is XOR (`0`), not `3` cubed. Use `**` to raise to a power.

```python
edge = 3
volume = edge ** 3
print(volume)  # 27
```

<sub>[Exercise](find-the-bug.md#exercise-2094--volume-of-a-cube) · [Runnable file](code/find_the_bug/ex_20_09_04_volume_of_a_cube.py)</sub>

### Solution 20.9.5 — Energy term squared

**Bug type:** Logical

`6 ^ 2` is XOR (`4`), not `6` squared. Use `**`.

```python
speed = 6
print(speed ** 2)  # 36
```

<sub>[Exercise](find-the-bug.md#exercise-2095--energy-term-squared) · [Runnable file](code/find_the_bug/ex_20_09_05_energy_term_squared.py)</sub>

## 20.10 Modifying a list item that does not exist

### Solution 20.10.1 — Setting a fourth temperature

**Bug type:** Runtime

`readings` has indexes 0–2, so assigning to `readings[3]` raises `IndexError`; assignment cannot grow a list. Use `append` to add a fourth value.

```python
readings = [20, 22, 21]
readings.append(23)
print(readings)
```

<sub>[Exercise](find-the-bug.md#exercise-20101--setting-a-fourth-temperature) · [Runnable file](code/find_the_bug/ex_20_10_01_setting_a_fourth_temperature.py)</sub>

### Solution 20.10.2 — Recording a new score

**Bug type:** Runtime

`scores[3]` does not exist yet, so assigning to it raises `IndexError`. Use `append` to add the new score.

```python
scores = [10, 15, 20]
scores.append(25)
print(scores)
```

<sub>[Exercise](find-the-bug.md#exercise-20102--recording-a-new-score) · [Runnable file](code/find_the_bug/ex_20_10_02_recording_a_new_score.py)</sub>

### Solution 20.10.3 — Filling in a weekly total

**Bug type:** Runtime

Index 3 is past the end of a three-item list, so the assignment raises `IndexError`. Use `append` to extend the list.

```python
weekly_sales = [100, 120, 90]
weekly_sales.append(110)
print(weekly_sales)
```

<sub>[Exercise](find-the-bug.md#exercise-20103--filling-in-a-weekly-total) · [Runnable file](code/find_the_bug/ex_20_10_03_filling_in_a_weekly_total.py)</sub>

### Solution 20.10.4 — Adding a fourth runner's time

**Bug type:** Runtime

`len(lap_times)` is `3`, which is one past the last valid index, so the assignment raises `IndexError`. Use `append`.

```python
lap_times = [45, 47, 44]
lap_times.append(46)
print(lap_times)
```

<sub>[Exercise](find-the-bug.md#exercise-20104--adding-a-fourth-runners-time) · [Runnable file](code/find_the_bug/ex_20_10_04_adding_a_fourth_runner_s_time.py)</sub>

### Solution 20.10.5 — Appending a measurement

**Bug type:** Runtime

Assigning to `ph_values[3]` on a three-item list raises `IndexError`. Use `append` to add a new reading.

```python
ph_values = [7.0, 6.8, 7.2]
ph_values.append(6.9)
print(ph_values)
```

<sub>[Exercise](find-the-bug.md#exercise-20105--appending-a-measurement) · [Runnable file](code/find_the_bug/ex_20_10_05_appending_a_measurement.py)</sub>

## 20.11 Going past the end of a list

### Solution 20.11.1 — Reading the last color

**Bug type:** Runtime

Indexes run 0–2, so `colors[3]` is out of range and raises `IndexError`. The last item is at index `2`.

```python
colors = ["red", "green", "blue"]
print(colors[2])
```

<sub>[Exercise](find-the-bug.md#exercise-20111--reading-the-last-color) · [Runnable file](code/find_the_bug/ex_20_11_01_reading_the_last_color.py)</sub>

### Solution 20.11.2 — Printing each day's high

**Bug type:** Runtime

`range(5)` reaches index 4, but the list has only indexes 0–3, so the loop raises `IndexError`. Loop to `len(highs)` (or iterate the list directly).

```python
highs = [28, 30, 29, 31]
for i in range(len(highs)):
    print(highs[i])
```

<sub>[Exercise](find-the-bug.md#exercise-20112--printing-each-days-high) · [Runnable file](code/find_the_bug/ex_20_11_02_printing_each_day_s_high.py)</sub>

### Solution 20.11.3 — Showing the third prize

**Bug type:** Runtime

The list has only two items (indexes 0 and 1), so `prizes[2]` raises `IndexError`. To print a third prize, the list must contain one.

```python
prizes = ["gold", "silver", "bronze"]
print(prizes[2])
```

<sub>[Exercise](find-the-bug.md#exercise-20113--showing-the-third-prize) · [Runnable file](code/find_the_bug/ex_20_11_03_showing_the_third_prize.py)</sub>

### Solution 20.11.4 — Last item by length

**Bug type:** Runtime

`len(students)` is `3`, one past the last index, so `students[3]` raises `IndexError`. The last index is `len(students) - 1`.

```python
students = ["Mia", "Noah", "Liam"]
print(students[len(students) - 1])
```

<sub>[Exercise](find-the-bug.md#exercise-20114--last-item-by-length) · [Runnable file](code/find_the_bug/ex_20_11_04_last_item_by_length.py)</sub>

### Solution 20.11.5 — Looping one step too far

**Bug type:** Runtime

`index <= len(prices)` lets `index` reach `3`, which is out of range, so the loop raises `IndexError`. Stop with `<` instead of `<=`.

```python
prices = [3, 5, 9]
index = 0
while index < len(prices):
    print(prices[index])
    index = index + 1
```

<sub>[Exercise](find-the-bug.md#exercise-20115--looping-one-step-too-far) · [Runnable file](code/find_the_bug/ex_20_11_05_looping_one_step_too_far.py)</sub>

## 20.12 Using parentheses instead of brackets for lists

### Solution 20.12.1 — Building a shopping list

**Bug type:** Runtime

Parentheses create a tuple, which has no `append` method, so the call raises `AttributeError`. Use square brackets to make a list.

```python
groceries = ["milk", "bread", "eggs"]
groceries.append("butter")
print(groceries)
```

<sub>[Exercise](find-the-bug.md#exercise-20121--building-a-shopping-list) · [Runnable file](code/find_the_bug/ex_20_12_01_building_a_shopping_list.py)</sub>

### Solution 20.12.2 — Collecting daily steps

**Bug type:** Runtime

`steps` is a tuple, so `append` raises `AttributeError`. Use brackets to create a list.

```python
steps = [8000, 9500, 7000]
steps.append(10000)
print(steps)
```

<sub>[Exercise](find-the-bug.md#exercise-20122--collecting-daily-steps) · [Runnable file](code/find_the_bug/ex_20_12_02_collecting_daily_steps.py)</sub>

### Solution 20.12.3 — A list of temperatures

**Bug type:** Runtime

Parentheses make a tuple, which is immutable, so `temperatures[0] = 19` raises `TypeError`. Use brackets to make an editable list.

```python
temperatures = [21, 22, 20]
temperatures[0] = 19
print(temperatures)
```

<sub>[Exercise](find-the-bug.md#exercise-20123--a-list-of-temperatures) · [Runnable file](code/find_the_bug/ex_20_12_03_a_list_of_temperatures.py)</sub>

### Solution 20.12.4 — Listing class names

**Bug type:** Runtime

`subjects` is a tuple, so `append` raises `AttributeError`. Use square brackets for a list.

```python
subjects = ["Math", "Science"]
subjects.append("History")
print(subjects)
```

<sub>[Exercise](find-the-bug.md#exercise-20124--listing-class-names) · [Runnable file](code/find_the_bug/ex_20_12_04_listing_class_names.py)</sub>

### Solution 20.12.5 — A list of scores to extend

**Bug type:** Runtime

Parentheses create a tuple, which has no `append`, raising `AttributeError`. Use brackets to make a list.

```python
scores = [88, 92]
scores.append(75)
print(scores)
```

<sub>[Exercise](find-the-bug.md#exercise-20125--a-list-of-scores-to-extend) · [Runnable file](code/find_the_bug/ex_20_12_05_a_list_of_scores_to_extend.py)</sub>

## 20.13 Forgetting that strings are immutable

### Solution 20.13.1 — Capitalizing a name

**Bug type:** Runtime

Strings are immutable, so `name[0] = "S"` raises `TypeError`. Build a new string instead.

```python
name = "sam"
name = "S" + name[1:]
print(name)
```

<sub>[Exercise](find-the-bug.md#exercise-20131--capitalizing-a-name) · [Runnable file](code/find_the_bug/ex_20_13_01_capitalizing_a_name.py)</sub>

### Solution 20.13.2 — Fixing a typo in a word

**Bug type:** Runtime

You cannot assign to a single character of a string; `word[1] = "e"` raises `TypeError`. Rebuild the word from slices.

```python
word = "hpllo"
word = word[0] + "e" + word[2:]
print(word)
```

<sub>[Exercise](find-the-bug.md#exercise-20132--fixing-a-typo-in-a-word) · [Runnable file](code/find_the_bug/ex_20_13_02_fixing_a_typo_in_a_word.py)</sub>

### Solution 20.13.3 — Replacing a digit in a code

**Bug type:** Runtime

Strings are immutable, so `code[0] = "9"` raises `TypeError`. Construct a new string.

```python
code = "12345"
code = "9" + code[1:]
print(code)
```

<sub>[Exercise](find-the-bug.md#exercise-20133--replacing-a-digit-in-a-code) · [Runnable file](code/find_the_bug/ex_20_13_03_replacing_a_digit_in_a_code.py)</sub>

### Solution 20.13.4 — Masking a letter

**Bug type:** Runtime

Assigning to `secret[3]` fails because strings cannot be changed in place, raising `TypeError`. Rebuild the string from its slices.

```python
secret = "open"
secret = secret[:3] + "*"
print(secret)
```

<sub>[Exercise](find-the-bug.md#exercise-20134--masking-a-letter) · [Runnable file](code/find_the_bug/ex_20_13_04_masking_a_letter.py)</sub>

### Solution 20.13.5 — Correcting a unit label

**Bug type:** Runtime

`unit[0] = "K"` tries to mutate an immutable string, raising `TypeError`. Make a new string instead.

```python
unit = "km"
unit = "K" + unit[1:]
print(unit)
```

<sub>[Exercise](find-the-bug.md#exercise-20135--correcting-a-unit-label) · [Runnable file](code/find_the_bug/ex_20_13_05_correcting_a_unit_label.py)</sub>

## 20.14 Using `is` instead of `==` for value comparison

### Solution 20.14.1 — Checking a student's full name

**Bug type:** Logical

The name built with `join` is a brand-new string object, so `is` (which tests identity) returns `False` even though the text matches. Compare values with `==`.

```python
enrolled_name = "Ada Lovelace"
typed_name = " ".join(["Ada", "Lovelace"])
if typed_name == enrolled_name:
    print("Name matches our records")
else:
    print("Name does not match")
```

<sub>[Exercise](find-the-bug.md#exercise-20141--checking-a-students-full-name) · [Runnable file](code/find_the_bug/ex_20_14_01_checking_a_student_s_full_name.py)</sub>

### Solution 20.14.2 — Matching a password phrase

**Bug type:** Logical

The built string is a different object from the stored literal, so `is` returns `False` even though the text matches. Compare values with `==`.

```python
stored_phrase = "open sesame"
typed_phrase = " ".join(["open", "sesame"])
if typed_phrase == stored_phrase:
    print("Access granted")
else:
    print("Access denied")
```

<sub>[Exercise](find-the-bug.md#exercise-20142--matching-a-password-phrase) · [Runnable file](code/find_the_bug/ex_20_14_02_matching_a_password_phrase.py)</sub>

### Solution 20.14.3 — Confirming a recipe title

**Bug type:** Logical

The title built by concatenation is a separate string object, so `is` returns `False` even when the text is identical. Use `==` to compare the values.

```python
saved_title = "Banana Bread"
first = "Banana"
second = "Bread"
built_title = first + " " + second
if built_title == saved_title:
    print("Recipe title matches")
else:
    print("Recipe title differs")
```

<sub>[Exercise](find-the-bug.md#exercise-20143--confirming-a-recipe-title) · [Runnable file](code/find_the_bug/ex_20_14_03_confirming_a_recipe_title.py)</sub>

### Solution 20.14.4 — Comparing two shopping lists

**Bug type:** Logical

Two lists with identical contents are still distinct objects, so `is` is always `False` here. Use `==` to compare contents.

```python
cart_one = ["milk", "eggs", "bread"]
cart_two = ["milk", "eggs", "bread"]
if cart_one == cart_two:
    print("The carts hold the same items")
else:
    print("The carts differ")
```

<sub>[Exercise](find-the-bug.md#exercise-20144--comparing-two-shopping-lists) · [Runnable file](code/find_the_bug/ex_20_14_04_comparing_two_shopping_lists.py)</sub>

### Solution 20.14.5 — Verifying a reading list

**Bug type:** Logical

Two lists with identical contents are still different objects, so `is` is always `False` here. Use `==` to compare contents.

```python
planned = ["Physics", "Algebra", "Biology"]
read_so_far = ["Physics", "Algebra", "Biology"]
if read_so_far == planned:
    print("You finished the planned books!")
else:
    print("Some planned books remain")
```

<sub>[Exercise](find-the-bug.md#exercise-20145--verifying-a-reading-list) · [Runnable file](code/find_the_bug/ex_20_14_05_verifying_a_reading_list.py)</sub>

## 20.15 Forgetting to call a function with parentheses

### Solution 20.15.1 — Reading the current temperature

**Bug type:** Logical

Writing `current_temperature` without parentheses prints the function object instead of calling it. Add `()` to invoke it.

```python
def current_temperature():
    return 21.5

print("Temperature:", current_temperature())
```

<sub>[Exercise](find-the-bug.md#exercise-20151--reading-the-current-temperature) · [Runnable file](code/find_the_bug/ex_20_15_01_reading_the_current_temperature.py)</sub>

### Solution 20.15.2 — Counting words in a sentence

**Bug type:** Logical

`word_count` alone is the function object; it was never called with the sentence. Call it as `word_count(note)`.

```python
def word_count(sentence):
    return len(sentence.split())

note = "the cat sat on the mat"
print("Words:", word_count(note))
```

<sub>[Exercise](find-the-bug.md#exercise-20152--counting-words-in-a-sentence) · [Runnable file](code/find_the_bug/ex_20_15_02_counting_words_in_a_sentence.py)</sub>

### Solution 20.15.3 — Rolling for a starting number

**Bug type:** Logical

`score = starting_score` stores the function itself, not its result. Add `()` to call it.

```python
def starting_score():
    return 100

score = starting_score()
print("You begin with", score, "points")
```

<sub>[Exercise](find-the-bug.md#exercise-20153--rolling-for-a-starting-number) · [Runnable file](code/find_the_bug/ex_20_15_03_rolling_for_a_starting_number.py)</sub>

### Solution 20.15.4 — Area of a circle

**Bug type:** Runtime

`circle_area / 2` tries to divide the function object by 2, raising `TypeError`. Call the function first, then divide its result.

```python
import math

def circle_area(radius):
    return math.pi * radius ** 2

print("Area:", circle_area(4))
print("Half area:", circle_area(4) / 2)
```

<sub>[Exercise](find-the-bug.md#exercise-20154--area-of-a-circle) · [Runnable file](code/find_the_bug/ex_20_15_04_area_of_a_circle.py)</sub>

### Solution 20.15.5 — Greeting the next runner

**Bug type:** Logical

`message = greet_runner` stores the function, so the print shows a function object. Call it with an argument.

```python
def greet_runner(name):
    return "Good luck, " + name + "!"

message = greet_runner("Sam")
print(message)
```

<sub>[Exercise](find-the-bug.md#exercise-20155--greeting-the-next-runner) · [Runnable file](code/find_the_bug/ex_20_15_05_greeting_the_next_runner.py)</sub>

## 20.16 Not returning a value from a function

### Solution 20.16.1 — Converting miles to kilometers

**Bug type:** Logical

The function computes `km` but never returns it, so the call yields `None`. Add a `return`.

```python
def miles_to_km(miles):
    km = miles * 1.60934
    return km

print("Kilometers:", miles_to_km(5))
```

<sub>[Exercise](find-the-bug.md#exercise-20161--converting-miles-to-kilometers) · [Runnable file](code/find_the_bug/ex_20_16_01_converting_miles_to_kilometers.py)</sub>

### Solution 20.16.2 — Averaging three test grades

**Bug type:** Logical

The average is computed into `average_value` but never returned, so `None` is printed. Return the value.

```python
def average(a, b, c):
    total = a + b + c
    average_value = total / 3
    return average_value

print("Average:", average(80, 90, 100))
```

<sub>[Exercise](find-the-bug.md#exercise-20162--averaging-three-test-grades) · [Runnable file](code/find_the_bug/ex_20_16_02_averaging_three_test_grades.py)</sub>

### Solution 20.16.3 — Doubling a recipe

**Bug type:** Logical

`doubled` is computed but not returned, so `flour` becomes `None`. Add `return doubled`.

```python
def double_amount(cups):
    doubled = cups * 2
    return doubled

flour = double_amount(2.5)
print("Use", flour, "cups of flour")
```

<sub>[Exercise](find-the-bug.md#exercise-20163--doubling-a-recipe) · [Runnable file](code/find_the_bug/ex_20_16_03_doubling_a_recipe.py)</sub>

### Solution 20.16.4 — Perimeter of a rectangle

**Bug type:** Logical

The perimeter `p` is calculated but never returned, so the program prints `None`. Return `p`.

```python
def perimeter(length, width):
    p = 2 * (length + width)
    return p

print("Perimeter:", perimeter(6, 4))
```

<sub>[Exercise](find-the-bug.md#exercise-20164--perimeter-of-a-rectangle) · [Runnable file](code/find_the_bug/ex_20_16_04_perimeter_of_a_rectangle.py)</sub>

### Solution 20.16.5 — Tax on a purchase

**Bug type:** Logical

The tax is computed into `tax` but never returned, so the result is `None`. Add a `return`.

```python
def tax_owed(price, rate):
    tax = price * rate / 100
    return tax

print("Tax:", tax_owed(200, 8))
```

<sub>[Exercise](find-the-bug.md#exercise-20165--tax-on-a-purchase) · [Runnable file](code/find_the_bug/ex_20_16_05_tax_on_a_purchase.py)</sub>

## 20.17 Changing a global variable inside a function by accident

### Solution 20.17.1 — Tallying rainfall

**Bug type:** Runtime

Assigning to `total_rain` inside the function makes it local, so reading it on the right raises `UnboundLocalError`. Declare it `global`.

```python
total_rain = 0.0

def add_rain(today):
    global total_rain
    total_rain = total_rain + today

add_rain(1.2)
print("Total rainfall:", total_rain)
```

<sub>[Exercise](find-the-bug.md#exercise-20171--tallying-rainfall) · [Runnable file](code/find_the_bug/ex_20_17_01_tallying_rainfall.py)</sub>

### Solution 20.17.2 — Keeping a running balance

**Bug type:** Runtime

The function assigns to `balance`, so Python treats it as local and the read raises `UnboundLocalError`. Add `global balance`.

```python
balance = 500

def withdraw(amount):
    global balance
    balance = balance - amount

withdraw(120)
print("Balance:", balance)
```

<sub>[Exercise](find-the-bug.md#exercise-20172--keeping-a-running-balance) · [Runnable file](code/find_the_bug/ex_20_17_02_keeping_a_running_balance.py)</sub>

### Solution 20.17.3 — Counting visitors

**Bug type:** Runtime

Because `visitors` is assigned inside `enter`, Python marks it local and raises `UnboundLocalError`. Declare it `global`.

```python
visitors = 0

def enter():
    global visitors
    visitors = visitors + 1

enter()
print("Visitors:", visitors)
```

<sub>[Exercise](find-the-bug.md#exercise-20173--counting-visitors) · [Runnable file](code/find_the_bug/ex_20_17_03_counting_visitors.py)</sub>

### Solution 20.17.4 — Accumulating distance

**Bug type:** Runtime

Assigning `distance_km` inside `drive` makes it local, so the read raises `UnboundLocalError`. Add `global distance_km`.

```python
distance_km = 0

def drive(leg):
    global distance_km
    distance_km = distance_km + leg

drive(45)
print("Distance:", distance_km)
```

<sub>[Exercise](find-the-bug.md#exercise-20174--accumulating-distance) · [Runnable file](code/find_the_bug/ex_20_17_04_accumulating_distance.py)</sub>

### Solution 20.17.5 — Building a points streak

**Bug type:** Runtime

`streak` is assigned inside the function, so Python treats it as local and raises `UnboundLocalError`. Declare it `global`.

```python
streak = 1

def double_streak():
    global streak
    streak = streak * 2

double_streak()
print("Streak:", streak)
```

<sub>[Exercise](find-the-bug.md#exercise-20175--building-a-points-streak) · [Runnable file](code/find_the_bug/ex_20_17_05_building_a_points_streak.py)</sub>

## 20.18 Forgetting to close a file

### Solution 20.18.1 — Saving a shopping list

**Bug type:** Logical

The file is opened but never closed, so the handle leaks and buffered data may not flush. Use a `with` block, which closes automatically.

```python
groceries = "milk\neggs\nbread\n"
with open("groceries.txt", "w") as list_file:
    list_file.write(groceries)
print("Shopping list saved")
```

<sub>[Exercise](find-the-bug.md#exercise-20181--saving-a-shopping-list) · [Runnable file](code/find_the_bug/ex_20_18_01_saving_a_shopping_list.py)</sub>

### Solution 20.18.2 — Logging a temperature reading

**Bug type:** Logical

The file handle is never closed. Wrap the write in a `with` block so the file is closed safely.

```python
with open("temps.txt", "a") as log:
    log.write("21.5\n")
```

<sub>[Exercise](find-the-bug.md#exercise-20182--logging-a-temperature-reading) · [Runnable file](code/find_the_bug/ex_20_18_02_logging_a_temperature_reading.py)</sub>

### Solution 20.18.3 — Recording a high score

**Bug type:** Logical

`score_file` is opened but never closed. Use `with open(...)` so the file closes automatically after writing.

```python
high_score = 4200
with open("highscore.txt", "w") as score_file:
    score_file.write(str(high_score))
print("High score recorded")
```

<sub>[Exercise](find-the-bug.md#exercise-20183--recording-a-high-score) · [Runnable file](code/find_the_bug/ex_20_18_03_recording_a_high_score.py)</sub>

### Solution 20.18.4 — Writing a daily journal entry

**Bug type:** Logical

The file is left open. A `with` block guarantees the file is closed even if an error occurs.

```python
entry = "Today I walked 10000 steps.\n"
with open("journal.txt", "w") as journal:
    journal.write(entry)
print("Entry written")
```

<sub>[Exercise](find-the-bug.md#exercise-20184--writing-a-daily-journal-entry) · [Runnable file](code/find_the_bug/ex_20_18_04_writing_a_daily_journal_entry.py)</sub>

### Solution 20.18.5 — Storing a measured weight

**Bug type:** Logical

`weight_file` is never closed, risking unflushed data. Use a `with` block to close it safely.

```python
weight_kg = 72.4
with open("weight.txt", "w") as weight_file:
    weight_file.write(f"{weight_kg}\n")
```

<sub>[Exercise](find-the-bug.md#exercise-20185--storing-a-measured-weight) · [Runnable file](code/find_the_bug/ex_20_18_05_storing_a_measured_weight.py)</sub>

## 20.19 Using a broad `except:` and hiding errors

### Solution 20.19.1 — Converting a typed age

**Bug type:** Logical

The bare `except:` hides every error, including programming mistakes. Catch only `ValueError`, which is the error `int()` raises on bad text.

```python
text = "12y"
try:
    age = int(text)
    print("Next year you will be", age + 1)
except ValueError:
    print("Please type a whole number")
```

<sub>[Exercise](find-the-bug.md#exercise-20191--converting-a-typed-age) · [Runnable file](code/find_the_bug/ex_20_19_01_converting_a_typed_age.py)</sub>

### Solution 20.19.2 — Dividing a bill among friends

**Bug type:** Logical

A broad `except:` would swallow unrelated bugs. Catch the specific `ZeroDivisionError` that division by zero raises.

```python
bill = 90
people = 0
try:
    share = bill / people
    print("Each pays", share)
except ZeroDivisionError:
    print("There must be at least one person")
```

<sub>[Exercise](find-the-bug.md#exercise-20192--dividing-a-bill-among-friends) · [Runnable file](code/find_the_bug/ex_20_19_02_dividing_a_bill_among_friends.py)</sub>

### Solution 20.19.3 — Looking up a price

**Bug type:** Logical

The bare `except:` hides all errors. A missing dictionary key raises `KeyError`, so catch exactly that.

```python
prices = {"apple": 0.5, "banana": 0.3}
item = "cherry"
try:
    print("Price:", prices[item])
except KeyError:
    print("That item is not on the price list")
```

<sub>[Exercise](find-the-bug.md#exercise-20193--looking-up-a-price) · [Runnable file](code/find_the_bug/ex_20_19_03_looking_up_a_price.py)</sub>

### Solution 20.19.4 — Parsing a temperature

**Bug type:** Logical

A bare `except:` masks unrelated problems. `float()` raises `ValueError` on non-numeric text, so catch `ValueError`.

```python
reading = "hot"
try:
    celsius = float(reading)
    print("Fahrenheit:", celsius * 9 / 5 + 32)
except ValueError:
    print("That is not a valid temperature")
```

<sub>[Exercise](find-the-bug.md#exercise-20194--parsing-a-temperature) · [Runnable file](code/find_the_bug/ex_20_19_04_parsing_a_temperature.py)</sub>

### Solution 20.19.5 — Reading a list position

**Bug type:** Logical

The broad `except:` hides real bugs. An out-of-range index raises `IndexError`, so catch exactly that.

```python
scores = [88, 92]
try:
    print("Third score:", scores[2])
except IndexError:
    print("There is no score at that position")
```

<sub>[Exercise](find-the-bug.md#exercise-20195--reading-a-list-position) · [Runnable file](code/find_the_bug/ex_20_19_05_reading_a_list_position.py)</sub>

## 20.20 Comparing text without thinking about case

### Solution 20.20.1 — Accepting a yes answer

**Bug type:** Logical

`"YES" == "yes"` is `False` because case differs. Normalize the case first with `.lower()`.

```python
answer = "YES"
if answer.lower() == "yes":
    print("Confirmed")
else:
    print("Not confirmed")
```

<sub>[Exercise](find-the-bug.md#exercise-20201--accepting-a-yes-answer) · [Runnable file](code/find_the_bug/ex_20_20_01_accepting_a_yes_answer.py)</sub>

### Solution 20.20.2 — Matching a chosen color

**Bug type:** Logical

`favorite.upper()` gives `"BLUE"`, which never equals the lowercase `"blue"`. Normalize both sides to the same case, for example `.lower() == "blue"`.

```python
favorite = "Blue"
if favorite.lower() == "blue":
    print("You picked blue")
```

<sub>[Exercise](find-the-bug.md#exercise-20202--matching-a-chosen-color) · [Runnable file](code/find_the_bug/ex_20_20_02_matching_a_chosen_color.py)</sub>

### Solution 20.20.3 — Checking a chemical symbol

**Bug type:** Logical

`"NA" == "Na"` is `False` because the cases differ. Normalize the typed symbol, for example with `.capitalize()`.

```python
symbol = "NA"
if symbol.capitalize() == "Na":
    print("That is sodium")
```

<sub>[Exercise](find-the-bug.md#exercise-20203--checking-a-chemical-symbol) · [Runnable file](code/find_the_bug/ex_20_20_03_checking_a_chemical_symbol.py)</sub>

### Solution 20.20.4 — Looking up a city name

**Bug type:** Logical

The list stores `"Paris"`, so a lowercase `"paris"` is not found. Compare in a consistent case, for example by lowercasing each city.

```python
cities = ["Paris", "London", "Tokyo"]
search = "paris"
if search in [city.lower() for city in cities]:
    print("City found")
else:
    print("City not found")
```

<sub>[Exercise](find-the-bug.md#exercise-20204--looking-up-a-city-name) · [Runnable file](code/find_the_bug/ex_20_20_04_looking_up_a_city_name.py)</sub>

### Solution 20.20.5 — Confirming a unit

**Bug type:** Logical

`unit.upper()` produces `"KG"`, which never equals lowercase `"kg"`. Compare against the same case you converted to, for example `.lower() == "kg"`.

```python
unit = "KG"
if unit.lower() == "kg":
    print("Kilograms")
```

<sub>[Exercise](find-the-bug.md#exercise-20205--confirming-a-unit) · [Runnable file](code/find_the_bug/ex_20_20_05_confirming_a_unit.py)</sub>

## 20.21 Using `range(len(...))` when iterating over items directly is simpler

### Solution 20.21.1 — Printing each planet

**Bug type:** Runtime

The loop indexes with `i` but prints `planet`, which was never defined, raising `NameError`. Iterate over the items directly.

```python
planets = ["Mercury", "Venus", "Earth", "Mars"]
for planet in planets:
    print(planet)
```

<sub>[Exercise](find-the-bug.md#exercise-20211--printing-each-planet) · [Runnable file](code/find_the_bug/ex_20_21_01_printing_each_planet.py)</sub>

### Solution 20.21.2 — Summing daily sales

**Bug type:** Runtime

`total + sales` adds an integer to the whole list, raising `TypeError`. Iterate over the items and add each value.

```python
sales = [120, 85, 200, 95]
total = 0
for amount in sales:
    total = total + amount
print("Total sales:", total)
```

<sub>[Exercise](find-the-bug.md#exercise-20212--summing-daily-sales) · [Runnable file](code/find_the_bug/ex_20_21_02_summing_daily_sales.py)</sub>

### Solution 20.21.3 — Greeting each guest

**Bug type:** Logical

`range(len(guests))` yields the numbers 0, 1, 2, so the greeting prints numbers, not names. Iterate over the guests directly.

```python
guests = ["Ana", "Ben", "Cara"]
for guest in guests:
    print("Welcome,", guest)
```

<sub>[Exercise](find-the-bug.md#exercise-20213--greeting-each-guest) · [Runnable file](code/find_the_bug/ex_20_21_03_greeting_each_guest.py)</sub>

### Solution 20.21.4 — Doubling each measurement

**Bug type:** Logical

`range(len(...))` makes `m` the index 0, 1, 2, so it doubles indexes, not values. Iterate over the measurements directly.

```python
measurements = [3, 5, 8]
for m in measurements:
    print(m * 2)
```

<sub>[Exercise](find-the-bug.md#exercise-20214--doubling-each-measurement) · [Runnable file](code/find_the_bug/ex_20_21_04_doubling_each_measurement.py)</sub>

### Solution 20.21.5 — Listing the ingredients

**Bug type:** Logical

`item` becomes the index 0, 1, 2 instead of the ingredient name. Iterate over the list itself.

```python
ingredients = ["flour", "sugar", "butter"]
for item in ingredients:
    print(item)
```

<sub>[Exercise](find-the-bug.md#exercise-20215--listing-the-ingredients) · [Runnable file](code/find_the_bug/ex_20_21_05_listing_the_ingredients.py)</sub>

## 20.22 Shadowing built-in names like `list`, `str`, or `sum`

### Solution 20.22.1 — Counting items in a basket

**Bug type:** Runtime

Assigning `len = [4, 8, 15]` shadows the built-in `len`, so `len(fruit)` tries to call a list and raises `TypeError`. Rename the variable.

```python
basket = [4, 8, 15]
fruit = "banana"
print("Letters in banana:", len(fruit))
```

<sub>[Exercise](find-the-bug.md#exercise-20221--counting-items-in-a-basket) · [Runnable file](code/find_the_bug/ex_20_22_01_counting_items_in_a_basket.py)</sub>

### Solution 20.22.2 — Totaling a receipt

**Bug type:** Runtime

`sum = 0` shadows the built-in `sum`, so `sum(prices)` tries to call an integer and raises `TypeError`. Use a different variable name.

```python
running_total = 0
prices = [2.50, 3.00, 1.25]
print("Receipt total:", sum(prices))
```

<sub>[Exercise](find-the-bug.md#exercise-20222--totaling-a-receipt) · [Runnable file](code/find_the_bug/ex_20_22_02_totaling_a_receipt.py)</sub>

### Solution 20.22.3 — Turning a word into letters

**Bug type:** Runtime

`list = "abc"` shadows the built-in `list`, so `list("hello")` tries to call a string and raises `TypeError`. Rename the variable.

```python
word = "abc"
letters = list("hello")
print(letters)
```

<sub>[Exercise](find-the-bug.md#exercise-20223--turning-a-word-into-letters) · [Runnable file](code/find_the_bug/ex_20_22_03_turning_a_word_into_letters.py)</sub>

### Solution 20.22.4 — Labeling a measurement

**Bug type:** Runtime

`str = "kilograms"` shadows the built-in `str`, so `str(weight)` tries to call a string and raises `TypeError`. Rename the variable.

```python
unit = "kilograms"
weight = 70
print(str(weight) + " " + unit)
```

<sub>[Exercise](find-the-bug.md#exercise-20224--labeling-a-measurement) · [Runnable file](code/find_the_bug/ex_20_22_04_labeling_a_measurement.py)</sub>

### Solution 20.22.5 — Finding the largest reading

**Bug type:** Runtime

`max = 9999` shadows the built-in `max`, so `max(readings)` tries to call an integer and raises `TypeError`. Use a different name.

```python
ceiling = 9999
readings = [33.1, 36.5, 31.0]
print("Highest reading:", max(readings))
```

<sub>[Exercise](find-the-bug.md#exercise-20225--finding-the-largest-reading) · [Runnable file](code/find_the_bug/ex_20_22_05_finding_the_largest_reading.py)</sub>

## 20.23 Expecting floating-point math to be exact

### Solution 20.23.1 — Splitting a bill exactly

**Bug type:** Logical

`0.10 + 0.10 + 0.10` is not exactly `0.30` in binary floating-point, so the equality fails. Compare with a small tolerance using `round` or `math.isclose`.

```python
import math

share = 0.10
total = share + share + share
if math.isclose(total, 0.30):
    print("The shares add up exactly")
else:
    print("The shares do not add up exactly")
```

<sub>[Exercise](find-the-bug.md#exercise-20231--splitting-a-bill-exactly) · [Runnable file](code/find_the_bug/ex_20_23_01_splitting_a_bill_exactly.py)</sub>

### Solution 20.23.2 — Adding two distances

**Bug type:** Logical

`0.1 + 0.2` is slightly more than `0.3` in floating-point, so the exact comparison is `False`. Use `math.isclose` to compare with tolerance.

```python
import math

leg_one = 0.1
leg_two = 0.2
if math.isclose(leg_one + leg_two, 0.3):
    print("Distances match")
else:
    print("Distances do not match")
```

<sub>[Exercise](find-the-bug.md#exercise-20232--adding-two-distances) · [Runnable file](code/find_the_bug/ex_20_23_02_adding_two_distances.py)</sub>

### Solution 20.23.3 — Checking a measured volume

**Bug type:** Logical

`0.1 * 3` does not equal `0.3` exactly in floating-point. Compare with a tolerance, for example `math.isclose`.

```python
import math

pour = 0.1
filled = pour * 3
if math.isclose(filled, 0.3):
    print("Cup is exactly full")
else:
    print("Cup is not exactly full")
```

<sub>[Exercise](find-the-bug.md#exercise-20233--checking-a-measured-volume) · [Runnable file](code/find_the_bug/ex_20_23_03_checking_a_measured_volume.py)</sub>

### Solution 20.23.4 — Verifying a percentage

**Bug type:** Logical

`0.7 + 0.1` is not exactly `0.8` in binary floating-point, so the strict equality fails. Use `math.isclose` to allow for rounding error.

```python
import math

part_one = 0.7
part_two = 0.1
if math.isclose(part_one + part_two, 0.8):
    print("Percentages add correctly")
else:
    print("Percentages do not add correctly")
```

<sub>[Exercise](find-the-bug.md#exercise-20234--verifying-a-percentage) · [Runnable file](code/find_the_bug/ex_20_23_04_verifying_a_percentage.py)</sub>

### Solution 20.23.5 — Comparing a savings target

**Bug type:** Logical

`1.10 * 3` does not land exactly on `3.30` in floating-point. Compare with a tolerance using `math.isclose`.

```python
import math

weekly = 1.10
saved = weekly * 3
if math.isclose(saved, 3.30):
    print("You reached the target")
else:
    print("You did not reach the target")
```

<sub>[Exercise](find-the-bug.md#exercise-20235--comparing-a-savings-target) · [Runnable file](code/find_the_bug/ex_20_23_05_comparing_a_savings_target.py)</sub>

## 20.24 Writing long code without testing small pieces

### Solution 20.24.1 — Average speed of a trip

**Bug type:** Logical

The formula is reversed: speed is distance divided by time, not time divided by distance. Swap the operands.

```python
def average_speed(distance, time):
    return distance / time

print("Average speed:", average_speed(150, 3))  # Average speed: 50.0
```

<sub>[Exercise](find-the-bug.md#exercise-20241--average-speed-of-a-trip) · [Runnable file](code/find_the_bug/ex_20_24_01_average_speed_of_a_trip.py)</sub>

### Solution 20.24.2 — Final price after discount

**Bug type:** Logical

A percentage must be divided by 100 first; `price * 20` computes a huge discount. Divide the percent by 100 (or test the discount step alone to catch this).

```python
def final_price(price, percent_off):
    discount = price * percent_off / 100
    return price - discount

print("Final price:", final_price(50, 20))  # Final price: 40.0
```

<sub>[Exercise](find-the-bug.md#exercise-20242--final-price-after-discount) · [Runnable file](code/find_the_bug/ex_20_24_02_final_price_after_discount.py)</sub>

### Solution 20.24.3 — Kinetic energy of a moving cart

**Bug type:** Logical

The speed must be squared (`speed ** 2`), but the code multiplies by 2 instead. Testing the squaring step alone would reveal this.

```python
def kinetic_energy(mass, speed):
    return 0.5 * mass * speed ** 2

print("Kinetic energy:", kinetic_energy(2, 3))  # Kinetic energy: 9.0
```

<sub>[Exercise](find-the-bug.md#exercise-20243--kinetic-energy-of-a-moving-cart) · [Runnable file](code/find_the_bug/ex_20_24_03_kinetic_energy_of_a_moving_cart.py)</sub>

### Solution 20.24.4 — Celsius to Fahrenheit

**Bug type:** Logical

The formula adds 32, but the code subtracts it. Change `- 32` to `+ 32`.

```python
def to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

print("Fahrenheit:", to_fahrenheit(100))  # Fahrenheit: 212.0
```

<sub>[Exercise](find-the-bug.md#exercise-20244--celsius-to-fahrenheit) · [Runnable file](code/find_the_bug/ex_20_24_04_celsius_to_fahrenheit.py)</sub>

### Solution 20.24.5 — Average of a list of grades

**Bug type:** Logical

The stray `- 1` skews the average. Testing the bare `sum / len` step alone would expose it; remove the `- 1`.

```python
def average(grades):
    return sum(grades) / len(grades)

print("Average:", average([80, 90, 80, 90]))  # Average: 85.0
```

<sub>[Exercise](find-the-bug.md#exercise-20245--average-of-a-list-of-grades) · [Runnable file](code/find_the_bug/ex_20_24_05_average_of_a_list_of_grades.py)</sub>

## 20.25 Shallow vs deep copy

### Solution 20.25.1 — Copying a seating chart

**Bug type:** Logical

`original.copy()` is a shallow copy: the inner row lists are still shared, so appending through `backup` also changes `original`. Use `copy.deepcopy`.

```python
import copy

original = [["Ana", "Ben"], ["Cara", "Dan"]]
backup = copy.deepcopy(original)
backup[0].append("Eve")
print("Original:", original)  # Original: [['Ana', 'Ben'], ['Cara', 'Dan']]
```

<sub>[Exercise](find-the-bug.md#exercise-20251--copying-a-seating-chart) · [Runnable file](code/find_the_bug/ex_20_25_01_copying_a_seating_chart.py)</sub>

### Solution 20.25.2 — Backing up monthly budgets

**Bug type:** Logical

Slicing with `[:]` copies only the outer list; the nested lists stay shared, so editing `saved` edits `budgets`. Use `copy.deepcopy`.

```python
import copy

budgets = [[100, 200], [300, 400]]
saved = copy.deepcopy(budgets)
saved[1][0] = 999
print("Budgets:", budgets)  # Budgets: [[100, 200], [300, 400]]
```

<sub>[Exercise](find-the-bug.md#exercise-20252--backing-up-monthly-budgets) · [Runnable file](code/find_the_bug/ex_20_25_02_backing_up_monthly_budgets.py)</sub>

### Solution 20.25.3 — Duplicating a tic-tac-toe board

**Bug type:** Logical

`list(board)` makes a shallow copy whose inner rows are shared, so editing `trial` changes `board`. Use `copy.deepcopy`.

```python
import copy

board = [["X", "O"], ["O", "X"]]
trial = copy.deepcopy(board)
trial[0][1] = "X"
print("Board:", board)  # Board: [['X', 'O'], ['O', 'X']]
```

<sub>[Exercise](find-the-bug.md#exercise-20253--duplicating-a-tic-tac-toe-board) · [Runnable file](code/find_the_bug/ex_20_25_03_duplicating_a_tic_tac_toe_board.py)</sub>

### Solution 20.25.4 — Snapshotting weekly readings

**Bug type:** Logical

`readings.copy()` is shallow, so the nested lists remain shared and editing `snapshot` also edits `readings`. Use `copy.deepcopy`.

```python
import copy

readings = [[1.0, 2.0], [3.0, 4.0]]
snapshot = copy.deepcopy(readings)
snapshot[0][0] = 99.0
print("Readings:", readings)  # Readings: [[1.0, 2.0], [3.0, 4.0]]
```

<sub>[Exercise](find-the-bug.md#exercise-20254--snapshotting-weekly-readings) · [Runnable file](code/find_the_bug/ex_20_25_04_snapshotting_weekly_readings.py)</sub>

### Solution 20.25.5 — Cloning a recipe with sub-steps

**Bug type:** Logical

Slicing with `[:]` copies only the outer list; the nested step lists are shared, so appending through `clone` changes `recipe`. Use `copy.deepcopy`.

```python
import copy

recipe = [["mix", "stir"], ["bake", "cool"]]
clone = copy.deepcopy(recipe)
clone[1].append("serve")
print("Recipe:", recipe)  # Recipe: [['mix', 'stir'], ['bake', 'cool']]
```

<sub>[Exercise](find-the-bug.md#exercise-20255--cloning-a-recipe-with-sub-steps) · [Runnable file](code/find_the_bug/ex_20_25_05_cloning_a_recipe_with_sub_steps.py)</sub>

## 20.26 Mutable default arguments

### Solution 20.26.1 — Collecting quiz answers

**Bug type:** Logical

The default `sheet=[]` is created once and reused, so answers accumulate across calls. Default to `None` and make a fresh list inside.

```python
def record_answer(answer, sheet=None):
    if sheet is None:
        sheet = []
    sheet.append(answer)
    return sheet

print(record_answer("A"))  # ['A']
print(record_answer("B"))  # ['B']
```

<sub>[Exercise](find-the-bug.md#exercise-20261--collecting-quiz-answers) · [Runnable file](code/find_the_bug/ex_20_26_01_collecting_quiz_answers.py)</sub>

### Solution 20.26.2 — Building a grocery list

**Bug type:** Logical

The mutable default `cart=[]` is shared between calls, so items pile up. Use `None` and create a new list inside the function.

```python
def add_item(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart

print(add_item("milk"))   # ['milk']
print(add_item("eggs"))   # ['eggs']
```

<sub>[Exercise](find-the-bug.md#exercise-20262--building-a-grocery-list) · [Runnable file](code/find_the_bug/ex_20_26_02_building_a_grocery_list.py)</sub>

### Solution 20.26.3 — Logging a single temperature

**Bug type:** Logical

The default `log=[]` is created once and reused across calls, so readings accumulate. Default to `None` and build a fresh list.

```python
def log_reading(reading, log=None):
    if log is None:
        log = []
    log.append(reading)
    return log

print(log_reading(21.5))  # [21.5]
print(log_reading(19.0))  # [19.0]
```

<sub>[Exercise](find-the-bug.md#exercise-20263--logging-a-single-temperature) · [Runnable file](code/find_the_bug/ex_20_26_03_logging_a_single_temperature.py)</sub>

### Solution 20.26.4 — Tracking a player's scores

**Bug type:** Logical

The shared default `board=[]` keeps old scores between calls. Use `None` and create a new list inside the function.

```python
def new_scoreboard(score, board=None):
    if board is None:
        board = []
    board.append(score)
    return board

print(new_scoreboard(10))  # [10]
print(new_scoreboard(20))  # [20]
```

<sub>[Exercise](find-the-bug.md#exercise-20264--tracking-a-players-scores) · [Runnable file](code/find_the_bug/ex_20_26_04_tracking_a_player_s_scores.py)</sub>

### Solution 20.26.5 — Noting one ingredient

**Bug type:** Logical

The mutable default `items=[]` is reused on every call, so ingredients accumulate. Default to `None` and make a fresh list.

```python
def note_ingredient(name, items=None):
    if items is None:
        items = []
    items.append(name)
    return items

print(note_ingredient("flour"))  # ['flour']
print(note_ingredient("sugar"))  # ['sugar']
```

<sub>[Exercise](find-the-bug.md#exercise-20265--noting-one-ingredient) · [Runnable file](code/find_the_bug/ex_20_26_05_noting_one_ingredient.py)</sub>
