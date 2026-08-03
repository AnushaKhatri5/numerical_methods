# Question 2: Propagation of Errors Using Python
"""
Write a Python program that accepts two measured quantities x and y,
along with their maximum absolute errors dx and dy. The program should compute:
1. The sum x + y and its maximum absolute error.
2. The product xy and its approximate absolute error.
3. The quotient x/y and its approximate absolute error.
4. The upper limit for the absolute error using the general error formula.

"""

x = float(input("Enter x: "))
dx = float(input("Enter Δx (max absolute error of x): "))
y = float(input("Enter y: "))
dy = float(input("Enter Δy (max absolute error of y): "))
print("\n      Results      ")

# 1. Sum
sum_result= x+y
sum_error= dx+dy
print(f"1. Sum:      x+y = {sum_result} ± {sum_error}")

# 2. Product
prod_result= x*y
prod_error= abs(y)*dx+abs(x)*dy
print(f"2. Product:  x*y = {prod_result} ± {prod_error}")
# 3. Quotient
if y!=0:
    quot_result= x/y
    quot_error= (abs(y)*dx+abs(x)*dy)/(y**2)
    print(f"3. Quotient: x/y = {quot_result} ± {quot_error}")
else:
    print("3. Quotient: undefined (y=0)")

# 4. Upper limit using the general error formula
print("\n4. Upper limit of absolute error (general formula):")
print(f"  Sum:      |1|*Δx+|1|*Δy         = {dx+dy}")
print(f"  Product:  |y|*Δx+|x|*Δy         = {abs(y)*dx+abs(x)*dy}")
if y != 0:
    print(f"  Quotient: |1/y|*Δx + |x/y^2|*Δy = {abs(1/y)*dx+abs(x/y**2)*dy}")