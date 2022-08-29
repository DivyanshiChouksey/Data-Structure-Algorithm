# Next Permutation
"""
    For edge case if all elements are in decreasing order -> return reverse array
    else loop from back of array and find first out of order element after then 
    from that element goto right side and find first greater element
    then swap it and then reverse the array from where we swapped and return it.
"""
# Time Complexity = O(n) || Space Complexity = O(1)

nums = [1, 5, 8, 4, 7, 6, 5, 3, 1]


def nextPermutation(nums):
    j = len(nums) - 1

    # find first decreasing elemnt
    for i in reversed(range(len(nums))):
        if i == 0:
            return nums.reverse()
        if nums[i] > nums[i - 1]:
            # print(nums[i - 1])
            break

    # find first greater element to right of i
    while nums[j] <= nums[i - 1]:
        j -= 1
    # print(nums[j])

    nums[j], nums[i - 1] = nums[i - 1], nums[j]
    nums[i:] = nums[len(nums) - 1 : i - 1 : -1]
    return nums


print(nextPermutation(nums))
