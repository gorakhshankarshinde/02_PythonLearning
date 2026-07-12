'''
Calculate the factorial of n numbers using a function in Python.
'''

print("Enter a positive integer:")  # prompting the user to enter a positive integer
n = int(input())  # taking input from the user for the value of n
factorial = 1  # initializing a variable to store the factorial

for i in range(1, n + 1):  # using range to generate numbers from 1 to n
   factorial = factorial * i  # calculating the factorial by multiplying the current value of factorial with i


print(f"The factorial of {n} is: {factorial}")  # printing the calculated factorial