# Chapter 14 — Objects: Find the Bug, Solutions

Each solution names the bug type — **syntax**, **runtime**, or **logical** — explains why the original program misbehaved, and shows the corrected program.

Back to [the exercises](find-the-bug.md).

## 14.1 Classes

### Solution 14.1.1 — Defining a class

**Bug type:** Syntax

The `def __init__(self, width, height)` header is missing the colon at the end, so Python cannot parse the method definition. Adding the colon fixes it.

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

room = Rectangle(4, 3)
print(room.area())   # 12
```

<sub>[Exercise](find-the-bug.md#exercise-1411--defining-a-class) · [Runnable file](code/find_the_bug/ex_06_01_01_defining_a_class.py)</sub>

### Solution 14.1.2 — Using self

**Bug type:** Runtime

Inside `to_fahrenheit` the bare name `celsius` is not defined; the value is stored on the instance, so it must be reached through `self``.celsius`. Using `self.celsius` fixes the `NameError`.

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return self.celsius * 9 / 5 + 32

reading = Temperature(100)
print(reading.to_fahrenheit())   # 212.0
```

<sub>[Exercise](find-the-bug.md#exercise-1412--using-self) · [Runnable file](code/find_the_bug/ex_06_01_02_using_self.py)</sub>

### Solution 14.1.3 — Storing an attribute

**Bug type:** Runtime

The attribute stored in `__init__` is named `score`, but `summary` reads `self.grade`, which was never set. Referring to `self.score` fixes the `AttributeError`.

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def summary(self):
        return f"{self.name} scored {self.score}"

learner = Student("Ava", 88)
print(learner.summary())   # Ava scored 88
```

<sub>[Exercise](find-the-bug.md#exercise-1413--storing-an-attribute) · [Runnable file](code/find_the_bug/ex_06_01_03_storing_an_attribute.py)</sub>

### Solution 14.1.4 — Calling a method

**Bug type:** Runtime

The method is called on the class, `Account.add_interest(0.05)`, so `0.05` is bound to `self` and no `rate` is supplied, raising a `TypeError`. Calling it on the instance, `savings.add_interest(0.05)`, passes `savings` as `self` and `0.05` as `rate`.

```python
class Account:
    def __init__(self, balance):
        self.balance = balance

    def add_interest(self, rate):
        self.balance = self.balance + self.balance * rate

savings = Account(1000)
savings.add_interest(0.05)
print(savings.balance)   # 1050.0
```

<sub>[Exercise](find-the-bug.md#exercise-1414--calling-a-method) · [Runnable file](code/find_the_bug/ex_06_01_04_calling_a_method.py)</sub>

### Solution 14.1.5 — Method calls need parentheses

**Bug type:** Logical

`wheel.circumference` refers to the method object instead of calling it, so the printout is a function reference, not the number. Adding parentheses — `wheel.circumference()` — calls the method and prints `62.8318`.

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * 3.14159 * self.radius

wheel = Circle(10)
print(wheel.circumference())   # 62.8318
```

<sub>[Exercise](find-the-bug.md#exercise-1415--method-calls-need-parentheses) · [Runnable file](code/find_the_bug/ex_06_01_05_method_calls_need_parentheses.py)</sub>

## 14.2 Instance Data vs Class Data

### Solution 14.2.1 — Instance vs class attribute

**Bug type:** Runtime

The class attribute is named `gravity_unit`, but the last line reads `earth.unit`, which does not exist. Using `earth.gravity_unit` fixes the `AttributeError`.

```python
class Planet:
    gravity_unit = "m/s^2"

    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

earth = Planet("Earth", 5.97e24)
mars = Planet("Mars", 6.42e23)

print(earth.name, earth.gravity_unit)   # Earth m/s^2
print(mars.name, mars.gravity_unit)     # Mars m/s^2
print(earth.gravity_unit)               # m/s^2
```

<sub>[Exercise](find-the-bug.md#exercise-1421--instance-vs-class-attribute) · [Runnable file](code/find_the_bug/ex_06_02_01_instance_vs_class_attribute.py)</sub>

### Solution 14.2.2 — Shared mutable class attribute

**Bug type:** Logical

`laps` is a class attribute, so a single list is shared by every runner; `amir.record` and `beth.record` append to the same list. Each runner needs its own list, created as an instance attribute in `__init__`.

```python
class Runner:
    def __init__(self, name):
        self.name = name
        self.laps = []

    def record(self, seconds):
        self.laps.append(seconds)

amir = Runner("Amir")
beth = Runner("Beth")
amir.record(58)
beth.record(61)
print(amir.laps)   # [58]
print(beth.laps)   # [61]
```

<sub>[Exercise](find-the-bug.md#exercise-1422--shared-mutable-class-attribute) · [Runnable file](code/find_the_bug/ex_06_02_02_shared_mutable_class_attribute.py)</sub>

### Solution 14.2.3 — Updating a class counter

**Bug type:** Logical

Writing `self.count = self.count + 1` reads the class value but creates a new *instance* attribute, leaving `Book.count` at 0. Incrementing `Book.count` updates the shared class counter, so it reaches 3.

```python
class Book:
    count = 0

    def __init__(self, title):
        self.title = title
        Book.count = Book.count + 1

Book("Algebra")
Book("Biology")
Book("Chemistry")
print(Book.count)   # 3
```

<sub>[Exercise](find-the-bug.md#exercise-1423--updating-a-class-counter) · [Runnable file](code/find_the_bug/ex_06_02_03_updating_a_class_counter.py)</sub>

### Solution 14.2.4 — Instance overriding shared default

**Bug type:** Logical

`Thermostat.target_c = 22` reassigns the shared *class* attribute, so both rooms read 22 and the bedroom does not keep the default. Assigning to the instance, `kitchen.target_c = 22`, creates an instance attribute that shadows the class default for the kitchen only, leaving the bedroom at 20.

```python
class Thermostat:
    target_c = 20

    def __init__(self, room):
        self.room = room

kitchen = Thermostat("kitchen")
bedroom = Thermostat("bedroom")
kitchen.target_c = 22   # set only this instance

print(kitchen.target_c)   # 22
print(bedroom.target_c)   # 20
```

<sub>[Exercise](find-the-bug.md#exercise-1424--instance-overriding-shared-default) · [Runnable file](code/find_the_bug/ex_06_02_04_instance_overriding_shared_default.py)</sub>

### Solution 14.2.5 — Reading a class constant

**Bug type:** Logical

Sales tax is added by *multiplying* the subtotal by the rate, not dividing by it. The corrected line uses `self.subtotal + self.subtotal * self.tax_rate`, giving `54.0`.

```python
class Cart:
    tax_rate = 0.08

    def __init__(self, subtotal):
        self.subtotal = subtotal

    def total(self):
        return self.subtotal + self.subtotal * self.tax_rate

groceries = Cart(50.0)
print(groceries.total())   # 54.0
```

<sub>[Exercise](find-the-bug.md#exercise-1425--reading-a-class-constant) · [Runnable file](code/find_the_bug/ex_06_02_05_reading_a_class_constant.py)</sub>

## 14.3 Duck Typing

### Solution 14.3.1 — Relying on a shared method

**Bug type:** Runtime

`shape.area` refers to the method without calling it, so adding it to a number raises a `TypeError`. Calling `shape.area()` invokes each shape's method and totals the areas to `25.0`.

```python
class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2

def total_area(shapes):
    total = 0
    for shape in shapes:
        total = total + shape.area()
    return total

print(total_area([Square(4), Triangle(6, 3)]))   # 25.0
```

<sub>[Exercise](find-the-bug.md#exercise-1431--relying-on-a-shared-method) · [Runnable file](code/find_the_bug/ex_06_03_01_relying_on_a_shared_method.py)</sub>

### Solution 14.3.2 — Same behavior, different types

**Bug type:** Runtime

`greet` calls `animal.speka()`, but both classes provide `speak`, not `speka`, so every call raises an `AttributeError`. Correcting the method name to `animal.speak()` lets duck typing work for any object that can `speak`.

```python
class Cat:
    def speak(self):
        return "Meow"

class Cow:
    def speak(self):
        return "Moo"

def greet(animal):
    print("The animal says:", animal.speak())

greet(Cat())
greet(Cow())   # The animal says: Moo
```

<sub>[Exercise](find-the-bug.md#exercise-1432--same-behavior-different-types) · [Runnable file](code/find_the_bug/ex_06_03_02_same_behavior_different_types.py)</sub>

### Solution 14.3.3 — Behavior over type

**Bug type:** Runtime

Both objects expose a `length` attribute, but `meters_of` reads `thing.size`, which neither class has. Reading `thing.length` fixes the `AttributeError`, and any object with a `length` works.

```python
class Field:
    def __init__(self, length):
        self.length = length

class Pool:
    def __init__(self, length):
        self.length = length

def meters_of(thing):
    return thing.length

print(meters_of(Field(100)))   # 100
print(meters_of(Pool(25)))     # 25
```

<sub>[Exercise](find-the-bug.md#exercise-1433--behavior-over-type) · [Runnable file](code/find_the_bug/ex_06_03_03_behavior_over_type.py)</sub>

### Solution 14.3.4 — Duck typing a method call

**Bug type:** Logical

`device.tick` only looks up the method; it never calls it, so `watch.seconds` stays 0. Adding parentheses — `device.tick()` — actually advances each device.

```python
class Stopwatch:
    def __init__(self):
        self.seconds = 0

    def tick(self):
        self.seconds = self.seconds + 1

class Metronome:
    def __init__(self):
        self.beats = 0

    def tick(self):
        self.beats = self.beats + 1

def advance(devices):
    for device in devices:
        device.tick()

watch = Stopwatch()
advance([watch])
print(watch.seconds)   # 1
```

<sub>[Exercise](find-the-bug.md#exercise-1434--duck-typing-a-method-call) · [Runnable file](code/find_the_bug/ex_06_03_04_duck_typing_a_method_call.py)</sub>

### Solution 14.3.5 — Trusting the interface

**Bug type:** Logical

`sensor.read` returns the bound method instead of the reading, so the printout is a method reference, not a number. Calling `sensor.read()` returns the value from whichever sensor was passed.

```python
class TempSensor:
    def read(self):
        return 21.5

class HumiditySensor:
    def read(self):
        return 48.0

def sample(sensor):
    return sensor.read()

print(sample(TempSensor()))       # 21.5
print(sample(HumiditySensor()))   # 48.0
```

<sub>[Exercise](find-the-bug.md#exercise-1435--trusting-the-interface) · [Runnable file](code/find_the_bug/ex_06_03_05_trusting_the_interface.py)</sub>
