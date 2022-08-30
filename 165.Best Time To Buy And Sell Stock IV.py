# Best Time Buy And Sell Stock
"""
    Start with creating a 2D matrix of prices and transactions  
    after that go through the prices and
    store max of previous and current profit and return max profit.
"""
# Time Complexity = O(nk) || Space Complexity = O(nk)

prices = [5, 11, 3, 50, 60, 90]
k = 2


def ktranscation(prices, k):
    if len(prices) == 0:
        return 0
    profit = [[0 for p in prices] for t in range(k + 1)]
    for t in range(1, k + 1):
        for d in range(1, len(prices)):
            profit[t][d] = max(
                profit[t][d - 1],
                max(profit[t - 1][x] - prices[x] + prices[d] for x in range(d)),
            )
    return profit[-1][-1]


print(ktranscation(prices, k))
