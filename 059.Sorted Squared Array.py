# Sorted Squared Array

array = [-4, -1, 0, 3, 10]

# Navie Solution
"""
    
"""
# Time Complexity = O(nlogn) || Space Complexity = O(n)
def sortedSquaredArray(array):
    ans = []
    for arr in array:
        arr *= arr
        ans.append(arr)

    ans.sort()
    return ans


# Optimized Solution
# Time Complexity = O(n) || Space Complexity = O(n)
def sortedSquaredArray1(array):
    ans = [0 for _ in array]
    l = 0
    r = len(array) - 1
    for i in reversed(range(len(array))):
        smallerValue = array[l]
        largerValue = array[r]
        if abs(smallerValue) > abs(largerValue):
            ans[i] = smallerValue * smallerValue
            l += 1
        else:
            ans[i] = largerValue * largerValue
            r -= 1
    return ans


print(sortedSquaredArray(array))
print(sortedSquaredArray1(array))
