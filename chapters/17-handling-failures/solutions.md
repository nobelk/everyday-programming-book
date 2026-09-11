# Chapter 17 — Handling Failures: Find the Bug, Solutions

Each solution names the bug type — **syntax**, **runtime**, or **logical** — explains why the original program misbehaved, and shows the corrected program.

Back to [the exercises](find-the-bug.md).

## 16.1 Handling Bad User Input

### Solution 17.1.1 — Reading an age

**Bug type:** Runtime

The `int(raw)` call happens *outside* the `try`, so a non-numeric entry raises `ValueError` before the `except` can catch it and the program crashes. Move the conversion inside the `try` so the failing line is actually protected.

```python
while True:
    raw = input("Enter your age in years: ")
    try:
        age = int(raw)
        print("Your age is", age)
        break
    except ValueError:
        print("That was not a whole number. Try again.")
```

<sub>[Exercise](find-the-bug.md#exercise-1611--reading-an-age) · [Runnable file](code/find_the_bug/ex_16_01_01_reading_an_age.py)</sub>

### Solution 17.1.2 — Parsing a price

**Bug type:** Runtime

The exception name is misspelled `VlaueError`, which Python treats as an unknown name; when `float` raises the real `ValueError` it is not caught and the program crashes (and the wrong name itself raises `NameError`). Spell it `ValueError`.

```python
try:
    price = float(input("Enter a price in dollars: "))
    print("Two of those cost", 2 * price)
except ValueError:
    print("That was not a valid price.")
```

<sub>[Exercise](find-the-bug.md#exercise-1612--parsing-a-price) · [Runnable file](code/find_the_bug/ex_16_01_02_parsing_a_price.py)</sub>

### Solution 17.1.3 — Counting jellybeans

**Bug type:** Logical

There is no `break` after a successful read, so even on valid input the `while True` loop never ends — it keeps re-asking forever. Add `break` once a valid count is printed.

```python
while True:
    try:
        beans = int(input("How many jellybeans? "))
        print("There are", beans, "jellybeans.")
        break
    except ValueError:
        print("Please type a whole number.")
```

<sub>[Exercise](find-the-bug.md#exercise-1613--counting-jellybeans) · [Runnable file](code/find_the_bug/ex_16_01_03_counting_jellybeans.py)</sub>

### Solution 17.1.4 — Temperature reading

**Bug type:** Syntax

The `except ValueError` line is missing its colon, so the file will not parse. Add the colon.

```python
try:
    celsius = float(input("Temperature in Celsius? "))
    fahrenheit = celsius * 9 / 5 + 32
    print("That is", fahrenheit, "degrees Fahrenheit.")
except ValueError:
    print("That was not a valid number.")
```

<sub>[Exercise](find-the-bug.md#exercise-1614--temperature-reading) · [Runnable file](code/find_the_bug/ex_16_01_04_temperature_reading.py)</sub>

### Solution 17.1.5 — Validating a test score

**Bug type:** Logical

The `except` block silently keeps the invalid text by assigning `score = raw`, so the program reports nonsense as a score instead of rejecting it. Validation should re-prompt or refuse bad input rather than swallow it.

```python
while True:
    raw = input("Enter your test score: ")
    try:
        score = int(raw)
        break
    except ValueError:
        print("Please type a whole number.")
print("Your score is", score)
```

<sub>[Exercise](find-the-bug.md#exercise-1615--validating-a-test-score) · [Runnable file](code/find_the_bug/ex_16_01_05_validating_a_test_score.py)</sub>

## 16.2 Handling Different Kinds of Errors

### Solution 17.2.1 — Splitting a bill

**Bug type:** Runtime

Dividing by zero raises `ZeroDivisionError`, but the code catches `ValueError`, so the real error escapes and the program crashes. Catch `ZeroDivisionError`.

```python
bill = 60.0
friends = 0
try:
    share = bill / friends
    print("Each person pays", share)
except ZeroDivisionError:
    print("There must be at least one person.")
```

<sub>[Exercise](find-the-bug.md#exercise-1621--splitting-a-bill) · [Runnable file](code/find_the_bug/ex_16_02_01_splitting_a_bill.py)</sub>

### Solution 17.2.2 — Adding a measurement

**Bug type:** Runtime

Adding an integer to a string raises `TypeError`, but the code catches `ZeroDivisionError`, so the error is not caught and the program crashes. Catch `TypeError`.

```python
total = 100
new_value = "twelve"
try:
    total = total + new_value
except TypeError:
    print("That measurement was not a number.")
print("Total is", total)
```

<sub>[Exercise](find-the-bug.md#exercise-1622--adding-a-measurement) · [Runnable file](code/find_the_bug/ex_16_02_02_adding_a_measurement.py)</sub>

### Solution 17.2.3 — Average speed

**Bug type:** Logical

The broad `except Exception` is listed first, and because `ZeroDivisionError` is a subclass of `Exception`, the first handler swallows a zero-time error and prints the misleading ``Distance was not a number'' message; the specific `ZeroDivisionError` handler is unreachable. Put the specific handler before the general one.

```python
distance = float(input("Distance in meters? "))
time = float(input("Time in seconds? "))
try:
    speed = distance / time
    print("Average speed:", speed)
except ZeroDivisionError:
    print("Time cannot be zero.")
except Exception:
    print("Distance was not a number.")
```

<sub>[Exercise](find-the-bug.md#exercise-1623--average-speed) · [Runnable file](code/find_the_bug/ex_16_02_03_average_speed.py)</sub>

### Solution 17.2.4 — Looking up a grade

**Bug type:** Runtime

Looking up a missing dictionary key raises `KeyError`, but the code catches `ValueError`, so the lookup failure is not handled and the program crashes. Catch `KeyError`.

```python
grades = {"Ann": 91, "Bo": 84}
name = "Cleo"
try:
    print(name, "scored", grades[name])
except KeyError:
    print("No grade recorded for", name)
```

<sub>[Exercise](find-the-bug.md#exercise-1624--looking-up-a-grade) · [Runnable file](code/find_the_bug/ex_16_02_04_looking_up_a_grade.py)</sub>

### Solution 17.2.5 — Percent off

**Bug type:** Logical

The broad `except Exception` comes first, and since `ZeroDivisionError` is a subclass of `Exception`, a zero divisor is caught by the first handler and reported as ``not a valid number''; the specific `ZeroDivisionError` handler can never run. List the specific handler before the general one.

```python
price = 50
divisor = input("Divide the discount by? ")
try:
    fraction = 100 / int(divisor)
    print("You pay", price * fraction)
except ZeroDivisionError:
    print("The divisor cannot be zero.")
except Exception:
    print("That was not a valid number.")
```

<sub>[Exercise](find-the-bug.md#exercise-1625--percent-off) · [Runnable file](code/find_the_bug/ex_16_02_05_percent_off.py)</sub>

## 16.3 Using `else`

### Solution 17.3.1 — Confirming a conversion

**Bug type:** Logical

The success line is printed twice — once inside `try` and again in `else`. Code that should run only on success belongs in `else`, not in `try`; remove the duplicate from the `try` block.

```python
text = "42"
try:
    number = int(text)
except ValueError:
    print("That was not a number.")
else:
    print("Conversion worked:", number)
```

<sub>[Exercise](find-the-bug.md#exercise-1631--confirming-a-conversion) · [Runnable file](code/find_the_bug/ex_16_03_01_confirming_a_conversion.py)</sub>

### Solution 17.3.2 — Area of a rectangle

**Bug type:** Logical

The `else` block computes `area` but never prints it, so the program produces no visible result on success. Print the area in the `else` block.

```python
try:
    width = float(input("Width? "))
    height = float(input("Height? "))
except ValueError:
    print("Both sides must be numbers.")
else:
    area = width * height
    print("Area:", area)
```

<sub>[Exercise](find-the-bug.md#exercise-1632--area-of-a-rectangle) · [Runnable file](code/find_the_bug/ex_16_03_02_area_of_a_rectangle.py)</sub>

### Solution 17.3.3 — Doubling a recipe

**Bug type:** Logical

The doubling work that should run only after a successful conversion is placed in the `try` block; if `cups * 2` or the print logic ever failed it would be wrongly treated as an input error. The success-only computation belongs in `else`, leaving only the risky conversion in `try`.

```python
try:
    cups = float(input("How many cups? "))
except ValueError:
    print("That was not a number.")
else:
    doubled = cups * 2
    print("You need", doubled, "cups.")
```

<sub>[Exercise](find-the-bug.md#exercise-1633--doubling-a-recipe) · [Runnable file](code/find_the_bug/ex_16_03_03_doubling_a_recipe.py)</sub>

### Solution 17.3.4 — Safe square root

**Bug type:** Syntax

The `try` keyword is missing its colon, so the file will not parse. Add the colon after `try`.

```python
import math

try:
    value = float(input("Enter a number: "))
except ValueError:
    print("That was not a number.")
else:
    print("Square root is", math.sqrt(value))
```

<sub>[Exercise](find-the-bug.md#exercise-1634--safe-square-root) · [Runnable file](code/find_the_bug/ex_16_03_04_safe_square_root.py)</sub>

### Solution 17.3.5 — Tax on a purchase

**Bug type:** Logical

The tax formula uses addition (`amount + 0.08`) instead of multiplication, so it adds eight cents rather than computing 8 percent of the amount. Use `amount * 0.08`.

```python
try:
    amount = float(input("Purchase amount? "))
except ValueError:
    print("That was not a number.")
else:
    tax = amount * 0.08
    print("Tax is", tax)
```

<sub>[Exercise](find-the-bug.md#exercise-1635--tax-on-a-purchase) · [Runnable file](code/find_the_bug/ex_16_03_05_tax_on_a_purchase.py)</sub>

## 16.4 Using `finally`

### Solution 17.4.1 — Closing a report

**Bug type:** Logical

The closing line sits inside the `except` block, so it prints only when the division fails; on the normal path it never runs. Move the always-run line into a `finally` block.

```python
try:
    result = 10 / 2
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Done with the calculation.")
```

<sub>[Exercise](find-the-bug.md#exercise-1641--closing-a-report) · [Runnable file](code/find_the_bug/ex_16_04_01_closing_a_report.py)</sub>

### Solution 17.4.2 — Releasing the scale

**Bug type:** Logical

``Scale released'' must always print, but it is in the `else` block, which runs only when no exception occurs; on bad input it is skipped. Use `finally` so it runs whether or not an error happened.

```python
try:
    weight = float(input("Weight in kilograms? "))
    print("Recorded weight:", weight)
except ValueError:
    print("That was not a number.")
finally:
    print("Scale released.")
```

<sub>[Exercise](find-the-bug.md#exercise-1642--releasing-the-scale) · [Runnable file](code/find_the_bug/ex_16_04_02_releasing_the_scale.py)</sub>

### Solution 17.4.3 — Logging an attempt

**Bug type:** Syntax

The `finally` keyword is missing its colon, so the file will not parse. Add the colon after `finally`.

```python
try:
    count = int(input("How many items? "))
    print("Count:", count)
except ValueError:
    print("Not a whole number.")
finally:
    print("Attempt logged.")
```

<sub>[Exercise](find-the-bug.md#exercise-1643--logging-an-attempt) · [Runnable file](code/find_the_bug/ex_16_04_03_logging_an_attempt.py)</sub>

### Solution 17.4.4 — Final tally

**Bug type:** Logical

The tally line sits inside the `try` right after the division, so a `ZeroDivisionError` skips it. A line that must always run belongs in a `finally` block, which executes whether or not an exception occurs.

```python
points = 90
rounds = 0
try:
    average = points / rounds
    print("Average:", average)
except ZeroDivisionError:
    print("No rounds played.")
finally:
    print("Final tally complete.")
```

<sub>[Exercise](find-the-bug.md#exercise-1644--final-tally) · [Runnable file](code/find_the_bug/ex_16_04_04_final_tally.py)</sub>

### Solution 17.4.5 — Cleanup message

**Bug type:** Syntax

The clauses are out of order: `finally` appears before `except`, which is not allowed — `except` (and `else`) must come before `finally`. Reorder so `except` precedes `finally`.

```python
try:
    distance = float(input("Distance in meters? "))
    print("Distance:", distance)
except ValueError:
    print("That was not a number.")
finally:
    print("Sensor reset.")
```

<sub>[Exercise](find-the-bug.md#exercise-1645--cleanup-message) · [Runnable file](code/find_the_bug/ex_16_04_05_cleanup_message.py)</sub>
