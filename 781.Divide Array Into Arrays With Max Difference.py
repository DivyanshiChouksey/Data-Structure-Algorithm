# Divide Array Into Arrays With Max Difference

nums = [1,3,4,8,7,9,3,5,1]
k = 2

def divideArray(nums, k):
    size = len(nums)
    if size % 3 != 0:
        return []

    nums.sort()

    result = []
    group_index = 0
    for i in range(0, size, 3):
        if i + 2 < size and nums[i + 2] - nums[i] <= k:
            result.append([nums[i], nums[i + 1], nums[i + 2]])
            group_index += 1
        else:
            return []
    return result


print(divideArray(nums, k))
