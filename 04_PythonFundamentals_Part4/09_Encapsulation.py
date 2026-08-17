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

    def __init__(self, name,accountNumber, balance, FD_Balance):
        self.name = name  # private attribute
        self._balance = balance  # protected attribute because it is prefixed with a single underscore
        self.__accountNumber = accountNumber  # private attribute because it is prefixed with double underscores
        self.__FD_Balance = FD_Balance # this is private attribute we have used.

    def get_AccountNumber(self): # This is getter function, nothing but just we named it as prefix with "get"
        return self.__accountNumber

    def set_Balance(self, newBalance): # here we have created setter function, which is setting the value to the private variable.
        self.__FD_Balance = newBalance
        return self.__FD_Balance

        


account1 = Bank("John Doe", 1155, 5000, 100000)

print("Account Holder:", account1.name)
print("Account Number:", account1.get_AccountNumber())
print("Account Balance:", account1._balance)


# Important we can access private variable outside like shown below.
print(f"Current FD amount is Rs.{account1._Bank__FD_Balance}")



print(f"New FD balance amount is Rs. {account1.set_Balance(200000)}")










