#!/usr/bin/python3

"""Create a Function for Min Operations"""


def minOperations(n):
    """Function that calculates the fewest number of operations"""
    if n <= 1:
        return 0

    res = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            res += divisor
            n = n // divisor
        divisor += 1

    return res
