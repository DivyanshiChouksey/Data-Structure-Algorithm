# Number of Closed Islands

# Time Complexity = O(n) || Space Complexity = O(1)

def closedIsland(self, grid: List[List[int]]) -> int:
    r =len(grid)
    c = len(grid[0])
    ans = 0
    def dfs(i,j):
        if  0<=i<r and 0<=j<c and grid[i][j]==0 :
            grid[i][j] = 1
            dfs(i-1,j)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i,j+1)

    for i in range(c):
        if grid[0][i] == 0:
            dfs(0,i)
        if grid[r-1][i] == 0:
            dfs(r-1,i)  
    print(grid)

    for i in range(r):
        if grid[i][0] == 0:
            dfs(i,0)
        if grid[i][c-1] == 0:
            dfs(i,c-1)  

    for i in range(r):
        for j in range(c):
            if grid[i][j] ==0:
                dfs(i,j)
                ans+=1

    return ans
