# Number of Subarrays With LCM Equal to K

nums = [3, 6, 2, 7, 1]
k = 6

"""
    Using two for loops and slice in-built function to create the all possible subarrays
    then check the LCM of each element of every possible subarray and if it is equals to given K 
    then increase the count of required subarrays at the end return the count
"""

# Time Complexity = O(n^2) || Space Complexity = O(1)

import math


def subarrayLCM(nums, k):
    cnt = 0
    for i in range(len(nums)):
        tmp = nums[i]
        for j in range(i, len(nums)):
            tmp = math.lcm(tmp, nums[j])
            if tmp == k:
                cnt += 1
            if tmp > k:
                break
    return cnt


print(subarrayLCM(nums, k))
