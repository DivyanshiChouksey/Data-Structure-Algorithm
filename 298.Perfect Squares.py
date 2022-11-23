# Perfect Squares


# Best Solution
"""
    There is an algorithm called Lagrange theorem which 
    states that we can get any number by adding max of 4 perfect square number
"""
# Time Complexity = O(n) || Space Complexity = O(1)

from math import sqrt

n = 12


def numSquares(n):
    while n % 4 == 0:
        # Reduction by factor of 4
        n //= 4

    if n % 8 == 7:
        # Quick response for n = 8k + 7
        return 4

    # Check whether n = a^2 + b^2
    for a in range(int(sqrt(n)) + 1):

        b = int(sqrt(n - a * a))

        if (a**2 + b**2) == n:
            return (a > 0) + (b > 0)

    # n = a^2 + b^2 + c^2
    return 3


# Naive Solution
"""
    So we start from finding all perfect square 
    upto n+1 and then we apply same logic of coin change
    coin change - (We make an inf array of size(amount) then to 
        make amount 0 we need 0 coins
        After this we loop to coins array and then 
        update min coins by subtrating the index
        by coin like this dp[i] = min(dp[i],dp[i-coin]+1))
"""
# Time Complexity = O(n^2) || Space Complexity = O(n)

n = 12


def numSquares2(n):
    dp = [float("inf") for i in range(n + 1)]
    dp[0] = 0
    square = []
    for i in range(1, n + 1):
        if i * i > n:
            break
        square.append(i * i)

    for i in square:
        for j in range(i, n + 1):
            dp[j] = min(dp[j], dp[j - i] + 1)
    return dp[-1]


print(numSquares(n))
print(numSquares2(n))
