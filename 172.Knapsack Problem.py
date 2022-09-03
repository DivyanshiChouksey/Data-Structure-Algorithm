# Knapsack Problem

"""
    Creating 2d array of items and capacity and at each indeces 
    will store knapsackValues[i-1][j] if weight of current item > j
    else store max(knapsackValues[i - 1][j], knapsackValues[i - 1][j - weight] + current item value)

    after that create array and append index of items if knapsackValues[i][j] != knapsackValues[i - 1][j]
    and update j -= items[i - 1][1] and i -= 1 else only update i -= 1
    and return the array along with the max value.
"""

# Time Complexity = O(nc), c - capacity
# Space Complexity = O(nc)

items = [[1, 2], [4, 3], [5, 6], [6, 7]]
capacity = 10


def knapsackProblem(items, capacity):
    knapsackValues = [[0 for i in range(capacity + 1)] for j in range(len(items) + 1)]
    for i in range(1, len(items) + 1):
        weight = items[i - 1][1]
        value = items[i - 1][0]
        for j in range(capacity + 1):
            if weight > j:
                knapsackValues[i][j] = knapsackValues[i - 1][j]
            else:
                knapsackValues[i][j] = max(
                    knapsackValues[i - 1][j], knapsackValues[i - 1][j - weight] + value
                )

    return (knapsackValues[-1][-1], getknapsackItems(knapsackValues, items))


def getknapsackItems(knapsackValues, items):
    sequence = []
    i = len(knapsackValues) - 1
    j = len(knapsackValues[0]) - 1

    while 0 < i:
        if knapsackValues[i][j] == knapsackValues[i - 1][j]:
            i -= 1
        else:
            sequence.append(i - 1)
            j -= items[i - 1][1]
            i -= 1
        if j == 0:
            break
    return list(reversed(sequence))


print(knapsackProblem(items, capacity))
