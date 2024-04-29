# Minimum Number of Operations to Make Array XOR Equal to K

nums = [2,1,3,4]
k = 1

class Solution:
  def minOperations(self, nums: List[int], k: int) -> int:
      final_xor = 0
      for n in nums:
          final_xor = final_xor ^ n

      return bin(final_xor ^ k).count('1')
