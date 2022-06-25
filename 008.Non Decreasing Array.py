# Non Decreasing Array
"""
    we want to find which value is has to be change
    the current value or the previous one ,
    so that our count remain minimum
"""
# Time Complexity = O(n) || Space Complexity = O(1)

nums = [3,4,2,3]
def checkPossibility(nums):
    count = 0
    for i in range(1,len(nums)):
        if nums[i-1]>nums[i]:
            if i < 2 or nums[i] >= nums[i-2]:    #[2,0,1] , [1,7,4,8]
                nums[i-1] = nums[i]              #[0,0,1] , [1,4,4,8]
            else:
                nums[i] = nums[i-1]
            count += 1
            break

    for i in range(1,len(nums)):
        if nums[i-1]>nums[i]:
            return False
    return True

print(checkPossibility(nums))