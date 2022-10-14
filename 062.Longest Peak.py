# Longest Peak
# Time Complexity = O(n) || Space Complexity = O(1)


def longestPeak(array):
    length = 0
    i = 1
    while i < len(array) - 1:
        isPeak = array[i - 1] < array[i] and array[i] > array[i + 1]

        if not isPeak:
            i += 1
            continue

        l = i - 2
        while l >= 0 and array[l] < array[l + 1]:
            l -= 1

        r = i + 2
        while r < len(array) and array[r] < array[r - 1]:
            r += 1

        current = r - l - 1
        length = max(length, current)
        i = r
    return length


array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
print(longestPeak(array))
