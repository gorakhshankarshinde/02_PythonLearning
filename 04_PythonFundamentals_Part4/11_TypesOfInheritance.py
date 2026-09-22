'''
Types of Inheritance:
1. Single level inheritance.
   Example: suppose We have parent class => Employee and it is inherited by Teacher class, so this is called single level inheritance.

   class Employee:
         a = 10
         b = 20

   class Teacher(Employee):
        def __init__(self, a , b)
           self.a = a
           self.b = b


2. Multi-level inheritance

    Example: 
               class Employee:
                       a = 10
                       b = 20

                class AdminStaff(Employee):
                     def __init__(self, role):
                        self.role = role


                class Accountant(AdminStaff):   # so this class can access Employee and AdminStaff class attributes and methods.
                     def __init__(self, salary):
                        self.salary = salary
'''

# In below example it is shown the multi level inheritance

class Employee:
	start_time = "10am"
	end_time = "6pm"

class AdminStaff(Employee):
	def __init__(self, role):
		self.role = role

class Accountant(AdminStaff):
	def __init__(self,salary, role):
		super().__init__(role) # here we have called the parent class constructor method to assign values.
		self.salary = salary


acc1 = Accountant(20_500, "CA")
print(f"Salary {acc1.salary} and Role: {acc1.role}")


# Below example shows multiple inheritance

class Teacher:
   def __init__(self, salary):
      self.salary = salary

class Student:
   def __init__(self, gpa):
      self.gpa = gpa

class TeacherStudent(Teacher, Student):  # here Teacher and Student class are inherited by TeacherStudent class.
   def __init__(self, salary, gpa, name):
      super().__init__(salary)  # here we have called the parent class constructor method to assign values.
      Student.__init__(self, gpa)   
      self.name = name

ta1 = TeacherStudent(50_000, 3.5, "John Doe")
print(f"Salary: {ta1.salary}, GPA: {ta1.gpa}, Name: {ta1.name}")


