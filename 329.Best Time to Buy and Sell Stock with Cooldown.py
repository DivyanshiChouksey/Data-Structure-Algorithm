# Best Time to Buy and Sell Stock with Cooldown

prices = [1, 2, 3, 0, 2]


def maxProfit(prices):
    p1, p2 = 0, 0
    for x in range(1, len(prices)):
        temp = p1
        p1 = max(p1 + prices[x] - prices[x - 1], p2)
        p2 = max(temp, p2)
    return max(p1, p2)


print(maxProfit(prices))
