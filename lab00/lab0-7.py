print("This program illustrates a chaotic function")
x = float(input("Enter a number between 0 and 1: ")) #taking input from user
for i in range(10):
    x = 2.0 * x * (1 - x)
    print(x)