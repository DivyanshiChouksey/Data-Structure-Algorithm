# Climbing Stairs
"""
    use concept of fibonacci number
"""
# Time Complexity = O(n) || Space Complexity = O(1)

n = 4


def climbingStair(n):
    a = 0
    b = 1
    for i in range(n):
        next = a + b
        a = b
        b = next

    return next


print(climbingStair(n))
