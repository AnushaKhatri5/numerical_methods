"""
Question 6: Finite Differences and Newton's Interpolation
1. Construct the forward difference table.
2. Construct the backward difference table.
3. Construct the central difference table.
4. Determine whether the given data represent a polynomial, and if yes, determine its degree using the difference table.

Data given in the question:
X : 0  1  2  3  4
Y : 1  3  7  13 21
"""
import pandas as pd

# Input Data
X= [0, 1, 2, 3, 4]
Y= [1, 3, 7, 13, 21]

n=len(Y)

#1.FORWARD DIFFERENCE TABLE 
# Builds the forward difference table
def forward_difference_table(y):
    table = [y[:]]     #First row contains original y values
    current = y[:]
    while len(current) > 1:
        # each new level has one fewer value than previous level
        current = [ round(current[i+1] - current[i],6) for i in range(len(current)-1)]
        table.append(current)
    return table

# Prints forward difference table
def print_forward_table(x, table):
    print("\n1. FORWARD DIFFERENCE TABLE")
    headers = ["x","y"]+ [f"Δ^{i}y" for i in range (1,len(table))]
    print("{:<6}".format(headers[0]),end="")
    for h in headers[1:]:
        print("{:>10}".format(h),end="")
    print()

    for i in range(n):
        print("{:<6}".format(x[i]),end="")
        for j in range(len(table)):
            if i<len(table[j]): # column j gets shorter each level
                print("{:>10}".format(table[j][i]),end="")
            else:
                print("{:>10}".format(""),end="")
        print()

#2.BACKWARD DIFFERENCE TABLE
# Builds backward difference table
def backward_difference_table(y):
    table = [y[:]]
    current = y[:]
    while len(current) > 1:
        #Starting from index 1 since there is no y[-1]
        current = [round(current[i] - current[i-1], 6) for i in range(1, len(current))]
        table.append(current)
    return table

# Prints the backward difference table
def print_backward_table(x, table):
    print("\n2. BACKWARD DIFFERENCE TABLE")
    headers = ["x", "y"] + [f"∇^{i}y" for i in range(1, len(table))]
    print("{:<6}".format(headers[0]), end="")
    for h in headers[1:]:
        print("{:>10}".format(h), end="")
    print()

    for i in range(n):
        print("{:<6}".format(x[i]), end="")
        for j in range(len(table)):
            # backward differences are aligned to the bottom of each column
            idx = i - j
            if 0 <= idx < len(table[j]):
                print("{:>10}".format(table[j][idx]), end="")
            else:
                print("{:>10}".format(""), end="")
        print()

#3.CENTRAL DIFFERENCE TABLE
# Builds raw central difference table
def central_difference_table(y):
    table = [y[:]]
    current = y[:]
    while len(current) > 1:
        current = [round(current[i+1] - current[i], 6) for i in range(len(current) - 1)]
        table.append(current)
    return table


# Prints the diamond shape central difference table using pandas
def print_central_table(x, table):
    print("\n3. CENTRAL DIFFERENCE TABLE")
    max_order = len(table) - 1        # highest order of difference 
    total_rows = 2 * (n - 1) + 1      # data rows plus spacer rows between them

    row_labels = []   # x values
    y_col = []         # y values

    for r in range(total_rows):
        if r % 2 == 0:             # even rows with actual data points
            i = r // 2
            row_labels.append(x[i])
            y_col.append(int(table[0][i]))
        else:                          # odd rows are spacer rows for odd order differences
            row_labels.append("")
            y_col.append("")

    cols = {"x": row_labels, "y": y_col}

    # place each order of difference at the row that centers it
    for k in range(1, max_order + 1):
        col = [""] * total_rows
        for j in range(len(table[k])):
            r = 2 * j + k       
            col[r] = table[k][j]
        cols[f"δ^{k}y"] = col

    df = pd.DataFrame(cols)

    #Print the table
    headers = list(df.columns)
    print("{:<6}".format(headers[0]), end="")
    for h in headers[1:]:
        print("{:>10}".format(h), end="")
    print()

    for _, row in df.iterrows():
        print("{:<6}".format(row["x"]), end="")
        for h in headers[1:]:
            print("{:>10}".format(row[h]), end="")
        print()

#4.DETERMINE POLYNOMIAL DEGREE
def determine_polynomial_degree(table, tol=1e-6):
    #Checking successive difference levels(Degree = order of constant difference level)
    for order in range(1, len(table)):
        level = table[order]
        if len(level) == 0:
            continue
        first_val = level[0]
        is_constant = all(abs(v - first_val) < tol for v in level)

        if is_constant and abs(first_val) > tol:
            # Checking if the next level is (numerically) zero, if it exists
            if order + 1 < len(table):
                next_level = table[order + 1]
                if all(abs(v) < tol for v in next_level):
                    return order
            else:
                return order
    return None

# MAIN PROGRAM
def main():
    print("Given Data:")
    df = pd.DataFrame({"X": X, "Y": Y})
    print(df.to_string(index=False))

    fwd_table = forward_difference_table(Y)
    print_forward_table(X, fwd_table)

    bwd_table = backward_difference_table(Y)
    print_backward_table(X, bwd_table)

    cen_table = central_difference_table(Y)
    print_central_table(X, cen_table)

    degree = determine_polynomial_degree(fwd_table)

    print("\n4. POLYNOMIAL CHECK ")
    if degree is not None:
        print(f"The data represents a polynomial of degree {degree}.")
    else:
        print("The data does not represent a polynomial "
              "(differences never become constant/zero).")


if __name__ == "__main__":
    main()