'''
We are going to learn about encapsulation in Python. 
Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). 
It refers to the bundling of data (attributes) and methods (functions) that operate on that data into a single unit, typically a class.

OOPs concepts are based on four pillars:
1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction

1. Encapsulation: In encapsulation we are wrapping data and functions into a single unit called class. 
It is used to restrict access to certain attributes and methods of an object, 
which can help prevent unintended interference and misuse of the data. 
In Python, encapsulation is achieved using access specifiers (public, protected, and private) to control the visibility of class members.

'''
class Bank:

    def __init__(self, name,accountNumber, balance):
        self.name = name  # private attribute
        self._balance = balance  # protected attribute because it is prefixed with a single underscore
        self.__accountNumber = accountNumber  # private attribute because it is prefixed with double underscores

    def get_AccountNumber(self):
        return self.__accountNumber


account1 = Bank("John Doe", 1155, 5000)

print("Account Holder:", account1.name)
print("Account Number:", account1.get_AccountNumber())
print("Account Balance:", account1._balance)





