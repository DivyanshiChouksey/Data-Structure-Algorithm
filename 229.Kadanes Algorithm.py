# Kadanes Algorithm

array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]


def kadanesAlgorithm(array):
    maxEnding = array[0]
    maxSoFar = array[0]
    for i in range(1, len(array)):
        maxEnding = max(array[i], maxEnding + array[i])
        maxSoFar = max(maxSoFar, maxEnding)
    return maxSoFar


print(kadanesAlgorithm(array))
