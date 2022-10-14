# Max Subset Sum No Adjacent


array = [75, 105, 120, 75, 90, 135]


def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]
    maxSum = array[:]
    maxSum[1] = max(array[0], array[1])
    for i in range(2, len(array)):
        maxSum[i] = max(maxSum[i - 1], maxSum[i - 2] + array[i])
    return maxSum[-1]


print(maxSubsetSumNoAdjacent(array))
