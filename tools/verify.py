#!/usr/bin/env python3
"""Check every problem and solution in this repository.

What is checked
---------------
1. Every ``.py`` file under ``chapters/`` parses.
2. Every corrected Find-the-Bug program runs to completion, or fails only for
   a declared reason (it waits for keyboard input, it is a pytest module, or
   it imports a companion module written elsewhere in the same chapter).
3. Every Find-the-Bug exercise really is broken, in the way its solution
   claims:

   * a **syntax** bug must stop the buggy program from parsing;
   * a **runtime** bug must make it raise;
   * a **logical** bug must let it run but produce different output from the
     corrected program.

   A handful of exercises hide a bug that stdout cannot show — a leaked file
   handle, an over-broad ``except``, a random number. Those are listed in
   ``STRUCTURAL_CHECKS`` below and are verified by inspecting the two programs
   instead of by comparing their output.
4. pytest exercises are run as tests: the buggy module must fail and the
   corrected module must pass. If pytest is not installed, modules that do not
   themselves import pytest are still run by a small built-in test runner.
5. Every applied problem runs, and its output contains the output the
   Markdown promises.

Usage
-----
    python3 tools/verify.py [--quiet]

Exit status is 0 when every check passes.
"""
import argparse
import ast
import importlib.util
import itertools
import pathlib
import re
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHAPTERS = ROOT / "chapters"
TIMEOUT = 30

HAVE_PYTEST = importlib.util.find_spec("pytest") is not None

# Programs that cannot run to completion unattended, and why.
INCOMPLETE_REASONS = {
    "needs-input": "reads from input(); run it yourself and type a value",
    "needs-pytest": "uses the pytest module; install pytest to run it",
    "needs-module": "imports a companion module written in the same chapter",
}

# Exercises whose bug does not change what the program prints. Each entry gives
# the reason plus a pattern that must appear in the buggy program and one that
# must appear in the corrected program, so the fix is still verified.
STRUCTURAL_CHECKS = {
    "13.1.3": ("the roll is random, so both programs usually print 1-6",
               r"randint\(1, 7\)", r"randint\(1, 6\)"),
    "20.18.1": ("the bug is a file handle that is never closed",
                r"= open\(", r"with open\("),
    "20.18.2": ("the bug is a file handle that is never closed",
                r"= open\(", r"with open\("),
    "20.18.3": ("the bug is a file handle that is never closed",
                r"= open\(", r"with open\("),
    "20.18.4": ("the bug is a file handle that is never closed",
                r"= open\(", r"with open\("),
    "20.18.5": ("the bug is a file handle that is never closed",
                r"= open\(", r"with open\("),
    "20.19.1": ("the bug is a bare except that hides unrelated errors",
                r"except\s*:", r"except \w+Error"),
    "20.19.2": ("the bug is a bare except that hides unrelated errors",
                r"except\s*:", r"except \w+Error"),
    "20.19.3": ("the bug is a bare except that hides unrelated errors",
                r"except\s*:", r"except \w+Error"),
    "20.19.4": ("the bug is a bare except that hides unrelated errors",
                r"except\s*:", r"except \w+Error"),
    "20.19.5": ("the bug is a bare except that hides unrelated errors",
                r"except\s*:", r"except \w+Error"),
    # A test that returns a value is reported by pytest as a warning (an error
    # in recent versions), which a plain test runner cannot see.
    "17.2.3": ("the bug is a test function that returns a value instead of "
               "relying on its assert",
               r"return True", r"assert discounted_price\(50, 20\) == 40\n?$"),
}

CODE_BLOCK = re.compile(r"```python\n(.*?)\n```", re.S)
FENCED_OUTPUT = re.compile(r"\*\*Output[^:]*:\*\*\s*```\n(.*?)\n```", re.S)
INLINE_OUTPUT = re.compile(r"\*\*Output[^:]*:\*\*\s*`([^`]*)`")

# A small runner used when pytest is unavailable: define the module, then call
# every test_* function it declares.
FALLBACK_PYTEST = """
import pathlib, sys, traceback
ns = {"__name__": "_module"}
exec(compile(pathlib.Path(%r).read_text(), "_module.py", "exec"), ns)
tests = [v for k, v in sorted(ns.items())
         if k.startswith("test_") and callable(v)]
if not tests:
    sys.exit("no test functions found")
failed = 0
for t in tests:
    try:
        t()
    except Exception:
        failed += 1
        traceback.print_exc()
print("%%d passed, %%d failed" %% (len(tests) - failed, failed))
sys.exit(1 if failed else 0)
"""


def run(source, cwd, args=(), stdin=""):
    """Run `source` as a script. Return (returncode, stdout, stderr)."""
    path = pathlib.Path(cwd) / "_program.py"
    path.write_text(source)
    try:
        p = subprocess.run([sys.executable, *args, str(path)], cwd=cwd,
                           input=stdin, capture_output=True, text=True,
                           timeout=TIMEOUT)
        return p.returncode, p.stdout, p.stderr
    except subprocess.TimeoutExpired:
        return -1, "", "TIMEOUT after %ds" % TIMEOUT


_test_run = itertools.count()


def run_tests(source, cwd):
    """Run a pytest-style module. Return (returncode, stdout, stderr).

    Each call gets a fresh file name. pytest caches its rewritten bytecode by
    (path, size, mtime), and a buggy program and its fix often differ only in a
    digit — same size, same second — so reusing one name would silently rerun
    the previous module.
    """
    n = next(_test_run)
    if HAVE_PYTEST:
        path = pathlib.Path(cwd) / ("test_program_%d.py" % n)
        path.write_text(source)
        p = subprocess.run([sys.executable, "-m", "pytest", "-q", "-p",
                            "no:cacheprovider", str(path)],
                           cwd=cwd, capture_output=True, text=True, timeout=TIMEOUT)
        return p.returncode, p.stdout, p.stderr
    path = pathlib.Path(cwd) / ("_module_%d.py" % n)
    path.write_text(source)
    runner = pathlib.Path(cwd) / ("_runner_%d.py" % n)
    runner.write_text(FALLBACK_PYTEST % str(path))
    p = subprocess.run([sys.executable, str(runner)], cwd=cwd,
                       capture_output=True, text=True, timeout=TIMEOUT)
    return p.returncode, p.stdout, p.stderr


def is_test_module(source):
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return False
    return any(isinstance(n, ast.FunctionDef) and n.name.startswith("test_")
               for n in tree.body)


def imports_pytest(source):
    return re.search(r"^\s*import pytest|^\s*from pytest\b", source, re.M) is not None


def classify_failure(stderr):
    if "EOFError" in stderr:
        return "needs-input"
    if "ModuleNotFoundError" in stderr and "pytest" in stderr:
        return "needs-pytest"
    if "ModuleNotFoundError" in stderr:
        return "needs-module"
    return None


def normalise(text):
    return re.sub(r"\s+", " ", text).strip()


def parse_exercises(chapter_dir):
    problems = (chapter_dir / "find-the-bug.md").read_text()
    solutions = (chapter_dir / "solutions.md").read_text()

    buggy = {}
    for m in re.finditer(r"^### Exercise ([\d.]+) — (.*?)\n(.*?)(?=^### |\Z)",
                         problems, re.S | re.M):
        buggy[m.group(1)] = {"title": m.group(2).strip(),
                             "code": CODE_BLOCK.search(m.group(3)).group(1)}

    fixed = {}
    for m in re.finditer(r"^### Solution ([\d.]+) — (.*?)\n(.*?)(?=^### |\Z)",
                         solutions, re.S | re.M):
        body = m.group(3)
        fixed[m.group(1)] = {
            "title": m.group(2).strip(),
            "code": CODE_BLOCK.search(body).group(1),
            "bug_type": re.search(r"\*\*Bug type:\*\* (.+)", body).group(1).strip(),
        }
    return buggy, fixed


def parse_applied(chapter_dir):
    path = chapter_dir / "applied-problems.md"
    if not path.exists():
        return {}
    text = path.read_text()
    out = {}
    for m in re.finditer(r"^### (?:Advanced problem|Problem) (\d+) — "
                         r"(.*?)\n(.*?)(?=^### |\Z)", text, re.S | re.M):
        body = m.group(3)
        fence = FENCED_OUTPUT.search(body)
        inline = INLINE_OUTPUT.search(body)
        out[int(m.group(1))] = {
            "title": m.group(2).strip(),
            "code": CODE_BLOCK.search(body).group(1),
            "expected": fence.group(1) if fence else (inline.group(1) if inline else None),
        }
    return out


def check_exercise(tag, eid, buggy, fixed, tmp, failures, notes):
    b, f = buggy, fixed
    if b["code"] == f["code"]:
        failures.append("%s %s: buggy and fixed code are identical" % (tag, eid))
        return
    try:
        ast.parse(f["code"])
    except SyntaxError as exc:
        failures.append("%s %s: corrected code does not parse: %s" % (tag, eid, exc))
        return

    kind = f["bug_type"].lower()
    try:
        ast.parse(b["code"])
        buggy_parses = True
    except SyntaxError:
        buggy_parses = False

    if "syntax" in kind and buggy_parses:
        failures.append("%s %s: declared a syntax bug but the buggy program parses"
                        % (tag, eid))
    if "syntax" not in kind and not buggy_parses:
        failures.append("%s %s: declared a %s bug but the buggy program does not parse"
                        % (tag, eid, kind))

    if eid in STRUCTURAL_CHECKS:
        reason, buggy_pat, fixed_pat = STRUCTURAL_CHECKS[eid]
        if not re.search(buggy_pat, b["code"], re.M):
            failures.append("%s %s: buggy program does not match %r" % (tag, eid, buggy_pat))
        if not re.search(fixed_pat, f["code"], re.M):
            failures.append("%s %s: corrected program does not match %r" % (tag, eid, fixed_pat))
        notes.append("%s %s: output-compare skipped — %s" % (tag, eid, reason))
        return

    # pytest-style exercises: the buggy module must fail, the fixed must pass.
    if is_test_module(f["code"]):
        if imports_pytest(f["code"]) and not HAVE_PYTEST:
            notes.append("%s %s: %s (needs-pytest)" % (tag, eid, INCOMPLETE_REASONS["needs-pytest"]))
            return
        frc, fout, ferr = run_tests(f["code"], tmp)
        if frc != 0:
            failures.append("%s %s: corrected test module does not pass: %s"
                            % (tag, eid, (ferr or fout).strip()[-200:]))
        if buggy_parses:
            brc, _, _ = run_tests(b["code"], tmp)
            if brc == 0:
                failures.append("%s %s: buggy test module passes; the exercise "
                                "has no bug" % (tag, eid))
        return

    frc, fout, ferr = run(f["code"], tmp)
    if frc != 0:
        reason = classify_failure(ferr)
        if reason is None:
            failures.append("%s %s: corrected program fails: %s"
                            % (tag, eid, ferr.strip().splitlines()[-1]))
        else:
            notes.append("%s %s: %s (%s)" % (tag, eid, INCOMPLETE_REASONS[reason], reason))
        return

    if not buggy_parses:
        return  # a syntax bug: there is nothing to run and compare.

    brc, bout, berr = run(b["code"], tmp)
    if "runtime" in kind and brc == 0:
        failures.append("%s %s: declared a runtime bug but the buggy program "
                        "does not raise" % (tag, eid))

    if brc == 0 and bout == fout:
        failures.append("%s %s: buggy program already prints the correct output"
                        % (tag, eid))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quiet", action="store_true",
                    help="do not list the programs that cannot run unattended")
    args = ap.parse_args()

    failures, notes = [], []
    counts = {"exercises": 0, "applied": 0, "files": 0, "worked": 0}

    with tempfile.TemporaryDirectory() as tmp:
        for chapter_dir in sorted(CHAPTERS.iterdir()):
            if not chapter_dir.is_dir():
                continue
            tag = chapter_dir.name

            for py in sorted(chapter_dir.rglob("*.py")):
                counts["files"] += 1
                try:
                    ast.parse(py.read_text())
                except SyntaxError as exc:
                    failures.append("%s: %s does not parse: %s" % (tag, py.name, exc))

            if (chapter_dir / "find-the-bug.md").exists():
                buggy, fixed = parse_exercises(chapter_dir)
                if set(buggy) != set(fixed):
                    failures.append("%s: exercise/solution ids differ: %s"
                                    % (tag, sorted(set(buggy) ^ set(fixed))))
                for eid in sorted(buggy, key=lambda s: [int(x) for x in s.split(".")]):
                    counts["exercises"] += 1
                    check_exercise(tag, eid, buggy[eid], fixed[eid], tmp, failures, notes)

            # Chapter 2 pairs pseudocode with Python; run the programs that do
            # not stop for keyboard input.
            for py in sorted((chapter_dir / "code").glob("we_*.py")):
                counts["worked"] += 1
                rc, out, err = run(py.read_text(), tmp)
                if rc != 0:
                    reason = classify_failure(err)
                    if reason is None:
                        failures.append("%s: %s fails: %s"
                                        % (tag, py.name, err.strip().splitlines()[-1]))
                    else:
                        notes.append("%s: %s %s (%s)"
                                     % (tag, py.name, INCOMPLETE_REASONS[reason], reason))

            for num, rec in sorted(parse_applied(chapter_dir).items()):
                counts["applied"] += 1
                rc, out, err = run(rec["code"], tmp)
                if rc != 0:
                    reason = classify_failure(err)
                    if reason is None:
                        failures.append("%s problem %d (%s): fails: %s"
                                        % (tag, num, rec["title"],
                                           err.strip().splitlines()[-1]))
                    else:
                        notes.append("%s problem %d: %s (%s)"
                                     % (tag, num, INCOMPLETE_REASONS[reason], reason))
                    continue
                if rec["expected"] is None:
                    failures.append("%s problem %d (%s): no expected output recorded"
                                    % (tag, num, rec["title"]))
                elif normalise(rec["expected"]) not in normalise(out):
                    failures.append("%s problem %d (%s): expected %r, printed %r"
                                    % (tag, num, rec["title"],
                                       normalise(rec["expected"])[:120],
                                       normalise(out)[:160]))

    print("pytest: %s" % ("installed" if HAVE_PYTEST else
                          "not installed (using the built-in fallback runner)"))
    print("checked %d Python files, %d Find-the-Bug exercises, %d applied "
          "problems, %d worked examples"
          % (counts["files"], counts["exercises"], counts["applied"],
             counts["worked"]))
    if notes and not args.quiet:
        print("\n%d note(s):" % len(notes))
        for n in notes:
            print("  -", n)
    if failures:
        print("\n%d PROBLEM(S):" % len(failures))
        for f in failures:
            print("  *", f)
        return 1
    print("\nAll checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
