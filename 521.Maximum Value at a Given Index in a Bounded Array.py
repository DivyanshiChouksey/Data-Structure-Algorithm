# Maximum Value at a Given Index in a Bounded Array

n = 4
index = 2
maxSum = 6


def getSum(index, value, n):
    count = 0
    
    # On index's left:
    # If value > index, there are index + 1 numbers in the arithmetic sequence:
    # [value - index, ..., value - 1, value].
    # Otherwise, there are value numbers in the arithmetic sequence:
    # [1, 2, ..., value - 1, value], plus a sequence of length (index - value + 1) of 1s. 
    if value > index:
        count += (value + value - index) * (index + 1) // 2
    else:
        count += (value + 1) * value // 2 + index - value + 1
    
    # On index's right:
    # If value >= n - index, there are n - index numbers in the arithmetic sequence:
    # [value, value - 1, ..., value - n + 1 + index].
    # Otherwise, there are value numbers in the arithmetic sequence:
    # [value, value - 1, ..., 1], plus a sequence of length (n - index - value) of 1s. 
    if value >= n - index:
        count += (value + value - n + 1 + index) * (n - index) // 2
    else:
        count += (value + 1) * value // 2 + n - index - value
    
    return count - value

def maxValue(n, index, maxSum):
    left, right = 1, maxSum
    while left < right:
        mid = (left + right + 1) // 2
        if getSum(index, mid, n) <= maxSum:
            left = mid
        else:
            right = mid - 1
    
    return left


print(maxValue(n, index, maxSum))