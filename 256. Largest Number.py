#  Largest Number

nums = [3, 30, 34, 5, 9]

def largestNumber(nums) -> str:
    def greaterOrEqual(digit, maxDigit):
        return int(str(digit) + str(maxDigit)) >= int(str(maxDigit) + str(digit))
    
    ans = []
    while nums!=[]:
        maxDigit = 0
        for num in nums:
            if greaterOrEqual(num,maxDigit):
                maxDigit = num
        ans.append(str(maxDigit))
        nums.remove(maxDigit)

    while  
    return "".join(ans)