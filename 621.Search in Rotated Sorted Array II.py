# Search in Rotated Sorted Array II

def search(nums, target):
    if len(nums) == 0:
        return False
    l = 0
    r = len(nums)-1
    while l <= r:
        m = (l+r)//2
        if nums[m] == target:
            return True

        if nums[l] == nums[m]:
            l += 1
            continue
        # now check if val is there in first
        pivotArray = nums[l] <= nums[m]
        targetArray = nums[l] <= target
        if pivotArray ^ targetArray:
            if pivotArray:
                l = m+1
            else:
                r = m-1
        else:
            if nums[m]<target:
                l = m+1
            else:
                r = m-1
    return False

print(search(nums, target))
