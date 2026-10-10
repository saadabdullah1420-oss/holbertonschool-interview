#!/usr/bin/python3
"""Calculate the fewest operations needed to obtain n H characters."""


def minOperations(n):
    """Return the minimum number of Copy All and Paste operations."""
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
