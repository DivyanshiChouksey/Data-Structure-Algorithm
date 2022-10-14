# 3Sum
"""

"""
# Time Complexity = O() || Space Complexity = O()

nums = [-1, 0, 1, 2, -1, -4]


def threeSum(nums):
    ans = set()
    nums.sort()
    for i in range(len(nums) - 2):
        l = i + 1
        r = len(nums) - 1
        while l < r:
            currentSum = nums[i] + nums[l] + nums[r]
            if currentSum == 0:
                ans.add((nums[i], nums[l], nums[r]))
                l += 1
                r -= 1
            elif currentSum < 0:
                l += 1
            else:
                r -= 1
    return list(ans)


print(threeSum(nums))
