name = 'Zed A. Shaw'
age = 35  # not a lie
height = 74  # inches
height = 74*2.54  # cm
weight = 180  # lbs
weight = 180*0.4536  # kg
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
# print(f"He's {height} inches tall.")  # inches
print(f"He's {round(height)} cm tall.")  # cm
# print(f"He's {weight} pounds heavy.")  # lb
print(f"He's {round(weight)} kg heavy.")  # kg
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
