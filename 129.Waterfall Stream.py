# Waterfall Stream

# Time Complexity = O(n*m) , n - len(array)
# Space Complexity = O(n) , m - len(array[0])
array = [
    [0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0],
]
source = 3


def waterfallStreams(array, source):

    rowAbove = array[0][:]  # copy
    rowAbove[source] = -1  # water coming
    # Now moving down or splitting
    for i in range(1, len(array)):
        currentRow = array[i][:]
        for j in range(len(rowAbove)):
            valueAbove = rowAbove[j]
            hasWater = valueAbove < 0
            hasBlock = currentRow[j] == 1
            if not hasWater:
                continue
            if not hasBlock:
                currentRow[j] += valueAbove
                continue
            splitWater = valueAbove / 2
            # Right
            rightIdx = j
            while rightIdx + 1 < len(rowAbove):
                rightIdx += 1
                if rowAbove[rightIdx] == 1:
                    break
                if currentRow[rightIdx] != 1:
                    currentRow[rightIdx] += splitWater
                    break
            # left
            leftIdx = j
            while leftIdx - 1 >= 0:
                leftIdx -= 1
                if rowAbove[leftIdx] == 1:
                    break
                if currentRow[leftIdx] != 1:
                    currentRow[leftIdx] += splitWater
                    break
        rowAbove = currentRow
    return list(map(lambda x: x * -100, rowAbove))


print(waterfallStreams(array, source))
