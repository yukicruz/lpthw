# ex7
snow = "snow"
print("Its fleece was white as {}.".format(snow))


# ex9
months = "Jan\nFeb\nMar\nApr"
print("Months are: ", months)
print("Months are: " + months)

# ex10
#     ESCAPE SEQUENCES
#     Escape --> What it does.
#     \\  --> Backslash (\)
#     \'  --> Single-quote (’)
#     \"  --> Double-quote (”)
#     \a  --> ASCII bell (BEL)  # This makes a bell ring!
#     \b  --> ASCII backspace (BS)  # Deletes letters in strings (not periods)
#     \f  --> ASCII formfeed (FF)  # Advance downward to next page or section
#     \n  --> ASCII linefeed (LF)   # Linefeed means to advance downward to the
#                                   # next line; however, it has been
#                                   # repurposed and renamed. Used as
#                                   # "newline", it terminates lines (commonly
#                                   # confused with separating lines). This is
#                                   # commonly escaped as "\n", abbreviated LF
#                                   # or NL, and has ASCII value 10 or 0x0A.
#                                   # CRLF (but not CRNL) is used for the pair
#                                   # "\r\n".
#     \N{name}  --> Character named name in the Unicode database (Unicode only)
#     \r  --> Carriage Return (CR)  # Returns to beginning of line and
#                                   # overrides existing text.
#                                   # Carriage return means to return to the
#                                   # beginning of the current line without
#                                   # advancing downward. The name comes from a
#                                   # printer's carriage, as monitors were rare
#                                   # when the name was coined. This is
#                                   # commonly escaped as "\r", abbreviated CR,
#                                   # and has ASCII value 13 or 0x0D.
#     \t  --> Horizontal Tab (TAB)
#     \uxxxx  --> Character with 16-bit hex value xxxx
#     \Uxxxxxxxx  --> Character with 32-bit hex value xxxxxxxx
#     \v  --> ASCII vertical tab (VT)
#     \ooo  --> Character with octal value ooo  # https://www.sciencebuddies.org/science-fair-projects/references/table-of-8-bit-ascii-character-codes
#     \xhh  --> Character with hex value hh  # https://www.sciencebuddies.org/science-fair-projects/references/table-of-8-bit-ascii-character-codes


# ex11
# How to access pydoc
# python -m pydoc  # https://docs.python.org/3.6/library/pydoc.html
# python -m pydoc input


# ex12 - I did this exercise through my own techniques in ex11

# ex13
# The argv is the ”argument variable,” a very standard name in programming that
# you will find used in many other languages. This variable holds the arguments
# you pass to your Python script when you run it. In the exercises you will get
# to play with this more and see what happens.
#
# Modules give you features; Modules are also called "libraries"
#
# Command lines are strings. Command lines are strings even if you typed
# numbers on the command line. Use int() to convert them just like with
# int(input()).

# ex18
# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")


# ok, that args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")


# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")


# this one takes no arguments
def print_none():
    print("I got nothin'.")


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

# FUNCTION CHECKLIST
# 1. Did you start your function definition with def?
# 2. Does your function name have only characters and _ (underscore) characters?
# 3. Did you put an open parenthesis ( right after the function name?
# 4. Did you put your arguments after the parenthesis ( separated by commas?
# 5. Did you make each argument unique (meaning no duplicated names)?
# 6. Did you put a close parenthesis and a colon ): after the arguments?
# 7. Did you indent all lines of code you want in the function four spaces? No more, no less.
# 8. Did you ”end” your function by going back to writing with no indent (dedenting we call it)?
#
# When you run (”use” or ”call”) a function, check these things:
# 1. Did you call/use/run this function by typing its name?
# 2. Did you put the ( character after the name to run it?
# 3. Did you put the values you want into the parenthesis separated by commas?
# 4. Did you end the function call with a ) character?

# ex19



# Appendix A
# 55.2.3
# Linux/macOS
# pwd --> print working directory
# hostname --> my computer’s network name
# mkdir --> make directory
# cd --> change directory
# ls --> list directory
# rmdir --> remove directory
# pushd --> push directory
# popd --> pop directory
# cp --> copy a file or directory
# mv --> move a file or directory
# less --> page through a file
# cat --> print the whole file
# xargs --> execute arguments
# find --> find files
# grep --> find things inside files
# man --> read a manual page
# apropos --> find which man page is appropriate
# env --> look at your environment
# echo --> print some arguments
# export --> export/set a new environment variable
# exit --> exit the shell
# sudo --> DANGER! become super user root DANGER!
#
# Windows
# If you’re using Windows then here’s your list of commands:
# pwd --> print working directory
# hostname --> my computer’s network name
# mkdir --> make directory
# cd --> change directory
# ls --> list directory
# rmdir --> remove directory
# pushd --> push directory
# popd --> pop directory
# cp --> copy a file or directory
# robocopy --> robust copy
# mv --> move a file or directory
# more --> page through a file
# type --> print the whole file
# forfiles --> run a command on lots of files
# dir -r --> find files
# select-string --> find things inside files
# help --> read a manual page
# helpctr --> find what man page is appropriate
# echo --> print some arguments
# set --> export/set a new environment variable
# exit --> exit the shell
# runas --> DANGER! become super user root DANGER!
#
# man <command> --> pull up a manual about a command when in terminal
# 55.9.1 (p311)
