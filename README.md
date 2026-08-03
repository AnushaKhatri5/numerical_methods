<<<<<<< HEAD

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


=======
# Numerical Methods Project

Python implementation of:
- **Question 2:** Propagation of Errors
- **Question 6:** Finite Differences and Newton's Interpolation

## Team & Task Division

| File | Task | Assigned To |
|---|---|---|
| `question2_error_propagation/q2_error_propagation.py` | Q2 (full) | Ukti |
| `question6_finite_diff_interpolation/q6_difference_tables.py` | Q6 parts 1-4 | Ushma |
| `question6_finite_diff_interpolation/q6_interpolation.py` | Q6 parts 5-7 | Anusha |
| `question6_finite_diff_interpolation/main.py` | Combines Q6 parts 1-7 into one run | (run together once both files are done) |

## How to Work on This

1. **Clone the repo (first time only):**
   ```bash
   git clone <repo-url>
   cd numerical-methods-project
   ```

2. **Before you start working, always pull the latest changes:**
   ```bash
   git pull origin main
   ```

3. **Go to your assigned file and fill in the `TODO` sections.**
   - Ukti → `question2_error_propagation/q2_error_propagation.py`
   - Ushma → `question6_finite_diff_interpolation/q6_difference_tables.py`
   - Anusha → `question6_finite_diff_interpolation/q6_interpolation.py`
     (needs Ushma's `q6_difference_tables.py` to be done first, since it imports from it)

4. **Run your file to test it:**
   ```bash
   python question2_error_propagation/q2_error_propagation.py
   # or
   python question6_finite_diff_interpolation/q6_difference_tables.py
   # or
   python question6_finite_diff_interpolation/q6_interpolation.py
   ```

5. **For Question 6, once BOTH `q6_difference_tables.py` (Ushma) and
   `q6_interpolation.py` (Anusha) are complete**, run `main.py` instead —
   it imports and runs both files together, giving one single terminal
   output covering all of parts 1-7:
   ```bash
   cd question6_finite_diff_interpolation
   python main.py
   ```

6. **Take a screenshot of the terminal output** once it's working correctly —
   you'll paste this into the report under "Results and Discussion".

6. **Push your work:**
   ```bash
   git add .
   git commit -m "Completed Q6 difference tables"
   git push origin main
   ```

## Notes
- Only edit your own assigned file to avoid merge conflicts.
- Anusha should pull Ushma's finished `q6_difference_tables.py` before starting,
  since her file imports functions from it.
- Report (Word doc with screenshots) goes in the `report/` folder.
>>>>>>> acd05b9c4def321b3d23a7cf61f610cc7e02aa07
