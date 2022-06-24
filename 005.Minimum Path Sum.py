# Minimum Path Sum 
"""
    instead of checking path sum many times
    we modify value by adding its previous value in it
    and for diagonals value we take the minimum of its row-1 and column-1 values
    then add  it in the current value
"""
# Time Complexity = O(m*n) || Space Complexity = O(1)

grid = [[1,3,1],[1,5,1],[4,2,1]]
def minPathsum(grid):
    for i in range(1,len(grid[0])):
        grid[0][i] += grid[0][i-1]

    for i in range(1,len(grid)):
        grid[i][0] += grid[i-1][0]

    for i in range(1,len(grid[0])):
        for j in range (1,len(grid)):
            grid[i][j] += min(grid[i-1][j] , grid[i][j-1])

    return grid[-1][-1]

print(minPathsum(grid))