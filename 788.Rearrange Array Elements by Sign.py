# Rearrange Array Elements by Sign

nums = [3,1,-2,-5,2,-4]

def rearrangeArray(nums):
    pos = []
    neg = []
    for num in nums:
        if num<0:
            neg.append(num)
        else:
            pos.append(num)
    m=0
    n=0
    for i in range(len(nums)):
        if i%2 == 0:
            nums[i] = pos[m]
            m+=1
        else:
            nums[i] = neg[n]
            n+=1

    return nums

print(rearrangeArray(nums))
