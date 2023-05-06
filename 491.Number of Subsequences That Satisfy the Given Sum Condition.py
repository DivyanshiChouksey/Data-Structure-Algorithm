# Number of Subsequences That Satisfy the Given Sum Condition

nums = [3,5,6,7]
target = 9

def numSubseq(nums, target):
    nums.sort()
    l, r = 0, len(nums) - 1
    res = 0
    mod = 10**9 + 7
    while l <= r:
        if nums[l] + nums[r] > target:
            r -= 1
        else:
            res += pow(2, r - l, mod)
            l += 1
    return res % mod
  
print(numSubseq(nums, target))
