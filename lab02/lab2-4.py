# Write a function days_in_years(number_of_years) that returns the number of days in the given number of years. You may assume that there are exactly 365 days in every year and that the numbers of years will always be a whole number.

# For example:

# days_in_years(1) → 365
# days_in_years(15) → 5475


def days_in_years(number_of_years):
    """ Return the number of days in the given number of years, assuming
        exactly 365 days in all years.
    """
    # Your code goes here
    return number_of_years * 365


print(days_in_years(10))
