'''
Product store

Design & create online store for Products(name, price)
Track total products being created.
Create a static method to calculate discount on each product based on % parameter passed to it.

'''

class Product: 

    count = 0 # class variable to track total products

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count = Product.count + 1 # incrementing the count of products as it is inside a counstructor and once object get created, it will increment the count of products.

    def get_product_info(self):  # this is our instance method to get the product info
        print(f"Price of the product {self.name} is rupees: Rs.{self.price}")

    @classmethod
    def get_Count(cls): # class method to get the total count of products
        print(f"Total products created: {cls.count}")

    @staticmethod
    def calculate_discount(price, discount_percentage): # static method to calculate discount on each product based on % parameter passed to it.
        discount_amount = (price * discount_percentage) / 100
        discounted_price = price - discount_amount
        return discounted_price
    

product1 = Product("Laptop", 1000)
product2 = Product("Mobile", 500)
product3 = Product("Tablet", 300)

product1.get_product_info()
product2.get_product_info()
product3.get_product_info()

Product.get_Count() # calling the class method to get the total count of products

# Using the static method to calculate discount
discounted_price1 = Product.calculate_discount(product1.price, 10) # 10% discount on product1
discounted_price2 = Product.calculate_discount(product2.price, 20) # 20%
#discount on product2
print(f"Discounted price of {product1.name} is: Rs.{discounted_price1}")
print(f"Discounted price of {product2.name} is: Rs.{discounted_price2}")

    






