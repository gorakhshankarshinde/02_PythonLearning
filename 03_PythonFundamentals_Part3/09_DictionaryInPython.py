'''
we are going to learn about dictionary in python.

1. dictonaries are mutable.
2. unique keys are used to store values in the dictionary.
3. dublicate keys are not allowed in the dictionary.
4. values can be of any data type, including lists and other dictionaries.
5. dictionaries are defined using curly braces {} instead of square brackets [].

Syntax:
dictionary_name = {key1: value1, key2: value2, key3: value3}

Example:
my_dict = {"name": "John", "age": 30, "city": "New York"}

'''

my_Dictonary = {"name": "John", "age": 30, "city": "New York"}

print("my_Dictonary: ", my_Dictonary) # output: {'name': 'John', 'age': 30, 'city': 'New York'}
# get the value of a key in the dictionary, see below example

print("Name: ", my_Dictonary["name"]) # output: Name:  John
print("Age: ", my_Dictonary["age"]) # output: Age:  30
print("City: ", my_Dictonary["city"]) # output: City:  New York

my_Dictonary2 = {"name": "John", "age": 30, "city": "New York", "age": 40, "subjects": ["Maths", "Science"]} # duplicate keys are not allowed in the dictionary, so the last value will be used

print("my_Dictonary2: ", my_Dictonary2) # output: {'name': 'John', 'age': 40, 'city': 'New York', 'subjects': ['Maths', 'Science']} 

print("Subjects: ", my_Dictonary2["subjects"]) # output: Subjects:  ['Maths', 'Science']
