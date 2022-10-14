# Non Constructible Change
"""

"""
# Time Complexity = O(nlogn) || Space Complexity = O(1)
coins = [5, 7, 1, 1, 2, 3, 22]


def nonConstructible(coins):
    coins.sort()
    currentSum = 0
    for coin in coins:
        if coin > currentSum + 1:
            return currentSum + 1
        currentSum += coin
    return currentSum + 1


print(nonConstructible(coins))
