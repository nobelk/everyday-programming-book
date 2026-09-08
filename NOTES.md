# Editorial notes

The problems and solutions in this repository are reproduced from *Everyday
Programming* without changing the programs. Everything here has been run and
checked (see [`tools/verify.py`](tools/verify.py)); this page records the few
places where the book's own text and the program's real behaviour do not quite
line up, so that a reader who notices the discrepancy knows it is not a
transcription error.

## Floating-point output written as exact decimals

Two exercises use `pi = 3.14159` and a radius of 3, and annotate the expected
output as `28.27431`. What Python actually prints is
`28.274309999999996` — `3.14159 * 3 * 3` is not exactly representable in binary
floating point.

| Exercise | Comment in the program | What it really prints |
|---|---|---|
| [11.1.3](chapters/11-scoping/find-the-bug.md#exercise-1113--a-global-constant-for-area) | `# expected: Area: 28.27431` | `Area: 28.274309999999996` |
| [20.4.3](chapters/20-common-pitfalls/find-the-bug.md#exercise-2043--using-a-result-before-computing-it) | `# 28.27431` | `28.274309999999996` |

Neither affects the bug being taught — both exercises are about *where* a name
is defined, not about the arithmetic. The prose in 11.1.3 says "about 28.27",
which is right. This is the same effect that
[§20.23](chapters/20-common-pitfalls/find-the-bug.md#2023-expecting-floating-point-math-to-be-exact)
makes a pitfall in its own right: use `round(...)` or a formatted string when
the printed digits matter.

## Exercise 11.3.2 — a prompt that gives the answer away

[Exercise 11.3.2](chapters/11-scoping/find-the-bug.md#exercise-1132--read-before-assign)
("read before assign") states in its prompt that "the read at the top should
fail", which is the diagnosis rather than the symptom. Its solution also changes
the function's signature — `advance()` becomes `advance(step)` — rather than
fixing the body in place. Both are the book's, and the underlying lesson is
sound: assigning to a name anywhere in a function makes that name local for the
whole function, so reading it before the assignment raises `UnboundLocalError`.

## Programs that cannot run unattended

These are not errata; they are simply programs that need something from you.
`tools/verify.py` recognises each case and reports it rather than failing.

| Where | Why |
|---|---|
| Chapter 8 (8.1.1, 8.1.2, 8.1.5); chapter 16 (all of §16.1, plus 16.2.3, 16.2.5, 16.3.2–16.3.5, 16.4.2, 16.4.3, 16.4.5); chapter 20 (all of §20.7) | They call `input()`. Run them from a terminal and type a value. |
| Chapter 13 (13.2.1, 13.2.2, 13.2.4, 13.2.5) | They import a companion module (`conversions`, `geometry`, `shapes`) that the chapter asks you to write yourself. |
| Chapter 17 (17.3.2, 17.3.4, 17.3.5) | They use `pytest.approx` and `pytest.mark.parametrize`, so they need pytest installed. |
| Chapter 2 (examples 1 and 2) | They call `input()`. |

## Exercise 17.2.3 and pytest versions

[Exercise 17.2.3](chapters/17-testing/find-the-bug.md#exercise-1723--discount-test)
turns on a test function that ends with `return True` instead of relying on its
`assert`. pytest reports a returning test — older versions as a warning, recent
ones as an error — but a plain `python3` run of the file cannot see it at all,
and neither can the small fallback runner in `tools/verify.py`. That exercise is
therefore checked structurally rather than by running it.

## Where the applied problems' expected output comes from

* The **100 applied problems** carry the output printed in the book, and
  `tools/verify.py` checks every one of them against what the program actually
  prints.
* The **70 advanced problems** are given in the book without expected output.
  The `**Output:**` block shown for each one here is what the program prints on
  CPython 3, captured when this repository was generated. A few of them are
  deliberate teaching simplifications rather than research-grade models — the
  simplified Köppen climate classes and the flat-earth great-circle distance,
  for instance — and the book presents them as such.
