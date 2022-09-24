def say_hello(name="User"):  # default value
    """
    Prints hello and then name.
    """
    print("hello", name)


# return value
def get_sum(num1, num2):
    total = num1 + num2
    return total

# add one to num


def addd_one_to_num(num):
    num += 1
    return num


say_hello("Divine")
print(get_sum(4, 5))

"""
A lambda function is a small anonymous function . A lambda function can only take a number of arguments but can only have one expression. Very similar to JavaScript arrow functions
"""


def get_sum(num1, num2): return num1 + num2
def add_one_to_num(num): return num + 1


print(get_sum(9, 2))
print(add_one_to_num(19, 22))
