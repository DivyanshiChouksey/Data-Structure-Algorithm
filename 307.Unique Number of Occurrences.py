# Unique Number of Occurrences

# Time Complexity = O(n) || Space Complexity = O(n)

arr = [1, 2, 2, 1, 1, 3]

from collections import Counter


def uniqueOccurrences(arr):
    count = Counter(arr)
    array = []
    freq = set()
    for k, v in count.items():
        freq.add(v)
        array.append(v)

    return len(freq) == len(array)


print(uniqueOccurrences(arr))
