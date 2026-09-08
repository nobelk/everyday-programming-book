# Chapter 7 — Operators: Find the Bug

Part III · Data and Operations — *Everyday Programming*

The exercises below cover Python operators—arithmetic, assignment, comparison, boolean, membership and identity—and each program hides exactly one bug; find the single bug in each.

Read each program, decide what it is supposed to print, and find the one line that stops it. Then check yourself against [the solutions](solutions.md). The corrected programs are also available as runnable files under [`code/find_the_bug/`](code/find_the_bug).

**25 exercises in 5 sections.**

## 7.1 Arithmetic Operators

### Exercise 7.1.1 — Average of three test scores

This program should print the average of three test scores, which is `84.0`.

```python
score1 = 78
score2 = 85
score3 = 89
average = score1 + score2 + score3 / 3
print(average)   # expected: 84.0
```

<sub>[Solution](solutions.md#solution-711--average-of-three-test-scores)</sub>

### Exercise 7.1.2 — Rectangle area

This program should compute the area of a rectangle (length times width) and print `15`.

```python
length = 5
width = 3
area = length + width
print(area)   # expected: 15
```

<sub>[Solution](solutions.md#solution-712--rectangle-area)</sub>

### Exercise 7.1.3 — Eggs left over

A baker has 17 eggs and packs them into cartons of 6. This program should print how many eggs are left over after filling whole cartons, which is `5`.

```python
total_eggs = 17
carton_size = 6
leftover = total_eggs // carton_size
print(leftover)   # expected: 5
```

<sub>[Solution](solutions.md#solution-713--eggs-left-over)</sub>

### Exercise 7.1.4 — Kinetic energy

Kinetic energy is one-half times mass times speed squared. For a mass of 2 kg moving at 3 m/s this should print `9.0`.

```python
mass = 2
speed = 3
energy = 0.5 * mass * speed * 2
print(energy)   # expected: 9.0
```

<sub>[Solution](solutions.md#solution-714--kinetic-energy)</sub>

### Exercise 7.1.5 — Total cost with tax

An item costs $20 and tax is 10%. This program should print the total cost including tax, which is `22.0`.

```python
price = 20
tax_rate = 0.10
total = price + price * tax_rate
print(total   # expected: 22.0
```

<sub>[Solution](solutions.md#solution-715--total-cost-with-tax)</sub>

## 7.2 Assignment Operator

### Exercise 7.2.1 — Saving up for a bike

A bike costs $240 and you start with $60, then add $45 each of two weeks. This program should print your savings, which is `150`.

```python
savings = 60
savings = 45
savings += 45
print(savings)   # expected: 150
```

<sub>[Solution](solutions.md#solution-721--saving-up-for-a-bike)</sub>

### Exercise 7.2.2 — Counting down rocket seconds

This program should subtract 3 from a 10-second countdown and print the time remaining, which is `7`.

```python
seconds_left = 10
seconds_left =- 3
print(seconds_left)   # expected: 7
```

<sub>[Solution](solutions.md#solution-722--counting-down-rocket-seconds)</sub>

### Exercise 7.2.3 — Doubling a recipe

A recipe needs 2 cups of flour, and this program should double it for a bigger batch, printing `4`.

```python
cups_flour = 2
cups_flour *= 2
print(Cups_flour)   # expected: 4
```

<sub>[Solution](solutions.md#solution-723--doubling-a-recipe)</sub>

### Exercise 7.2.4 — Splitting candy among friends

There are 12 pieces of candy to split evenly among 4 friends. This program should update the count to pieces-per-friend and print `3`.

```python
candy = 12
friends = 4
candy /= friends
print(candy)   # expected: 3
```

<sub>[Solution](solutions.md#solution-724--splitting-candy-among-friends)</sub>

### Exercise 7.2.5 — Running total of steps

This program should add today's 4{,}000 steps to yesterday's 6{,}000 and print the running total, which is `10000`.

```python
total_steps = 6000
today_steps = 4000
total_steps + today_steps
print(total_steps)   # expected: 10000
```

<sub>[Solution](solutions.md#solution-725--running-total-of-steps)</sub>

## 7.3 Comparison Operators

### Exercise 7.3.1 — Passing grade check

A grade of 60 or above passes. For a score of 60 this program should print `True`.

```python
score = 60
passing = score > 60
print(passing)   # expected: True
```

<sub>[Solution](solutions.md#solution-731--passing-grade-check)</sub>

### Exercise 7.3.2 — Are two distances equal?

This program should check whether two measured distances are equal and print `True`.

```python
distance_a = 100
distance_b = 100
print(distance_a = distance_b)   # expected: True
```

<sub>[Solution](solutions.md#solution-732--are-two-distances-equal)</sub>

### Exercise 7.3.3 — Temperature in safe range

Water is liquid between 0 and 100 degrees Celsius. For 25 degrees this program should print `True`.

```python
temp_c = 25
in_range = 0 < temp_c > 100
print(in_range)   # expected: True
```

<sub>[Solution](solutions.md#solution-733--temperature-in-safe-range)</sub>

### Exercise 7.3.4 — Different answers

This program should check whether a student's answer differs from the correct answer and print `True`.

```python
correct_answer = 42
student_answer = 38
print(student_answer = ! correct_answer)   # expected: True
```

<sub>[Solution](solutions.md#solution-734--different-answers)</sub>

### Exercise 7.3.5 — Within speed limit

The speed limit is 65. For a speed of 65 this program should report that the driver is within the limit and print `True`.

```python
speed = 65
limit = 65
within_limit = speed < limit
print(within_limit)   # expected: True
```

<sub>[Solution](solutions.md#solution-735--within-speed-limit)</sub>

## 7.4 Boolean Operators

### Exercise 7.4.1 — Eligible to vote

A person may vote only if they are at least 18 *and* a citizen. This adult is not a citizen, so the program should print `False`.

```python
age = 20
is_citizen = False
can_vote = age >= 18 or is_citizen
print(can_vote)   # expected: False
```

<sub>[Solution](solutions.md#solution-741--eligible-to-vote)</sub>

### Exercise 7.4.2 — Weekend or holiday

You can sleep in if it is a weekend or a holiday. This program should print `True`.

```python
is_weekend = False
is_holiday = True
sleep_in = is_weekend and is_holiday
print(sleep_in)   # expected: True
```

<sub>[Solution](solutions.md#solution-742--weekend-or-holiday)</sub>

### Exercise 7.4.3 — Not raining

This program should report that it is not raining and print `True`.

```python
is_raining = False
stay_dry = is_raining not
print(stay_dry)   # expected: True
```

<sub>[Solution](solutions.md#solution-743--not-raining)</sub>

### Exercise 7.4.4 — Safe to swim

It is safe to swim if a lifeguard is on duty and the water is calm. This program should print `True`.

```python
lifeguard_on_duty = True
water_is_calm = True
safe_to_swim = lifeguard_on_duty and water_is_calm:
print(safe_to_swim)   # expected: True
```

<sub>[Solution](solutions.md#solution-744--safe-to-swim)</sub>

### Exercise 7.4.5 — Free shipping

Shipping is free if the order is over $50 or the customer is a member. This program should print `True` for a $30 order by a member.

```python
order_total = 30
is_member = True
free_shipping = order_total > 50 and is_member
print(free_shipping)   # expected: True
```

<sub>[Solution](solutions.md#solution-745--free-shipping)</sub>

## 7.5 Other Operators

### Exercise 7.5.1 — Vowel check

This program should report whether the letter is a vowel and print `True`.

```python
letter = "e"
vowels = "aeiou"
is_vowel = letter not in vowels
print(is_vowel)   # expected: True
```

<sub>[Solution](solutions.md#solution-751--vowel-check)</sub>

### Exercise 7.5.2 — Odd number not in list

This program should check that 7 is not among the listed even numbers and print `True`.

```python
even_numbers = [2, 4, 6, 8]
number = 7
result = number in not even_numbers
print(result)   # expected: True
```

<sub>[Solution](solutions.md#solution-752--odd-number-not-in-list)</sub>

### Exercise 7.5.3 — Missing value check

This program should report that a measurement is missing (its value is `None`) and print `True`.

```python
measurement = None
is_missing = measurement is not None
print(is_missing)   # expected: True
```

<sub>[Solution](solutions.md#solution-753--missing-value-check)</sub>

### Exercise 7.5.4 — First planet in the list

This program should print the first planet, `"Mercury"`.

```python
planets = ["Mercury", "Venus", "Earth"]
first_planet = planets[1]
print(first_planet)   # expected: Mercury
```

<sub>[Solution](solutions.md#solution-754--first-planet-in-the-list)</sub>

### Exercise 7.5.5 — Day in the schedule

This program should report whether "Wednesday" is in the schedule and print `True`.

```python
schedule = ["Monday", "Wednesday", "Friday"]
has_wednesday = "Wednesday" not in schedule
print(has_wednesday)   # expected: True
```

<sub>[Solution](solutions.md#solution-755--day-in-the-schedule)</sub>
