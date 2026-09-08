# Chapter 9 — Control Flow: Find the Bug

Part IV · Control Flow — *Everyday Programming*

These exercises cover Python's control-flow tools—branching, loops, and the keywords that steer them—and each program below contains exactly one bug for you to find and fix.

Read each program, decide what it is supposed to print, and find the one line that stops it. Then check yourself against [the solutions](solutions.md). The corrected programs are also available as runnable files under [`code/find_the_bug/`](code/find_the_bug).

**55 exercises in 11 sections.**

## 9.1 `if`, `elif`, `else`

### Exercise 9.1.1 — Grading with elif

This program should print the letter grade for a score. A score of 82 should print `Grade: B`.

```python
score = 82

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else
    print("Needs improvement")
```

<sub>[Solution](solutions.md#solution-911--grading-with-elif)</sub>

### Exercise 9.1.2 — Temperature category

This program should classify a temperature in Celsius. With 36.5 it should print only `Heat warning`.

```python
temp_c = 36.5

if temp_c > 35:
print("Heat warning")
elif temp_c < 0:
    print("Freezing")
else:
    print("Normal")
```

<sub>[Solution](solutions.md#solution-912--temperature-category)</sub>

### Exercise 9.1.3 — Independent checks that should be alternatives

A water sample's pH should be labelled once: acidic, neutral, or basic. With pH 6.0 it should print only `Acidic`.

```python
ph = 6.0

if ph < 7:
    print("Acidic")
if ph == 7:
    print("Neutral")
else:
    print("Basic")
```

<sub>[Solution](solutions.md#solution-913--independent-checks-that-should-be-alternatives)</sub>

### Exercise 9.1.4 — Pass or fail

This program should print `Pass` when a score is at least 60, otherwise `Fail`. With 75 it should print `Pass`.

```python
score = 75

if score >= 60:
    print("Pass")
    else:
    print("Fail")
```

<sub>[Solution](solutions.md#solution-914--pass-or-fail)</sub>

### Exercise 9.1.5 — Ticket price by age

This program should set a discounted price for children under 12 and a full price otherwise. A 10-year-old should pay 5.

```python
age = 10

if age < 12:
    price = 5
else:
    price = 12
    print("Ticket price:", price)
# Expected: Ticket price: 5
```

<sub>[Solution](solutions.md#solution-915--ticket-price-by-age)</sub>

## 9.2 Common Comparison Operators

### Exercise 9.2.1 — Exact match

This program should print `Correct` only when the answer equals 42.

```python
answer = 42

if answer = 42:
    print("Correct")
else:
    print("Try again")
```

<sub>[Solution](solutions.md#solution-921--exact-match)</sub>

### Exercise 9.2.2 — Freezing point

Water freezes at 0 degrees Celsius or below. This program should print `Frozen` for a temperature of 0.

```python
temp_c = 0

if temp_c < 0:
    print("Frozen")
else:
    print("Liquid")
# Expected: Frozen
```

<sub>[Solution](solutions.md#solution-922--freezing-point)</sub>

### Exercise 9.2.3 — Not equal

This program should print `Sold out` only when the remaining seats is not 0. With 0 seats it should print nothing.

```python
seats_left = 0

if seats_left == 0:
    print("Sold out")
# Expected: (no output)
```

<sub>[Solution](solutions.md#solution-923--not-equal)</sub>

### Exercise 9.2.4 — Speed limit check

A car at exactly the speed limit is allowed. This program should print `OK` when speed is at most 60. At 60 it should print `OK`.

```python
speed = 60
limit = 60

if speed < limit:
    print("OK")
else:
    print("Too fast")
# Expected: OK
```

<sub>[Solution](solutions.md#solution-924--speed-limit-check)</sub>

### Exercise 9.2.5 — Adult check

This program should print `Adult` for anyone 18 or older. An 18-year-old should print `Adult`.

```python
age = 18

if age > 18:
    print("Adult")
else:
    print("Minor")
# Expected: Adult
```

<sub>[Solution](solutions.md#solution-925--adult-check)</sub>

## 9.3 Logical Operators

### Exercise 9.3.1 — Entry rules

Entry is allowed only when a person is at least 18 *and* has an ID. With age 20 and no ID, this should print `Entry denied`.

```python
age = 20
has_id = False

if age >= 18 or has_id:
    print("Entry allowed")
else:
    print("Entry denied")
# Expected: Entry denied
```

<sub>[Solution](solutions.md#solution-931--entry-rules)</sub>

### Exercise 9.3.2 — Weekend check

This program should print `Relax` on Saturday or Sunday. For "Saturday" it should print `Relax`.

```python
day = "Saturday"

if day == "Saturday" and day == "Sunday":
    print("Relax")
# expected: Relax
```

<sub>[Solution](solutions.md#solution-932--weekend-check)</sub>

### Exercise 9.3.3 — Comfortable room

A room is comfortable when the temperature is between 20 and 25 degrees inclusive. At 30 degrees (too warm) this should print `Adjust the thermostat`.

```python
temp_c = 30

if temp_c >= 20 or temp_c <= 25:
    print("Comfortable")
else:
    print("Adjust the thermostat")
# expected: Adjust the thermostat
```

<sub>[Solution](solutions.md#solution-933--comfortable-room)</sub>

### Exercise 9.3.4 — Out of stock

This program should print `Reorder` when an item is not in stock. With stock False it should print `Reorder`.

```python
in_stock = False

if not in_stock = True:
    print("Reorder")
# Expected: Reorder
```

<sub>[Solution](solutions.md#solution-934--out-of-stock)</sub>

### Exercise 9.3.5 — Free shipping

Free shipping applies when the cart total is at least 50 or the customer is a member. A $30 order from a member should print `Free shipping`.

```python
total = 30
is_member = True

if total >= 50 and is_member:
    print("Free shipping")
else:
    print("Pay shipping")
# expected: Free shipping
```

<sub>[Solution](solutions.md#solution-935--free-shipping)</sub>

## 9.4 `for` Loops

### Exercise 9.4.1 — Sum of a list

This program should add up the prices in a cart and print the total, 60.

```python
prices = [10, 20, 30]
total = 0

for price in prices:
    total = price

print("Total:", total)
# Expected: Total: 60
```

<sub>[Solution](solutions.md#solution-941--sum-of-a-list)</sub>

### Exercise 9.4.2 — Counting vowels

This program should count the vowels in a word. For "education" it should print 5.

```python
word = "education"
vowels = "aeiou"
count = 0

for letter in word:
    if letter in vowels:
        count = count + 1

print(count + 1)
# Expected: 5
```

<sub>[Solution](solutions.md#solution-942--counting-vowels)</sub>

### Exercise 9.4.3 — Printing each fruit

This program should print each fruit in the list on its own line.

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits
    print(fruit)
```

<sub>[Solution](solutions.md#solution-943--printing-each-fruit)</sub>

### Exercise 9.4.4 — Average of readings

This program should print the average of three temperature readings, 30.0.

```python
readings = [28, 30, 32]
total = 0

for reading in readings:
    total += reading

average = total / len(reading)
print(average)
# Expected: 30.0
```

<sub>[Solution](solutions.md#solution-944--average-of-readings)</sub>

### Exercise 9.4.5 — Largest measurement

This program should find the largest of several distances and print it, 45.

```python
distances = [12, 45, 9, 33]
largest = 0

for distance in distances:
    if distance < largest:
        largest = distance

print(largest)
# Expected: 45
```

<sub>[Solution](solutions.md#solution-945--largest-measurement)</sub>

## 9.5 `range`

### Exercise 9.5.1 — Counting to five

Using `range`, this program should print the numbers 1 through 5.

```python
for number in range(1, 5):
    print(number)
# Expected: 1 2 3 4 5 (one per line)
```

<sub>[Solution](solutions.md#solution-951--counting-to-five)</sub>

### Exercise 9.5.2 — Even numbers

This program should print the even numbers from 2 up to 10 using a step.

```python
for number in range(2, 11, 1):
    print(number)
# Expected: 2 4 6 8 10 (one per line)
```

<sub>[Solution](solutions.md#solution-952--even-numbers)</sub>

### Exercise 9.5.3 — Counting down

This program should count down from 5 to 1.

```python
for number in range(5, 0):
    print(number)
# Expected: 5 4 3 2 1 (one per line)
```

<sub>[Solution](solutions.md#solution-953--counting-down)</sub>

### Exercise 9.5.4 — Sum of first ten numbers

This program should add the numbers 1 through 10 and print 55.

```python
total = 0

for number in range(1, 10):
    total += number

print(total)
# Expected: 55
```

<sub>[Solution](solutions.md#solution-954--sum-of-first-ten-numbers)</sub>

### Exercise 9.5.5 — Three repetitions

This program should print `Hello` exactly three times.

```python
for count in range(3):
    print("Hello")
    print(count)
# Expected: Hello printed 3 times
```

<sub>[Solution](solutions.md#solution-955--three-repetitions)</sub>

## 9.6 `while` Loops

### Exercise 9.6.1 — Counting with while

This program should print the numbers 1 through 5 using a `while` loop.

```python
count = 1

while count <= 5:
    print(count)

# Expected: 1 2 3 4 5 (one per line)
```

<sub>[Solution](solutions.md#solution-961--counting-with-while)</sub>

### Exercise 9.6.2 — Countdown

This program should count down from 3 to 1 and then print `Liftoff`.

```python
count = 3

while count > 0:
    print(count)
    count += 1

print("Liftoff")
# Expected: 3 2 1 then Liftoff
```

<sub>[Solution](solutions.md#solution-962--countdown)</sub>

### Exercise 9.6.3 — Doubling savings

Starting at $1, this should double the balance until it reaches at least $8, printing each balance.

```python
balance = 1

while balance < 8:
    print(balance)
    balance = balance + 2

# Expected: 1 2 4 (one per line)
```

<sub>[Solution](solutions.md#solution-963--doubling-savings)</sub>

### Exercise 9.6.4 — Loop condition

This program should print the numbers 1 through 5.

```python
count = 1

while count < 5:
    print(count)
    count += 1
# Expected: 1 2 3 4 5
```

<sub>[Solution](solutions.md#solution-964--loop-condition)</sub>

### Exercise 9.6.5 — Sum until limit

This program should add 1, 2, 3, ... until the total reaches at least 10, then print the total, 10.

```python
total = 0
number = 1

while total < 10:
    number += 1
    total += number

print(total)
# Expected: 10
```

<sub>[Solution](solutions.md#solution-965--sum-until-limit)</sub>

## 9.7 `break`

### Exercise 9.7.1 — Stop at the target

This program should print numbers from 1 and stop *before* printing 3, so it prints 1 and 2.

```python
for number in range(1, 6):
    if number == 3:
        continue
    print(number)
# Expected: 1 2
```

<sub>[Solution](solutions.md#solution-971--stop-at-the-target)</sub>

### Exercise 9.7.2 — First over budget

This program should print the first expense that is over 100 and then stop.

```python
expenses = [40, 80, 150, 90]

for expense in expenses:
    if expense > 100:
        print("Over budget:", expense)
    break
# Expected: Over budget: 150
```

<sub>[Solution](solutions.md#solution-972--first-over-budget)</sub>

### Exercise 9.7.3 — Search for a name

This program should stop as soon as it finds "Ana" and print `Found`.

```python
names = ["Sam", "Ana", "Leo"]

for name in names:
    if name == "Ana":
        print("Found")
        brake
```

<sub>[Solution](solutions.md#solution-973--search-for-a-name)</sub>

### Exercise 9.7.4 — First even number

This program should print the first even number in the list and stop. For these numbers it should print 4.

```python
numbers = [3, 7, 4, 6]

for number in numbers:
    if number % 2 == 0:
        break
        print(number)
# Expected: 4
```

<sub>[Solution](solutions.md#solution-974--first-even-number)</sub>

### Exercise 9.7.5 — Stop at zero

This program should print readings until it hits a 0, then stop. It should print 5 and 8.

```python
readings = [5, 8, 0, 3]

for reading in readings:
    if reading == 0:
        continue
    print(reading)
# Expected: 5 8
```

<sub>[Solution](solutions.md#solution-975--stop-at-zero)</sub>

## 9.8 `continue`

### Exercise 9.8.1 — Skip the empty entries

This program should print every non-empty word in the list.

```python
words = ["cat", "", "dog", ""]

for word in words:
    if word == "":
        break
    print(word)
# Expected: cat dog
```

<sub>[Solution](solutions.md#solution-981--skip-the-empty-entries)</sub>

### Exercise 9.8.2 — Skip one value

This program should print 1, 2, 4, 5, 6, skipping only 3.

```python
for number in range(1, 7):
    if number == 3:
        pass
    print(number)
# Expected: 1 2 4 5 6
```

<sub>[Solution](solutions.md#solution-982--skip-one-value)</sub>

### Exercise 9.8.3 — Sum positive numbers

This program should add only the positive numbers and print 9.

```python
numbers = [4, -2, 5, -1]
total = 0

for number in numbers:
    if number < 0:
        continue
    total += number
    continue

print(total + 1)
# Expected: 9
```

<sub>[Solution](solutions.md#solution-983--sum-positive-numbers)</sub>

### Exercise 9.8.4 — Skip the indentation

This program should print every odd number from 1 to 6, skipping the even ones.

```python
for number in range(1, 7):
    if number % 2 == 0:
    continue
    print(number)
# Expected: 1 3 5
```

<sub>[Solution](solutions.md#solution-984--skip-the-indentation)</sub>

### Exercise 9.8.5 — Skip a specific student

This program should print every name except "Leo".

```python
names = ["Ana", "Leo", "Sam"]

for name in names:
    if name != "Leo":
        continue
    print(name)
# Expected: Ana Sam
```

<sub>[Solution](solutions.md#solution-985--skip-a-specific-student)</sub>

## 9.9 `pass`

### Exercise 9.9.1 — Placeholder for later

The `if` branch is a planned feature not yet written, so it should do nothing for now; the program should still print every item.

```python
for item in [1, 2, 3]:
    if item == 2:

    print(item)
# Expected: 1 2 3
```

<sub>[Solution](solutions.md#solution-991--placeholder-for-later)</sub>

### Exercise 9.9.2 — Empty function

This empty helper is a placeholder, and the program should print `Done`.

```python
def future_feature():

future_feature()
print("Done")
# Expected: Done
```

<sub>[Solution](solutions.md#solution-992--empty-function)</sub>

### Exercise 9.9.3 — Doing nothing where logic was needed

This program should add up the prices and print the total, 60, but the loop body was left as a placeholder.

```python
prices = [10, 20, 30]
total = 0

for price in prices:
    pass

print(total)
# Expected: 60
```

<sub>[Solution](solutions.md#solution-993--doing-nothing-where-logic-was-needed)</sub>

### Exercise 9.9.4 — Placeholder branch

For now, negative readings should be ignored (handled later) while others are printed. With this data it should print 5 and 8.

```python
readings = [5, -3, 8]

for reading in readings:
    if reading < 0:
        pass
        print(reading)
    else:
        print(reading)
# Expected: 5 8
```

<sub>[Solution](solutions.md#solution-994--placeholder-branch)</sub>

### Exercise 9.9.5 — Stub class

This program defines a placeholder class and should print `Ready`.

```python
class Sensor:
    pas

print("Ready")
# Expected: Ready
```

<sub>[Solution](solutions.md#solution-995--stub-class)</sub>

## 9.10 `match` / `case`

### Exercise 9.10.1 — Matching a command

This program should respond to a command. For "start" it should print `Starting...`.

```python
command = "start"

match command:
    case "start"
        print("Starting...")
    case "stop":
        print("Stopping...")
    case _:
        print("Unknown command")
```

<sub>[Solution](solutions.md#solution-9101--matching-a-command)</sub>

### Exercise 9.10.2 — Weekend or weekday

This program should print `Weekend` for Saturday or Sunday and `Weekday` otherwise. For "Monday" it should print `Weekday`.

```python
day = "Monday"

match day:
    case "Saturday" or "Sunday":
        print("Weekend")
    case _:
        print("Weekday")
# Expected: Weekday
```

<sub>[Solution](solutions.md#solution-9102--weekend-or-weekday)</sub>

### Exercise 9.10.3 — Locating a point

This program should describe a point. For (0, 5) it should print `On the y-axis at 5`.

```python
point = (0, 5)

match point:
    case (0, 0):
        print("Origin")
    case (x, y):
        print("Somewhere else:", x, y)
    case (0, y):
        print("On the y-axis at", y)
# Expected: On the y-axis at 5
```

<sub>[Solution](solutions.md#solution-9103--locating-a-point)</sub>

### Exercise 9.10.4 — Default case

This program should print `Unknown command` for anything it does not recognize. For "fly" it should print `Unknown command`.

```python
command = "fly"

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case "_":
        print("Unknown command")
# Expected: Unknown command
```

<sub>[Solution](solutions.md#solution-9104--default-case)</sub>

### Exercise 9.10.5 — Traffic light

This program should print the action for a traffic light colour. For an unknown colour like "blue" it should print `Unknown`.

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
        "Unknown"
# Expected: Unknown
```

<sub>[Solution](solutions.md#solution-9105--traffic-light)</sub>

## 9.11 Functions and `return`

### Exercise 9.11.1 — Even check

This function should return `True` when a number is even. `is_even(4)` should print `True`.

```python
def is_even(number):
    number % 2 == 0

print(is_even(4))
# Expected: True
```

<sub>[Solution](solutions.md#solution-9111--even-check)</sub>

### Exercise 9.11.2 — Describe a number

This function should return "positive", "negative", or "zero". `describe(-3)` should print `negative`.

```python
def describe(number):
    if number > 0:
        return "positive"
    elif number < 0:
        "negative"
    else:
        return "zero"

print(describe(-3))
# Expected: negative
```

<sub>[Solution](solutions.md#solution-9112--describe-a-number)</sub>

### Exercise 9.11.3 — First match returns

This function should return the first number greater than 10, or `None`. For this list it should print 15.

```python
def first_big(numbers):
    for number in numbers:
        if number > 10:
            print(number)

print(first_big([4, 15, 22]))
# Expected: 15
```

<sub>[Solution](solutions.md#solution-9113--first-match-returns)</sub>

### Exercise 9.11.4 — Total with tax

This function should return the price plus 10% tax. `with_tax(100)` should print `110.0`.

```python
def with_tax(price):
    tax = price * 0.10
    return price
    total = price + tax

print(with_tax(100))
# Expected: 110.0
```

<sub>[Solution](solutions.md#solution-9114--total-with-tax)</sub>

### Exercise 9.11.5 — Absolute value

This function should return the absolute value of a number. `absolute(7)` should print `7`.

```python
def absolute(number):
    if number < 0:
        return -number

print(absolute(7))
# Expected: 7
```

<sub>[Solution](solutions.md#solution-9115--absolute-value)</sub>
