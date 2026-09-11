# Chapter 11 — Functions: Find the Bug, Solutions

Each solution names the bug type — **syntax**, **runtime**, or **logical** — explains why the original program misbehaved, and shows the corrected program.

Back to [the exercises](find-the-bug.md).

## 10.1 Your First Function

### Solution 11.1.1 — Defining and calling

**Bug type:** Logical

Writing `welcome` only refers to the function object; it does not run it. You must add parentheses to call it, `welcome()`, so the body executes.

```python
def welcome():
    print("Welcome to the science club!")

welcome()
```

<sub>[Exercise](find-the-bug.md#exercise-1011--defining-and-calling) · [Runnable file](code/find_the_bug/ex_10_01_01_defining_and_calling.py)</sub>

### Solution 11.1.2 — The colon

**Bug type:** Syntax

The `def` header must end with a colon. Without it Python cannot tell where the body begins and raises a `SyntaxError`.

```python
def boiling_point():
    print("Water boils at 100 degrees Celsius.")

boiling_point()
```

<sub>[Exercise](find-the-bug.md#exercise-1012--the-colon) · [Runnable file](code/find_the_bug/ex_10_01_02_the_colon.py)</sub>

### Solution 11.1.3 — The function body

**Bug type:** Syntax

The body must be indented under the `def` line. An unindented `print` makes Python expect an indented block and raises an `IndentationError`.

```python
def days_in_week():
    print("A week has 7 days.")

days_in_week()
```

<sub>[Exercise](find-the-bug.md#exercise-1013--the-function-body) · [Runnable file](code/find_the_bug/ex_10_01_03_the_function_body.py)</sub>

### Solution 11.1.4 — Indenting the body

**Bug type:** Syntax

The two body lines must share the same indentation. The second `print` is indented two spaces instead of four, so Python raises an `IndentationError`.

```python
def study_plan():
    print("Read the chapter.")
    print("Solve five problems.")

study_plan()
```

<sub>[Exercise](find-the-bug.md#exercise-1014--indenting-the-body) · [Runnable file](code/find_the_bug/ex_10_01_04_indenting_the_body.py)</sub>

### Solution 11.1.5 — Remember to call

**Bug type:** Logical

Defining a function never runs it. You must call `freezing_point()` for anything to appear on screen.

```python
def freezing_point():
    print("Water freezes at 0 degrees Celsius.")

freezing_point()
```

<sub>[Exercise](find-the-bug.md#exercise-1015--remember-to-call) · [Runnable file](code/find_the_bug/ex_10_01_05_remember_to_call.py)</sub>

## 10.2 Parameters

### Solution 11.2.1 — Passing an argument

**Bug type:** Runtime

The function needs one argument but the call passes none, raising a `TypeError`. Supply the name in the call.

```python
def greet_student(name):
    print("Hello,", name)

greet_student("Maya")
```

<sub>[Exercise](find-the-bug.md#exercise-1021--passing-an-argument) · [Runnable file](code/find_the_bug/ex_10_02_01_passing_an_argument.py)</sub>

### Solution 11.2.2 — Parameter order

**Bug type:** Logical

The arguments are passed in the wrong order, so `name` becomes 15 and `age` becomes "Maya". Pass the name first, then the age.

```python
def describe(name, age):
    print(name, "is", age, "years old")

describe("Maya", 15)
```

<sub>[Exercise](find-the-bug.md#exercise-1022--parameter-order) · [Runnable file](code/find_the_bug/ex_10_02_02_parameter_order.py)</sub>

### Solution 11.2.3 — Too many arguments

**Bug type:** Runtime

The function takes two parameters but the call passes three, raising a `TypeError`. Pass exactly width and height.

```python
def rectangle_area(width, height):
    return width * height

print(rectangle_area(4, 6))
```

<sub>[Exercise](find-the-bug.md#exercise-1023--too-many-arguments) · [Runnable file](code/find_the_bug/ex_10_02_03_too_many_arguments.py)</sub>

### Solution 11.2.4 — Using the parameter

**Bug type:** Runtime

The call uses `number`, a name that exists only inside the function, so Python raises a `NameError`. Pass an actual value such as 5.

```python
def double(number):
    return number * 2

print(double(5))
```

<sub>[Exercise](find-the-bug.md#exercise-1024--using-the-parameter) · [Runnable file](code/find_the_bug/ex_10_02_04_using_the_parameter.py)</sub>

### Solution 11.2.5 — Two parameters

**Bug type:** Logical

The formula uses `width` twice, ignoring the second parameter. It should be `2 * width + 2 * height` to use both arguments.

```python
def perimeter(width, height):
    return 2 * width + 2 * height

print(perimeter(3, 5))  # 16
```

<sub>[Exercise](find-the-bug.md#exercise-1025--two-parameters) · [Runnable file](code/find_the_bug/ex_10_02_05_two_parameters.py)</sub>

## 10.3 Returning a Result

### Solution 11.3.1 — Return, do not print

**Bug type:** Logical

The function prints instead of returning, so `total` becomes `None`. Use `return` so the caller receives the value.

```python
def add(a, b):
    return a + b

total = add(5, 7)
print(total)  # 12
```

<sub>[Exercise](find-the-bug.md#exercise-1031--return-do-not-print) · [Runnable file](code/find_the_bug/ex_10_03_01_return_do_not_print.py)</sub>

### Solution 11.3.2 — Return the right value

**Bug type:** Logical

Division binds tighter than addition, so only `c` is divided by 3. Wrap the sum in parentheses before dividing.

```python
def average_of_three(a, b, c):
    return (a + b + c) / 3

print(average_of_three(80, 90, 100))  # 90.0
```

<sub>[Exercise](find-the-bug.md#exercise-1032--return-the-right-value) · [Runnable file](code/find_the_bug/ex_10_03_02_return_the_right_value.py)</sub>

### Solution 11.3.3 — Returning early

**Bug type:** Logical

A bare `return` exits immediately and yields `None`; the formula on the next line never runs. Put the expression on the `return` line.

```python
def c_to_f(celsius):
    return celsius * 9 / 5 + 32

print(c_to_f(100))  # 212.0
```

<sub>[Exercise](find-the-bug.md#exercise-1033--returning-early) · [Runnable file](code/find_the_bug/ex_10_03_03_returning_early.py)</sub>

### Solution 11.3.4 — Return what was asked

**Bug type:** Logical

The `else` branch returns `a` instead of `b`, so the larger value is never returned when `b` is bigger. Return `b` in the `else` branch.

```python
def larger(a, b):
    if a > b:
        return a
    else:
        return b

print(larger(4, 9))  # 9
```

<sub>[Exercise](find-the-bug.md#exercise-1034--return-what-was-asked) · [Runnable file](code/find_the_bug/ex_10_03_04_return_what_was_asked.py)</sub>

### Solution 11.3.5 — Use the returned value

**Bug type:** Runtime

The returned value is discarded and `area` is never defined, so printing it raises a `NameError`. Store the result, then print it.

```python
def square(side):
    return side * side

area = square(6)
print(area)  # 36
```

<sub>[Exercise](find-the-bug.md#exercise-1035--use-the-returned-value) · [Runnable file](code/find_the_bug/ex_10_03_05_use_the_returned_value.py)</sub>

## 10.4 Default Arguments

### Solution 11.4.1 — A default value

**Bug type:** Logical

`greet` without parentheses does not call the function. Add `()` so it runs with the default name.

```python
def greet(name="friend"):
    print("Hello,", name)

greet()
```

<sub>[Exercise](find-the-bug.md#exercise-1041--a-default-value) · [Runnable file](code/find_the_bug/ex_10_04_01_a_default_value.py)</sub>

### Solution 11.4.2 — Default tax rate

**Bug type:** Logical

The body multiplies by the literal 0.8 instead of the `rate` parameter, charging 80 percent. Use `rate` so the default 0.08 applies.

```python
def with_tax(price, rate=0.08):
    return price + price * rate

print(with_tax(50))  # 54.0
```

<sub>[Exercise](find-the-bug.md#exercise-1042--default-tax-rate) · [Runnable file](code/find_the_bug/ex_10_04_02_default_tax_rate.py)</sub>

### Solution 11.4.3 — Overriding the default

**Bug type:** Logical

The call meant to keep the default 100 steps but passed 200 as the override, giving `2 * 200 = 400`. To get 200 for two days, pass 100 as the per-day count (or omit it to use the default).

```python
def total_steps(days, per_day=100):
    return days * per_day

print(total_steps(2, 100))  # 200
```

<sub>[Exercise](find-the-bug.md#exercise-1043--overriding-the-default) · [Runnable file](code/find_the_bug/ex_10_04_03_overriding_the_default.py)</sub>

### Solution 11.4.4 — Order of defaults

**Bug type:** Syntax

A parameter with a default cannot come before one without a default, so `def area(height=1, width)` is a `SyntaxError`. Put the non-default parameter first.

```python
def area(width, height=1):
    return width * height

print(area(width=5))  # 5
```

<sub>[Exercise](find-the-bug.md#exercise-1044--order-of-defaults) · [Runnable file](code/find_the_bug/ex_10_04_04_order_of_defaults.py)</sub>

### Solution 11.4.5 — The default is optional

**Bug type:** Runtime

The first parameter `value` has no default, so calling `increase()` with no arguments raises a `TypeError`. Pass a value, or give `value` a default.

```python
def increase(value=0, by=10):
    return value + by

print(increase())  # 10
```

<sub>[Exercise](find-the-bug.md#exercise-1045--the-default-is-optional) · [Runnable file](code/find_the_bug/ex_10_04_05_the_default_is_optional.py)</sub>

## 10.5 Keyword Arguments

### Solution 11.5.1 — Calling by name

**Bug type:** Runtime

`grade=7` is an unexpected keyword argument the function does not accept, raising a `TypeError`. Pass only `name` and `age`.

```python
def introduce(name, age):
    print(name, "is", age, "years old")

introduce(name="Lina", age=12)
```

<sub>[Exercise](find-the-bug.md#exercise-1051--calling-by-name) · [Runnable file](code/find_the_bug/ex_10_05_01_calling_by_name.py)</sub>

### Solution 11.5.2 — Order independence

**Bug type:** Logical

The keyword values are swapped: `time=100` and `distance=5` give 0.05, not 20.0. Match each keyword to the intended value.

```python
def speed(distance, time):
    return distance / time

print(speed(distance=100, time=5))  # 20.0
```

<sub>[Exercise](find-the-bug.md#exercise-1052--order-independence) · [Runnable file](code/find_the_bug/ex_10_05_02_order_independence.py)</sub>

### Solution 11.5.3 — Spelling the keyword

**Bug type:** Runtime

The keyword `temp` does not match the parameter `temperature`, raising a `TypeError`. Use the exact parameter name.

```python
def report(city, temperature):
    print(city, "is at", temperature, "degrees")

report(city="Denver", temperature=30)
```

<sub>[Exercise](find-the-bug.md#exercise-1053--spelling-the-keyword) · [Runnable file](code/find_the_bug/ex_10_05_03_spelling_the_keyword.py)</sub>

### Solution 11.5.4 — Keyword after positional

**Bug type:** Syntax

A positional argument cannot follow a keyword argument, so `score_line(name="Sam", 95)` is a `SyntaxError`. Either make both keywords or both positional.

```python
def score_line(name, points):
    print(name, "scored", points)

score_line(name="Sam", points=95)
```

<sub>[Exercise](find-the-bug.md#exercise-1054--keyword-after-positional) · [Runnable file](code/find_the_bug/ex_10_05_04_keyword_after_positional.py)</sub>

### Solution 11.5.5 — Mixing names and positions

**Bug type:** Runtime

`time=3` is an unexpected keyword the function does not accept, raising a `TypeError`. Pass only the three real parameters.

```python
def interest(principal, rate, years):
    return principal * rate * years

print(interest(1000, years=3, rate=0.02))  # 60.0
```

<sub>[Exercise](find-the-bug.md#exercise-1055--mixing-names-and-positions) · [Runnable file](code/find_the_bug/ex_10_05_05_mixing_names_and_positions.py)</sub>

## 10.6 Multiple Return Values

### Solution 11.6.1 — Returning a pair

**Bug type:** Runtime

The function returns a single value, so unpacking into two names raises a `ValueError`. Return both `min` and `max` as a pair.

```python
def min_max(a, b, c):
    return min(a, b, c), max(a, b, c)

low, high = min_max(31.0, 36.5, 33.0)
print(low, high)  # 31.0 36.5
```

<sub>[Exercise](find-the-bug.md#exercise-1061--returning-a-pair) · [Runnable file](code/find_the_bug/ex_10_06_01_returning_a_pair.py)</sub>

### Solution 11.6.2 — Unpacking the result

**Bug type:** Runtime

The pair is stored in one name `quotient`, and `remainder` is never defined, so printing it raises a `NameError`. Unpack into two names.

```python
def divide(a, b):
    return a // b, a % b

quotient, remainder = divide(17, 5)
print(quotient, remainder)  # 3 2
```

<sub>[Exercise](find-the-bug.md#exercise-1062--unpacking-the-result) · [Runnable file](code/find_the_bug/ex_10_06_02_unpacking_the_result.py)</sub>

### Solution 11.6.3 — Matching the count

**Bug type:** Runtime

The function returns three values but only two names receive them, raising a `ValueError`. Return just the two values you unpack.

```python
def person():
    return "Luis", 14

name, age = person()
print(name, age)  # Luis 14
```

<sub>[Exercise](find-the-bug.md#exercise-1063--matching-the-count) · [Runnable file](code/find_the_bug/ex_10_06_03_matching_the_count.py)</sub>

### Solution 11.6.4 — Order of the tuple

**Bug type:** Logical

The tuple is returned as `(3, 8)` but the caller expects width first, so width prints as 3. Return width then height: `return 8, 3`.

```python
def dimensions():
    return 8, 3

width, height = dimensions()
print("width", width, "height", height)
```

<sub>[Exercise](find-the-bug.md#exercise-1064--order-of-the-tuple) · [Runnable file](code/find_the_bug/ex_10_06_04_order_of_the_tuple.py)</sub>

### Solution 11.6.5 — Returning both values

**Bug type:** Runtime

The first `return` exits the function, so it returns a single integer and tuple unpacking raises a `TypeError`. Return both values in one tuple.

```python
def sum_and_product(a, b):
    return a + b, a * b

total, product = sum_and_product(4, 5)
print(total, product)  # 9 20
```

<sub>[Exercise](find-the-bug.md#exercise-1065--returning-both-values) · [Runnable file](code/find_the_bug/ex_10_06_05_returning_both_values.py)</sub>

## 10.7 Implicit `None` Return

### Solution 11.7.1 — No return means None

**Bug type:** Logical

The function explicitly returns "done", so `result` is not `None`. Remove the `return` so the function returns `None` implicitly.

```python
def announce():
    print("The meeting starts now.")

result = announce()
print(result)  # None
```

<sub>[Exercise](find-the-bug.md#exercise-1071--no-return-means-none) · [Runnable file](code/find_the_bug/ex_10_07_01_no_return_means_none.py)</sub>

### Solution 11.7.2 — Forgetting to return

**Bug type:** Logical

The function computes `answer` but never returns it, so it returns `None` and prints `None`. Add a `return`.

```python
def double(number):
    answer = number * 2
    return answer

print(double(7))  # 14
```

<sub>[Exercise](find-the-bug.md#exercise-1072--forgetting-to-return) · [Runnable file](code/find_the_bug/ex_10_07_02_forgetting_to_return.py)</sub>

### Solution 11.7.3 — Printing is not returning

**Bug type:** Runtime

The function prints but returns `None`, so `area` is `None` and `area * 2` raises a `TypeError`. Return the value instead of printing it.

```python
def circle_area(radius):
    return 3.14 * radius * radius

area = circle_area(5)
print(area * 2)  # uses the area twice
```

<sub>[Exercise](find-the-bug.md#exercise-1073--printing-is-not-returning) · [Runnable file](code/find_the_bug/ex_10_07_03_printing_is_not_returning.py)</sub>

### Solution 11.7.4 — None in arithmetic

**Bug type:** Runtime

The function never returns `total`, so it returns `None`, and `None + 5` raises a `TypeError`. Return the value.

```python
def base_value():
    total = 10
    return total

print(base_value() + 5)  # 15
```

<sub>[Exercise](find-the-bug.md#exercise-1074--none-in-arithmetic) · [Runnable file](code/find_the_bug/ex_10_07_04_none_in_arithmetic.py)</sub>

### Solution 11.7.5 — Expecting a value

**Bug type:** Logical

The function assigns `chosen` but never returns it, so `number` is `None`. Return `chosen`.

```python
def lucky_number():
    chosen = 42
    return chosen

number = lucky_number()
print(number)  # 42
```

<sub>[Exercise](find-the-bug.md#exercise-1075--expecting-a-value) · [Runnable file](code/find_the_bug/ex_10_07_05_expecting_a_value.py)</sub>

## 10.8 Docstrings

### Solution 11.8.1 — Triple quotes

**Bug type:** Syntax

The string opens with a single double-quote but closes with triple single-quotes, so the quotes do not match and Python raises a `SyntaxError`. Use matching triple quotes.

```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b

print(add(2, 3))  # 5
```

<sub>[Exercise](find-the-bug.md#exercise-1081--triple-quotes) · [Runnable file](code/find_the_bug/ex_10_08_01_triple_quotes.py)</sub>

### Solution 11.8.2 — Docstring placement

**Bug type:** Logical

A string becomes the docstring only when it is the first statement in the body; here it sits after an assignment, so `__doc__` is `None`. Move the docstring to the top.

```python
def to_meters(feet):
    """Convert feet to meters."""
    result = feet * 0.3048
    return result

print(to_meters.__doc__)  # Convert feet to meters.
```

<sub>[Exercise](find-the-bug.md#exercise-1082--docstring-placement) · [Runnable file](code/find_the_bug/ex_10_08_02_docstring_placement.py)</sub>

### Solution 11.8.3 — Reading the docstring

**Bug type:** Runtime

The attribute is `__doc__`, not `__docs__`, so accessing it raises an `AttributeError`. Use the correct name.

```python
def half(number):
    """Return half of a number."""
    return number / 2

print(half.__doc__)
```

<sub>[Exercise](find-the-bug.md#exercise-1083--reading-the-docstring) · [Runnable file](code/find_the_bug/ex_10_08_03_reading_the_docstring.py)</sub>

### Solution 11.8.4 — Closing the quotes

**Bug type:** Syntax

The triple-quoted docstring is never closed, so Python reads the rest of the file as part of the string and raises a `SyntaxError`. Close the docstring.

```python
def square_perimeter(side):
    """Return the perimeter of a square."""
    return side * 4

print(square_perimeter(3))  # 12
```

<sub>[Exercise](find-the-bug.md#exercise-1084--closing-the-quotes) · [Runnable file](code/find_the_bug/ex_10_08_04_closing_the_quotes.py)</sub>

### Solution 11.8.5 — Docstring, then code

**Bug type:** Syntax

The triple-quoted docstring is opened with `"""` but never closed, so Python reads the rest of the file as one unterminated string and reports a syntax error. Close the docstring on the same line.

```python
def kelvin(celsius):
    """Convert Celsius to Kelvin."""
    return celsius + 273.15

print(kelvin.__doc__)   # Convert Celsius to Kelvin.
```

<sub>[Exercise](find-the-bug.md#exercise-1085--docstring-then-code) · [Runnable file](code/find_the_bug/ex_10_08_05_docstring_then_code.py)</sub>

## 10.9 `*args` and `**kwargs`

### Solution 11.9.1 — Collecting positionals

**Bug type:** Runtime

Without a `*`, `args` is a single parameter, so passing three numbers raises a `TypeError`. Add the star to collect them into a tuple.

```python
def total(*args):
    return sum(args)

print(total(90, 85, 95))  # 270
```

<sub>[Exercise](find-the-bug.md#exercise-1091--collecting-positionals) · [Runnable file](code/find_the_bug/ex_10_09_01_collecting_positionals.py)</sub>

### Solution 11.9.2 — The star on args

**Bug type:** Runtime

`args` without a star accepts only one argument, so passing three raises a `TypeError`. Use `*args` to gather them.

```python
def show_numbers(*args):
    print(args)

show_numbers(1, 2, 3)  # (1, 2, 3)
```

<sub>[Exercise](find-the-bug.md#exercise-1092--the-star-on-args) · [Runnable file](code/find_the_bug/ex_10_09_02_the_star_on_args.py)</sub>

### Solution 11.9.3 — Keyword collection

**Bug type:** Runtime

A single star collects positional arguments; keyword arguments need two stars. With one star, the keyword call raises a `TypeError`. Use `**kwargs`.

```python
def show_options(**kwargs):
    print(kwargs)

show_options(color="blue", size="large")
# {'color': 'blue', 'size': 'large'}
```

<sub>[Exercise](find-the-bug.md#exercise-1093--keyword-collection) · [Runnable file](code/find_the_bug/ex_10_09_03_keyword_collection.py)</sub>

### Solution 11.9.4 — Unpacking into a call

**Bug type:** Runtime

Passing the list as one argument fills only `a`, leaving `b` and `c` missing, which raises a `TypeError`. Unpack with a star: `add_three(*numbers)`.

```python
def add_three(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print(add_three(*numbers))  # 6
```

<sub>[Exercise](find-the-bug.md#exercise-1094--unpacking-into-a-call) · [Runnable file](code/find_the_bug/ex_10_09_04_unpacking_into_a_call.py)</sub>

### Solution 11.9.5 — Order of args and kwargs

**Bug type:** Syntax

`**kwargs` must come after `*args` in the definition, so `def collect(**kwargs, *args)` is a `SyntaxError`. Put `*args` first.

```python
def collect(*args, **kwargs):
    print(args)
    print(kwargs)

collect(1, 2, unit="cm")
```

<sub>[Exercise](find-the-bug.md#exercise-1095--order-of-args-and-kwargs) · [Runnable file](code/find_the_bug/ex_10_09_05_order_of_args_and_kwargs.py)</sub>

## 10.10 Lambdas

### Solution 11.10.1 — Lambda syntax

**Bug type:** Syntax

A lambda body is a single expression and cannot contain `return`, so `lambda x: return x * x` is a `SyntaxError`. Drop the `return`.

```python
square = lambda x: x * x

print(square(5))  # 25
```

<sub>[Exercise](find-the-bug.md#exercise-10101--lambda-syntax) · [Runnable file](code/find_the_bug/ex_10_10_01_lambda_syntax.py)</sub>

### Solution 11.10.2 — Sorting with a key

**Bug type:** Logical

The key `-len(w)` sorts longest first; for shortest first the key should be `len(w)`.

```python
words = ["pear", "fig", "banana"]
print(sorted(words, key=lambda w: len(w)))
# ['fig', 'pear', 'banana']
```

<sub>[Exercise](find-the-bug.md#exercise-10102--sorting-with-a-key) · [Runnable file](code/find_the_bug/ex_10_10_02_sorting_with_a_key.py)</sub>

### Solution 11.10.3 — Lambda with map

**Bug type:** Logical

The lambda adds 2 instead of doubling, so `1` becomes 3, not 2. Multiply by 2 to double each number.

```python
numbers = [1, 2, 3]
doubled = list(map(lambda n: n * 2, numbers))
print(doubled)  # [2, 4, 6]
```

<sub>[Exercise](find-the-bug.md#exercise-10103--lambda-with-map) · [Runnable file](code/find_the_bug/ex_10_10_03_lambda_with_map.py)</sub>

### Solution 11.10.4 — Lambda with filter

**Bug type:** Logical

`n % 2 == 1` keeps odd numbers, not even ones. Test `n % 2 == 0` to keep the even numbers.

```python
numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda n: n % 2 == 0, numbers))
print(evens)  # [2, 4]
```

<sub>[Exercise](find-the-bug.md#exercise-10104--lambda-with-filter) · [Runnable file](code/find_the_bug/ex_10_10_04_lambda_with_filter.py)</sub>

### Solution 11.10.5 — A lambda with two inputs

**Bug type:** Syntax

Lambda parameters must be separated by a comma, so `lambda a b: a + b` is a `SyntaxError`. Write `lambda a, b: a + b`.

```python
add = lambda a, b: a + b

print(add(3, 4))  # 7
```

<sub>[Exercise](find-the-bug.md#exercise-10105--a-lambda-with-two-inputs) · [Runnable file](code/find_the_bug/ex_10_10_05_a_lambda_with_two_inputs.py)</sub>

## 10.11 Mutable Default Argument Trap

### Solution 11.11.1 — The shared default list

**Bug type:** Logical

The default list is created once and shared across calls, so it keeps growing. Use `None` as the default and build a fresh list inside.

```python
def collect(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket

print(collect("apple"))   # ['apple']
print(collect("bread"))   # ['bread']
```

<sub>[Exercise](find-the-bug.md#exercise-10111--the-shared-default-list) · [Runnable file](code/find_the_bug/ex_10_11_01_the_shared_default_list.py)</sub>

### Solution 11.11.2 — A safe default

**Bug type:** Logical

The guard checks for `None`, but the default is a shared list, not `None`, so the guard never runs and the list grows. Make the default `None`.

```python
def add_reading(value, readings=None):
    if readings is None:
        readings = []
    readings.append(value)
    return readings

print(add_reading(20))  # [20]
print(add_reading(22))  # [22]
```

<sub>[Exercise](find-the-bug.md#exercise-10112--a-safe-default) · [Runnable file](code/find_the_bug/ex_10_11_02_a_safe_default.py)</sub>

### Solution 11.11.3 — Guarding the default

**Bug type:** Runtime

The guard assigns `scores = scores`, leaving it `None`, so `append` raises an `AttributeError`. Assign a new empty list instead.

```python
def add_score(score, scores=None):
    if scores is None:
        scores = []
    scores.append(score)
    return scores

print(add_score(90))  # [90]
```

<sub>[Exercise](find-the-bug.md#exercise-10113--guarding-the-default) · [Runnable file](code/find_the_bug/ex_10_11_03_guarding_the_default.py)</sub>

### Solution 11.11.4 — Fresh dictionary each time

**Bug type:** Logical

The default dictionary is created once and shared, so entries accumulate across calls. Use `None` and create a fresh dictionary inside.

```python
def tally(name, counts=None):
    if counts is None:
        counts = {}
    counts[name] = 1
    return counts

print(tally("Maya"))   # {'Maya': 1}
print(tally("Luis"))   # {'Luis': 1}
```

<sub>[Exercise](find-the-bug.md#exercise-10114--fresh-dictionary-each-time) · [Runnable file](code/find_the_bug/ex_10_11_04_fresh_dictionary_each_time.py)</sub>

### Solution 11.11.5 — Checking for None

**Bug type:** Runtime

The default is `None`, but the guard checks `== []`, which is never true for `None`, so `days.append` raises an `AttributeError` on the first call. Check `is None`.

```python
def append_day(day, days=None):
    if days is None:
        days = []
    days.append(day)
    return days

print(append_day("Mon"))  # ['Mon']
print(append_day("Tue"))  # ['Tue']
```

<sub>[Exercise](find-the-bug.md#exercise-10115--checking-for-none) · [Runnable file](code/find_the_bug/ex_10_11_05_checking_for_none.py)</sub>

## 10.12 Pass by Reference vs Pass by Sharing

### Solution 11.12.1 — Mutating shares the change

**Bug type:** Logical

`numbers = numbers + [1]` builds a new list and rebinds the local name, leaving the caller's list unchanged. Use `append`, which mutates the shared list.

```python
def add_one(numbers):
    numbers.append(1)

my_list = [10, 20]
add_one(my_list)
print(my_list)  # [10, 20, 1]
```

<sub>[Exercise](find-the-bug.md#exercise-10121--mutating-shares-the-change) · [Runnable file](code/find_the_bug/ex_10_12_01_mutating_shares_the_change.py)</sub>

### Solution 11.12.2 — Rebinding stays local

**Bug type:** Logical

`clear` and `extend` mutate the shared list in place, so the caller sees `[99, 100]`, not the original. To leave the caller unchanged, rebind the local name instead.

```python
def replace(numbers):
    numbers = [99, 100]

my_list = [10, 20]
replace(my_list)
print(my_list)  # [10, 20]
```

<sub>[Exercise](find-the-bug.md#exercise-10122--rebinding-stays-local) · [Runnable file](code/find_the_bug/ex_10_12_02_rebinding_stays_local.py)</sub>

### Solution 11.12.3 — Integers are immutable

**Bug type:** Logical

The `global` line makes the function overwrite the caller's `score`, so it prints 15. An integer is passed by sharing: reassigning the local `value` never affects the caller. Drop the `global` line and work with the parameter.

```python
def add_ten(value):
    value = value + 10

score = 5
add_ten(score)
print(score)   # 5
```

<sub>[Exercise](find-the-bug.md#exercise-10123--integers-are-immutable) · [Runnable file](code/find_the_bug/ex_10_12_03_integers_are_immutable.py)</sub>

### Solution 11.12.4 — Mutate in place

**Bug type:** Logical

`grades = grades + [grade]` rebinds the local name to a new list, so the caller's list is unchanged. Use `append` to mutate the shared list in place.

```python
def record_grade(grades, grade):
    grades.append(grade)

scores = [80, 90]
record_grade(scores, 100)
print(scores)  # [80, 90, 100]
```

<sub>[Exercise](find-the-bug.md#exercise-10124--mutate-in-place) · [Runnable file](code/find_the_bug/ex_10_12_04_mutate_in_place.py)</sub>

### Solution 11.12.5 — Sharing the same object

**Bug type:** Logical

`items = list(items)` makes a separate copy, so the append affects only the copy and the caller's list is unchanged. Append directly to the passed-in list.

```python
def append_value(items, value):
    items.append(value)

box = [1, 2, 3]
append_value(box, 4)
print(box)  # [1, 2, 3, 4]
```

<sub>[Exercise](find-the-bug.md#exercise-10125--sharing-the-same-object) · [Runnable file](code/find_the_bug/ex_10_12_05_sharing_the_same_object.py)</sub>
