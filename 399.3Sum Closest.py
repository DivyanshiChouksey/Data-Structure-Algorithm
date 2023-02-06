# 3Sum Closest

"""
    The approach is same as 3SUM, only for optimization skip the adjacent duplicate values
    and keep the record for the closest value from target by checking and updating mininum absolute
    value of currentSum minus target and return it.
"""

# Time Complexity = O(n^2) || Space Complexity = O(1)

num = [-1,2,1,-4]
target = 1


def threeSumClosest(num, target):
    num.sort()
    result = num[0] + num[1] + num[2]
    for i in range(len(num) - 2):
        if i > 0 and num[i] == num[i-1]:    # here we skip if the number on index i appears before
            continue
        j, k = i+1, len(num) - 1
        while j < k:
            sum = num[i] + num[j] + num[k]
            if sum == target:
                return sum
            if abs(sum - target) < abs(result - target):
                result = sum
            if sum < target:
                j += 1
            else:
                k -= 1            
    return result


print(threeSumClosest(num, target)) 