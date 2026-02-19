# Banking System Assignment Instructions

## Introduction and Purpose
This assignment is a simplified banking application written in C. It simulates common account operations such as checking balances, depositing funds, withdrawing funds, and projecting growth with compound interest.

The purpose of this exercise is to practice core C programming skills:
- Writing and calling functions with clear contracts
- Using pointers for pass-by-reference updates
- Applying conditional logic for business rules (for example, insufficient funds)
- Implementing recursive logic for financial calculations

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

### Important Rate Convention
- `calculateCompoundInterest(...)` expects `rate` in **decimal form** (for example, `0.05` for 5%).
- If you build an interactive `main()` that asks users for a percent (for example, `5`), convert it to decimal before calling the function (for example, `rate /= 100`).

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

The grading scope assumes valid assignment inputs for the required operations. Handling invalid edge cases (for example, non-positive compounding frequency) is not part of the rubric unless explicitly announced by the instructor.

## Submission
Submit **only**:

- `banking_system.c`
- `makefile`
