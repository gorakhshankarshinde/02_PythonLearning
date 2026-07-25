'''
We are going to learn dictionary methods in Python.
1. dict.keys() return a view object that displays a list of all the keys in the dictionary.
2. dict.values() return a view object that displays a list of all the values in the dictionary.
3. dict.items() return a view object that displays a list of a dictionary's key-value tuple pairs.
4. dict.get() return the value of the specified key.
5. dict.update() update the dictionary with the specified key-value pairs.
6. dict.pop() remove the specified key and return the corresponding value.

'''

# dict.keys() return a view object that displays a list of all the keys in the dictionary.
my_Dictonary = {"name": "John", "age": 30, "city": "New York"}
dic_keys = list(my_Dictonary.keys())

print("dictionary keys: ", dic_keys)
print("dictionary keys: ", dic_keys[0])

dic_values = list(my_Dictonary.values())

print("Dictionary values", dic_values)
print("Dictionary single value", dic_values[0])

# get dictionary key values pairs using dictionary.items() method.

dic_items = my_Dictonary.items()

print("Dictionary items: ", dic_items)

# use dictionary.get() method, to retrieve value of that key
val1 = my_Dictonary.get("name")
print("Value of name:", val1)

# dictionary.update() method
my_Dictonary.update({"Pin": "19150"})
print("New list items", my_Dictonary)




