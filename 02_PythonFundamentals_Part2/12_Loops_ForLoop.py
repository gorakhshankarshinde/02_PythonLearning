'''
for loop we are using for sequential traversal 
of a sequence (like a list, tuple, string, etc.) 
or other iterable objects. 
 '''

string = "Hello, World!"  # initializing a string variable

# in below for loop, "in" is called membership operator which checks if the value is present in the sequence or not.
for var in string:  # iterating over each character in the string
    print(var)  # printing the current character    


if "o" in string:  # checking if the character "o" is present in the string
    print("The character 'o' is present in the string.")  # printing a message if "o" is found