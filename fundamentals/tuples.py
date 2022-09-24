# a tuple is a collections which is ordered and unchangeable. allows duplicate members
# simple tuple

fruit_tuple = ("apple", "orange", "mango")
# print(fruit_tuple)

# using constructor
# fruit_tuple = tuple(("apple", "orange", "mango"))

# get a single value
# print(fruit_tuple[1])

# change value
# fruit_tuple[1] = "grape"   # cannot change values. This will cause an error
# print(fruit_tuple)

# tuples with one value should have trailing comma
fruit_tuple2 = ("apple",)
# print(fruit_tuple2)

# length
# print(len(fruit_tuple))

del fruit_tuple2


"""
Sets are collections which are unordered and unindexed. no duplicate members allowed
"""

# no duplicate members, so mango will be ignored
fruit_set = {"apple", "orange", "mango", "mango"}
print(fruit_set)

# check if in set
print("apple" in fruit_set)

# add to set
fruit_set.add("grape")  # adds to index 0
print(fruit_set)

# remove from set
fruit_set.remove("apple")
print(fruit_set)

# clear set
fruit_set.clear()

# delete set
del fruit_set

print(fruit_set)
