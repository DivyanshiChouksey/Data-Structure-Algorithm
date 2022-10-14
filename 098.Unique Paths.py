# Unique Paths
import math


def uniquePaths(m: int, n: int) -> int:
    # return ( factorial(m+n-2)//factorial(m-1) )//factorial(n-1) #8C2

    dp = [1 for i in range(n)]
    # dp = [[1 for i in range(n)]for j in range(m)]
    # print(dp)
    for i in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]
    return dp[-1]


print(uniquePaths(3, 7))


def uniquePaths2(m: int, n: int) -> int:
    dp = [[1 for i in range(n)] for j in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]


print(uniquePaths2(3, 7))
