# Buy Two Chocolates

prices = [1,2,2]
money = 3


def buyChoco(prices, money):
    # Sort the Array in Increasing Order
    prices.sort()

    # Minimum Cost
    min_cost = prices[0] + prices[1]

    # We can buy chocolates only if we have enough money
    if min_cost <= money:
        # Return the Amount of Money Left
        return money - min_cost
    else:
        # We cannot buy chocolates. Return the initial amount of money
        return money


print( buyChoco(prices, money))
