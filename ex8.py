# create a variable that can given four variables
formatter = "{} {} {} {}"

# practice calling variables into "formatter" with the format function
print(formatter.format(1, 2, 3, 4))
print(formatter.format(1, False, "tres", "4"))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a rock song",
    "Or a poem about beer."
))
