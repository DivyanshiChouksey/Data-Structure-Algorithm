# Contain Duplicate

nums = [1, 2, 3, 1]

# Solution 1
"""
    Make a set and iterate through the given array nums and
    if current element not in set then add current element to set
    or current element is in set that means it is a duplicate return True
"""
# Time Complexity = O(n) || Space Complexity = O(n)
def containDuplicate1(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# Solution 2
"""
    Sort the nums array check if current element is equal to next element return True or else return False.
"""
# Time Complexity = O(nlogn) || Space Complexity = O(1)

nums = [1, 2, 3, 1]


def containDuplicate2(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False


# Solution 3
"""
    Create a dictionary and iterate through the given array nums and
    if current element not in dictionary then add current element to dictionary with value True
    or current element is in dictionary that means it is a duplicate return True
"""
# Time Complexity = O(n) || Space Complexity = O(n)
nums = [1, 2, 3, 1]


def containDuplicate3(nums):
    seen = {}
    for num in nums:
        if num in seen:
            return True
        seen[num] = True
    return False


print(containDuplicate1(nums))

print(containDuplicate2(nums))

print(containDuplicate3(nums))
