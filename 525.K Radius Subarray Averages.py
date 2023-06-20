# K Radius Subarray Averages

nums = [7,4,3,9,1,8,5,2,6]
k = 3

def getAverages(nums, k):
    ans = [-1]*len(nums)
    if k==0:
        return nums
    if ((2*k)+1)>len(nums):
        return ans

    window = sum(nums[:((2*k)+1)])
    ans[k] = window//((2*k)+1)

    for i in range(((2*k)+1),len(nums)):
        window = window - nums[i - (2 * k + 1)] + nums[i]
        ans[i - k] = window // (2 * k + 1)
    return ans

print( getAverages(nums, k))
