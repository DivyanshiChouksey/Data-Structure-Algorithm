# Move Zeroes
"""
    instead of moving zeroes to the end of array
    move non-zeroes elements to the beginning of the array 
    this will maintain the relative order of the non-zero elements.
"""
# Time Complexity = O(n) || Space Complexity = O(1)

nums = [0,1,0,3,12]

def moveZeroes(nums):
    k = 0
    for i in range(len(nums)):
        if nums[i]:
            nums[k] , nums[i] = nums[i] , nums[k]
            k += 1
  
moveZeroes(nums)
print(nums)