# Find the Score of All Prefixes of an Array

nums = [2,3,7,5,10]

def findPrefixScore( nums):
    conver = [0 for i in range(len(nums))]
    tmp=0
    for i in range(len(nums)):
        tmp= max(tmp,nums[i])
        conver[i] = nums[i] + tmp + conver[i-1]

    return conver
  
 print(findPrefixScore( nums)
