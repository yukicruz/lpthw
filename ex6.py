# How many types of people
types_of_people = 10

# start of joke
x = f"There are {types_of_people} types of people."


# assign "binary" variable with string "binary"
binary = "binary"

# assign "do_not" variable with string "don't"
do_not = "don't"

# punchline using variables: "binary" and "do_not"
y = f"Those who know {binary} and those who {do_not}."  # 2 str in a string


# print start of joke
print(x)

# print punchline of joke
print(y)


# repeat joke
print(f"I said: {x}")  # string placed in a string

# repeat punchline
print(f"I also said: '{y}'")  # string placed in a string


# value of hilariousness of joke
hilarious = False


# use a variable to question joke's hilariousness
joke_evaluation = "Isn't that joke so funny?! {}"


# print joke evaluation with variable and formatting
print(joke_evaluation.format(hilarious))


# left variable and right variable
w = "This is the left side of..."
e = "a string with a right side."


# combine left variable and right variable
print(w + e)
