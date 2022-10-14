# Combination Sum IV
# def combinationSum4(self, nums: List[int], target: int) -> int:
"""
If we want to find the combination of target made from nums, we can just find
sum(target - nums[1] , target - nums[2], ..., target - nums[n-1]) where n = len(nums)
"""
nums = [1, 2, 3]
target = 4
dp = [0 for i in range(target + 1)]
dp[0] = 1
for i in range(1, target + 1):
    for num in nums:
        if num > i:
            break
        dp[i] += dp[i - num]
print(dp)
# return dp[-1]
