'''
In below list there are list of items having student name and subject information.
inside list there is single list item is tuple type
We have to find below things.

'''

info = [
("Alice", "Math"),
("Bob", "Science"),
("Alice", "Science"),
("Charlie", "Science"),
("Charlie", "Math"),
("Bob", "Math"),
("Alice", "English"),
("Charlie", "English"),
]

# Question 1: List all unique courses
uniqueCourses = set() # here we assign empty set

for tup in info:
    #print(f"{tup[0]} - {tup[1]}") # we will get all name
    uniqueCourses.add(tup[1])


print(uniqueCourses) # here we are going to print set values and as we know set can store only unique values.

#above for loop we can write like below way
for name,course in info:
    print(name, course)

# Question 2: List students name enrolled in English

print("\nBelow list of student who enrolled in English:")
for name, course in info:
    
    if(course == "English"):
        print(name)



# Question 3: Create a dictionary contain (Student, set of courses)

dict = {} # initially we have created empty dictionary

for name, course in info:
    if(dict.get(name) == None):
            dict.update({name: set()}) # here we have created key and one empty set
            dict[name].add(course)
    else:
         dict[name].add(course)


print(dict)

        

