# Everyday Programming — Problems and Solutions

Every problem and solution from *Everyday Programming* by Dr. Nobel Khandaker, laid out chapter by chapter as Markdown you can read and Python you can run.

**622 problems in total:**

| Set | Count | What it is |
|---|---:|---|
| Find the Bug | 445 | A short program with exactly one bug in it. Find the bug, then read the solution: it names the bug type, explains the misbehaviour, and shows the corrected program. |
| Applied problems | 170 | A real-world situation from physics, chemistry, mathematics, biology, engineering, geology, or geography, with a worked Python solution and its output. |
| Worked examples | 7 | Chapter 2's pseudocode, paired with the Python it turns into. |

Nothing here needs more mathematics than 10th grade: arithmetic, powers, square roots, and a little trigonometry.

## Contents

| Chapter | Find the Bug | Other | Links |
|---|---:|---:|---|
| **I. Foundations** | | | |
| 1. Mathematical Concepts | — | — | *no problem set* |
| 2. [Problem Solving](chapters/02-problem-solving) | — | 7 | [worked examples](chapters/02-problem-solving/worked-examples.md) |
| **II. Getting Started** | | | |
| 3. Computers | — | — | *no problem set* |
| 4. Language Fundamentals | — | — | *no problem set* |
| 5. Tools | — | — | *no problem set* |
| **III. Data** | | | |
| 6. [Data Structures](chapters/06-data-structures) | 50 | 20 | [find the bug](chapters/06-data-structures/find-the-bug.md) · [solutions](chapters/06-data-structures/solutions.md) · [applied](chapters/06-data-structures/applied-problems.md) |
| 7. [Lists](chapters/07-lists) | 10 | — | [find the bug](chapters/07-lists/find-the-bug.md) · [solutions](chapters/07-lists/solutions.md) |
| 8. [Operators](chapters/08-operators) | 25 | — | [find the bug](chapters/08-operators/find-the-bug.md) · [solutions](chapters/08-operators/solutions.md) |
| 9. [Input and Output](chapters/09-input-and-output) | 5 | — | [find the bug](chapters/09-input-and-output/find-the-bug.md) · [solutions](chapters/09-input-and-output/solutions.md) |
| **IV. Control Flow** | | | |
| 10. [Control Flow](chapters/10-control-flow) | 55 | 40 | [find the bug](chapters/10-control-flow/find-the-bug.md) · [solutions](chapters/10-control-flow/solutions.md) · [applied](chapters/10-control-flow/applied-problems.md) |
| 11. [Functions](chapters/11-functions) | 60 | 40 | [find the bug](chapters/11-functions/find-the-bug.md) · [solutions](chapters/11-functions/solutions.md) · [applied](chapters/11-functions/applied-problems.md) |
| 12. [Scoping](chapters/12-scoping) | 30 | — | [find the bug](chapters/12-scoping/find-the-bug.md) · [solutions](chapters/12-scoping/solutions.md) |
| **V. Building Programs** | | | |
| 13. [A Python Program](chapters/13-a-python-program) | — | 70 | [applied](chapters/13-a-python-program/applied-problems.md) |
| 14. [Objects](chapters/14-objects) | 15 | — | [find the bug](chapters/14-objects/find-the-bug.md) · [solutions](chapters/14-objects/solutions.md) |
| 15. [Modules](chapters/15-modules) | 10 | — | [find the bug](chapters/15-modules/find-the-bug.md) · [solutions](chapters/15-modules/solutions.md) |
| 16. Packages | — | — | *no problem set* |
| **VI. Quality** | | | |
| 17. [Handling Failures](chapters/17-handling-failures) | 20 | — | [find the bug](chapters/17-handling-failures/find-the-bug.md) · [solutions](chapters/17-handling-failures/solutions.md) |
| 18. [Testing](chapters/18-testing) | 15 | — | [find the bug](chapters/18-testing/find-the-bug.md) · [solutions](chapters/18-testing/solutions.md) |
| 19. [Bugs](chapters/19-bugs) | 20 | — | [find the bug](chapters/19-bugs/find-the-bug.md) · [solutions](chapters/19-bugs/solutions.md) |
| **VII. Reference** | | | |
| 20. [Common Pitfalls](chapters/20-common-pitfalls) | 130 | — | [find the bug](chapters/20-common-pitfalls/find-the-bug.md) · [solutions](chapters/20-common-pitfalls/solutions.md) |
| 21. Find the Bug: Solutions | — | — | *pointer chapter in the book* |

## How the sets map onto the book

* **Find the Bug** exercises are distributed through the book itself; each one lives here in the chapter that hosts it, numbered `chapter.section.exercise` exactly as the book numbers it. Section *s* of chapter *n* drills the topic of section *s* of that chapter — exercise 9.7.2 is about `break`, because §9.7 is the section on `break`.
* **Applied problems 1–100** are grouped in the book by the feature they teach, so they are filed here under the chapter that introduces that feature: variables with [Data Structures](chapters/05-data-structures), conditionals and loops with [Control Flow](chapters/09-control-flow), functions and recursion with [Functions](chapters/10-functions).
* **The 70 advanced problems** each combine variables, functions, loops, and conditionals into one program, which is what [A Python Program](chapters/12-a-python-program) is about. Half of them are written imperatively and half in a purely functional style, so neighbouring problems can be compared.

## The three kinds of bug

Every Find-the-Bug solution names one of these, following chapter 18:

| Bug type | What happens | Example |
|---|---|---|
| **Syntax** | The program will not even start; Python cannot parse it. | A missing `:` after `if`. |
| **Runtime** | The program starts, then raises and stops. | Adding an `int` to a `str`. |
| **Logical** | The program runs happily and prints the wrong answer. | `+` where `*` was meant. |

The third kind is the dangerous one, and most of the exercises here are of that kind.

## Running the code

Every solution is also a standalone file with a docstring that restates the problem. Python 3 is the only requirement.

```sh
python3 chapters/09-control-flow/code/find_the_bug/ex_09_07_02_first_over_budget.py
python3 chapters/12-a-python-program/code/applied/adv061_haversine_distance_between_cities.py
```

A few programs cannot run unattended and say so: those that call `input()`, the pytest exercises in [chapter 17](chapters/17-testing), and the four exercises in [chapter 13](chapters/13-modules) that import a companion module you write yourself.

## Checking the material

```sh
python3 tools/verify.py
```

`tools/verify.py` re-reads the Markdown and checks it, rather than trusting it:

1. every Python file parses;
2. every corrected program runs, or fails only for a declared reason;
3. every exercise really is broken in the way its solution claims — a syntax bug must stop the program parsing, a runtime bug must raise, and a logical bug must run but print something other than the corrected program prints;
4. pytest exercises fail before the fix and pass after it (pytest is used when installed, and a small built-in runner otherwise);
5. every applied problem prints the output this repository claims it prints.

A handful of exercises hide a bug that stdout cannot reveal — a leaked file handle, an over-broad `except`, a random number. Those are listed in `STRUCTURAL_CHECKS` in the script and are checked by comparing the two programs' structure instead.

## Editorial notes

[NOTES.md](NOTES.md) records the handful of places where the book's own annotation and the program's real behaviour differ (two exercises print a longer float than their comment claims), and lists the programs that need something from you before they can run — a typed value, a companion module, or pytest.

## Licence

Apache License 2.0 — see [LICENSE](LICENSE).
