nums = [3, 0, 1]

# Time Complexity = O(n^2) || Space Complexity = O(1)
def missingNumber(nums):
    for i in range(len(nums) + 1):
        if i not in nums:
            return i


print(missingNumber(nums))

#
def missingNumber2(nums):
    nums.sort()
    for i in range(len(nums) + 1):
        if nums[i] != i:
            return i


print(missingNumber2(nums))
# BlockChain - Monday Flask
# 65-95 - Desc + copy or 100 without copy
# Tic Tac Toe Logic - leaderboard - logically
