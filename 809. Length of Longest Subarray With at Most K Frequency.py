#  Length of Longest Subarray With at Most K Frequency

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = Counter()
        start = 0
        over_k = 0
        for i in range(n):
            freq[nums[i]]+=1
            if freq[nums[i]] == k+1:
                over_k+=1
            if over_k:
                freq[nums[start]] -=1
                if freq[nums[start]]==k:
                    over_k -=1
                start+=1
        return n-start
