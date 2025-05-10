#!/usr/bin/python3
import sys


def factorial(n):
    """
    Calculate the factorial of a non-negative integer n recursively.

    Parameters:
    n (int): A non-negative integer whose factorial is to be computed.

    Returns:
    int: The factorial of the input integer n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


# Read an integer from the command-line argument, compute its factorial, and print the result
f = factorial(int(sys.argv[1]))
print(f)
