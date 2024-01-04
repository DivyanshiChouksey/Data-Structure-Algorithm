# Minimum Number of Operations to Make Array Empty

nums = [2,3,3,2,2,4,2,3,4]

from collections import Counter

def minOperations(nums):
    counter = Counter(nums)
    ans = 0
    for c in counter.values():
        if c == 1: 
            return -1
        ans += ceil(c / 3)
    return ans

print(minOperations(nums))
