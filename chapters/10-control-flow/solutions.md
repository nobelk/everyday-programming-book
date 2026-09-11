# Chapter 10 — Control Flow: Find the Bug, Solutions

Each solution names the bug type — **syntax**, **runtime**, or **logical** — explains why the original program misbehaved, and shows the corrected program.

Back to [the exercises](find-the-bug.md).

## 9.1 `if`, `elif`, `else`

### Solution 10.1.1 — Grading with elif

**Bug type:** Syntax

The `else` line is missing its colon, so Python cannot parse the block. Adding the colon fixes it.

```python
score = 82

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Needs improvement")
```

<sub>[Exercise](find-the-bug.md#exercise-911--grading-with-elif) · [Runnable file](code/find_the_bug/ex_09_01_01_grading_with_elif.py)</sub>

### Solution 10.1.2 — Temperature category

**Bug type:** Syntax

The body of the first `if` is not indented, so Python raises an `IndentationError`. Indenting the `print` four spaces fixes it.

```python
temp_c = 36.5

if temp_c > 35:
    print("Heat warning")
elif temp_c < 0:
    print("Freezing")
else:
    print("Normal")
```

<sub>[Exercise](find-the-bug.md#exercise-912--temperature-category) · [Runnable file](code/find_the_bug/ex_09_01_02_temperature_category.py)</sub>

### Solution 10.1.3 — Independent checks that should be alternatives

**Bug type:** Logical

The second test starts a new `if` instead of chaining with `elif`, so its `else` attaches to the second `if` only; an acidic value (pH 6.0) makes the first `if` print `Acidic` and the second `else` also print `Basic`. Using `elif` makes the three cases mutually exclusive.

```python
ph = 6.0

if ph < 7:
    print("Acidic")
elif ph == 7:
    print("Neutral")
else:
    print("Basic")
```

<sub>[Exercise](find-the-bug.md#exercise-913--independent-checks-that-should-be-alternatives) · [Runnable file](code/find_the_bug/ex_09_01_03_independent_checks_that_should_be_alternatives.py)</sub>

### Solution 10.1.4 — Pass or fail

**Bug type:** Syntax

The `else` is indented as if it were inside the `if` body, which is illegal. Aligning `else` with `if` fixes it.

```python
score = 75

if score >= 60:
    print("Pass")
else:
    print("Fail")
```

<sub>[Exercise](find-the-bug.md#exercise-914--pass-or-fail) · [Runnable file](code/find_the_bug/ex_09_01_04_pass_or_fail.py)</sub>

### Solution 10.1.5 — Ticket price by age

**Bug type:** Logical

The `print` is indented inside the `else` branch, so it only runs for the full price; the child's price is never shown. Moving `print` out to run after the `if`/`else` fixes it.

```python
age = 10

if age < 12:
    price = 5
else:
    price = 12

print("Ticket price:", price)
```

<sub>[Exercise](find-the-bug.md#exercise-915--ticket-price-by-age) · [Runnable file](code/find_the_bug/ex_09_01_05_ticket_price_by_age.py)</sub>

## 9.2 Common Comparison Operators

### Solution 10.2.1 — Exact match

**Bug type:** Syntax

A single `=` is assignment, not comparison, and is not allowed in an `if` condition. Use `==` to compare.

```python
answer = 42

if answer == 42:
    print("Correct")
else:
    print("Try again")
```

<sub>[Exercise](find-the-bug.md#exercise-921--exact-match) · [Runnable file](code/find_the_bug/ex_09_02_01_exact_match.py)</sub>

### Solution 10.2.2 — Freezing point

**Bug type:** Logical

`<` excludes 0 itself, but water freezes *at* 0 too. Using `<=` includes the freezing point.

```python
temp_c = 0

if temp_c <= 0:
    print("Frozen")
else:
    print("Liquid")
```

<sub>[Exercise](find-the-bug.md#exercise-922--freezing-point) · [Runnable file](code/find_the_bug/ex_09_02_02_freezing_point.py)</sub>

### Solution 10.2.3 — Not equal

**Bug type:** Logical

The condition should test ``not 0'' but uses `==`, so it prints `Sold out` exactly when seats is 0. Use `!=` to match the intended meaning.

```python
seats_left = 0

if seats_left != 0:
    print("Sold out")
```

<sub>[Exercise](find-the-bug.md#exercise-923--not-equal) · [Runnable file](code/find_the_bug/ex_09_02_03_not_equal.py)</sub>

### Solution 10.2.4 — Speed limit check

**Bug type:** Logical

``At most 60'' includes 60, but `<` excludes it, so a car at the limit is wrongly flagged. Use `<=`.

```python
speed = 60
limit = 60

if speed <= limit:
    print("OK")
else:
    print("Too fast")
```

<sub>[Exercise](find-the-bug.md#exercise-924--speed-limit-check) · [Runnable file](code/find_the_bug/ex_09_02_04_speed_limit_check.py)</sub>

### Solution 10.2.5 — Adult check

**Bug type:** Logical

``18 or older'' includes 18, but `>` excludes it. Use `>=`.

```python
age = 18

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

<sub>[Exercise](find-the-bug.md#exercise-925--adult-check) · [Runnable file](code/find_the_bug/ex_09_02_05_adult_check.py)</sub>

## 9.3 Logical Operators

### Solution 10.3.1 — Entry rules

**Bug type:** Logical

`or` allows entry when *either* condition holds, but both age and ID are required. Using `and` enforces both.

```python
age = 20
has_id = False

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")
```

<sub>[Exercise](find-the-bug.md#exercise-931--entry-rules) · [Runnable file](code/find_the_bug/ex_09_03_01_entry_rules.py)</sub>

### Solution 10.3.2 — Weekend check

**Bug type:** Logical

A day cannot equal both `Saturday` and `Sunday`, so the `and` condition is never true and nothing prints. The cases are alternatives, so use `or`.

```python
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("Relax")
# expected: Relax
```

<sub>[Exercise](find-the-bug.md#exercise-932--weekend-check) · [Runnable file](code/find_the_bug/ex_09_03_02_weekend_check.py)</sub>

### Solution 10.3.3 — Comfortable room

**Bug type:** Logical

With `or`, almost every temperature satisfies at least one side, so even 30 degrees prints ``Comfortable''. The range requires *both* bounds, so use `and`.

```python
temp_c = 30

if temp_c >= 20 and temp_c <= 25:
    print("Comfortable")
else:
    print("Adjust the thermostat")
# expected: Adjust the thermostat
```

<sub>[Exercise](find-the-bug.md#exercise-933--comfortable-room) · [Runnable file](code/find_the_bug/ex_09_03_03_comfortable_room.py)</sub>

### Solution 10.3.4 — Out of stock

**Bug type:** Syntax

`not in_stock = True` mixes `not` with an assignment, which is invalid. The intent is simply to test the negation, so write `if not in_stock:`.

```python
in_stock = False

if not in_stock:
    print("Reorder")
```

<sub>[Exercise](find-the-bug.md#exercise-934--out-of-stock) · [Runnable file](code/find_the_bug/ex_09_03_04_out_of_stock.py)</sub>

### Solution 10.3.5 — Free shipping

**Bug type:** Logical

Free shipping should apply when *either* condition holds, but `and` requires both, so a member with a $30 order is wrongly charged. Using `or` matches the rule.

```python
total = 30
is_member = True

if total >= 50 or is_member:
    print("Free shipping")
else:
    print("Pay shipping")
# expected: Free shipping
```

<sub>[Exercise](find-the-bug.md#exercise-935--free-shipping) · [Runnable file](code/find_the_bug/ex_09_03_05_free_shipping.py)</sub>

## 9.4 `for` Loops

### Solution 10.4.1 — Sum of a list

**Bug type:** Logical

`total = price` overwrites the running sum each pass instead of adding to it, leaving only the last price. Use `total += price` to accumulate.

```python
prices = [10, 20, 30]
total = 0

for price in prices:
    total += price

print("Total:", total)
```

<sub>[Exercise](find-the-bug.md#exercise-941--sum-of-a-list) · [Runnable file](code/find_the_bug/ex_09_04_01_sum_of_a_list.py)</sub>

### Solution 10.4.2 — Counting vowels

**Bug type:** Logical

The count is correct, but `print(count + 1)` adds one extra at the end. Print `count` itself.

```python
word = "education"
vowels = "aeiou"
count = 0

for letter in word:
    if letter in vowels:
        count = count + 1

print(count)
```

<sub>[Exercise](find-the-bug.md#exercise-942--counting-vowels) · [Runnable file](code/find_the_bug/ex_09_04_02_counting_vowels.py)</sub>

### Solution 10.4.3 — Printing each fruit

**Bug type:** Syntax

The `for` statement is missing its colon. Adding it fixes the parse error.

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

<sub>[Exercise](find-the-bug.md#exercise-943--printing-each-fruit) · [Runnable file](code/find_the_bug/ex_09_04_03_printing_each_fruit.py)</sub>

### Solution 10.4.4 — Average of readings

**Bug type:** Runtime

`len(reading)` uses the loop variable (the last item, an integer) instead of the list, raising a `TypeError`. Use `len(readings)`.

```python
readings = [28, 30, 32]
total = 0

for reading in readings:
    total += reading

average = total / len(readings)
print(average)
```

<sub>[Exercise](find-the-bug.md#exercise-944--average-of-readings) · [Runnable file](code/find_the_bug/ex_09_04_04_average_of_readings.py)</sub>

### Solution 10.4.5 — Largest measurement

**Bug type:** Logical

The comparison `<` keeps the smallest value, not the largest. To track the maximum, replace it when the current value is *greater*, using `>`.

```python
distances = [12, 45, 9, 33]
largest = 0

for distance in distances:
    if distance > largest:
        largest = distance

print(largest)
```

<sub>[Exercise](find-the-bug.md#exercise-945--largest-measurement) · [Runnable file](code/find_the_bug/ex_09_04_05_largest_measurement.py)</sub>

## 9.5 `range`

### Solution 10.5.1 — Counting to five

**Bug type:** Logical

`range` stops before its end value, so `range(1, 5)` yields 1–4. To reach 5, use `range(1, 6)`.

```python
for number in range(1, 6):
    print(number)
```

<sub>[Exercise](find-the-bug.md#exercise-951--counting-to-five) · [Runnable file](code/find_the_bug/ex_09_05_01_counting_to_five.py)</sub>

### Solution 10.5.2 — Even numbers

**Bug type:** Logical

A step of 1 prints every number, not just the evens. The step should be 2.

```python
for number in range(2, 11, 2):
    print(number)
```

<sub>[Exercise](find-the-bug.md#exercise-952--even-numbers) · [Runnable file](code/find_the_bug/ex_09_05_02_even_numbers.py)</sub>

### Solution 10.5.3 — Counting down

**Bug type:** Logical

To count downward, `range` needs a negative step; `range(5, 0)` counts *up* and produces nothing because 5 is already past 0. Use `range(5, 0, -1)`.

```python
for number in range(5, 0, -1):
    print(number)
```

<sub>[Exercise](find-the-bug.md#exercise-953--counting-down) · [Runnable file](code/find_the_bug/ex_09_05_03_counting_down.py)</sub>

### Solution 10.5.4 — Sum of first ten numbers

**Bug type:** Logical

`range(1, 10)` stops at 9, so 10 is left out and the total is 45. Use `range(1, 11)` to include 10.

```python
total = 0

for number in range(1, 11):
    total += number

print(total)
```

<sub>[Exercise](find-the-bug.md#exercise-954--sum-of-first-ten-numbers) · [Runnable file](code/find_the_bug/ex_09_05_04_sum_of_first_ten_numbers.py)</sub>

### Solution 10.5.5 — Three repetitions

**Bug type:** Logical

`range(3)` runs three times, but the extra `print(count)` also prints the index each pass, which was not intended. Removing that line prints `Hello` three times.

```python
for count in range(3):
    print("Hello")
```

<sub>[Exercise](find-the-bug.md#exercise-955--three-repetitions) · [Runnable file](code/find_the_bug/ex_09_05_05_three_repetitions.py)</sub>

## 9.6 `while` Loops

### Solution 10.6.1 — Counting with while

**Bug type:** Runtime

The loop never updates `count`, so the condition stays true forever—an infinite loop. Incrementing `count` each pass lets it terminate.

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

<sub>[Exercise](find-the-bug.md#exercise-961--counting-with-while) · [Runnable file](code/find_the_bug/ex_09_06_01_counting_with_while.py)</sub>

### Solution 10.6.2 — Countdown

**Bug type:** Runtime

`count += 1` moves away from the stop condition, so `count > 0` never becomes false—an infinite loop. Use `count -= 1` to count down.

```python
count = 3

while count > 0:
    print(count)
    count -= 1

print("Liftoff")
```

<sub>[Exercise](find-the-bug.md#exercise-962--countdown) · [Runnable file](code/find_the_bug/ex_09_06_02_countdown.py)</sub>

### Solution 10.6.3 — Doubling savings

**Bug type:** Logical

`balance + 2` adds a fixed 2 each pass instead of *doubling*, so the balance grows 1, 3, 5, 7, ... and the values are wrong. Multiplying by 2 doubles it as intended.

```python
balance = 1

while balance < 8:
    print(balance)
    balance = balance * 2
```

<sub>[Exercise](find-the-bug.md#exercise-963--doubling-savings) · [Runnable file](code/find_the_bug/ex_09_06_03_doubling_savings.py)</sub>

### Solution 10.6.4 — Loop condition

**Bug type:** Logical

`while count < 5` stops after printing 4, so 5 is never reached. Use `<=` to include 5.

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

<sub>[Exercise](find-the-bug.md#exercise-964--loop-condition) · [Runnable file](code/find_the_bug/ex_09_06_04_loop_condition.py)</sub>

### Solution 10.6.5 — Sum until limit

**Bug type:** Logical

`number` is incremented *before* being added, so the loop adds 2+3+4+5 = 14 and skips 1. Adding first, then incrementing, sums 1+2+3+4 = 10.

```python
total = 0
number = 1

while total < 10:
    total += number
    number += 1

print(total)
```

<sub>[Exercise](find-the-bug.md#exercise-965--sum-until-limit) · [Runnable file](code/find_the_bug/ex_09_06_05_sum_until_limit.py)</sub>

## 9.7 `break`

### Solution 10.7.1 — Stop at the target

**Bug type:** Logical

`continue` only skips 3 and keeps going (printing 4, 5), but the program should stop entirely before 3. Use `break` to exit the loop.

```python
for number in range(1, 6):
    if number == 3:
        break
    print(number)
```

<sub>[Exercise](find-the-bug.md#exercise-971--stop-at-the-target) · [Runnable file](code/find_the_bug/ex_09_07_01_stop_at_the_target.py)</sub>

### Solution 10.7.2 — First over budget

**Bug type:** Logical

`break` is not indented inside the `if`, so it runs on the very first item and the loop stops before finding 150. Indenting `break` under the `if` makes it exit only after a match.

```python
expenses = [40, 80, 150, 90]

for expense in expenses:
    if expense > 100:
        print("Over budget:", expense)
        break
```

<sub>[Exercise](find-the-bug.md#exercise-972--first-over-budget) · [Runnable file](code/find_the_bug/ex_09_07_02_first_over_budget.py)</sub>

### Solution 10.7.3 — Search for a name

**Bug type:** Runtime

`brake` is a misspelling of `break`, so Python raises a `NameError`. Correcting the keyword fixes it.

```python
names = ["Sam", "Ana", "Leo"]

for name in names:
    if name == "Ana":
        print("Found")
        break
```

<sub>[Exercise](find-the-bug.md#exercise-973--search-for-a-name) · [Runnable file](code/find_the_bug/ex_09_07_03_search_for_a_name.py)</sub>

### Solution 10.7.4 — First even number

**Bug type:** Logical

`break` runs before the `print`, so nothing is ever shown. Print the number first, then break.

```python
numbers = [3, 7, 4, 6]

for number in numbers:
    if number % 2 == 0:
        print(number)
        break
```

<sub>[Exercise](find-the-bug.md#exercise-974--first-even-number) · [Runnable file](code/find_the_bug/ex_09_07_04_first_even_number.py)</sub>

### Solution 10.7.5 — Stop at zero

**Bug type:** Logical

`continue` merely skips the 0 and keeps going (printing 3 afterward), but the loop should stop at 0. Use `break`.

```python
readings = [5, 8, 0, 3]

for reading in readings:
    if reading == 0:
        break
    print(reading)
```

<sub>[Exercise](find-the-bug.md#exercise-975--stop-at-zero) · [Runnable file](code/find_the_bug/ex_09_07_05_stop_at_zero.py)</sub>

## 9.8 `continue`

### Solution 10.8.1 — Skip the empty entries

**Bug type:** Logical

`break` stops the loop at the first empty string, so "dog" is never printed. To skip just the empty entries and continue, use `continue`.

```python
words = ["cat", "", "dog", ""]

for word in words:
    if word == "":
        continue
    print(word)
```

<sub>[Exercise](find-the-bug.md#exercise-981--skip-the-empty-entries) · [Runnable file](code/find_the_bug/ex_09_08_01_skip_the_empty_entries.py)</sub>

### Solution 10.8.2 — Skip one value

**Bug type:** Logical

`pass` does nothing, so 3 is still printed. To actually skip it, use `continue`.

```python
for number in range(1, 7):
    if number == 3:
        continue
    print(number)
```

<sub>[Exercise](find-the-bug.md#exercise-982--skip-one-value) · [Runnable file](code/find_the_bug/ex_09_08_02_skip_one_value.py)</sub>

### Solution 10.8.3 — Sum positive numbers

**Bug type:** Logical

The `continue` after `total += number` is harmless, but `print(total + 1)` adds an extra 1, giving 10 instead of 9. Printing `total` gives the correct sum.

```python
numbers = [4, -2, 5, -1]
total = 0

for number in numbers:
    if number < 0:
        continue
    total += number

print(total)
```

<sub>[Exercise](find-the-bug.md#exercise-983--sum-positive-numbers) · [Runnable file](code/find_the_bug/ex_09_08_03_sum_positive_numbers.py)</sub>

### Solution 10.8.4 — Skip the indentation

**Bug type:** Syntax

The `continue` under the `if` is not indented, so Python raises an `IndentationError`. Indenting it inside the `if` fixes the parse.

```python
for number in range(1, 7):
    if number % 2 == 0:
        continue
    print(number)
```

<sub>[Exercise](find-the-bug.md#exercise-984--skip-the-indentation) · [Runnable file](code/find_the_bug/ex_09_08_04_skip_the_indentation.py)</sub>

### Solution 10.8.5 — Skip a specific student

**Bug type:** Logical

The condition skips everyone *except* Leo, so only Leo is printed—the opposite of what we want. Skip when the name *is* Leo by using `==`.

```python
names = ["Ana", "Leo", "Sam"]

for name in names:
    if name == "Leo":
        continue
    print(name)
```

<sub>[Exercise](find-the-bug.md#exercise-985--skip-a-specific-student) · [Runnable file](code/find_the_bug/ex_09_08_05_skip_a_specific_student.py)</sub>

## 9.9 `pass`

### Solution 10.9.1 — Placeholder for later

**Bug type:** Syntax

The `if` body is empty, so Python raises an `IndentationError`. A placeholder body needs `pass`.

```python
for item in [1, 2, 3]:
    if item == 2:
        pass
    print(item)
```

<sub>[Exercise](find-the-bug.md#exercise-991--placeholder-for-later) · [Runnable file](code/find_the_bug/ex_09_09_01_placeholder_for_later.py)</sub>

### Solution 10.9.2 — Empty function

**Bug type:** Syntax

A function with an empty body is illegal; Python raises an `IndentationError`. Adding `pass` as the placeholder body fixes it.

```python
def future_feature():
    pass

future_feature()
print("Done")
```

<sub>[Exercise](find-the-bug.md#exercise-992--empty-function) · [Runnable file](code/find_the_bug/ex_09_09_02_empty_function.py)</sub>

### Solution 10.9.3 — Doing nothing where logic was needed

**Bug type:** Logical

The loop body is left as `pass`, so nothing is added and the total stays 0. The real work—accumulating the prices—must replace the placeholder.

```python
prices = [10, 20, 30]
total = 0

for price in prices:
    total += price

print(total)
```

<sub>[Exercise](find-the-bug.md#exercise-993--doing-nothing-where-logic-was-needed) · [Runnable file](code/find_the_bug/ex_09_09_03_doing_nothing_where_logic_was_needed.py)</sub>

### Solution 10.9.4 — Placeholder branch

**Bug type:** Logical

After `pass` (which does nothing), the indented `print(reading)` still runs, so negative readings are printed too. Removing that stray `print` leaves the branch as a true placeholder.

```python
readings = [5, -3, 8]

for reading in readings:
    if reading < 0:
        pass
    else:
        print(reading)
```

<sub>[Exercise](find-the-bug.md#exercise-994--placeholder-branch) · [Runnable file](code/find_the_bug/ex_09_09_04_placeholder_branch.py)</sub>

### Solution 10.9.5 — Stub class

**Bug type:** Runtime

`pas` is a typo for the keyword `pass`; Python reads it as a reference to an undefined name, so executing the class body raises a `NameError`. Correct the spelling to `pass`.

```python
class Sensor:
    pass

print("Ready")
```

<sub>[Exercise](find-the-bug.md#exercise-995--stub-class) · [Runnable file](code/find_the_bug/ex_09_09_05_stub_class.py)</sub>

## 9.10 `match` / `case`

### Solution 10.10.1 — Matching a command

**Bug type:** Syntax

The first `case` line is missing its colon. Adding it fixes the parse.

```python
command = "start"

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case _:
        print("Unknown command")
```

<sub>[Exercise](find-the-bug.md#exercise-9101--matching-a-command) · [Runnable file](code/find_the_bug/ex_09_10_01_matching_a_command.py)</sub>

### Solution 10.10.2 — Weekend or weekday

**Bug type:** Syntax

In a `case` pattern, alternatives are joined with `|`, not the keyword `or`. Using `|` fixes the pattern.

```python
day = "Monday"

match day:
    case "Saturday" | "Sunday":
        print("Weekend")
    case _:
        print("Weekday")
```

<sub>[Exercise](find-the-bug.md#exercise-9102--weekend-or-weekday) · [Runnable file](code/find_the_bug/ex_09_10_02_weekend_or_weekday.py)</sub>

### Solution 10.10.3 — Locating a point

**Bug type:** Logical

The catch-all `(x, y)` pattern matches *any* pair, so it is reached before the specific y-axis case and (0, 5) is wrongly labelled ``Somewhere else''. The general pattern must come last, after the specific ones.

```python
point = (0, 5)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print("On the y-axis at", y)
    case (x, y):
        print("Somewhere else:", x, y)
```

<sub>[Exercise](find-the-bug.md#exercise-9103--locating-a-point) · [Runnable file](code/find_the_bug/ex_09_10_03_locating_a_point.py)</sub>

### Solution 10.10.4 — Default case

**Bug type:** Logical

`case "_"` matches the literal string `"_"`, not ``anything else''. The wildcard default is the bare `_` with no quotes.

```python
command = "fly"

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case _:
        print("Unknown command")
```

<sub>[Exercise](find-the-bug.md#exercise-9104--default-case) · [Runnable file](code/find_the_bug/ex_09_10_04_default_case.py)</sub>

### Solution 10.10.5 — Traffic light

**Bug type:** Logical

The default case builds the string `"Unknown"` but never prints it, so an unrecognized colour produces no output. Adding `print` produces the expected output.

```python
color = "blue"

match color:
    case "green":
        print("Go")
    case "yellow":
        print("Slow down")
    case "red":
        print("Stop")
    case _:
        print("Unknown")
```

<sub>[Exercise](find-the-bug.md#exercise-9105--traffic-light) · [Runnable file](code/find_the_bug/ex_09_10_05_traffic_light.py)</sub>

## 9.11 Functions and `return`

### Solution 10.11.1 — Even check

**Bug type:** Logical

The function computes `number % 2 == 0` but never returns it, so it returns `None`. Adding `return` sends the result back.

```python
def is_even(number):
    return number % 2 == 0

print(is_even(4))
```

<sub>[Exercise](find-the-bug.md#exercise-9111--even-check) · [Runnable file](code/find_the_bug/ex_09_11_01_even_check.py)</sub>

### Solution 10.11.2 — Describe a number

**Bug type:** Logical

The negative branch builds the string `"negative"` but never returns it, so `describe(-3)` falls off that branch and returns `None`. Adding `return` fixes it.

```python
def describe(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"

print(describe(-3))
```

<sub>[Exercise](find-the-bug.md#exercise-9112--describe-a-number) · [Runnable file](code/find_the_bug/ex_09_11_02_describe_a_number.py)</sub>

### Solution 10.11.3 — First match returns

**Bug type:** Logical

The function `print`s the match instead of returning it, so `first_big` returns `None`. Replacing `print` with `return` sends the value back to the caller.

```python
def first_big(numbers):
    for number in numbers:
        if number > 10:
            return number

print(first_big([4, 15, 22]))
```

<sub>[Exercise](find-the-bug.md#exercise-9113--first-match-returns) · [Runnable file](code/find_the_bug/ex_09_11_03_first_match_returns.py)</sub>

### Solution 10.11.4 — Total with tax

**Bug type:** Logical

The function returns `price` before computing the total, so the line after `return` never runs. Returning `price + tax` gives the taxed total.

```python
def with_tax(price):
    tax = price * 0.10
    total = price + tax
    return total

print(with_tax(100))
```

<sub>[Exercise](find-the-bug.md#exercise-9114--total-with-tax) · [Runnable file](code/find_the_bug/ex_09_11_04_total_with_tax.py)</sub>

### Solution 10.11.5 — Absolute value

**Bug type:** Logical

When the number is not negative there is no `return`, so the function falls off the end and returns `None`. Adding an `else` (or a final `return number`) handles the non-negative case.

```python
def absolute(number):
    if number < 0:
        return -number
    else:
        return number

print(absolute(7))
```

<sub>[Exercise](find-the-bug.md#exercise-9115--absolute-value) · [Runnable file](code/find_the_bug/ex_09_11_05_absolute_value.py)</sub>
