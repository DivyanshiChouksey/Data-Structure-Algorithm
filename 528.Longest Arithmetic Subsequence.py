# Longest Arithmetic Subsequence

from collections import Counter

nums = [20,1,15,3,10,5,8]

def longestArithSeqLength(nums):
    count = Counter()
    for i in range(len(nums)):
        for j in range(0,i):
            count[(i,nums[i]-nums[j])] = count[(j,nums[i]-nums[j])]+1

    return max(count.values())+1

print(longestArithSeqLength(nums)
