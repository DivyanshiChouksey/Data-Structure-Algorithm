# Minimize Maximum of Array

""" 
    answer = 0 and prefixSum = 0.
    Iterate over nums, for each index i:
    Update the prefix sum as prefixSum += nums[i].

    Check the maximum value we can obtain by averaging prefixSum into i + 1 evenly using ceiling division.

    answer = max(answer, math.ceil(prefix_sum / (i + 1))) 
    Return answer.
"""

class Solution:
    def minimizeArrayValue(self, nums: List[int]):
        ans = 0
        prefix = 0
        i=0
        for n in nums:
            prefix+=n
            ans = max(ans,math.ceil(prefix/(i+1)))
            i+=1
        return ans
