'''
Write simple function which can return the CGPA values of the student
'''



class Student:
     def __init__(self, studentName, CGPA):  # this method is nothing but the constructor method.
            self.studentName = studentName
            self.CGPA = CGPA

     def Get_CGPA(self):
           return self.CGPA
      
      
      


stud = Student("Gorakh", "8.0") # Constructor gets invoke when object gets created.
stud2 = Student("Aish", "7.8")


print(stud.Get_CGPA())
print(stud2.Get_CGPA())


# There are two types of constructor in python, 1. Default constructor and 2. Parameterized constructor




