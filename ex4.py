# How many cars?
cars = 100

# How many spaces per car?
space_in_a_car = 4.0

# How many drivers?
drivers = 30

# How many passengers?
passengers = 90

# How many cars are not driven?
cars_not_driven = cars - drivers

# How many cars are driven?
cars_driven = drivers

# Carpool capacity?
carpool_capacity = cars_driven * space_in_a_car

# Average number of passengers per car?
average_passengers_per_car = passengers / cars_driven


# Print cars available
print("There are", cars, "cars available.")

# Print drivers available
print("There are only", drivers, "drivers available.")

# Print vehicles not being driven
print("There will be", cars_not_driven, "empty cars today.")

# Print number of people being transported today
print("We can transport", carpool_capacity, "people today.")

# Print number of passengers transported today
print("We have", passengers, "to carpool today.")

# Print number of passengers per car
print("We need to put about", average_passengers_per_car, "in each car.")
