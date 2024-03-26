# Write a function odd_finder(a,b,c,d,e,f,g,h,i,j) which takes 10 integers as inputs and returns the count of positive odd integers.  For instance, if the 10 integers inputted by the user are 1,2,3,4,5,-1,-2,-3,-4,0 then output by the function will be 3 (3 positive odd integers: 1,3 and 5).


def is_positive_odd(num: int) -> bool:
    return num % 2 == 1 and num > 0


def odd_finder(a: int, b: int, c: int, d: int, e: int, f: int, g: int, h: int,
               i: int, j: int) -> int:
    num_list = [a, b, c, d, e, f, g, h, i, j]
    count = 0
    for num in num_list:
        if is_positive_odd(num):
            count += 1
    return count


print(odd_finder(1, 2, 3, 4, 5, -1, -2, -3, -4, 0))
