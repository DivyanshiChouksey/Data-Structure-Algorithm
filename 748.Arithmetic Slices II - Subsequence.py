# Arithmetic Slices II - Subsequence

nums = [2,4,6,8,10]

from collections import defaultdict 

def numberOfArithmeticSlices(nums):
    n = len(nums)
    dp = [defaultdict(int) for _ in range(n)]
    
    ans = 0
    for i in range(1, n):
        for j in range(i):
            diff = nums[i] - nums[j]
            cnt = 0
            if diff in dp[j]:
                cnt = dp[j][diff]
                
            dp[i][diff] += cnt + 1
            ans += cnt
            
    return ans

print(numberOfArithmeticSlices(nums))
