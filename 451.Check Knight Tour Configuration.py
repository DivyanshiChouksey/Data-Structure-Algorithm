# Check Knight Tour Configuration

# Time Complexity = O(n*n) || Space Complexity = O(1) 

grid = [[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]

def checkValidGrid(grid):
    if grid[0][0]!=0:
        return False
    n = len(grid)
    visit = n*n
    x = 0
    y = 0
    for t in range(visit-1): # if n=5 check only till 23
        notFound = True     # t+1 found or not 
        for i,j in [(x+2,y+1),(x+2,y-1),(x-2,y+1),(x-2,y-1),(x+1,y+2),(x+1,y-2),(x-1,y+2),(x-1,y-2)]:
            if 0<=i<n and 0<=j<n and grid[i][j]==t+1:
                x=i
                y=j
                notFound = False
                break
        if notFound:
            return False
    return True

print(checkValidGrid(grid))