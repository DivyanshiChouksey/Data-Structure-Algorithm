# Continuous Subarray Sum

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        given a and b if a % k == b % k
        then the distance abs(a - b) % k == 0

        """
        hm = {0: -1}
        s = 0
        for i, num in enumerate(nums):
            s = (s + num) % k
            if s in hm and i - hm[s] > 1:
                return True
            if s not in hm:
                hm[s] = i
        return False
        
