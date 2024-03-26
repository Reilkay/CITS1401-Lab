# Create a function dinner_calculator(meal_cost, drinks_cost) that calculates and returns the total cost of the meal for a small restaurant during happy hour (drinks only are discounted).

# The function takes two values, the cost of the meals and drinks before GST.
# Before GST is applied, a 30% discount needs to be applied to the drinks cost.
# Goods and services tax (GST) needs to be added to the meal and drinks cost, GST is set to 15%.
# The function should return the total cost.
# In our tests, we round the answer you return to 2 decimal places before printing but don't worry about that - your function should simply return the exact answer (to the extent that any floating point calculation is "exact").


def dinner_calculator(meal_cost, drinks_cost):
    """ Calculate the cost of dinner during happy hour.
        Takes into consideration:
         - Pre-GST meal and drink costs
         - Happy Hour discounts
         - GST
    """
    return 1.15 * (meal_cost + 0.7 * drinks_cost)


total_cost = dinner_calculator(10, 0)
# We round your answer to 2 decimal places before printing.
# Don't worry about why.
print(round(total_cost, 2))
