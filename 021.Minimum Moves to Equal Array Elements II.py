# Minimum Moves to Equal Array Elements II
"""
    Sort the array, find the median of the array and then
    calculate the steps taken to make every element of array equals to the median of the array,
    finally return the total steps taken.
"""

# Time Complexity = O(nlog) || Space Complexity = O(1)
nums = [1,2,3]

def minMoves2(nums): 
    nums.sort()
    mid = len(nums)//2
    moves = 0
    for i in range(len(nums)):
        moves += abs(nums[i] - nums[mid])

    return moves

print(minMoves2(nums))
