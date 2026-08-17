'''
There are two types of attributes

1. Class attributes and 
2. Instance attributes

'''

#Example 1: 

class Student:
    collegeName = "ABC College" # this will become a class attribute because it is not using self

    def __init__(self, studentName, marks):
        self.studentName = studentName # here studentName is instance attribute
        self.marks = marks # here marks is also instance attribute as we are using it with self



# so when we want to call collegeName then we can access it using class name or object name 

stud = Student("Gorakh", "50")

print("Calling college name using class name: ",Student.collegeName)
print("Calling college name using object name: ",stud.collegeName)




