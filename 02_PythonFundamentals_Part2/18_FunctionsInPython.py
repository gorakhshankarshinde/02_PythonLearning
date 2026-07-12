'''
Basically functions are the block of statements that perform a specific task. 
Functions help break our program into smaller and modular chunks. 
As our program grows larger and larger, functions make it more organized and manageable.
Furthermore, it avoids repetition and makes the code reusable.
'''

def HelloWorld():  # defining a function named HelloWorld
    print("Hello, World!")  # printing "Hello, World!" when the function is called  



HelloWorld()  # calling the HelloWorld function to execute its code

def sum(a, b):
    s = a + b
    return s


ans = sum(5,6)  # calling the sum function with arguments 5 and 6, and returning the result
print(ans)  # printing the result