# Write a program that can add first n positive odd numbers starting from 1 and the number n is entered by the user. The program should only work for positive input data and give zero output for negative data
n = int(input())


# write your program below
def func(x: int):
    return sum(i * 2 - 1 for i in range(1, x + 1)) if x > 0 else 0


print(func(n))
