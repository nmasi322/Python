# lists
# creating lists
numbers = [1, 2, 3, 4, 5]
# print(type(numbers))
# print(numbers)

# using a constructor
numbers = list((1, 2, 3, 4, 5))
print(numbers)
fruits = ["apples", "oranges", "bananas", "pears"]

# get value
print(fruits[1])
print(len(fruits))

# append to list
fruits.append("mangoes")
print(fruits)

# remove from list
fruits.remove("bananas")
print(fruits)

# insert into position
fruits.insert(2, "strawberries")
print(fruits)

# remove from position
fruits.pop(4)
print(fruits)

# reverse list
fruits.reverse()
print(fruits)

# sort
fruits.sort()
print(fruits)

# reverse sort
fruits.sort(reverse=True)
print(fruits)
