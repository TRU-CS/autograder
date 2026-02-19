# sample-py-script: Gradescope Python Autograder Template

This folder is a minimal Python-script autograder template for Gradescope.

## What This Template Contains
### Student-facing files
- `student/lab1.py`: starter file students download and submit.
- `student/INSTRUCTIONS.md`: student-facing assignment instructions.

### Instructor files
- `solution/lab1.py`: instructor reference solution.
- `test/test.py`: autograder tests (uses `gradescope-utils` decorators like `@weight` and `@number`).

### Autograder runtime files
- `requirements.txt`: Python dependencies installed in Gradescope.
- `setup.sh`: installs Python + dependencies in the Gradescope container.
- `run_autograder`: Gradescope entrypoint script.
- `run_tests.py`: discovers tests and writes Gradescope JSON results.

### Build artifact
- `autograder.zip`: upload artifact for Gradescope.

## How Grading Works (High Level)
1. Gradescope unzips `autograder.zip` into `/autograder/source`.
2. `setup.sh` installs dependencies.
3. `run_autograder` copies student submission files from `/autograder/submission` to `/autograder/source`.
4. `run_tests.py` runs `unittest` tests in `test/`.
5. Results are written to `/autograder/results/results.json`.

## Step-by-Step: Insert a New Question

### 1) Add the new function to the student template
1. Open `student/lab1.py`.
2. Add a new function stub with `pass`.
3. Do not rename existing functions used by tests.

Example:
```python
def reverse_words():
    """Print words in reverse order."""
    pass
```

### 2) Add the same function to the instructor solution
1. Open `solution/lab1.py`.
2. Implement the new function with the expected correct output/behavior.

### 3) Add the question to student instructions
1. Open `student/INSTRUCTIONS.md`.
2. Add a new section with:
- question description
- exact expected output (if output-based)
- any constraints (formatting, naming, etc.)

### 4) Update function list constraints (if present)
1. In `student/INSTRUCTIONS.md`, update any list of required function names.
2. Make sure the new function name exactly matches the test import.

## Step-by-Step: Update the Test

### 1) Import the new function in tests
1. Open `test/test.py`.
2. Add the function to the import block from `lab1`.

Example:
```python
from lab1 import (
    ...,
    reverse_words,
)
```

### 2) Add a test case method
1. Add a new `test_...` method inside `TestPatterns` (or a new test class).
2. Add `@weight(...)` and `@number("...")` decorators.
3. Call the function and assert exact expected behavior.

Example:
```python
@weight(5)
@number("1.8")
def test_reverse_words(self):
    reverse_words()
    output_lines = self.held_output.getvalue().split('\n')
    expected_output = ["world hello"]
    output_lines = [line.strip() for line in output_lines]
    for line, expected in zip(output_lines, expected_output):
        self.assertEqual(line, expected)
```

### 3) Keep total points intentional
1. Rebalance `@weight` values as needed.
2. Ensure test numbers are unique and ordered.

### 4) Validate tests locally (quick check)
Run both checks from the `sample-py-script` folder.

Check A: Validate the instructor solution (should pass).
```bash
cd sample-py-script
cp solution/lab1.py lab1.py
python3 -m unittest test/test.py
rm lab1.py
```

Check B: Validate the student starter template (usually fails until implemented).
```bash
cd sample-py-script
cp student/lab1.py lab1.py
python3 -m unittest test/test.py
rm lab1.py
```

## Step-by-Step: Generate `autograder.zip` for Gradescope

From the `sample-py-script` folder:
```bash
cd sample-py-script
rm -f autograder.zip
zip -r autograder.zip \
  run_autograder setup.sh run_tests.py requirements.txt test \
  -x "__MACOSX/*" "*.DS_Store"
```

Notes:
- Include only autograder runtime files (`run_autograder`, `setup.sh`, `run_tests.py`, `requirements.txt`, `test/`).
- Do not include `student/` or `solution/` in the uploaded autograder zip.

## Step-by-Step: Upload to Gradescope
1. Open your Gradescope assignment.
2. Go to **Configure Autograder**.
3. Upload `autograder.zip` from your local `sample-py-script` folder.
4. Save and run a test submission using `student/lab1.py`.
5. Confirm each test appears with the expected score and output.

## Common Pitfalls
- Renaming `lab1.py` or tested function names.
- Updating instructions but forgetting to update tests.
- Forgetting to regenerate `autograder.zip` after test changes.
