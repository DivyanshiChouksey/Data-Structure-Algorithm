# Minimum Number of Operations to Make Array Continuous

nums = [1,2,3,5,6]


def minOperations(nums):
    n = len(nums)
    ans = n
    new_nums = sorted(set(nums))
    
    for i in range(len(new_nums)):
        left = new_nums[i]
        right = left + n - 1
        j = bisect_right(new_nums, right)
        count = j - i
        ans = min(ans, n - count)

    return ans

print(minOperations(nums))
