'''
We are going to learn some tuples methods in Python.
1. tuple.count() return the number of occurrences of an item.
2. tuple.index() return the index of the first occurrence of an item.
3. tuple slicing() return a new tuple that is a subset of the original tuple.
4. tuple concatenation() return a new tuple that is the concatenation of two or more tuples.
5. tuple repetition() return a new tuple that is the repetition of the original tuple.  
'''

myTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("myTuple: ", myTuple) # output: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10

# tuple.count() return the number of occurrences of an item.
myTuple = (1, 2, 3, 4, 5, 1, 5, 3, 4, 5)
count_of_5 = myTuple.count(5) # return the number of occurrences of 5
print("Count of 5 in myTuple: ", count_of_5) # output: 3

# tuple.index() return the index of the first occurrence of an item.
index_of_4 = myTuple.index(4) # return the index of the first occurrence of 4
print("Index of 4 in myTuple: ", index_of_4) # output: 3

# tuple slicing() return a new tuple that is a subset of the original tuple.
sliced_tuple = myTuple[2:5] # return a new tuple that is a subset of the original tuple
print("Sliced tuple from index 2 to 5: ", sliced_tuple) # output: (3, 4, 5)



