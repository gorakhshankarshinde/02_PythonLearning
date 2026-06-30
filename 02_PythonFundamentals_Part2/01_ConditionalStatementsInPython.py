print("Please enter your age:")

age = int(input())

if age < 18:
    print("You are a minor.")
else:
    print("You are not a minor.")   


# elif How to use elif in Python

print("Please enter color:")
color = input()

if(color == "red"):
    print("stop")
elif(color == "green"):
    print("go")
elif(color == "yellow"):
    print("look")
else:
    print("invalid color")