# Longest Consecutive Sequence
"""
    First convert nums array to set
    then check for n-1 value in set if 
    not found then search for all consecutive number
"""
# Time Complexity = O(n) || Space Complexity = O(n)

nums = [0,3,7,2,5,8,4,6,0,1]

def longestConsecutive(nums):
    count = 0
    nums = set(nums)
    for num in nums:
        if num-1 not in nums:
            tmpCnt = 0
            while num in nums:
                num += 1
                tmpCnt += 1
            count = max(count,tmpCnt)
    return count

print(longestConsecutive(nums))


