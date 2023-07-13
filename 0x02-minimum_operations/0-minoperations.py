#!/usr/bin/python3

"""
    0x02 minimum operations
"""


def minOperations(n):
    """
        method that calculates the fewest number of operations needed to result in exactly n H characters in the file.
    """

    current = 1
    init = 0
    recorder = 0
    while current < n:
        remainder = n - current
        if (remainder % current == 0):
            init = current
            current += init
            recorder += 2
        else:
            current += init
            recorder += 1
    return recorder

