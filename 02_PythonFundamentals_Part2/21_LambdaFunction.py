'''
Lambda functions are small anonymous functions in Python that can have any number of arguments 
but only one expression. They are defined using the lambda keyword 
and are often used for short, simple functions that can be defined in a single line of code.
The syntax for a lambda function is as follows:
lambda arguments: expression
example:
square = lambda x: x ** 2
print(square(5))  # Output: 25
'''



sum = lambda a,b: a + b  # This is a lambda function that takes two arguments a and b and returns their sum
print(sum(3, 4))  # Output: 7

avg = lambda a,b: (a + b) / 2  # This is a lambda function that takes two arguments a and b and returns their average
print(avg(10, 20))  # Output: 15.0  

