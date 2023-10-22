# Maximum Score of a Good Subarray

nums = [1,4,3,7,4,5]
k = 3


def maximumScore(nums, k):
    n = len(nums)
    left = k
    right = k
    ans = nums[k]
    curr_min = nums[k]
    
    while left > 0 or right < n - 1:
        if (nums[left - 1] if left else 0) < (nums[right + 1] if right < n - 1 else 0):
            right += 1
            curr_min = min(curr_min, nums[right])
        else:
            left -= 1
            curr_min = min(curr_min, nums[left])

        ans = max(ans, curr_min * (right - left + 1))
    
    return ans


print( maximumScore(nums, k))
