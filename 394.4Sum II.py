# 4Sum II

"""
    It is similar to 2Sum 
    keep record of 2Sum of nums1 and nums2 then go through the nums3 and nums4 and check 
    negative of their sum in present in 2Sum of nums1 ans nums2 then increase the count with their values.
"""

# Time Complexity = O(n^2) || Space Complexity = O(n^2) 

from collections import defaultdict

nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]

def fourSumCount(nums1, nums2, nums3, nums4):
    
    dct = defaultdict(int)
    count = 0
    for n in nums1:
        for m in nums2:
            dct[n+m]+=1
    # dct{} -1:1    0:2     1:1
    for n in nums3:
        for m in nums4:
            count+=dct[-(n+m)] # if i am getting -1 then we need 1 
    
    return count

print(fourSumCount(nums1, nums2, nums3, nums4))
