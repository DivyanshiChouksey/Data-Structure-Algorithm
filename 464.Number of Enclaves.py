# Number of Enclaves

# Time Complexity = O(m*n) || Space Complexity = O(1)

grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]

def numEnclaves(grid):
    r = len(grid)
    c = len(grid[0])
    def dfs(i,j):
        if 0<=i<r and 0<=j<c and grid[i][j]==1:
            grid[i][j]=2
            return 1+dfs(i+1,j) + dfs(i-1,j) + dfs(i,j+1)+ dfs(i,j-1)
        return 0
    
    count=0

    for i in range(c):
        if grid[0][i]==1:
            dfs(0,i)
        if grid[r-1][i]==1:
            dfs(r-1,i)
        
    for i in range(r):
        if grid[i][0]==1:
            dfs(i,0)
        if grid[i][c-1]==1:
            dfs(i,c-1)

    for i in range(r):
        for j in range(c):
            if grid[i][j]==1:
                count+=dfs(i,j)

    return count 


print(numEnclaves(grid))
