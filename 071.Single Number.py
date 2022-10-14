# Single Number

# 100 ^ 100 # same bits zero diffent them 1
"""
0 0 -> 0
1 1 -> 0
1 0 -> 1
0 1 -> 1
           s
[4,1,2,1,2], x = 0
x = 000^ 100 -> 100 ^ 001 -> 101 ^ 010-> 111^001 -> 110 ^ 010 -> 100
"""

nums = [4, 2, 1, 2, 1]

# Time Complexity = O(n) || Space Complexity = O(1)
def singleNumber(nums):
    x = 0
    for num in nums:
        x ^= num
    return x


# Time Complexity = O(n) || Space Complexity = O(n)
def singleNumber1(nums):
    dct = {}
    for num in nums:
        if num in dct:
            dct[num] += 1
        else:
            dct[num] = 1

    for key, value in dct.items():
        if value == 1:
            return key


# or solution
from collections import defaultdict


def singleNumber2(nums):
    dct = defaultdict(int)
    for num in nums:
        dct[num] += 1

    for key, value in dct.items():
        if value == 1:
            return key


print(singleNumber(nums))
print(singleNumber1(nums))
print(singleNumber2(nums))
