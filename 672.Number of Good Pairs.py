# Number of Good Pairs

nums = [1,2,3,1,1,3]

"""
There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
"""

def numIdenticalPairs(nums):
    ans = 0
    dct =  defaultdict(int)
    for num in nums:
        ans+=dct[num]
        dct[num]+=1

    return ans


print(numIdenticalPairs(nums))
