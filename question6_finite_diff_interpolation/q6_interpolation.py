"""

5. Using Newton's Forward Interpolation Formula, estimate the value of f(2.5).
6. Using Newton's Backward Interpolation Formula, estimate the value of f(3.7).
7. Compare the interpolated values with the exact values (if available)
   and compute the interpolation error.

Data given in the question:
X : 0  1  2  3  4
Y : 1  3  7  13 21
"""

from q6_difference_tables import forward_difference_table, backward_difference_table


def newton_forward_interpolation(x, y, value):
    """
    Estimate f(value) using Newton's Forward Interpolation Formula.
    Uses the FIRST value of each order from the forward difference table.
    """
    table = forward_difference_table(y)
    h = x[1] - x[0]
    p = (value - x[0]) / h

    result = table[0][0]
    p_term = 1
    fact = 1
    for i in range(1, len(table)):
        p_term *= (p - (i - 1))
        fact *= i
        result += (p_term / fact) * table[i][0]

    return result


def newton_backward_interpolation(x, y, value):
    """
    Estimate f(value) using Newton's Backward Interpolation Formula.
    Uses the LAST value of each order from the backward difference table.
    """
    table = backward_difference_table(y)
    h = x[1] - x[0]
    p = (value - x[-1]) / h

    result = table[0][-1]
    p_term = 1
    fact = 1
    for i in range(1, len(table)):
        p_term *= (p + (i - 1))
        fact *= i
        result += (p_term / fact) * table[i][-1]

    return result


def compute_error(interpolated_value, exact_value):
    """
    Compute the interpolation error between the interpolated value
    and the exact value (if known).
    Returns absolute error and percentage error.
    """
    absolute_error = abs(exact_value - interpolated_value)
    percentage_error = (absolute_error / abs(exact_value)) * 100 if exact_value != 0 else None
    return absolute_error, percentage_error


def main():
    x = [0, 1, 2, 3, 4]
    y = [1, 3, 7, 13, 21]

    # Part 5: Newton's Forward Interpolation at f(2.5)
    forward_result = newton_forward_interpolation(x, y, 2.5)
    print(f"Estimated f(2.5) using Newton's Forward Interpolation = {forward_result}")

    # Part 6: Newton's Backward Interpolation at f(3.7)
    backward_result = newton_backward_interpolation(x, y, 3.7)
    print(f"Estimated f(3.7) using Newton's Backward Interpolation = {backward_result}")

    # Part 7: Compare with exact values
    # The difference table shows the data follows y = x^2 + x + 1 (degree 2 polynomial)
    exact_2_5 = 2.5**2 + 2.5 + 1
    exact_3_7 = 3.7**2 + 3.7 + 1

    abs_err_fwd, pct_err_fwd = compute_error(forward_result, exact_2_5)
    abs_err_bwd, pct_err_bwd = compute_error(backward_result, exact_3_7)

    print(f"\nExact f(2.5) = {exact_2_5}")
    print(f"Absolute Error = {abs_err_fwd}, Percentage Error = {pct_err_fwd:.4f}%")

    print(f"\nExact f(3.7) = {exact_3_7}")
    print(f"Absolute Error = {abs_err_bwd}, Percentage Error = {pct_err_bwd:.4f}%")


if __name__ == "__main__":
    main()
