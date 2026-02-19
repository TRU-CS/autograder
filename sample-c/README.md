# Sample C Autograder Template

## Purpose
This folder is a reference implementation of a Gradescope-style autograder setup for C programming assignments.

It includes:
- A **student starter** version of the question
- An **instructor solution** version
- Python **tests** that grade compiled C functions
- Runtime scripts used by the Gradescope autograder container

## Folder Structure
| Path | What it is for |
|---|---|
| `student/` | Starter files distributed to students |
| `solution/` | Instructor reference implementation |
| `tests/test_banking.py` | Unit tests (Python + `ctypes`) run against compiled student code |
| `run_autograder` | Main entrypoint Gradescope executes |
| `run_tests.py` | Runs tests and writes Gradescope JSON results |
| `setup.sh` | Installs system and Python dependencies inside autograder container |
| `requirements.txt` | Python dependencies for test runner |
| `autograder.zip` | Packaged autograder artifact (for upload) |

## How the Autograder Works
1. Gradescope runs `setup.sh` to install dependencies.
2. Gradescope runs `run_autograder`.
3. `run_autograder` copies student submission files into `/autograder/source/`.
4. `make` compiles:
   - `banking_system.out` (executable)
   - `banking.so` (shared library for Python tests)
5. `run_tests.py` discovers tests in `tests/` and writes JSON to `/autograder/results/results.json`.
6. Gradescope displays test results and score.

## Creating a New C Question (Step-by-Step)
Use these steps when creating another C assignment using this template.

### 1. Copy this template to a new folder
Create a new sibling folder (example: `sample-c-arrays`) and copy:
- `student/`
- `solution/`
- `tests/`
- `run_autograder`
- `run_tests.py`
- `setup.sh`
- `requirements.txt`

### 2. Define the new problem API first
Decide function names and signatures students must implement.

Guidelines:
- Keep signatures stable across `student/`, `solution/`, and tests.
- Prefer simple C types and pointer parameters when you need pass-by-reference behavior.
- Avoid changing function names later; tests depend on exact symbol names.

### 3. Build the student starter files
Update `student/banking_system.c` (or rename to your new question file) to include:
- Required includes
- Function prototypes
- TODO stubs for each required function
- Any required `main()` scaffold (if relevant)

Update `student/INSTRUCTION.md` with:
- Problem statement
- Constraints
- Local run instructions
- What to submit

Update `student/makefile` so it builds both:
- Program executable
- Shared library (`.so`) for tests

### 4. Build the instructor solution
Implement the full, correct answer in `solution/banking_system.c` (or your renamed file).

Use this to:
- Validate expected behavior
- Sanity-check tests before release

### 5. Write/update tests
Edit `tests/test_banking.py` to match your new question:
- Load the correct shared library with `ctypes.CDLL("./<name>.so")`
- Set `argtypes` and `restype` for every tested function
- Add deterministic test cases with grading weights

Recommendations:
- Cover normal cases and edge cases
- Keep tests independent
- Include at least one failure-path test if applicable

### 6. Update autograder execution script
Edit `run_autograder` so it copies the correct submitted files from `/autograder/submission/` and compiles expected outputs.

Verify:
- Copied filenames match your assignment exactly
- Build command succeeds with the provided student starter `makefile`
- Compilation failures produce a clear results message

### 7. Verify locally before packaging
From this folder, do a dry run:

```bash
cd solution
make clean && make
cd ..
python3 -m unittest discover tests
```

Then verify the student starter currently fails or is incomplete as intended.

### 8. Package for Gradescope
Create/update `autograder.zip` so it contains the autograder root files and folders (not nested incorrectly).

Expected root layout inside zip:
- `run_autograder`
- `run_tests.py`
- `setup.sh`
- `requirements.txt`
- `tests/`
- `solution/` (optional for grading, useful for internal reference)

Upload zip to Gradescope and configure submission files to match the student instructions.

## Maintenance Tips
- Keep naming consistent across C source, Makefile targets, tests, and `run_autograder`.
- Keep test output deterministic (no random behavior unless seeded).
- If you rename source files, update all references in:
  - `student/makefile`
  - `solution/makefile`
  - `run_autograder`
  - `tests/*.py`
