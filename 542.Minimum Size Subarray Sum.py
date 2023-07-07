# Minimum Size Subarray Sum

target = 7
nums = [2,3,1,2,4,3]

def minSubArrayLen(target, nums):
    left = 0
    ans = float("inf")
    cur = 0

    for i in range(len(nums)):
        cur+=nums[i]
        while cur>=target:
            ans = min(ans,i-left+1)
            cur -= nums[left]
            left+=1
    
    return ans if ans != float("inf") else 0

print(minSubArrayLen(target, nums))

