# You already wrote Fibonacci program which you just created in earlier question. Now update it such that it calculates the summation of Fibonacci number with each number too. Below is the sample for Fibonacci sequence and its summation
# Fibonacci       Summation
# 0               0
# 1               1
# 1               2
# 2               4
# 3               7
# 5               12
# 8               20
# and so on.
# The program should ask the user to provide an input n and displays the summation value up to that nth number in the series. For instance, if input is provided as 7 (n=7) then the displayed value is 20.
n = int(input())

# Don't change the above line. You need to write your code below this line. Remember to print the final value only.


def fibonacci_yield(i: int):
    x, y = 0, 1
    while i > 0:
        yield x
        x, y = y, x + y
        i = i - 1


print(sum(fibonacci_yield(n)))
