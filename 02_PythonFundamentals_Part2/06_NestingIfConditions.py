'''
Nesting If Conditions
'''
print("Please enter your username:")
username = input()

print("Please enter your password:")
password = input()

if(username == "admin"):
    if(password == "pass123"):   # here we are nesting the if condition inside another if condition
        print("Access granted")
    else:
        print("Access denied")