'''
write a program to identify if the age of the person is <13 then print "You are a child", if the age is between 13 and 19 then print "You are a teenager", if the age is between 20 and 59 then print "You are an adult" and if the age is 60 or above then print "You are a senior citizen".
'''

print("Please enter your age:")
age = int(input()) 

if age < 13:
    print("You are a child.")
elif age >= 13 and age <= 19:
    print("You are a teenager.")
elif age >= 20 and age <= 59:
    print("You are an adult.")
else:
    print("You are a senior citizen.")


    