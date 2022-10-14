# Next Permutation

# Time Complexity = O(n) || Space Complexity = O(1)

nums = [1, 5, 8, 4, 7, 6, 5, 3, 1]


def nextPermutation(nums):
    j = len(nums) - 1

    for i in reversed(range(len(nums))):
        if i == 0:
            return nums.reverse()
        if nums[i] > nums[i - 1]:
            # print(nums[i - 1])
            break
    while nums[j] <= nums[i - 1]:
        j -= 1

    nums[j], nums[i - 1] = nums[i - 1], nums[j]
    nums[i:] = nums[len(nums) - 1 : i - 1 : -1]
    return nums


print(nextPermutation(nums))
