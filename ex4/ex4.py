#Setting the number of cars
cars = 100
#Setting the number of passengers that a car can hold
space_in_a_car = 4.0
#Setting the number of people we have to drive the cars
drivers = 30
#Setting the number of passengers that we have to transport today
passengers = 90
#Setting the number of cars that we don't have drivers for
cars_not_driven = cars - drivers
#Setting the number of cars that we have drivers for and will be driven
cars_driven = drivers
#Setting the total capacity of the carpool
carpool_capacity = cars_driven * space_in_a_car
#Setting the number of passengers that we need to put in a car on average to meet capacity
average_passengers_per_car =  passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to pur about", average_passengers_per_car, "in each car.")
