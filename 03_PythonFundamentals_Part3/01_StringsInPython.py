'''
1. Generally we create strings in double quotes or single quotes.
2. We can use triple quotes for multi-line strings.
3. Strings are immutable in Python.
4. We can access individual characters in a string using indexing.
5. We can slice strings to get a substring.
6. Strings have various built-in methods for manipulation.
'''

# first we will print the length of the string using len() function

my_string = "Hello, World!"
print("Length of the string:", len(my_string))

# output: Length of the string: 13

#now we will concatenate two strings using the + operator

first_string = "I love"
second_string = "Python"

concatenated_string = first_string + " " + second_string
print("Concatenated string:", concatenated_string)  

# output: Concatenated string: I love Python

#indexing and slicing 

My_string = "Python Programming" # Note: here string index starts from 0 like in most programming languages.

print("Character at index 0:", My_string[0])  # output: P
print("Character at index 6:", My_string[6])  # output: P
print("Substring from index 0 to 6:", My_string[0:7])  # output: Python
print("Substring from index 7 to 18:", My_string[7:17])  # output: Programming

# Now let's use for loop to iterate through the string and print each character
# basically string are sequences, so we can use for loop for iteration

sample_string = "Python"
for char in sample_string:
    print(char)


# below example shows that strings are immutable in python, which means we cannot change the value of a string once it is created.
# my_string[0] = "p"  # This will raise an error 
