'''
We are going to learn about string formatting in python.
string formatting is a technique to create a new string by inserting values into a string template.
'''

# we can use the format() method to format strings in python.

a = 10
b = 20

sum = a + b
formatted_string = "The sum of {} and {} is {}".format(a, b, sum)

print(formatted_string)  # output: The sum of 10 and 20 is 30

print("Language is {}".format("Python"))  # output: Language is Python  

#index based formatting, 
print("The sum is {0}  of  {1} and  {2}".format(sum, a, b))  # output: The sum of 10 and 20 is 30

#value based formatting.
print("Value of a={a} & b={b}".format(a = 11, b=22))
# output: Value of a=11 & b=22

print("a={a}, a={a},  Value of a={a} & b={b}".format(a = 11, b=22))
#output: a=11, a=11,  Value of a=11 & b=22

#f-string formatting. This is most important and most used formatting in python. It is available from python 3.6 and above.
x = 10
y = 20

print(f"The sum of {x} and {y} is {x + y}")  # output: The sum of 10 and 20 is 30





