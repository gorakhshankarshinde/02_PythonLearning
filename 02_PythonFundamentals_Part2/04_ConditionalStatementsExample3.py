'''
if n is multiply of 3 and 5, then print "FizzBuzz"
if n is multiply of 3, then print "Fizz"
if n is multiply of 5, then print "Buzz" 
'''

print("We are going to check if the number is a multiple of 3 and 5, or just 3 or just 5.")
print("if the number is a multiple of 3 and 5, then print 'FizzBuzz'")
print("if the number is a multiple of 3, then print 'Fizz'")
print("if the number is a multiple of 5, then print 'Buzz'")

print("Please enter a number:")
n = int(input())    

if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")   
else:
    print("Not a multiple of 3 or 5")
