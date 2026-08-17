'''
There are three types of methods in python
1. Instance methods
2. Class methods
3. Static methods
'''

class Laptop:
    # Instance method
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # Instance method
    def display_info(self): 
        return f"Laptop Brand: {self.brand}, Model: {self.model}"

    # Class method
    @classmethod # we are using class method decorator to define class method
    def from_string(cls, laptop_str):
        brand, model = laptop_str.split('-')
        return cls(brand, model)

    # Static method
    @staticmethod # we are using static method decorator to define static method
    def is_laptop(obj):
        return isinstance(obj, Laptop)



# Creating an instance of Laptop using the constructor
laptop1 = Laptop("Dell", "XPS 13")

# Creating an instance of Laptop using the class method
laptop_str = "HP-Envy"
laptop2 = Laptop.from_string(laptop_str)

# Using the instance method
print(laptop1.display_info())

# Using the static method
print(Laptop.is_laptop(laptop1))  # True
print(Laptop.is_laptop("Not a Laptop"))  # False


