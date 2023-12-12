# Maximum Product of Two Elements in an Array

nums = [1,5,4,5]

def maxProduct(nums):
    a = 0
    b = 0 
    for num in nums:
        if num > a:
            b = a
            a = num
        else:
            b = max(b,num)
        
    return (a-1)*(b-1)


print(maxProduct(nums))
