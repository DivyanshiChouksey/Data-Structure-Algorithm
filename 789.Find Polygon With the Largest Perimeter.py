# Find Polygon With the Largest Perimeter

nums = [1,12,1,2,5,50,3]

def largestPerimeter(nums):
    nums.sort()
  
    ans = -1
    sums = 0
    for i in range(len(nums)):
        if sums > nums[i]:
            ans = sums+nums[i]
        sums+=nums[i]

    return ans


print( largestPerimeter(nums))
