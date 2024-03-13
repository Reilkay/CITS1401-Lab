# Write a program that finds the sum of squares of all numbers between zero and a whole number x that the user enters (x can be positive or negative). The program must then print the result of this calculation to the shell. For instance, if the user enters 5, then the sum of the squares of numbers 0, 1, 2, 3, 4 and 5 is 55, so your program should print 55 to the shell. Similarly the sum of squares for all numbers up to -4 is 30. Note that the 'user entry' part of the program has already been written for you (this is the x = int(input("")) line the is pre-loaded into the answer box).
x = int(input())


# Don't change the above line of code. Add your code after this line. Remember not to print anything other than final answer
def func(n: int):
    return sum(i**2 for i in range(0, n + 1)) if n >= 0 else sum(
        i**2 for i in range(n, 0))


print(func(x))
