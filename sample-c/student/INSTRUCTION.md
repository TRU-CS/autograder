# Banking System Assignment Instructions

## Overview
In this assignment, you will implement a menu-driven C program that supports:

- Balance inquiry
- Deposits
- Withdrawals (with insufficient-funds handling)
- Compound interest calculation using recursion

## What You Need to Implement
Complete the TODO sections in `banking_system.c` for the following functions:

1. `displayBalance(double balance)`
2. `deposit(double *balance, double amount)`
3. `withdraw(double *balance, double amount)`
4. `calculateCompoundInterest(double principal, double rate, int years, int compounds)`

## Rules and Constraints
- Do **not** rename any function.
- Do **not** change function signatures.
- Keep the expected structure compatible with the autograder.
- Your code must compile with the provided `makefile`.

## Compound Interest Reference
Use the standard compound interest behavior, where:

- `P` = principal
- `r` = annual interest rate (decimal form)
- `n` = number of compounds per year
- `t` = number of years

## Project Files
| File | Purpose |
|---|---|
| `banking_system.c` | Student implementation file |
| `makefile` | Build rules for the executable and shared library |

## Run Locally
### 1. Compile
```bash
make
```

### 2. Run the Program
```bash
./banking_system.out
```

### 3. Clean Build Artifacts (Optional)
```bash
make clean
```

## How Grading Works
The autograder checks for:

- Successful compilation
- Correct deposit behavior
- Correct withdrawal behavior
- Proper insufficient-funds handling
- Correct compound interest calculation

## Submission
Submit **only**:

- `banking_system.c`
- `makefile`
