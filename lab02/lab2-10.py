# Write a function dseries(n_terms) to calculate the first n terms of the following series
# 1^2 + 2^2 + 3^2 + 4^2 + .....


def dseries(n_terms):
    return 0 if n_terms == 0 else n_terms**2 + dseries(n_terms - 1)


print(dseries(3))
