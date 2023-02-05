# Minimum Sum of Four Digit Number After Splitting Digits

"""
    For the minimum sum of digit, sort the given integer and return (int(nums[0]+nums[2]) + int(nums[1]+nums[3]))
    2932 -> 2,2,3,9 
    23+29 = 52 return 
"""

# Time Complexity = O(1) || Space Complexity = O(1) 
# n = 4 fixed  

num = 2932

def minimumSum(num):
    nums = list(str(num))
    nums.sort()
    return (int(nums[0]+nums[2]) + int(nums[1]+nums[3]))

print(minimumSum(num))