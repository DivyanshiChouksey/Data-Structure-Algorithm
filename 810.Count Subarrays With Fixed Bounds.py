# Count Subarrays With Fixed Bounds

nums = [1,3,5,2,7,5]
minK = 1
maxK = 5

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        lastmn = 0
        lastmx = 0
        mn = float("inf")
        mx = -1
        x = 0
        ans = 0
        for i in range(len(nums)):
            if(nums[i] == minK): lastmn = i+1
            if(nums[i] == maxK): lastmx = i+1
            if(nums[i] < minK or nums[i] > maxK) :
                lastmn = 0
                lastmx = 0
                x = i+1
            if(lastmn and lastmx): 
                ans += min(lastmn-x, lastmx-x)
        
        
        return ans
#         totalSum = 0
#         n = len(nums)
#         for k in range(n+1):`
#             for i in range(n-k+1):
#                 minCurrent = 1e9
#                 maxCurrent = -1

#                 for j in range(i, i+k):
#                     if nums[j] < minCurrent:
#                         minCurrent = nums[j]

#                     if nums[j] > maxCurrent:
#                         maxCurrent = nums[j]
#                 if minCurrent==minK and maxCurrent==maxK:
#                     totalSum += 1

#         return totalSum
