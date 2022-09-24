# Dictionary -> a collection that is unordered, indexed and changeable. no duplicate members allowed
# smple dict
person = {
    "firstName": "John",
    "lastName": "Doe",
    "age": 30
}
print(person)

# using a constructor
# person = dict(
#     firstName="John",
#     lastName="Doe",
#     age=30
# )

# access a single value
print(person["firstName"])
print(person.get("lastName"))

# add a key to dict
person["phone"] = "565-456-3667"

# get keys
print(person.keys())

# get values
print(person.items())

# make copy
person2 = person.copy()
person2["city"] = "Enugu"
print(person2)

# removing an item
del (person["age"])  # OR
person.pop("phone")
# clear dict
person.clear()

print(person)
print(len(person2))

# list of dict
people = [
    {
        "name": "Divine",
        "age": 30
    },
    {
        "name": "Martha",
        "age": 50
    }
]

print(people)
