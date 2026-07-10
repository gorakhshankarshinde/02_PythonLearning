'''
print multiplication table of a number using a while loop in Python. The while loop will continue to execute as long as the condition is true. In this case, we will start with a variable initialized to 1 and increment it until it reaches 10, printing the product of the number and the current value of the variable in each iteration.
'''

print("Please enter a number to print its multiplication table:")

num = int(input())  # taking input from the user and converting it to an integer

i = 1  # initializing the value of i to 1
while(i<=10):
    print(f"{num} x {i} = {num*i}")  # printing the multiplication table of the number
    i = i+ 1  # incrementing the value of i by 1 in each iteration

    