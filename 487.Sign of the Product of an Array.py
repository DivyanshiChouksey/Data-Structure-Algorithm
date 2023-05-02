# Sign of the Product of an Array

nums = [-1,-2,-3,-4,3,2,1]

def arraySign(nums):
    x = 1
    for n in nums:
        if n==0:
            return 0
        if n<0:
            x*=-1
    return x
  
print(arraySign(nums))
