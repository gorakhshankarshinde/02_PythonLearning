'''
We are going to learn how to loop through lists in Python.
'''

numbersList = [1, 2, 3, 4, 5]

for value in numbersList:
    print("value: ", value) # output: 1, 2, 3, 4, 5


# find the value in the list using for loop, see below example

searchValue = 3
i = 0
for value in numbersList:
    if value == searchValue:
        print(f"Found the value {searchValue} at index {i}: ") # output: Found the value 3 at index 2
        break # here we are using break statement to exit the loop once we found the value in the list
    i = i + 1



