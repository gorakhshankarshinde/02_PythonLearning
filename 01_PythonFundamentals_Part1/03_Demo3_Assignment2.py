'''
Q2. Take two numbers as input from the user and
 print their sum, difference, product, and quotient.
'''
print("Enter the first number:")
num1 = float(input())
print("Enter the second number:")
num2 = float(input())

print(f"Sum: {num1 + num2}") # Or you can use print("Sum:", num1 + num2)
print(f"Difference: {num1 - num2}") # Or you can use print("Difference:", num1 - num2)
print(f"Product: {num1 * num2}")
print(f"Quotient: {num1 / num2 if num2 != 0 else 'Undefined (division by zero)'}")