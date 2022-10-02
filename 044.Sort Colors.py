# Sort Colors

nums = [2, 0, 2, 1, 1, 0]

# Naive Solution
"""
    Go through the given array and keep record of count of '0', '1' and '2' by using dictionary 
    and go through the dictionary keys and append the keys * values that no. of time they occur in '0','1','2' order,
    and return the ans. 
"""
# Time Complexity = O(n) || Space Complexity = O(n)


def sortColors(nums):
    dct = {0: 0, 1: 0, 2: 0}
    for i in range(0, len(nums)):
        dct[nums[i]] += 1
    out = []
    for key, value in dct.items():
        out += [key] * value
    return out


print(sortColors(nums))


# Best Solution
"""
    Take three pointers - left, mid, right initially at 0, 0, len(nums)-1 respectively
    then if mid pointer value is '0' then swap it with the left pointer and increase both pointers by one 
    or if the mid pointer value is '2' then swap it with the right pointer and decrease right pointer by one
    or else just move our mid pointer by one that means we found '1' and it should be place between '0' and '2'.
    return the nums. 

"""
# Time Complexity = O(n) || Space Complexity = O(1)


def sortColors2(nums):
    low, mid, right = 0, 0, len(nums) - 1
    while mid <= right:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            mid += 1
            low += 1
        elif nums[mid] == 2:
            nums[right], nums[mid] = nums[mid], nums[right]
            right -= 1
        else:
            mid += 1
    return nums


print(sortColors2(nums))
