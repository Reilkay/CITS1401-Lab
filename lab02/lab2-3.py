# Write a function to_celsius(fahrenheit) that takes a float temperature in degrees fahrenheit and returns the equivalent temperature in degrees celsius. The formula is:
# degrees_celsius = (fahrenheit - 32) * (5 / 9)


def to_celsius(fahrenheit):
    """Return the given fahrenheit temperature in degrees celsius"""
    degrees_celsius = (fahrenheit - 32) * (5 / 9)
    return degrees_celsius


print(to_celsius(1))
