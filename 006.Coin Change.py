# Coin Change
"""
    in this we make a record of min coins required for every
    small amount and then use it for bigger amount
"""
# Time Complexity = O(m*n) || Space Complexity = O(n)

coins = [1,2,5]
amount = 11

def coinChange(coins,amount):
    dp = [float("inf") for i in range(amount+1)]
    dp[0] = 0
    for coin in coins:
        for i in range(coin,amount+1):
            dp[i] = min(dp[i],dp[i-coin]+1)
    if dp[-1] == float("inf"):
        return -1
    return dp[-1]

print(coinChange(coins,amount))