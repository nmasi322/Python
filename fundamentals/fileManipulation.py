# Python has method for creating, updating, reading and deleting files

my_file = open("myfile.txt", "w")  # creates a new file

# get some info from file
print("Name:", my_file.name)
print("Closed:", my_file.closed)
print("Opening mode:", my_file.mode)

# write to file
my_file.write("I love Python programming!!")
my_file.write(" I love Javascript programming!!")
my_file.write(" I hate Typescript programming!!")
my_file.close()

# append to file
# put an "a" if you want to append. Adding "w" rewrite evrything there.
my_file = open("myfile.txt", "a")
my_file.write("Hey divine! How're you doing?")

# reading from file
# put an "a" if you want to append. Adding "w" rewrite evrything there.
my_file = open("myfile.txt", "r+")
text = my_file.read(100)  # gets the first 100 letters in the file
print(text)
