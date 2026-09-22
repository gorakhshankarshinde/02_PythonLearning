'''
Inheritance: Reusing attributes & methods from a Parent(Base) class.
'''

class Employee:
    start_Time = "10am" # this is public attribute
    end_Time = "6pm" # this is public attribute

    def change_time(self, new_end_time):
        self.end_Time = new_end_time
        


class Teacher(Employee): # here in parenthesis we have added parent class, here we are inheriting it.
    def __init__(self,subject):
        self.subject = subject


t1 = Teacher("Math")
t1.change_time("8pm")

print(f"Subject name: {t1.subject} \nStart time: {t1.start_Time} \nEnd time: {t1.end_Time}")


'''
Note:
1. If the parent class attribute is private then it won't accessible in child class.
2. If the parent class attribute is protected then it will be accessible in child class.
'''