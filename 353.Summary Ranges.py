# Summary Ranges

"""
    Take a pointer and go through the array and find while next element is in array 
    then increase the pointer and range after that if not then append the range start -> range end in the ans 
    and if start and end are equal then only append the start after that return the ans.

"""

# Time Complexity = O() || Space Complexity = O()

nums = [0, 1, 2, 4, 5, 7]


def summaryRanges(nums):
    ans = []
    i = 0
    while i < len(nums):
        start = nums[i]
        end = nums[i]
        while nums[i] + 1 in nums:
            end = nums[i] + 1
            i += 1
        if start != end:
            ans.append(str(start) + "->" + str(end))
        else:
            ans.append(str(start))
        i += 1
    return ans


print(summaryRanges(nums))
