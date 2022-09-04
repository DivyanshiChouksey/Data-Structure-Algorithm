# Replace Elements With Greatest Element On Right Side
"""
    We start iterating through the array in reversed order and taking a variable to store
    rightMax initially storing -1 and replace current value with the max of current value and right max.
"""
# Time Complexity = O(n) || Space Complexity = O(1)

arr = [17, 18, 5, 4, 6, 1]


def replaceElements(arr):
    rightMax = arr[-1]
    arr[-1] = -1
    for i in reversed(range(len(arr) - 1)):
        temp = arr[i]
        arr[i] = rightMax
        rightMax = max(temp, rightMax)
    return arr


print(replaceElements(arr))
