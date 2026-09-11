# Chapter 11 — Functions: Find the Bug

Part IV · Control Flow — *Everyday Programming*

These exercises cover Python functions — defining them, passing arguments, returning results, and the small surprises along the way; each program below contains exactly one bug, so read carefully and find it.

Read each program, decide what it is supposed to print, and find the one line that stops it. Then check yourself against [the solutions](solutions.md). The corrected programs are also available as runnable files under [`code/find_the_bug/`](code/find_the_bug).

**60 exercises in 12 sections.**

## 10.1 Your First Function

### Exercise 11.1.1 — Defining and calling

This program should define a function that prints a welcome message and then call it once.

```python
def welcome():
    print("Welcome to the science club!")

welcome
```

<sub>[Solution](solutions.md#solution-1011--defining-and-calling)</sub>

### Exercise 11.1.2 — The colon

This program defines a function that prints the boiling point of water and calls it.

```python
def boiling_point()
    print("Water boils at 100 degrees Celsius.")

boiling_point()
```

<sub>[Solution](solutions.md#solution-1012--the-colon)</sub>

### Exercise 11.1.3 — The function body

This program should print the number of days in a week when called.

```python
def days_in_week():
print("A week has 7 days.")

days_in_week()
```

<sub>[Solution](solutions.md#solution-1013--the-function-body)</sub>

### Exercise 11.1.4 — Indenting the body

This program defines a function with two body lines and calls it once.

```python
def study_plan():
    print("Read the chapter.")
  print("Solve five problems.")

study_plan()
```

<sub>[Solution](solutions.md#solution-1014--indenting-the-body)</sub>

### Exercise 11.1.5 — Remember to call

This program should actually print the freezing point of water on screen.

```python
def freezing_point():
    print("Water freezes at 0 degrees Celsius.")
```

<sub>[Solution](solutions.md#solution-1015--remember-to-call)</sub>

## 10.2 Parameters

### Exercise 11.2.1 — Passing an argument

This program should greet a student by name.

```python
def greet_student(name):
    print("Hello,", name)

greet_student()
```

<sub>[Solution](solutions.md#solution-1021--passing-an-argument)</sub>

### Exercise 11.2.2 — Parameter order

This program should print `"Maya is 15 years old"`.

```python
def describe(name, age):
    print(name, "is", age, "years old")

describe(15, "Maya")
```

<sub>[Solution](solutions.md#solution-1022--parameter-order)</sub>

### Exercise 11.2.3 — Too many arguments

This program should print the area of a rectangle that is 4 by 6.

```python
def rectangle_area(width, height):
    return width * height

print(rectangle_area(4, 6, 8))
```

<sub>[Solution](solutions.md#solution-1023--too-many-arguments)</sub>

### Exercise 11.2.4 — Using the parameter

This program should double the number that is passed in and print 10.

```python
def double(number):
    return number * 2

print(double(number))
```

<sub>[Solution](solutions.md#solution-1024--using-the-parameter)</sub>

### Exercise 11.2.5 — Two parameters

This program should compute the perimeter of a rectangle (2 times width plus 2 times height) for a 3 by 5 rectangle, giving 16.

```python
def perimeter(width, height):
    return 2 * width + 2 * width

print(perimeter(3, 5))  # 16
```

<sub>[Solution](solutions.md#solution-1025--two-parameters)</sub>

## 10.3 Returning a Result

### Exercise 11.3.1 — Return, do not print

This program should store the sum of two numbers and then print 12.

```python
def add(a, b):
    print(a + b)

total = add(5, 7)
print(total)  # 12
```

<sub>[Solution](solutions.md#solution-1031--return-do-not-print)</sub>

### Exercise 11.3.2 — Return the right value

This function should return the average of three test scores.

```python
def average_of_three(a, b, c):
    return a + b + c / 3

print(average_of_three(80, 90, 100))  # 90.0
```

<sub>[Solution](solutions.md#solution-1032--return-the-right-value)</sub>

### Exercise 11.3.3 — Returning early

This program should convert Celsius to Fahrenheit and print 212.0 for 100 degrees.

```python
def c_to_f(celsius):
    return
    celsius * 9 / 5 + 32

print(c_to_f(100))  # 212.0
```

<sub>[Solution](solutions.md#solution-1033--returning-early)</sub>

### Exercise 11.3.4 — Return what was asked

This function should return the larger of two numbers; here it should return 9.

```python
def larger(a, b):
    if a > b:
        return a
    else:
        return a

print(larger(4, 9))  # 9
```

<sub>[Solution](solutions.md#solution-1034--return-what-was-asked)</sub>

### Exercise 11.3.5 — Use the returned value

This program should print the square of 6, which is 36.

```python
def square(side):
    return side * side

square(6)
print(area)  # 36
```

<sub>[Solution](solutions.md#solution-1035--use-the-returned-value)</sub>

## 10.4 Default Arguments

### Exercise 11.4.1 — A default value

This program should print a greeting with the default name when called with no argument.

```python
def greet(name="friend"):
    print("Hello,", name)

greet
```

<sub>[Solution](solutions.md#solution-1041--a-default-value)</sub>

### Exercise 11.4.2 — Default tax rate

This function should add an 8 percent tax by default, so a 50 dollar bill becomes 54.0.

```python
def with_tax(price, rate=0.08):
    return price + price * 0.8

print(with_tax(50))  # 54.0
```

<sub>[Solution](solutions.md#solution-1042--default-tax-rate)</sub>

### Exercise 11.4.3 — Overriding the default

This program should print 200 by overriding the default step count.

```python
def total_steps(days, per_day=100):
    return days * per_day

print(total_steps(2, 200))  # 200
```

<sub>[Solution](solutions.md#solution-1043--overriding-the-default)</sub>

### Exercise 11.4.4 — Order of defaults

This function gives the area of a rectangle, using a default height of 1.

```python
def area(height=1, width):
    return width * height

print(area(width=5))  # 5
```

<sub>[Solution](solutions.md#solution-1044--order-of-defaults)</sub>

### Exercise 11.4.5 — The default is optional

This program should print 10 by relying on the default increment.

```python
def increase(value, by=10):
    return value + by

print(increase())  # 10
```

<sub>[Solution](solutions.md#solution-1045--the-default-is-optional)</sub>

## 10.5 Keyword Arguments

### Exercise 11.5.1 — Calling by name

This program should print `"Lina is 12 years old"` using keyword arguments.

```python
def introduce(name, age):
    print(name, "is", age, "years old")

introduce(name="Lina", age=12, grade=7)
```

<sub>[Solution](solutions.md#solution-1051--calling-by-name)</sub>

### Exercise 11.5.2 — Order independence

Keyword arguments let you reorder; this should print the speed as distance over time, 20.0.

```python
def speed(distance, time):
    return distance / time

print(speed(time=100, distance=5))  # 20.0
```

<sub>[Solution](solutions.md#solution-1052--order-independence)</sub>

### Exercise 11.5.3 — Spelling the keyword

This program should print a labeled temperature using a keyword argument.

```python
def report(city, temperature):
    print(city, "is at", temperature, "degrees")

report(city="Denver", temp=30)
```

<sub>[Solution](solutions.md#solution-1053--spelling-the-keyword)</sub>

### Exercise 11.5.4 — Keyword after positional

This program should print `"Sam scored 95"` using one positional and one keyword argument.

```python
def score_line(name, points):
    print(name, "scored", points)

score_line(name="Sam", 95)
```

<sub>[Solution](solutions.md#solution-1054--keyword-after-positional)</sub>

### Exercise 11.5.5 — Mixing names and positions

This should compute simple interest (principal times rate times years) as 60.0.

```python
def interest(principal, rate, years):
    return principal * rate * years

print(interest(1000, years=3, rate=0.02, time=3))  # 60.0
```

<sub>[Solution](solutions.md#solution-1055--mixing-names-and-positions)</sub>

## 10.6 Multiple Return Values

### Exercise 11.6.1 — Returning a pair

This program should print the smallest and largest of three temperatures.

```python
def min_max(a, b, c):
    return min(a, b, c)

low, high = min_max(31.0, 36.5, 33.0)
print(low, high)  # 31.0 36.5
```

<sub>[Solution](solutions.md#solution-1061--returning-a-pair)</sub>

### Exercise 11.6.2 — Unpacking the result

This program should print the quotient and remainder of 17 divided by 5.

```python
def divide(a, b):
    return a // b, a % b

quotient = divide(17, 5)
print(quotient, remainder)  # 3 2
```

<sub>[Solution](solutions.md#solution-1062--unpacking-the-result)</sub>

### Exercise 11.6.3 — Matching the count

This program should unpack a name and an age into two variables.

```python
def person():
    return "Luis", 14, "grade 8"

name, age = person()
print(name, age)  # Luis 14
```

<sub>[Solution](solutions.md#solution-1063--matching-the-count)</sub>

### Exercise 11.6.4 — Order of the tuple

This should report width then height of a 8 by 3 rectangle, printing `"width 8 height 3"`.

```python
def dimensions():
    return 3, 8

width, height = dimensions()
print("width", width, "height", height)
```

<sub>[Solution](solutions.md#solution-1064--order-of-the-tuple)</sub>

### Exercise 11.6.5 — Returning both values

This program should return and print both the sum and the product of 4 and 5.

```python
def sum_and_product(a, b):
    return a + b
    return a * b

total, product = sum_and_product(4, 5)
print(total, product)  # 9 20
```

<sub>[Solution](solutions.md#solution-1065--returning-both-values)</sub>

## 10.7 Implicit `None` Return

### Exercise 11.7.1 — No return means None

This program prints a message, and the returned value should be `None`.

```python
def announce():
    print("The meeting starts now.")
    return "done"

result = announce()
print(result)  # None
```

<sub>[Solution](solutions.md#solution-1071--no-return-means-none)</sub>

### Exercise 11.7.2 — Forgetting to return

This program should print the doubled value 14, using the function's return value.

```python
def double(number):
    answer = number * 2

print(double(7))  # 14
```

<sub>[Solution](solutions.md#solution-1072--forgetting-to-return)</sub>

### Exercise 11.7.3 — Printing is not returning

This should store the area of a circle approximation and print about 78.5, then use it again.

```python
def circle_area(radius):
    print(3.14 * radius * radius)

area = circle_area(5)
print(area * 2)  # uses the area twice
```

<sub>[Solution](solutions.md#solution-1073--printing-is-not-returning)</sub>

### Exercise 11.7.4 — None in arithmetic

This program should add 5 to the result of a function that returns a number.

```python
def base_value():
    total = 10

print(base_value() + 5)  # 15
```

<sub>[Solution](solutions.md#solution-1074--none-in-arithmetic)</sub>

### Exercise 11.7.5 — Expecting a value

This should check whether the helper returned a usable number and print it; it should print 42.

```python
def lucky_number():
    chosen = 42

number = lucky_number()
print(number)  # 42
```

<sub>[Solution](solutions.md#solution-1075--expecting-a-value)</sub>

## 10.8 Docstrings

### Exercise 11.8.1 — Triple quotes

This function has a docstring describing what it does.

```python
def add(a, b):
    "Return the sum of two numbers.'''
    return a + b

print(add(2, 3))  # 5
```

<sub>[Solution](solutions.md#solution-1081--triple-quotes)</sub>

### Exercise 11.8.2 — Docstring placement

The docstring should sit directly under the `def` line so it becomes the function's documentation.

```python
def to_meters(feet):
    result = feet * 0.3048
    """Convert feet to meters."""
    return result

print(to_meters.__doc__)  # Convert feet to meters.
```

<sub>[Solution](solutions.md#solution-1082--docstring-placement)</sub>

### Exercise 11.8.3 — Reading the docstring

This program should print the docstring of the function.

```python
def half(number):
    """Return half of a number."""
    return number / 2

print(half.__docs__)
```

<sub>[Solution](solutions.md#solution-1083--reading-the-docstring)</sub>

### Exercise 11.8.4 — Closing the quotes

This function should have a one-line docstring and return a perimeter.

```python
def square_perimeter(side):
    """Return the perimeter of a square.
    return side * 4

print(square_perimeter(3))  # 12
```

<sub>[Solution](solutions.md#solution-1084--closing-the-quotes)</sub>

### Exercise 11.8.5 — Docstring, then code

This program should print the function's docstring.

```python
def kelvin(celsius):
    """Convert Celsius to Kelvin.
    return celsius + 273.15

print(kelvin.__doc__)
```

<sub>[Solution](solutions.md#solution-1085--docstring-then-code)</sub>

## 10.9 `*args` and `**kwargs`

### Exercise 11.9.1 — Collecting positionals

This program should sum any number of grades passed in; here the total should be 270.

```python
def total(args):
    return sum(args)

print(total(90, 85, 95))  # 270
```

<sub>[Solution](solutions.md#solution-1091--collecting-positionals)</sub>

### Exercise 11.9.2 — The star on args

This program should print all the extra numbers it receives as a tuple.

```python
def show_numbers(args):
    print(args)

show_numbers(1, 2, 3)  # (1, 2, 3)
```

<sub>[Solution](solutions.md#solution-1092--the-star-on-args)</sub>

### Exercise 11.9.3 — Keyword collection

This program should print the keyword arguments as a dictionary.

```python
def show_options(*kwargs):
    print(kwargs)

show_options(color="blue", size="large")
# {'color': 'blue', 'size': 'large'}
```

<sub>[Solution](solutions.md#solution-1093--keyword-collection)</sub>

### Exercise 11.9.4 — Unpacking into a call

This program should pass the list as separate positional arguments and print 6.

```python
def add_three(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print(add_three(numbers))  # 6
```

<sub>[Solution](solutions.md#solution-1094--unpacking-into-a-call)</sub>

### Exercise 11.9.5 — Order of args and kwargs

This should print both the positional tuple and the keyword dictionary.

```python
def collect(**kwargs, *args):
    print(args)
    print(kwargs)

collect(1, 2, unit="cm")
```

<sub>[Solution](solutions.md#solution-1095--order-of-args-and-kwargs)</sub>

## 10.10 Lambdas

### Exercise 11.10.1 — Lambda syntax

This program should make a one-line function that squares a number and print 25.

```python
square = lambda x: return x * x

print(square(5))  # 25
```

<sub>[Solution](solutions.md#solution-10101--lambda-syntax)</sub>

### Exercise 11.10.2 — Sorting with a key

This should sort the words from shortest to longest.

```python
words = ["pear", "fig", "banana"]
print(sorted(words, key=lambda w: -len(w)))
# ['fig', 'pear', 'banana']
```

<sub>[Solution](solutions.md#solution-10102--sorting-with-a-key)</sub>

### Exercise 11.10.3 — Lambda with map

This should double every number in the list, giving `[2, 4, 6]`.

```python
numbers = [1, 2, 3]
doubled = list(map(lambda n: n + 2, numbers))
print(doubled)  # [2, 4, 6]
```

<sub>[Solution](solutions.md#solution-10103--lambda-with-map)</sub>

### Exercise 11.10.4 — Lambda with filter

This should keep only the even numbers, giving `[2, 4]`.

```python
numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda n: n % 2 == 1, numbers))
print(evens)  # [2, 4]
```

<sub>[Solution](solutions.md#solution-10104--lambda-with-filter)</sub>

### Exercise 11.10.5 — A lambda with two inputs

This should make a one-line function that adds two numbers and print 7.

```python
add = lambda a b: a + b

print(add(3, 4))  # 7
```

<sub>[Solution](solutions.md#solution-10105--a-lambda-with-two-inputs)</sub>

## 10.11 Mutable Default Argument Trap

### Exercise 11.11.1 — The shared default list

Each call should start with a fresh list, so both lines print a single-item list.

```python
def collect(item, basket=[]):
    basket.append(item)
    return basket

print(collect("apple"))   # ['apple']
print(collect("bread"))   # ['bread']
```

<sub>[Solution](solutions.md#solution-10111--the-shared-default-list)</sub>

### Exercise 11.11.2 — A safe default

This should add a reading to a fresh list each call, printing a one-item list each time.

```python
def add_reading(value, readings=[]):
    if readings is None:
        readings = []
    readings.append(value)
    return readings

print(add_reading(20))  # [20]
print(add_reading(22))  # [22]
```

<sub>[Solution](solutions.md#solution-10112--a-safe-default)</sub>

### Exercise 11.11.3 — Guarding the default

The guard should replace the shared default with a new list when none is given.

```python
def add_score(score, scores=None):
    if scores is None:
        scores = scores
    scores.append(score)
    return scores

print(add_score(90))  # [90]
```

<sub>[Solution](solutions.md#solution-10113--guarding-the-default)</sub>

### Exercise 11.11.4 — Fresh dictionary each time

Each call should return a dictionary with just one entry.

```python
def tally(name, counts={}):
    counts[name] = 1
    return counts

print(tally("Maya"))   # {'Maya': 1}
print(tally("Luis"))   # {'Luis': 1}
```

<sub>[Solution](solutions.md#solution-10114--fresh-dictionary-each-time)</sub>

### Exercise 11.11.5 — Checking for None

The guard should run when no list is passed; both calls should print a one-item list.

```python
def append_day(day, days=None):
    if days == []:
        days = []
    days.append(day)
    return days

print(append_day("Mon"))  # ['Mon']
print(append_day("Tue"))  # ['Tue']
```

<sub>[Solution](solutions.md#solution-10115--checking-for-none)</sub>

## 10.12 Pass by Reference vs Pass by Sharing

### Exercise 11.12.1 — Mutating shares the change

Appending inside the function should change the caller's list too.

```python
def add_one(numbers):
    numbers = numbers + [1]

my_list = [10, 20]
add_one(my_list)
print(my_list)  # [10, 20, 1]
```

<sub>[Solution](solutions.md#solution-10121--mutating-shares-the-change)</sub>

### Exercise 11.12.2 — Rebinding stays local

Reassigning the parameter should not change the caller's list, so this prints the original.

```python
def replace(numbers):
    numbers.clear()
    numbers.extend([99, 100])

my_list = [10, 20]
replace(my_list)
print(my_list)  # [10, 20]
```

<sub>[Solution](solutions.md#solution-10122--rebinding-stays-local)</sub>

### Exercise 11.12.3 — Integers are immutable

Changing the parameter inside the function should not affect the caller's number, which stays 5.

```python
def add_ten(value):
    global score
    score = value + 10

score = 5
add_ten(score)
print(score)   # expected: 5
```

<sub>[Solution](solutions.md#solution-10123--integers-are-immutable)</sub>

### Exercise 11.12.4 — Mutate in place

This should add a grade to the shared list in place, so the caller sees three items.

```python
def record_grade(grades, grade):
    grades = grades + [grade]

scores = [80, 90]
record_grade(scores, 100)
print(scores)  # [80, 90, 100]
```

<sub>[Solution](solutions.md#solution-10124--mutate-in-place)</sub>

### Exercise 11.12.5 — Sharing the same object

Both names point to the same list, so the append should be visible outside; this prints a 4-item list.

```python
def append_value(items, value):
    items = list(items)
    items.append(value)

box = [1, 2, 3]
append_value(box, 4)
print(box)  # [1, 2, 3, 4]
```

<sub>[Solution](solutions.md#solution-10125--sharing-the-same-object)</sub>
