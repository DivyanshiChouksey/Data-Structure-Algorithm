# Check if Matrix Is X-Matrix
"""
    Return False if anti-diagonal and diagonal are zero
    and remaining elements are non zero value
    Otherwise return True
"""
# Time Complexity = O(n^2) || Space Complexity = O(1)
grid = [[2, 0, 0, 1], [0, 3, 1, 0], [0, 5, 2, 0], [4, 0, 0, 2]]


def checkXMatrix(grid):
    n = len(grid)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == j or (i + j) == n - 1:
                if grid[i][j] == 0:
                    return False
            else:
                if grid[i][j] != 0:
                    return False
    return True


print(checkXMatrix(grid))
