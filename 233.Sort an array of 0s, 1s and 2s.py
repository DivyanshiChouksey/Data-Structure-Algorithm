# Sort an array of 0s, 1s and 2s

nums = [2, 0, 2, 1, 1, 0]


def sortColors(nums):
    left, mid, right = 0, 0, len(nums) - 1
    while mid <= right:
        if nums[mid] == 0:
            nums[left], nums[mid] = nums[mid], nums[left]
            mid += 1
            left += 1
        elif nums[mid] == 2:
            nums[right], nums[mid] = nums[mid], nums[right]
            right -= 1
        else:
            mid += 1


sortColors(nums)
print(nums)
