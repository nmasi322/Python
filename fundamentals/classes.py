# a class is like a blueprint for creating objects. an object has properties and methods(functions) associated with it. Almost everything in Python is an object.

# create a class
from copyreg import constructor


class User:
    # constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f"My name is {self.name} and i am {self.age} years old"

    def has_birthday(self):
        self.age += 1

# extending classes


class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f"My name is {self.name} and i am {self.age} years old and I owe a balance of {self.balance}"


# init user_object
divine = User("Divine", "edehdivine042@gmail.com",
              14)  # divine is a node/object now
# edit property
divine.age = 18
print(divine.age)

Janet = User("Janet williams", "janet@gmail.com", 27)
print(Janet.email)

# methods
print(Janet.greeting())

# editing values from methods
print(Janet.age)
Janet.has_birthday()
print(Janet.age)

# init customer
customer_1 = Customer("John Doe", "johndoe@gmail.com", 56)
print(customer_1.greeting())
customer_1.set_balance(900)
print(customer_1.greeting())
