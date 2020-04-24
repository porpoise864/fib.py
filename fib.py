# Author: Sarah Oertly
# Date: 10/18/2019
# Description: The first and second numbers in the Fibonacci sequence are both 1. After that, each subsequent number is
# the sum of the two preceding numbers. The first several numbers in the sequence are: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,
# 89, etc. Write a function named fib that takes a positive integer parameter and returns the number at that position of
# the Fibonacci sequence. For example fib(1) = 1, fib(3) = 2, fib(10) = 55, etc.
def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
print(fib(15))