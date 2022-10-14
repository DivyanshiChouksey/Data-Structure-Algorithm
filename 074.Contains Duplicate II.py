#  Contains Duplicate II

nums = [1, 0, 1, 1]
k = 1

# Naive Solution
# Time Complexity = O(n^2) || Space Complexity = O(1)
def containsNearbyDuplicate(nums, k):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j] and abs(i - j) <= k:
                return True
    return False


# Optimize Solution
# Time Complexity = O(n) || Space Complexity = O()
def containsNearbyDuplicate2(nums, k):
    dct = {}
    for idx, key in enumerate(nums):
        if key in dct and (idx - dct[key]) <= k:
            return True
        dct[key] = idx
    return False


print(containsNearbyDuplicate(nums, k))
print(containsNearbyDuplicate2(nums, k))
