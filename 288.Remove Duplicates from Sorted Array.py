# Remove Duplicates from Sorted Array

nums = [1, 1, 2]

# Time Complexity = O(n) || Space Complexity = O(1)


def removeDuplicates(nums) -> int:
    size = len(nums)
    insertIndex = 1
    for i in range(1, size):
        # Found unique element
        if nums[i - 1] != nums[i]:
            # Updating insertIndex in our main array
            nums[insertIndex] = nums[i]
            # Incrementing insertIndex count by 1
            insertIndex = insertIndex + 1
    return insertIndex


print(removeDuplicates(nums))
