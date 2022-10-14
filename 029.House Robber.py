# House Robber
"""
[7,1,1,2]
"""
# Time Complexity = O() || Space Complexity = O()

nums = [1,2,3,1]

def rob(nums):
    r1 = r2 = 0
    for n in nums:
        temp = max(r1+n , r2)
        r1 = r2
        r2 = temp
    return r2

print(rob(nums))