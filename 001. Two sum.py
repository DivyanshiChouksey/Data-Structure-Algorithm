# Two Sum
nums = [2,7,11,15]
target = 9


# Naive solution
"""
    using a nested loop and going to every element and checking the sum
"""
# Time Complexity = O(n^2) || Space Complexity = O(1)
def twoSum(nums, target) :
    for i in range(len(nums)):
        for j in range(1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]



# Effective Solution
"""
    here we are going to do is sorting
    so we sort the array and then make 2 pointer
    So we just perform a sum and get the desired output
"""
# Time Complexity = O(nlogn) || Space Complexity = O(1)
def twoSum2(nums, target) :
    i = 0
    j = len(nums)-1
    while i<j:
        if nums[i] + nums[j] == target:
            return [i,j]
        elif nums[i] + nums[j] > target:
            j-=1
        else:
            i+=1



# Best Solution
"""
    we are using hashmap ,starting with an empty hashmap
    if we got the desired value in our hashmap then we return the index value otherwise
    add the value in our hashmap
"""
# Time Complexity = O(n) || Space Complexity = O(n)
def twoSum3(nums, target) :
    dct = {}
    for i,num in enumerate(nums) :
        if num in dct:
            return ([dct[num],i])
        else:
            dct[target-num] = i 



print(twoSum(nums,target))
print(twoSum2(nums, target))  
print(twoSum3(nums, target))