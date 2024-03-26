# Define and implement a function trip_cost(price,distance,economy)

# The inputs are:

# price: Fuel price in Litres
# distance: Distance to travel in kilometers
# economy: Fuel economy of the vehicle as L/100km
# The function returns the cost to travel in the vehicle (don’t include the dollar-sign, just return the real number).  You are required to pass the arguments to the function in the same order as described.

# What is the cost to travel for the following values. Do not include the units :

# Price = $1.3 ; Distance = 10 Km ; Economy = 5 L/100Km


def trip_cost(price, distance, economy):
    return price * distance * economy / 100


# We will round your answer to two decimal places
print(round(trip_cost(1.3, 10, 5), 2))
