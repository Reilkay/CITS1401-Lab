# A local biologist needs a program to predict virus population growth. The inputs would be

# the initial number of virus infected persons (num)
# the rate of growth (a real number greater than 0) (rate)
# the number of hours it takes to achieve this rate (hour)
# and a number of hours during which the virus population grows (time)
# For example, one might start with a virus population (num) of 500 infected persons, a growth rate (rate) of 2, and a growth period (hour) to achieve this rate of 6 hours. Assuming that none of the infected persons die, this would imply that the population of infected persons would double in size every 6 hours. Thus after 6 hours (time in this case), we would have 1000 infected persons. Similarly for time=12 hours, we would have 2000 infected persons.

# Write a function virus_growth that takes these inputs and returns a prediction of the total population.


def virus_growth(num, rate, hour, time):
    return num * (rate**(time / hour))


print(round(virus_growth(100, 2, 4, 16), 1))
