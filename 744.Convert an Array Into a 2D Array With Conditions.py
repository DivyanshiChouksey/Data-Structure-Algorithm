# Convert an Array Into a 2D Array With Conditions

from collections import Counter

nums = [1,3,4,1,2,3,1]

def findMatrix(nums):
    cnt = Counter(nums)
    ans = []
    n = max(cnt.values())
    for i in range(n):
        tmp = []
        for k,v in cnt.items():
            if cnt[k]:

                tmp.append(k)
                cnt[k]-=1
        ans.append(tmp)
    return ans

print(findMatrix(nums))
