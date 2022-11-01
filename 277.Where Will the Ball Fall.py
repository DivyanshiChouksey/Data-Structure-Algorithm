# Where Will the Ball Fall

"""
    Explanation
    We drop the ball at grid[0][i]
    and track ball position i1, which initlized as i.
    
    An observation is that,
    if the ball wants to move from i1 to i2,
    we must have the board direction grid[j][i1] == grid[j][i2]
        
"""
# Time Complexity = O(mn) || Space Complexity = O(n)

grid = [
    [1, 1, 1, -1, -1],
    [1, 1, 1, -1, -1],
    [-1, -1, -1, 1, 1],
    [1, 1, 1, 1, -1],
    [-1, -1, -1, -1, -1],
]


def findBall(grid):
    m, n = len(grid), len(grid[0])

    def test(i):
        for j in range(m):
            i2 = i + grid[j][i]
            if i2 < 0 or i2 >= n or grid[j][i2] != grid[j][i]:
                return -1
            i = i2
        return i

    return map(test, range(n))


print(findBall(grid))
