'''
print the sum of first n natural numbers using for loop and range function in Python.
'''

n = int(input("Enter a positive integer: "))  # taking input from the user for the value of n
sum_of_natural_numbers = 0  # initializing a variable to store the sum

for i in range(1, n + 1):  # using range to generate numbers from 1 to n
    sum_of_natural_numbers += i  # adding the current number to the sum

print(f"The sum of the first {n} natural numbers is: {sum_of_natural_numbers}")
    