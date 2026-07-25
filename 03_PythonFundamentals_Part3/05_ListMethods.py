'''
We are going to learn below list methods.

1. list.append() add one item to the end of the list.
2. list.extend() add multiple items to the end of the list.
3. list.insert() add an item at a specific index.
4. list.remove() remove the first occurrence of an item.
5. list.pop() remove and return the item at a specific index.
6. list.index() return the index of the first occurrence of an item.
7. list.count() return the number of occurrences of an item.
8. list.sort() sort the items in the list.
9. list.reverse() reverse the order of the items in the list.
10. list.clear() remove all items from the list.
'''

# list.append() add one item to the end of the list.
numbersList = [1, 2, 3, 4, 5]
numbersList.append(6)
print("After append(6), numbersList: ", numbersList) # output: [1, 2, 3, 4, 5, 6]

# list.extend() add multiple items to the end of the list.
numbersList.extend([7, 8, 9])
print("After extend([7, 8, 9]), numbersList: ", numbersList) # output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# list.insert() add an item at a specific index.
numbersList.insert(0, 0) # insert 0 at index 0
print("After insert(0, 0), numbersList: ", numbersList) # output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# list.remove() remove the first occurrence of an item.
numbersList.remove(5) # remove the first occurrence of 5
print("After remove(5), numbersList: ", numbersList) # output: [0, 1, 2, 3, 4, 6, 7, 8, 9]

# list.pop() remove and return the item at a specific index.
popped_item = numbersList.pop(2) # remove and return the item at index 2
print("After pop(2), popped_item: ", popped_item) # output: 2
print("After pop(2), numbersList: ", numbersList) # output: [0, 1, 3, 4, 6, 7, 8, 9]    

# list.index() return the index of the first occurrence of an item.
index_of_4 = numbersList.index(4) # return the index of the first occurrence of 4
print("Index of 4 in numbersList: ", index_of_4) # output: 3

# list.count() return the number of occurrences of an item.
numbersList.append(4) # add another 4 to the list   
count_of_4 = numbersList.count(4) # return the number of occurrences of 4
print("Count of 4 in numbersList: ", count_of_4) # output: 2

# list.sort() sort the items in the list.
numbersList.sort() # sort the items in the list
print("After sort(), numbersList: ", numbersList) # output: [0, 1, 3, 4, 4, 6, 7, 8, 9]

# list.reverse() reverse the order of the items in the list.
numbersList.reverse() # reverse the order of the items in the list  
print("After reverse(), numbersList: ", numbersList) # output: [9, 8, 7, 6, 4, 4, 3, 1, 0]

# list.clear() remove all items from the list.
numbersList.clear() # remove all items from the list
print("After clear(), numbersList: ", numbersList) # output: []
