'''
Write a conditional statement that checks username and password. If the username is "admin" and the password is "pass123", print "Access granted". Otherwise, print "Access denied".
'''

print("Please enter your username:")
username = input()

print("Please enter your password:")
password = input()

if username == "admin" and password == "pass123":
    print("Access granted")
else:
    print("Access denied")