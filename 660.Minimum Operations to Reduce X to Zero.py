# Minimum Operations to Reduce X to Zero


nums = [3,2,20,1,1,3]
x = 10

def minOperations(nums,x):
    target = sum(nums)-x
    ans = tmp = 0
    i=j=0
    flag = False
    
    while j<len(nums):
        tmp +=nums[j]
        while i<=j and tmp > target :
            tmp -= nums[i]
            i+=1   
        
        if tmp == target:
            flag = True
            ans = max(ans,(j-i+1))               
        j+=1
        
    return len(nums)-ans if flag else -1


print(minOperations(nums,x))
