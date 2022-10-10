# Three Number Sum

# Time Complexity = O(nlogn) || Space Complexity = O(n)
array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0


def threeNumberSum(array, targetSum):
    array.sort()
    ans = []
    for i in range(len(array) - 2):
        l = i + 1
        r = len(array) - 1
        while l < r:
            currentSum = array[i] + array[l] + array[r]
            if currentSum == targetSum:
                ans.append([array[i], array[l], array[r]])
                l += 1
                r -= 1
            elif currentSum < targetSum:
                l += 1
            else:
                r -= 1
    return ans


print(threeNumberSum(array, targetSum))
