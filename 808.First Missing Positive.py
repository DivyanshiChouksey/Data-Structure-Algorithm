# First Missing Positive

 nums = [3,4,-1,1]

def firstMissingPositive(self, nums: List[int]) -> int:
    for i, v in enumerate(nums):
        while 0 < v <= i and nums[v-1] != v:
            nums[v-1], nums[i] = nums[i], nums[v-1]
            v = nums[i]
    for i, v in enumerate(nums):
        if v != i+1:
            return i+1
    return len(nums) + 1


print(firstMissingPositive(nums))
