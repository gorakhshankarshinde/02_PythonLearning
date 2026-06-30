'''
Write a program to swap values of two 
numbers entered by the user
'''

print("Enter the first number:")
num1 = float(input())
print("Enter the second number:")
num2 = float(input())

print(f"Before swapping: num1 = {num1}, num2 = {num2}")

# Swapping the values
temp = num1
num1 = num2
num2 = temp

print(f"After swapping: num1 = {num1}, num2 = {num2}")
