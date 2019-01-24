# import argv module from sys package
from sys import argv

# provide variables to argv; you'll need to pass arguments to these variables
# when you run the script.
script, filename = argv

# create a variable with the ability to open a file
txt = open(filename)

# Show file which file will be opened.
print(f"Here's your file {filename}:")
# Show user contents of file.
print(txt.read())

# Prompt user for filename
print("Type the filename again:")
file_again = input("> ")

# Create a variable to open the file that the user typed in
txt_again = open(file_again)

# Display contents of file that the user typed into the prompt.
print(txt_again.read())

txt.close()
txt_again.close()
