# Write a function calculate_cartons(eggs) for a small local farm that takes a number of eggs and returns the number of egg cartons that will be needed to pack these eggs, assuming 12 eggs fit into a carton. Don't worry about any left over eggs (they will be eaten by the owner for breakfast).


def calculate_cartons(eggs):
    """ Calculate the number of cartons needed to hold 
        the specified number of eggs.
    """
    return eggs // 12


print(calculate_cartons(65))
