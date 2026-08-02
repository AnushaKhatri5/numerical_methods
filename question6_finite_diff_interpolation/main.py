"""
Question 6: Finite Differences and Newton's Interpolation
Combined Runner File

This file merges:
- q6_difference_tables.py   (Parts 1-4)
- q6_interpolation.py       (Parts 5-7)

Running this file executes the ENTIRE Question 6 (parts 1-7) in one go,
producing one continuous terminal output for the report.

"""

import pandas as pd

from q6_difference_tables import (
    X,
    Y,
    forward_difference_table,
    backward_difference_table,
    central_difference_table,
    print_forward_table,
    print_backward_table,
    print_central_table,
    determine_polynomial_degree,
)

from q6_interpolation import (
    newton_forward_interpolation,
    newton_backward_interpolation,
    compute_error,
)


def main():
    x = X
    y = Y

    print("Given Data:")
    df = pd.DataFrame({"X": x, "Y": y})
    print(df.to_string(index=False))

    print("\n" + "=" * 60)
    print("PARTS 1-3: DIFFERENCE TABLES")
    print("=" * 60)

    fwd_table = forward_difference_table(y)
    print_forward_table(x, fwd_table)

    bwd_table = backward_difference_table(y)
    print_backward_table(x, bwd_table)

    cen_table = central_difference_table(y)
    print_central_table(x, cen_table)

    print("\n" + "=" * 60)
    print("PART 4: POLYNOMIAL DEGREE CHECK")
    print("=" * 60)

    degree = determine_polynomial_degree(fwd_table)
    if degree is not None:
        print(f"The given data represents a polynomial of degree {degree}.")
    else:
        print("The given data does not represent a polynomial.")

    print("\n" + "=" * 60)
    print("PART 5: NEWTON'S FORWARD INTERPOLATION - f(2.5)")
    print("=" * 60)

    forward_result = newton_forward_interpolation(x, y, 2.5)
    print(f"Estimated f(2.5) = {forward_result}")

    print("\n" + "=" * 60)
    print("PART 6: NEWTON'S BACKWARD INTERPOLATION - f(3.7)")
    print("=" * 60)

    backward_result = newton_backward_interpolation(x, y, 3.7)
    print(f"Estimated f(3.7) = {backward_result}")

    print("\n" + "=" * 60)
    print("PART 7: COMPARISON WITH EXACT VALUES")
    print("=" * 60)

    exact_2_5 = 2.5**2 + 2.5 + 1
    exact_3_7 = 3.7**2 + 3.7 + 1

    abs_err_fwd, pct_err_fwd = compute_error(forward_result, exact_2_5)
    abs_err_bwd, pct_err_bwd = compute_error(backward_result, exact_3_7)

    print(f"Exact f(2.5) = {exact_2_5}")
    print(f"Absolute Error = {abs_err_fwd}, Percentage Error = {pct_err_fwd:.4f}%")

    print(f"\nExact f(3.7) = {exact_3_7}")
    print(f"Absolute Error = {abs_err_bwd}, Percentage Error = {pct_err_bwd:.4f}%")


if __name__ == "__main__":
    main()
