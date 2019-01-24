# import an argv argument from sys library
from sys import argv

script, filename = argv

print(
    f"We're going to erase {filename}.\n"
    "If you don't want that, hit CTRL-C (^C).\n"
    "If you do want that hit RETURN"
    )
input("?")

print("Opening the file...")

# target = open(filename)
target = open(filename, 'w')
# target = open(filename, 'a')
input("?")

print("Truncating the file.  Goodbye!")
target.truncate()  # This line isn't necessary if open(filename, 'w') b/c "w" will open and truncate by default.

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print("And finally, we close it.")
target.close()
