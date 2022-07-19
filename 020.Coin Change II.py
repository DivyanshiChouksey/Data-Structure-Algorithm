# Coin Change II
"""
    In this we have to find out total number of possible ways for we can generate a number
    Make an array starting from [1,0,0,0...] then
    update values using previous i-coin value in array then return out[-1]
"""
# Time Complexity = O(n^2) || Space Complexity = O(n)

amount = 5
coins = [1, 2, 5]


def change(amount, coins):
    dp = [0 for i in range(amount + 1)]
    dp[0] = 1
    for coin in coins:
        for i in range(coin, len(dp)):
            dp[i] += dp[i - coin]

    return dp[-1]


print(change(amount, coins))
