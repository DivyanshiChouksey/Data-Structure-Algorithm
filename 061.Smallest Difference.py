array1 = [-1, 5, 10, 20, 28, 3]
array2 = [26, 134, 135, 15, 17]
"""
[-1,3,5,10,20,28]
[15,17,26,134,135]   
 28<26  2

"""


def smallestDiff(array1, array2):
    array1.sort()
    array2.sort()
    ans = []
    i = 0
    j = 0
    smallest = float("inf")
    current = float("inf")
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            current = array2[j] - array1[i]
            i += 1
        elif array1[i] > array2[j]:
            current = array1[i] - array2[j]
            j += 1
        else:
            return [array1[i], array2[j]]
        if smallest > current:
            smallest = current
            ans = [array1[i], array2[j]]
    return ans


print(smallestDiff(array1, array2))
