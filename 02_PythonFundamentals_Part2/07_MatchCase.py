'''
Match Case Statement, we will take color input from user and print the message based on the color.
'''

print("Please enter color:")
color = input()

match color:
    case "red": 
        print("stop")
    case "green":
        print("go")
    case "yellow":  
        print("look")
    case _: # this is the default case, if none of the above cases match, this case will be executed
        print("invalid color")
