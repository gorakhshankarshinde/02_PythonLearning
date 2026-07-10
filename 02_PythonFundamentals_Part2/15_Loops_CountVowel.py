'''
Count the number of vowels in the string "Artificial Intelligence" using for loop and if statement in Python.
'''

count = 0  # initializing a counter variable to count occurrences of vowels

for char in "Artificial Intelligence":  # iterating over each character in the string
    if char.lower() in "aeiou":  # checking if the current character is a vowel (case-insensitive)
        print(char)  # printing the vowel if found
        count += 1  # incrementing the counter if a vowel is found

print(f"The number of vowels in the string 'Artificial Intelligence' is {count}.")  # printing the total count of vowels in the string