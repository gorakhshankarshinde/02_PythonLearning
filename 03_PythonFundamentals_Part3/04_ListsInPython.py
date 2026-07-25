'''
Lists in Python
How to create a list in python. see below example

Syntax:
list_name = [item1, item2, item3]

Example:
my_list = [1, 2, 3, 4, 5]
'''

numbersList = [1, 2, 3, 4, 5]

print("first element of numbersList: ", numbersList[0]) # output: 1
#print("last element of numbersList: ", numbersList[6]) # output: IndexError: list index out of range
print("numbersList: ", numbersList) # output: [1, 2, 3, 4, 5]
print("Length of numbersList: ", len(numbersList)) # output: 5

for number in numbersList:
   print("number: ", number)


# update list elements, as list are mutable

numbersList[0] = 10 # update the first element value from 1 to 10
print("Updated numbersList: ", numbersList) # output: [10, 2, 3, 4, 5]





