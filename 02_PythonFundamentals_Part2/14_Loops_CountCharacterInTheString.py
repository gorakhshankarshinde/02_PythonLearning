'''
Count the i in the string "Artificial Intelligence" using for loop and if statement in Python.
'''

count = 0  # initializing a counter variable to count occurrences of "i"

for char in "Artificial Intelligence":  # iterating over each character in the string
    if char == "i":  # checking if the current character is "i"
        print(char)  # printing the character "i" if found
        count += 1  # incrementing the counter if "i" is found

print(f"The character 'i' is present {count} times in the string 'Artificial Intelligence'.")  # printing the total count of "i" in the string



