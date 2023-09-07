# Remove Element

nums = [0,1,2,2,3,0,4,2], val = 2

def removeElement(nums, val):
    idx = 0
    for i in range(len(nums)):
        if nums[i]!=val:
            nums[idx] = nums[i]
            idx+=1
    print(nums)
    return idx 

print(removeElement(nums, val))
