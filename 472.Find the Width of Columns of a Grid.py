# Find the Width of Columns of a Grid

grid = [[-15,1,3],[15,7,12],[5,6,-2]]

def findColumnWidth(grid):
    ans = []
    for i in range(len(grid[0])):
        tmp = 0
        for j in range(len(grid)):
            tmp = max(tmp,len(str(grid[j][i])))
        ans.append(tmp)
    return ans
  
print(findColumnWidth(grid))
