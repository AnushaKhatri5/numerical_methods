
# Numerical Methods in Python

A Python implementation of core numerical analysis techniques, including error propagation, finite difference methods, and Newton's interpolation formulas.

##  Overview

This project demonstrates practical applications of numerical methods commonly used in scientific computing and engineering analysis. It focuses on two key areas:

1. **Propagation of Errors** — Computing how measurement uncertainties propagate through arithmetic operations (addition, multiplication, division) and deriving the general error bound.
2. **Finite Differences & Newton's Interpolation** — Constructing forward, backward, and central difference tables, identifying polynomial behavior in tabulated data, and estimating unknown function values using Newton's Forward and Backward Interpolation formulas.

##  Project Structure

```
numerical-methods-project/
│
├── README.md
│
├── question2_error_propagation/
│   └── q2_error_propagation.py
│
├── question6_finite_diff_interpolation/
│   ├── q6_difference_tables.py
│   ├── q6_interpolation.py
│   └── main.py
│
└── report/
    └── (project report with results and screenshots)
```

## ⚙️ Features

- Computes the sum, product, and quotient of two measured quantities along with their propagated errors
- Derives the upper limit of absolute error using the general error formula
- Constructs forward, backward, and central difference tables for equally spaced data
- Determines whether tabulated data represents a polynomial and identifies its degree
- Estimates function values using Newton's Forward and Backward Interpolation formulas
- Compares interpolated results with exact values and computes interpolation error

##  How to Run

**Run Question 2 (Error Propagation):**
```bash
python question2_error_propagation/q2_error_propagation.py
```

**Run Question 6 (Finite Differences & Interpolation) — full combined output:**
```bash
cd question6_finite_diff_interpolation
python main.py


##  Requirements

- Python 3.x
- No external libraries required


