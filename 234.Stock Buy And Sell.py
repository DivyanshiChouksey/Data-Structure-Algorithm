# Stock Buy And Sell

prices = [7, 6, 4, 3, 1]


def maxProfit(prices):
    l, r = 0, 1
    maxP = 0
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
        else:
            l = r
        r += 1

    return maxP


print(maxProfit(prices))
