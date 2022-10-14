# Sqrt(x)
"""

"""
# Time Complexity = O() || Space Complexity = O()
x = 8


def mySqrt(x):
    l, r = 0, x
    while l <= r:
        mid = (l + r) // 2
        if mid * mid <= x < (mid + 1) * (mid + 1):
            return mid
        elif x < mid * mid:
            r = mid - 1
        else:
            l = mid + 1


print(mySqrt(x))
