'''
we are going to learn about the range function in python. 
The range function is used to generate a sequence of numbers.
 It can take one, two, or three arguments.

 below syntax is used to generate range(start, stop, step) 
 where start is the starting number of the sequence (inclusive),
 stop is the end number of the sequence (exclusive),
 and step is the difference between each number in the sequence. 
 If only one argument is provided, it is treated as the stop value, 
 and the start value defaults to 0. The step value defaults to 1 if not provided.
'''

for num in range(5):  # using range to generate numbers from 0 to 4
    print(num)  # printing the current value of num


for num in range(1, 6):  # using range to generate numbers from 1 to 5
    print(num)  # printing the current value of num

for num in range(1, 11, 2):  # using range to generate odd numbers from 1 to 10
    print(num)  # printing the current value of num 

    