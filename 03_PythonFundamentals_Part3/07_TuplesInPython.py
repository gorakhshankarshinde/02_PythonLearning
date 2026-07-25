'''
We are going to learn about the touples in Python.
Tuples are similar to lists, but they are immutable, meaning that once a tuple is created
, its elements cannot be changed, added, or removed. Tuples are defined using parentheses () 
instead of square brackets [].

syntax:
tuple_name = (item1, item2, item3)

Example:
myTuple = (1, 2, 3)

'''

myTuple = (1, 2, 3)

print("type of myTuple: ", type(myTuple)) # output: <class 'tuple'>
print("first element of myTuple: ", myTuple[0]) # output: 1
print("second element of myTuple: ", myTuple[1]) # output: 2
print("Touple length:", len(myTuple)) # output: 3

# iterating through a tuple using for loop
for value in myTuple:
    print("value: ", value) # output: 1, 2, 3

# we cannot create tuble using single value, see below example
singleValueTuple = (1) # this will create an integer, not a tuple
print("type of singleValueTuple: ", type(singleValueTuple)) # output: <class 'int'>

# to create a single value tuple, we need to add a comma after the value, see below example
singleValueTuple = (1,) # this will create a tuple with a single value  

#print the tuple first 5 elements, see below example
myTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print("first 5 elements of myTuple: ", myTuple[0:5]) # output: (1, 2, 3, 4, 5)
print("last 5 elements of myTuple: ", myTuple[5:10]) # output: (6, 7, 8, 9, 10)




