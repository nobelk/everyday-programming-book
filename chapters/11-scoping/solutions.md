# Chapter 11 — Scoping: Find the Bug, Solutions

Each solution names the bug type — **syntax**, **runtime**, or **logical** — explains why the original program misbehaved, and shows the corrected program.

Back to [the exercises](find-the-bug.md).

## 11.1 Local and Global Scope

### Solution 11.1.1 — reading a global from a function

**Bug type:** Runtime

The top-level `print` reads `speed_limit`, but the global is named `speed_limit_kmh`, so Python raises `NameError`. Use the correct global name.

```python
speed_limit_kmh = 100

def report():
    print("Inside:", speed_limit_kmh)

report()
print("Outside:", speed_limit_kmh)
```

<sub>[Exercise](find-the-bug.md#exercise-1111--reading-a-global-from-a-function) · [Runnable file](code/find_the_bug/ex_11_01_01_reading_a_global_from_a_function.py)</sub>

### Solution 11.1.2 — a local name stays local

**Bug type:** Runtime

`temperature_c` is local to `take_reading()`, so it does not exist at the top level; the final `print` raises `NameError`. Remove that line (a local name is not visible outside its function).

```python
def take_reading():
    temperature_c = 21.5
    print("Reading:", temperature_c)

take_reading()
```

<sub>[Exercise](find-the-bug.md#exercise-1112--a-local-name-stays-local) · [Runnable file](code/find_the_bug/ex_11_01_02_a_local_name_stays_local.py)</sub>

### Solution 11.1.3 — a global constant for area

**Bug type:** Runtime

The global `pi` is visible inside the function, but `area` is created *inside* `circle_area`, so it does not exist at the top level and the final `print` raises `NameError`. Return the value and capture it in a variable.

```python
pi = 3.14159

def circle_area():
    return pi * 3 * 3

area = circle_area()
print("Area:", area)   # Area: 28.27431
```

<sub>[Exercise](find-the-bug.md#exercise-1113--a-global-constant-for-area) · [Runnable file](code/find_the_bug/ex_11_01_03_a_global_constant_for_area.py)</sub>

### Solution 11.1.4 — the helper's result must come back out

**Bug type:** Logical

`edges` is a local variable; without a `return`, the function hands back `None`, so `result` is `None`. Return the value so it leaves the local scope.

```python
def perimeter(length, width):
    edges = 2 * (length + width)
    return edges

result = perimeter(5, 3)
print("Perimeter:", result)
```

<sub>[Exercise](find-the-bug.md#exercise-1114--the-helpers-result-must-come-back-out) · [Runnable file](code/find_the_bug/ex_11_01_04_the_helper_s_result_must_come_back_out.py)</sub>

### Solution 11.1.5 — global list, read inside the function

**Bug type:** Syntax

The `def` line is missing its colon, so the file will not parse. Add the colon after the parentheses.

```python
scores = [80, 90, 100]

def average():
    return sum(scores) / len(scores)

print("Average:", average())
```

<sub>[Exercise](find-the-bug.md#exercise-1115--global-list-read-inside-the-function) · [Runnable file](code/find_the_bug/ex_11_01_05_global_list_read_inside_the_function.py)</sub>

## 11.2 A Local Variable Can Hide a Global Variable

### Solution 11.2.1 — local hides global, on purpose

**Bug type:** Logical

The intended output uses 0.10 for the sale, but inside the function the local `discount` is set to 0.25, which shadows the global. To make both lines print 0.10, the local should not override it; assign the sale rate to match the intended 0.10.

```python
discount = 0.10

def checkout():
    discount = 0.10
    print("Sale rate:", discount)

checkout()
print("Normal rate:", discount)
```

<sub>[Exercise](find-the-bug.md#exercise-1121--local-hides-global-on-purpose) · [Runnable file](code/find_the_bug/ex_11_02_01_local_hides_global_on_purpose.py)</sub>

### Solution 11.2.2 — the local shadow should win inside

**Bug type:** Logical

To convert kilometers to meters you multiply by 1000; the code divides instead, so it shrinks the value. Use multiplication with the local `factor`.

```python
factor = 1

def convert(kilometers):
    factor = 1000
    return kilometers * factor

print("Meters:", convert(5))
```

<sub>[Exercise](find-the-bug.md#exercise-1122--the-local-shadow-should-win-inside) · [Runnable file](code/find_the_bug/ex_11_02_02_the_local_shadow_should_win_inside.py)</sub>

### Solution 11.2.3 — shadowing a built-in name

**Bug type:** Runtime

The global `sum = 0` shadows the built-in `sum` function, so `sum(prices)` tries to call an integer and raises `TypeError`. Remove the shadowing variable so the built-in is used.

```python
prices = [2.50, 1.25, 3.00]

def total():
    return sum(prices)

print("Total:", total())
```

<sub>[Exercise](find-the-bug.md#exercise-1123--shadowing-a-built-in-name) · [Runnable file](code/find_the_bug/ex_11_02_03_shadowing_a_built_in_name.py)</sub>

### Solution 11.2.4 — which value gets printed

**Bug type:** Logical

The local `tax_rate` is set to 0.08, but the formula hard-codes 0.05, so the local shadow is never used and the answer is 105.0. Use the local `tax_rate` in the calculation.

```python
tax_rate = 0.05

def quote(price):
    tax_rate = 0.08
    return price + price * tax_rate

print("With tax:", quote(100))
```

<sub>[Exercise](find-the-bug.md#exercise-1124--which-value-gets-printed) · [Runnable file](code/find_the_bug/ex_11_02_04_which_value_gets_printed.py)</sub>

### Solution 11.2.5 — parameter shadows the global

**Bug type:** Logical

The parameter `gravity` shadows the global, which is exactly what lets a caller test the Moon, but the call passes 9.8 (Earth) instead of 1.6. Pass the Moon's value as the argument.

```python
gravity = 9.8

def weight(mass, gravity):
    return mass * gravity

print("Moon weight:", weight(10, 1.6))
```

<sub>[Exercise](find-the-bug.md#exercise-1125--parameter-shadows-the-global) · [Runnable file](code/find_the_bug/ex_11_02_05_parameter_shadows_the_global.py)</sub>

## 11.3 Assignment Inside a Function Usually Creates a Local Variable

### Solution 11.3.1 — assigning makes it local

**Bug type:** Runtime

Because `total` is assigned inside `add()`, Python treats it as local everywhere in the function; reading `total` on the right-hand side before it has a local value raises `UnboundLocalError`. Start the local from a literal instead of the global.

```python
total = 0

def add():
    total = 10
    print("Inside:", total)

add()
print("Outside:", total)
```

<sub>[Exercise](find-the-bug.md#exercise-1131--assigning-makes-it-local) · [Runnable file](code/find_the_bug/ex_11_03_01_assigning_makes_it_local.py)</sub>

### Solution 11.3.2 — read before assign

**Bug type:** Runtime

Assigning `step` later in the function makes `step` local throughout, so the `print` reads a local that has no value yet — `UnboundLocalError`. Read the value through a parameter (or remove the local assignment) so the read is valid.

```python
step = 1

def advance(step):
    print("Current:", step)
    step = step + 1

advance(step)
```

<sub>[Exercise](find-the-bug.md#exercise-1132--read-before-assign) · [Runnable file](code/find_the_bug/ex_11_03_02_read_before_assign.py)</sub>

### Solution 11.3.3 — counting without touching the global

**Bug type:** Runtime

The local `count` should be increased by 1 per item, but `count + item` adds a string to an integer and raises `TypeError`. Increment by 1 instead.

```python
count = 0
basket = ["apple", "pear", "plum"]

def tally():
    count = 0
    for item in basket:
        count = count + 1
    return count

print("Items:", tally())
```

<sub>[Exercise](find-the-bug.md#exercise-1133--counting-without-touching-the-global) · [Runnable file](code/find_the_bug/ex_11_03_03_counting_without_touching_the_global.py)</sub>

### Solution 11.3.4 — local sum inside a loop

**Bug type:** Logical

The running total should add each distance, but the loop subtracts, giving a negative total. Use addition.

```python
distance = 0
trips = [10, 15, 20]

def trip_total():
    distance = 0
    for d in trips:
        distance = distance + d
    return distance

print("Total distance:", trip_total())
```

<sub>[Exercise](find-the-bug.md#exercise-1134--local-sum-inside-a-loop) · [Runnable file](code/find_the_bug/ex_11_03_04_local_sum_inside_a_loop.py)</sub>

### Solution 11.3.5 — assignment creates a fresh local

**Bug type:** Runtime

The final `print` reads `balanace`, a misspelling, so Python raises `NameError`. Use the correct global name `balance`.

```python
balance = 50

def spend():
    balance = 20

spend()
print("Balance:", balance)
```

<sub>[Exercise](find-the-bug.md#exercise-1135--assignment-creates-a-fresh-local) · [Runnable file](code/find_the_bug/ex_11_03_05_assignment_creates_a_fresh_local.py)</sub>

## 11.4 Using `global`

### Solution 11.4.1 — declaring global

**Bug type:** Runtime

Without a `global` declaration, assigning `visitors` makes it local, so reading it on the right-hand side raises `UnboundLocalError`. Declare `global visitors` so the module-level variable is updated.

```python
visitors = 0

def arrive():
    global visitors
    visitors = visitors + 1

arrive()
print("Visitors:", visitors)
```

<sub>[Exercise](find-the-bug.md#exercise-1141--declaring-global) · [Runnable file](code/find_the_bug/ex_11_04_01_declaring_global.py)</sub>

### Solution 11.4.2 — global then assign

**Bug type:** Logical

`score == 100` is a comparison, not an assignment, so the global is never changed and stays 0. Use `=` to assign.

```python
score = 0

def set_perfect():
    global score
    score = 100

set_perfect()
print("Score:", score)
```

<sub>[Exercise](find-the-bug.md#exercise-1142--global-then-assign) · [Runnable file](code/find_the_bug/ex_11_04_02_global_then_assign.py)</sub>

### Solution 11.4.3 — global keyword spelling

**Bug type:** Syntax

The keyword is `global` (lowercase); `Global` is not a keyword, so the line fails to parse. Use the lowercase keyword.

```python
temperature = 0

def set_room():
    global temperature
    temperature = 25

set_room()
print("Temperature:", temperature)
```

<sub>[Exercise](find-the-bug.md#exercise-1143--global-keyword-spelling) · [Runnable file](code/find_the_bug/ex_11_04_03_global_keyword_spelling.py)</sub>

### Solution 11.4.4 — accumulate into a global

**Bug type:** Runtime

The final `print` reads `saving`, but the global is `savings`, so Python raises `NameError`. Use the correct name.

```python
savings = 0
deposits = [10, 20, 30]

def collect():
    global savings
    for amount in deposits:
        savings = savings + amount

collect()
print("Savings:", savings)
```

<sub>[Exercise](find-the-bug.md#exercise-1144--accumulate-into-a-global) · [Runnable file](code/find_the_bug/ex_11_04_04_accumulate_into_a_global.py)</sub>

### Solution 11.4.5 — global so the change sticks

**Bug type:** Runtime

Python's boolean is `True` with a capital T; `false` is not defined, so the assignment raises `NameError`. Use `True`.

```python
is_open = False

def open_shop():
    global is_open
    is_open = True

open_shop()
print("Open:", is_open)
```

<sub>[Exercise](find-the-bug.md#exercise-1145--global-so-the-change-sticks) · [Runnable file](code/find_the_bug/ex_11_04_05_global_so_the_change_sticks.py)</sub>

## 11.5 Using `nonlocal` in Nested Functions

### Solution 11.5.1 — nonlocal counter

**Bug type:** Runtime

Assigning `count` inside `increment()` makes it local, so `count + 1` reads a local with no value — `UnboundLocalError`. Declare `nonlocal count` to target the enclosing variable.

```python
def make_counter():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        return count

    return increment

counter = make_counter()
print(counter())
print(counter())
```

<sub>[Exercise](find-the-bug.md#exercise-1151--nonlocal-counter) · [Runnable file](code/find_the_bug/ex_11_05_01_nonlocal_counter.py)</sub>

### Solution 11.5.2 — running total in an enclosing scope

**Bug type:** Logical

A deposit should add to the total, but the code subtracts, so the balance goes negative. Use addition.

```python
def make_account():
    total = 0

    def deposit(amount):
        nonlocal total
        total = total + amount
        return total

    return deposit

account = make_account()
account(10)
print("Balance:", account(20))
```

<sub>[Exercise](find-the-bug.md#exercise-1152--running-total-in-an-enclosing-scope) · [Runnable file](code/find_the_bug/ex_11_05_02_running_total_in_an_enclosing_scope.py)</sub>

### Solution 11.5.3 — nonlocal keyword

**Bug type:** Syntax

The final `print` call is missing its closing parenthesis, so the file will not parse. Add the closing parenthesis.

```python
def make_tracker():
    highest = 0

    def record(value):
        nonlocal highest
        if value > highest:
            highest = value
        return highest

    return record

record = make_tracker()
record(4)
print("Highest:", record(9))
```

<sub>[Exercise](find-the-bug.md#exercise-1153--nonlocal-keyword) · [Runnable file](code/find_the_bug/ex_11_05_03_nonlocal_keyword.py)</sub>

### Solution 11.5.4 — which scope nonlocal targets

**Bug type:** Runtime

The first call uses `steper()`, a misspelling of `stepper`, so Python raises `NameError`. Use the correct name.

```python
def make_stepper():
    position = 0

    def step():
        nonlocal position
        position += 5
        return position

    return step

stepper = make_stepper()
print(stepper())
print(stepper())
```

<sub>[Exercise](find-the-bug.md#exercise-1154--which-scope-nonlocal-targets) · [Runnable file](code/find_the_bug/ex_11_05_04_which_scope_nonlocal_targets.py)</sub>

### Solution 11.5.5 — nonlocal vs global

**Bug type:** Runtime

`times` lives in the enclosing function, not the module, so `global times` cannot find it and raises `NameError` at call time. Use `nonlocal` to target the enclosing scope.

```python
def make_logger():
    times = 0

    def log():
        nonlocal times
        times += 1
        return times

    return log

log = make_logger()
log()
print("Times:", log())
```

<sub>[Exercise](find-the-bug.md#exercise-1155--nonlocal-vs-global) · [Runnable file](code/find_the_bug/ex_11_05_05_nonlocal_vs_global.py)</sub>

## 11.6 Scope with Objects and Classes

### Solution 11.6.1 — self attribute vs local

**Bug type:** Runtime

In `__init__`, `temperature = temperature` just reassigns the local parameter; it never stores anything on the object, so `read()` raises an `AttributeError` for the missing `self.temperature`. Assign to `self.temperature`.

```python
class Thermometer:
    def __init__(self, temperature):
        self.temperature = temperature

    def read(self):
        return self.temperature

device = Thermometer(22)
print("Temp:", device.read())
```

<sub>[Exercise](find-the-bug.md#exercise-1161--self-attribute-vs-local) · [Runnable file](code/find_the_bug/ex_11_06_01_self_attribute_vs_local.py)</sub>

### Solution 11.6.2 — reading an instance attribute

**Bug type:** Runtime

`get_score` returns plain `score`, which is not a local or global name, so Python raises `NameError`. Read the attribute through `self.score`.

```python
class Student:
    def __init__(self, score):
        self.score = score

    def get_score(self):
        return self.score

learner = Student(95)
print("Score:", learner.get_score())
```

<sub>[Exercise](find-the-bug.md#exercise-1162--reading-an-instance-attribute) · [Runnable file](code/find_the_bug/ex_11_06_02_reading_an_instance_attribute.py)</sub>

### Solution 11.6.3 — class variable shared by all

**Bug type:** Runtime

The class variable is named `unit`, but the last line reads `mars.units`, which does not exist, so Python raises `AttributeError`. Use the correct attribute name.

```python
class Planet:
    unit = "km"

    def __init__(self, name):
        self.name = name

earth = Planet("Earth")
mars = Planet("Mars")
print(earth.unit)
print(mars.unit)
```

<sub>[Exercise](find-the-bug.md#exercise-1163--class-variable-shared-by-all) · [Runnable file](code/find_the_bug/ex_11_06_03_class_variable_shared_by_all.py)</sub>

### Solution 11.6.4 — a local inside a method

**Bug type:** Runtime

`area()` uses bare `width`, which is not defined in the method's local scope, so Python raises `NameError`. Read the stored side through `self.width`.

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        result = self.width * self.height
        return result

box = Rectangle(3, 4)
print("Area:", box.area())
```

<sub>[Exercise](find-the-bug.md#exercise-1164--a-local-inside-a-method) · [Runnable file](code/find_the_bug/ex_11_06_04_a_local_inside_a_method.py)</sub>

### Solution 11.6.5 — updating an instance attribute

**Bug type:** Logical

`deposit` assigns to a local `balance`, which vanishes when the method returns; the object's `self.balance` is never updated, so it stays 50. Assign to `self.balance`.

```python
class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

savings = Account(50)
savings.deposit(20)
print("Balance:", savings.balance)
```

<sub>[Exercise](find-the-bug.md#exercise-1165--updating-an-instance-attribute) · [Runnable file](code/find_the_bug/ex_11_06_05_updating_an_instance_attribute.py)</sub>
