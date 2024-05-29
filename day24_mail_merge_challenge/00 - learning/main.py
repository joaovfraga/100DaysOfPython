
# Option 1 to open a file:
my_file = open("my_file.txt")
contents = my_file.read()
print(contents)
my_file.close()

# Option 2 to open a file:
with open("my_file.txt") as file:
    contents_v2 = file.read()
    print(contents_v2)

# Append a new string to a existing file:
with open("my_file.txt", mode="a") as my_file:
    my_file.write("\nNew Text.")

# Create a new file:
with open("new_file.txt", mode="w") as my_file:
    my_file.write("New Text.")