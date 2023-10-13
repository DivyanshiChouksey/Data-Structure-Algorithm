# Domino and Tromino Tiling

# Time Complexity = O(n) || Space Complexity = O(n)
n = 3


def numTilings(n):
    dp = [[0, 0] for _ in range(3)]
    dp[1], dp[2] = [1, 1], [2, 2]
    for i in range(3, n + 1):
        dp[i % 3][0] = dp[(i - 1) % 3][0] + dp[(i - 2) % 3][0] + 2 * dp[(i - 2) % 3][1]
        dp[i % 3][1] = dp[(i - 1) % 3][0] + dp[(i - 1) % 3][1]
    return dp[n % 3][0] % 1_000_000_007



# Solution 2

n=3
def numTilings(n):
    # 1 1 2 5 11 24 53 117 0 
    if n<2:
        return 1

    dp = [0 for _ in range(n+1)]
    dp[0] = dp[1]= 1
    dp[2] = 2
    for i in range(3,n+1):
        dp[i] = (dp[i-1]*2)+dp[i-3]
    # print(dp)
    return (dp[-1]) % ((10**9)+7)


print(numTilings(n))
print(numTilings(n))
