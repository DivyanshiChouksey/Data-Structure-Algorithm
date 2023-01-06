# Maximum Ice Cream Bars

"""
    go through the sorted costs array and if cost is smaller and equals to coins then
    buy the icecream and deduct that cost from coins and return the count of icecream
"""

# Time Complexity = O(nlogn) || Space Complexity = O(1)


def maxIceCream(costs, coins):
    count = 0
    costs.sort()
    # print(costs)
    for c in costs:
        if c <= coins:
            count += 1
            coins -= c

    return count
