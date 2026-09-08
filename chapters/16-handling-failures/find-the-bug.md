# Chapter 16 — Handling Failures: Find the Bug

Part VI · Quality — *Everyday Programming*

Each program below uses Python's exception handling (`try`, `except`, `else`, `finally`) to recover from failures, but each one hides exactly one bug — find it.

Read each program, decide what it is supposed to print, and find the one line that stops it. Then check yourself against [the solutions](solutions.md). The corrected programs are also available as runnable files under [`code/find_the_bug/`](code/find_the_bug).

**20 exercises in 4 sections.**

## 16.1 Handling Bad User Input

### Exercise 16.1.1 — Reading an age

This program should keep asking until the user types a whole number for their age, then print it.

```python
while True:
    raw = input("Enter your age in years: ")
    age = int(raw)
    try:
        print("Your age is", age)
        break
    except ValueError:
        print("That was not a whole number. Try again.")
```

<sub>[Solution](solutions.md#solution-1611--reading-an-age)</sub>

### Exercise 16.1.2 — Parsing a price

This program should read a price like `"4.99"` and print double it, recovering from bad input.

```python
try:
    price = float(input("Enter a price in dollars: "))
    print("Two of those cost", 2 * price)
except VlaueError:
    print("That was not a valid price.")
```

<sub>[Solution](solutions.md#solution-1612--parsing-a-price)</sub>

### Exercise 16.1.3 — Counting jellybeans

This program reads how many jellybeans are in a jar and prints the count, retrying on bad input.

```python
while True:
    try:
        beans = int(input("How many jellybeans? "))
        print("There are", beans, "jellybeans.")
    except ValueError:
        print("Please type a whole number.")
```

<sub>[Solution](solutions.md#solution-1613--counting-jellybeans)</sub>

### Exercise 16.1.4 — Temperature reading

This program reads a Celsius temperature and converts it to Fahrenheit, handling bad input.

```python
try:
    celsius = float(input("Temperature in Celsius? "))
    fahrenheit = celsius * 9 / 5 + 32
    print("That is", fahrenheit, "degrees Fahrenheit.")
except ValueError
    print("That was not a valid number.")
```

<sub>[Solution](solutions.md#solution-1614--temperature-reading)</sub>

### Exercise 16.1.5 — Validating a test score

This program should accept a score the user types only if it is a whole number, then print it.

```python
raw = input("Enter your test score: ")
try:
    score = int(raw)
except ValueError:
    score = raw
print("Your score is", score)
```

<sub>[Solution](solutions.md#solution-1615--validating-a-test-score)</sub>

## 16.2 Handling Different Kinds of Errors

### Exercise 16.2.1 — Splitting a bill

This program divides a restaurant bill among friends and should report when there are zero friends.

```python
bill = 60.0
friends = 0
try:
    share = bill / friends
    print("Each person pays", share)
except ValueError:
    print("There must be at least one person.")
```

<sub>[Solution](solutions.md#solution-1621--splitting-a-bill)</sub>

### Exercise 16.2.2 — Adding a measurement

This program adds a typed measurement to a running total and warns if the text is not a number.

```python
total = 100
new_value = "twelve"
try:
    total = total + new_value
except ZeroDivisionError:
    print("That measurement was not a number.")
print("Total is", total)
```

<sub>[Solution](solutions.md#solution-1622--adding-a-measurement)</sub>

### Exercise 16.2.3 — Average speed

This program reads a distance and a time, divides to get average speed, and should report a typed-in non-number and a zero time with separate messages.

```python
distance = float(input("Distance in meters? "))
time = float(input("Time in seconds? "))
try:
    speed = distance / time
    print("Average speed:", speed)
except Exception:
    print("Distance was not a number.")
except ZeroDivisionError:
    print("Time cannot be zero.")
```

<sub>[Solution](solutions.md#solution-1623--average-speed)</sub>

### Exercise 16.2.4 — Looking up a grade

This program looks up a student's grade in a dictionary and reports a clear message if the name is missing.

```python
grades = {"Ann": 91, "Bo": 84}
name = "Cleo"
try:
    print(name, "scored", grades[name])
except ValueError:
    print("No grade recorded for", name)
```

<sub>[Solution](solutions.md#solution-1624--looking-up-a-grade)</sub>

### Exercise 16.2.5 — Percent off

This program reads a typed divisor, builds a fraction from it, and should report a non-number and a zero divisor with separate messages.

```python
price = 50
divisor = input("Divide the discount by? ")
try:
    fraction = 100 / int(divisor)
    print("You pay", price * fraction)
except Exception:
    print("That was not a valid number.")
except ZeroDivisionError:
    print("The divisor cannot be zero.")
```

<sub>[Solution](solutions.md#solution-1625--percent-off)</sub>

## 16.3 Using `else`

### Exercise 16.3.1 — Confirming a conversion

This program converts a string to a number and, only when that succeeds, prints a success line.

```python
text = "42"
try:
    number = int(text)
    print("Conversion worked:", number)
except ValueError:
    print("That was not a number.")
else:
    print("Conversion worked:", number)
```

<sub>[Solution](solutions.md#solution-1631--confirming-a-conversion)</sub>

### Exercise 16.3.2 — Area of a rectangle

This program reads two side lengths and, if both parse, prints the area in the `else` block.

```python
try:
    width = float(input("Width? "))
    height = float(input("Height? "))
except ValueError:
    print("Both sides must be numbers.")
else:
    area = width * height
```

<sub>[Solution](solutions.md#solution-1632--area-of-a-rectangle)</sub>

### Exercise 16.3.3 — Doubling a recipe

This program reads a cup amount and, when valid, prints the doubled amount using `else`.

```python
try:
    cups = float(input("How many cups? "))
    doubled = cups * 2
    print("You need", doubled, "cups.")
except ValueError:
    print("That was not a number.")
else:
    print("Measurement accepted.")
```

<sub>[Solution](solutions.md#solution-1633--doubling-a-recipe)</sub>

### Exercise 16.3.4 — Safe square root

This program reads a number and, only if it parses, prints its square root in the `else` block.

```python
import math

try
    value = float(input("Enter a number: "))
except ValueError:
    print("That was not a number.")
else:
    print("Square root is", math.sqrt(value))
```

<sub>[Solution](solutions.md#solution-1634--safe-square-root)</sub>

### Exercise 16.3.5 — Tax on a purchase

This program parses a purchase amount and, when it succeeds, computes 8 percent tax in the `else` block.

```python
try:
    amount = float(input("Purchase amount? "))
except ValueError:
    print("That was not a number.")
else:
    tax = amount + 0.08
    print("Tax is", tax)
```

<sub>[Solution](solutions.md#solution-1635--tax-on-a-purchase)</sub>

## 16.4 Using `finally`

### Exercise 16.4.1 — Closing a report

This program divides two numbers and should always print a closing line, whether or not the division fails.

```python
try:
    result = 10 / 2
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero.")
    print("Done with the calculation.")
```

<sub>[Solution](solutions.md#solution-1641--closing-a-report)</sub>

### Exercise 16.4.2 — Releasing the scale

This program weighs an item and must always print that the scale is released, even when input is bad.

```python
try:
    weight = float(input("Weight in kilograms? "))
    print("Recorded weight:", weight)
except ValueError:
    print("That was not a number.")
else:
    print("Scale released.")
```

<sub>[Solution](solutions.md#solution-1642--releasing-the-scale)</sub>

### Exercise 16.4.3 — Logging an attempt

This program parses a count and must always log that an attempt was made, regardless of success.

```python
try:
    count = int(input("How many items? "))
    print("Count:", count)
except ValueError:
    print("Not a whole number.")
finally
    print("Attempt logged.")
```

<sub>[Solution](solutions.md#solution-1643--logging-an-attempt)</sub>

### Exercise 16.4.4 — Final tally

Whatever happens above, this program must always print `Final tally complete.` at the end. With `rounds` set to 0 it currently does not.

```python
points = 90
rounds = 0
try:
    average = points / rounds
    print("Average:", average)
    print("Final tally complete.")
except ZeroDivisionError:
    print("No rounds played.")
```

<sub>[Solution](solutions.md#solution-1644--final-tally)</sub>

### Exercise 16.4.5 — Cleanup message

This program reads a distance and must always print a cleanup line at the very end, no matter what happens.

```python
try:
    distance = float(input("Distance in meters? "))
    print("Distance:", distance)
finally:
    print("Sensor reset.")
except ValueError:
    print("That was not a number.")
```

<sub>[Solution](solutions.md#solution-1645--cleanup-message)</sub>
