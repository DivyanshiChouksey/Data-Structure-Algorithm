# Combination Sum IV


nums = [1,2,3]
target = 4

def combinationSum4(nums, target):
    dp = [0 for i in range(target+1)]
    dp[0] = 1
    for i in range(target+1):
        for num in nums:
            if i-num>=0:
                dp[i] += dp[i-num]

    return dp[target]


print(combinationSum4(nums, target)
