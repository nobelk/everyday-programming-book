# Chapter 7 — Operators: Find the Bug, Solutions

Each solution names the bug type — **syntax**, **runtime**, or **logical** — explains why the original program misbehaved, and shows the corrected program.

Back to [the exercises](find-the-bug.md).

## 7.1 Arithmetic Operators

### Solution 7.1.1 — Average of three test scores

**Bug type:** Logical

Because `/` has higher precedence than `+`, only `score3` is divided by 3, so the answer is wrong. Wrap the sum in parentheses so the division applies to the whole total.

```python
score1 = 78
score2 = 85
score3 = 89
average = (score1 + score2 + score3) / 3
print(average)   # 84.0
```

<sub>[Exercise](find-the-bug.md#exercise-711--average-of-three-test-scores) · [Runnable file](code/find_the_bug/ex_07_01_01_average_of_three_test_scores.py)</sub>

### Solution 7.1.2 — Rectangle area

**Bug type:** Logical

Area is length times width, but the program adds them, giving 8 instead of 15. Use `*` instead of `+`.

```python
length = 5
width = 3
area = length * width
print(area)   # 15
```

<sub>[Exercise](find-the-bug.md#exercise-712--rectangle-area) · [Runnable file](code/find_the_bug/ex_07_01_02_rectangle_area.py)</sub>

### Solution 7.1.3 — Eggs left over

**Bug type:** Logical

Floor division `//` gives the number of full cartons (2), not the leftover eggs. The remainder operator `%` gives what is left over.

```python
total_eggs = 17
carton_size = 6
leftover = total_eggs % carton_size
print(leftover)   # 5
```

<sub>[Exercise](find-the-bug.md#exercise-713--eggs-left-over) · [Runnable file](code/find_the_bug/ex_07_01_03_eggs_left_over.py)</sub>

### Solution 7.1.4 — Kinetic energy

**Bug type:** Logical

The formula multiplies speed by 2 instead of squaring it, giving 6.0 rather than 9.0. Use the power operator `**` to square the speed.

```python
mass = 2
speed = 3
energy = 0.5 * mass * speed ** 2
print(energy)   # 9.0
```

<sub>[Exercise](find-the-bug.md#exercise-714--kinetic-energy) · [Runnable file](code/find_the_bug/ex_07_01_04_kinetic_energy.py)</sub>

### Solution 7.1.5 — Total cost with tax

**Bug type:** Syntax

The call to `print` is missing its closing parenthesis, so the program will not parse. Add the `)`.

```python
price = 20
tax_rate = 0.10
total = price + price * tax_rate
print(total)   # 22.0
```

<sub>[Exercise](find-the-bug.md#exercise-715--total-cost-with-tax) · [Runnable file](code/find_the_bug/ex_07_01_05_total_cost_with_tax.py)</sub>

## 7.2 Assignment Operator

### Solution 7.2.1 — Saving up for a bike

**Bug type:** Logical

The second line uses plain assignment `=` and overwrites the starting $60 with $45, so the final total is wrong. It should be augmented assignment `+=` to add the deposit.

```python
savings = 60
savings += 45
savings += 45
print(savings)   # 150
```

<sub>[Exercise](find-the-bug.md#exercise-721--saving-up-for-a-bike) · [Runnable file](code/find_the_bug/ex_07_02_01_saving_up_for_a_bike.py)</sub>

### Solution 7.2.2 — Counting down rocket seconds

**Bug type:** Logical

The line `seconds_left =- 3` is parsed as assigning the value `-3`, not as subtracting 3. The intended augmented-assignment operator is `-=`.

```python
seconds_left = 10
seconds_left -= 3
print(seconds_left)   # 7
```

<sub>[Exercise](find-the-bug.md#exercise-722--counting-down-rocket-seconds) · [Runnable file](code/find_the_bug/ex_07_02_02_counting_down_rocket_seconds.py)</sub>

### Solution 7.2.3 — Doubling a recipe

**Bug type:** Runtime

The variable is `cups_flour`, but `print` refers to `Cups_flour` with a capital C, raising a `NameError`. Match the name exactly.

```python
cups_flour = 2
cups_flour *= 2
print(cups_flour)   # 4
```

<sub>[Exercise](find-the-bug.md#exercise-723--doubling-a-recipe) · [Runnable file](code/find_the_bug/ex_07_02_03_doubling_a_recipe.py)</sub>

### Solution 7.2.4 — Splitting candy among friends

**Bug type:** Logical

`/=` performs true division and produces `3.0`, a float, instead of the whole number 3. Use floor-division assignment `//=` to keep an integer count of pieces per friend.

```python
candy = 12
friends = 4
candy //= friends
print(candy)   # 3
```

<sub>[Exercise](find-the-bug.md#exercise-724--splitting-candy-among-friends) · [Runnable file](code/find_the_bug/ex_07_02_04_splitting_candy_among_friends.py)</sub>

### Solution 7.2.5 — Running total of steps

**Bug type:** Logical

The line computes `total_steps + today_steps` but throws the result away because it never assigns it back. Use `+=` so the running total is updated.

```python
total_steps = 6000
today_steps = 4000
total_steps += today_steps
print(total_steps)   # 10000
```

<sub>[Exercise](find-the-bug.md#exercise-725--running-total-of-steps) · [Runnable file](code/find_the_bug/ex_07_02_05_running_total_of_steps.py)</sub>

## 7.3 Comparison Operators

### Solution 7.3.1 — Passing grade check

**Bug type:** Logical

A score of exactly 60 should pass, but `>` excludes 60 and gives `False`. Use `>=` to include the boundary.

```python
score = 60
passing = score >= 60
print(passing)   # True
```

<sub>[Exercise](find-the-bug.md#exercise-731--passing-grade-check) · [Runnable file](code/find_the_bug/ex_07_03_01_passing_grade_check.py)</sub>

### Solution 7.3.2 — Are two distances equal?

**Bug type:** Runtime

Inside a function call, `distance_a = distance_b` is read as a keyword argument, so `print` raises a `TypeError` about an invalid keyword argument. Comparison needs the equality operator `==`.

```python
distance_a = 100
distance_b = 100
print(distance_a == distance_b)   # True
```

<sub>[Exercise](find-the-bug.md#exercise-732--are-two-distances-equal) · [Runnable file](code/find_the_bug/ex_07_03_02_are_two_distances_equal.py)</sub>

### Solution 7.3.3 — Temperature in safe range

**Bug type:** Logical

The chained comparison `0 < temp_c > 100` checks that the temperature is above both 0 and 100, which is wrong. It should be `0 < temp_c < 100` to test the range between them.

```python
temp_c = 25
in_range = 0 < temp_c < 100
print(in_range)   # True
```

<sub>[Exercise](find-the-bug.md#exercise-733--temperature-in-safe-range) · [Runnable file](code/find_the_bug/ex_07_03_03_temperature_in_safe_range.py)</sub>

### Solution 7.3.4 — Different answers

**Bug type:** Syntax

The "not equal" operator is written `!=`, not `= !`, so the expression will not parse. Use `!=`.

```python
correct_answer = 42
student_answer = 38
print(student_answer != correct_answer)   # True
```

<sub>[Exercise](find-the-bug.md#exercise-734--different-answers) · [Runnable file](code/find_the_bug/ex_07_03_04_different_answers.py)</sub>

### Solution 7.3.5 — Within speed limit

**Bug type:** Logical

A speed of exactly 65 is within the limit, but `<` excludes it and gives `False`. Use `<=` to include the limit itself.

```python
speed = 65
limit = 65
within_limit = speed <= limit
print(within_limit)   # True
```

<sub>[Exercise](find-the-bug.md#exercise-735--within-speed-limit) · [Runnable file](code/find_the_bug/ex_07_03_05_within_speed_limit.py)</sub>

## 7.4 Boolean Operators

### Solution 7.4.1 — Eligible to vote

**Bug type:** Logical

Voting requires both conditions, but `or` returns `True` when only one holds, so a non-citizen adult is wrongly allowed. Use `and` so both age and citizenship must be satisfied.

```python
age = 20
is_citizen = False
can_vote = age >= 18 and is_citizen
print(can_vote)   # False
```

<sub>[Exercise](find-the-bug.md#exercise-741--eligible-to-vote) · [Runnable file](code/find_the_bug/ex_07_04_01_eligible_to_vote.py)</sub>

### Solution 7.4.2 — Weekend or holiday

**Bug type:** Logical

Either condition should let you sleep in, but `and` requires both to be true, giving `False`. Use `or`.

```python
is_weekend = False
is_holiday = True
sleep_in = is_weekend or is_holiday
print(sleep_in)   # True
```

<sub>[Exercise](find-the-bug.md#exercise-742--weekend-or-holiday) · [Runnable file](code/find_the_bug/ex_07_04_02_weekend_or_holiday.py)</sub>

### Solution 7.4.3 — Not raining

**Bug type:** Syntax

`not` is a prefix operator and must come before its value; writing `is_raining not` will not parse. Move `not` in front to get `not is_raining`.

```python
is_raining = False
stay_dry = not is_raining
print(stay_dry)   # True
```

<sub>[Exercise](find-the-bug.md#exercise-743--not-raining) · [Runnable file](code/find_the_bug/ex_07_04_03_not_raining.py)</sub>

### Solution 7.4.4 — Safe to swim

**Bug type:** Syntax

A boolean expression assigned to a variable must not end with a colon; the trailing `:` makes the line invalid. Remove it.

```python
lifeguard_on_duty = True
water_is_calm = True
safe_to_swim = lifeguard_on_duty and water_is_calm
print(safe_to_swim)   # True
```

<sub>[Exercise](find-the-bug.md#exercise-744--safe-to-swim) · [Runnable file](code/find_the_bug/ex_07_04_04_safe_to_swim.py)</sub>

### Solution 7.4.5 — Free shipping

**Bug type:** Logical

Free shipping needs the order over $50 *or* the customer to be a member, but `and` requires both, so a $30 member order returns `False`. Use `or`. (Note short-circuiting: with `or`, once `is_member` is true the result is true regardless of the order total.)

```python
order_total = 30
is_member = True
free_shipping = order_total > 50 or is_member
print(free_shipping)   # True
```

<sub>[Exercise](find-the-bug.md#exercise-745--free-shipping) · [Runnable file](code/find_the_bug/ex_07_04_05_free_shipping.py)</sub>

## 7.5 Other Operators

### Solution 7.5.1 — Vowel check

**Bug type:** Logical

The code used `not in`, which would report `False` for a real vowel. To confirm membership, use the `in` operator.

```python
letter = "e"
vowels = "aeiou"
is_vowel = letter in vowels
print(is_vowel)   # True
```

<sub>[Exercise](find-the-bug.md#exercise-751--vowel-check) · [Runnable file](code/find_the_bug/ex_07_05_01_vowel_check.py)</sub>

### Solution 7.5.2 — Odd number not in list

**Bug type:** Syntax

The membership operator is the two-word phrase `not in`, written in that order; `in not` will not parse. Use `not in` so a value absent from the list yields `True`.

```python
even_numbers = [2, 4, 6, 8]
number = 7
result = number not in even_numbers
print(result)   # True
```

<sub>[Exercise](find-the-bug.md#exercise-752--odd-number-not-in-list) · [Runnable file](code/find_the_bug/ex_07_05_02_odd_number_not_in_list.py)</sub>

### Solution 7.5.3 — Missing value check

**Bug type:** Logical

`measurement is not None` is `False` when the value really is `None`, the opposite of what we want. Use the identity operator `is` to test that the value is exactly `None`.

```python
measurement = None
is_missing = measurement is None
print(is_missing)   # True
```

<sub>[Exercise](find-the-bug.md#exercise-753--missing-value-check) · [Runnable file](code/find_the_bug/ex_07_05_03_missing_value_check.py)</sub>

### Solution 7.5.4 — First planet in the list

**Bug type:** Logical

List indexing starts at 0, so `planets[1]` is the second planet, "Venus". Use index `0` to get the first.

```python
planets = ["Mercury", "Venus", "Earth"]
first_planet = planets[0]
print(first_planet)   # Mercury
```

<sub>[Exercise](find-the-bug.md#exercise-754--first-planet-in-the-list) · [Runnable file](code/find_the_bug/ex_07_05_04_first_planet_in_the_list.py)</sub>

### Solution 7.5.5 — Day in the schedule

**Bug type:** Logical

`not in` returns `False` when the day is present, the reverse of what we want. Use the `in` operator to confirm membership.

```python
schedule = ["Monday", "Wednesday", "Friday"]
has_wednesday = "Wednesday" in schedule
print(has_wednesday)   # True
```

<sub>[Exercise](find-the-bug.md#exercise-755--day-in-the-schedule) · [Runnable file](code/find_the_bug/ex_07_05_05_day_in_the_schedule.py)</sub>
