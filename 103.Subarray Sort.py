array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]


def subarraySort(array):
    l = r = float("inf")
    tmp = sorted(array)
    for i in range(len(array)):
        if tmp[i] != array[i]:
            l = i
            break
    if l == float("inf"):
        return [-1, -1]

    for i in range(len(array) - 1, -1, -1):
        if tmp[i] != array[i]:
            r = i
            break
    return [l, r]


print(subarraySort(array))


def subarraySort1(array):
    if len(array) == 1:
        return [-1, -1]

    maxVal = float("-inf")
    minVal = float("inf")

    def outOfOrder(i, array):
        if i == 0:
            return array[0] > array[1]
        elif i == len(array) - 1:
            return array[i] < array[i - 1]
        return array[i] > array[i + 1] or array[i] < array[i - 1]

    for i in range(len(array)):
        if outOfOrder(i, array):
            maxVal = max(maxVal, array[i])
            minVal = min(minVal, array[i])

    if minVal == float("inf"):
        return [-1, -1]

    i = 0
    while minVal >= array[i]:
        i += 1

    j = len(array) - 1
    while maxVal <= array[j]:
        j -= 1

    if i == j:
        return [-1, -1]

    return [i, j]


print(subarraySort1(array))
