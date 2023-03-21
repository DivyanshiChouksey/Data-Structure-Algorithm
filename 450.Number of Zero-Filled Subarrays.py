# Number of Zero-Filled Subarrays

nums = [0,0,0,2,0,0]

"""
    Naive Solution
    by using sliding window count the number of consecutive zero then add (n*n+1//2 ) 
    to our ans where n = count for the subset count and make count = 0 then repeat this
    return ans 

"""
# Time Complexity - O(n) || Space Complexity - O(1)

def zeroFilledSubarray(nums):
    ans = 0
    i = 0
    j = 0
    while i<len(nums):
        while j<len(nums) and nums[j]==0:
            j+=1
        ans += (j-i)*(j-i+1)//2
        j+=1
        i=j
    return ans


"""
    Optimized Solution
    Using hashmap but in a optimized way
    for every zero add prev and cur count record to our ans and at the end return the ans
    example :- 
        [0,0,0,2,0,0]
         1 3 6 0 1 3
         1 3 6 0 1 3
         count = 2
         prev + count
         no need of dp we only need 2 variables prev and count 

"""
# Time Complexity - O(n) || Space Complexity - O(1)


def zeroFilledSubarray2(nums):
    ans = 0
    count = 0
    for num in nums:
        if num==0:
            count+=1
        else:
            count=0
        ans+=count
    return ans


print(zeroFilledSubarray(nums))

print(zeroFilledSubarray2(nums))
