'''
Calculate the average of a list of numbers using a function in Python.
'''

print("Enter first number in integer:")
num1 = int(input())  # taking the first number as input from the user
print("Enter second number:")   
num2 = int(input())  # taking the second number as input from the user
print("Enter third number:")
num3 = int(input())  # taking the third number as input from the user


def calculate_average(num1, num2, num3):  # defining a function to calculate the average
    total = num1 + num2 + num3
    average = total / 3
    return average

result = calculate_average(num1, num2, num3)  # calling the function with the three numbers
print(f"The average of the three numbers is: {result}")


# Example of default parameter values in a function
def Salary(Basic, Bonus=5000):  # defining a function with default parameter values
    total_salary = Basic + Bonus
    return total_salary


Emp1 = Salary(10000); # Here we have passed only one parameter, so the default value of Bonus will be used

print(f"Total salary of employee 1 is: {Emp1}")  # printing the total salary of employee 1

Emp2 = Salary(15000, 7000);  # calling the function with both parameters
print(f"Total salary of employee 2 is: {Emp2}")  # printing the total salary of employee 2