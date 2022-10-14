# Find All Numbers Disappeared In a Array
"""
"""
# Time Complexity = O() || Space Complexity = O()

nums = [4,3,2,7,8,2,3,1]

def disappearedNum(nums):
    lst = []
    nums.sort()
    i = 1
    idx = 0
    while idx < len(nums) :
        if i == nums[idx]:
            i += 1
            idx += 1
        elif nums[idx] == nums[idx - 1]:
            idx += 1
        else:
            lst.append(i)
            i += 1
    return lst

print(disappearedNum(nums))