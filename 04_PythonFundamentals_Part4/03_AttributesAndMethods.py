'''
Attributes and methods in python

Inside class we store two things 1. properties and 2. methods (behaviour)
'''

# Example 1: Methods in python, below first we are going to learn constructor in python.
# In below student class __init__(self) is the syntax of creating constructor in python.

class Student:
     def __init__(self):  # this method is nothing but the constructor method. This constructor also called as default constructor
            print("Constructor was called")

stud = Student() # Constructor gets invoke when object gets created.


# Example 2:

class Employee:
      def __init__(self, firstName):  # this is parameterized constructor
            self.firstName = firstName


emp = Employee("Gorakh")
emp2= Employee("Aish")

print(emp.firstName)
print(emp2.firstName)




