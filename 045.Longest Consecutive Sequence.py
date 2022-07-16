# Longest Consecutive Sequence
"""
    First convert nums array to set
    then check if n-1 value is not in our set, then start from including n value
    keep the record temporary count and max of temporary count ie. our ans count
    return max of count and temporary count
"""
# Time Complexity = O(n) || Space Complexity = O(n)

nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]


def longestConsecutive(nums):
    count = 0
    nums = set(nums)
    for num in nums:
        if num - 1 not in nums:
            tmpCnt = 0
            while num in nums:
                num += 1
                tmpCnt += 1
            count = max(count, tmpCnt)
    return count


print(longestConsecutive(nums))
