# Ugly Number

"""
    An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5
"""

# Time Complexity = O(logn) || Space Complexity = O(1)

n = 6


def isUgly(n):
    if n <= 0:
        return False
    for p in [2, 3, 5]:
        while n % p == 0:
            n = n // p
    return n == 1


print(isUgly(n))
