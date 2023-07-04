# Longest Even Odd Subarray With Threshold

nums = [3,2,5,4]
threshold = 5

def longestAlternatingSubarray(nums, threshold):
    i,j=0,0
    ans = 0
    while i<len(nums):
        j=i+1
        if nums[i]%2 == 0 and nums[i] <= threshold:
            while j<len(nums) and nums[j] % 2 != nums[j - 1] % 2 and nums[j] <= threshold:
                j+=1

            ans = max(ans,j-i)
        i=j

    return ans

print(longestAlternatingSubarray(nums, threshold))
