# Practicing variables, the right side valu will be storred in left variable.
cars = 100
space_in_a_car = 4.0 # 4.0 indicates floating point while 4 is an integer.
drivers = 30
passengers = 90
#  A variable can also be result of an operation
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven *space_in_a_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can trasport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")