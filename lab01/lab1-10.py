# Write a program to print the factorial of variable x.
x = int(input(""))


# Don't change the above line of code. You can assume that x will always be either a positive integer or 0.
def factorial(n: int):
    return 1 if n <= 1 else n * factorial(n - 1)


print(factorial(x))
