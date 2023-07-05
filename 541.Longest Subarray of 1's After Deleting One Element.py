# Longest Subarray of 1's After Deleting One Element

nums = [0,1,1,1,0,1,1,0,1]

def longestSubarray(nums):                
    left = 0
    zeros = 0
    ans = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            zeros += 1
        while zeros > 1:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        ans = max(ans, i - left)
    return ans


print(longestSubarray(nums))
