# The Fibonacci Sequence is the series of numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# The next number is found by adding up the two numbers before it.
# Write a program to generate Fibonacci Sequence and print the nth number where n is taken as input from the use. For instance, if user inputs 9 (n=9) then 21 should be printed.
n = int(input())


# Don't change the above line of code. Write your program below this line. Remember to print the final result only.
def fibonacci(x: int):
    return x - 1 if x <= 2 else fibonacci(x - 1) + fibonacci(x - 2)


print(fibonacci(n))
