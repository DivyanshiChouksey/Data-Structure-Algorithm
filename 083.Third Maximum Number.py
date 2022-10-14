# Third Maximum Number
nums = [2, 2, 3, 1]


def thirdMax(nums):
    first, sec, third = float("-inf"), float("-inf"), float("-inf")
    for i in range(len(nums)):
        if nums[i] not in [first, sec, third]:
            if nums[i] > first:
                third = sec
                sec = first
                first = nums[i]
            elif nums[i] > sec:
                third = sec
                sec = nums[i]
            elif nums[i] > third:
                third = nums[i]
    if third == float("-inf"):
        return first
    return third


def thirdMax2(nums):
    arr = [float("-inf"), float("-inf"), float("-inf")]
    for num in nums:
        if num >= arr[0]:
            arr = [num, arr[0], arr[1]]
        elif num >= arr[1]:
            arr = [arr[0], num, arr[1]]
        elif num >= arr[2]:
            arr = [arr[0], arr[1], num]
    if arr[2] == float("-inf"):
        return arr[0]
    return arr[2]


print(thirdMax(nums))

print(thirdMax2(nums))
