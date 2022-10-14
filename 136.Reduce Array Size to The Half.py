# Reduce Array Size to The Half

from typing import Counter


arr = [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]


def minSetSize(arr):
    count = Counter(arr)  # increasing order
    currentValue = currentSize = 0
    for val in sorted(count.values(), reverse=True):
        currentSize += 1
        if currentValue + val >= len(arr) // 2:
            return currentSize
        currentValue += val


print(minSetSize(arr))
