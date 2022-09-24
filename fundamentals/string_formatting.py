print("Hello, my name is {name} and i am {age} years old".format(
    name="Divine", age="14"))
name = "Divine"
age = "14"
print(f"my name is {name} and i am {age}")

s = "Hello there world"
print(s.capitalize())
print(s.upper())
print(s.swapcase())
print(len(s))
# age = int(input("How old are you? "))
print("You are", age, "years old")

print(s.replace("world", "divine"))

sub = "e"
print(s.count(sub))

print(s.split())
print(s.find("d"))
print(s.isalnum())
print(s.isalpha())
print(s.isnumeric())
print(s.startswith("hello"))
print(s.endswith("d"))
