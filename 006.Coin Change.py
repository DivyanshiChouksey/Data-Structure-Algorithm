# Coin Change
"""
    We make an inf array of size(amount) then to 
    make amount 0 we need 0 coins
    After this we loop to coins array and then 
    update min coins by subtrating the index
    by coin like this dp[i] = min(dp[i],dp[i-coin]+1)
    
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