'''
In python string slicing is a technique to extract a portion of a string by specifying the start and end indices. 
The syntax for slicing is as follows:
string[start:end:step]
'''

My_string = "Python Programming"

# Slicing from index 0 to 6 (not including 6)
print("Substring from index 0 to 6:", My_string[0:6])
# output: Substring from index 0 to 6: Python

print("Substring from index 7 to 18:", My_string[7:18]) # here suppse we don't mention the end index, it will take the rest of the string from the start index to the end of the string.

#output: Substring from index 7 to 18: Programming

# one more example of slicing, where we will use length of the string to slice the string from the end.
print("Substring from index 0 to -1:", My_string[7:len(My_string)]) 
# output: Substring from index 0 to -1: Programming 