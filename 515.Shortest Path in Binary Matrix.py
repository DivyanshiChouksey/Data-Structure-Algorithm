# Shortest Path in Binary Matrix

from collections import deque

grid = [[0,0,0],[1,1,0],[1,1,0]]

def shortestPathBinaryMatrix(grid):
    if grid[0][0]:
        return -1
    n = len(grid)
    queue = deque([(0,0)])
    d = 1
    while queue:
        for _ in range(len(queue)):
            i,j = queue.popleft()
            if i == n-1 and j == n-1 :
                return d
            for x,y in [(i+1,j+1),(i-1,j-1),(i+1,j),(i,j+1),(i-1,j),(i,j-1),(i+1,j-1),(i-1,j+1)]:
                if 0<=x<n and 0<=y<n and grid[x][y]==0:
                    grid[x][y] = 1
                    queue.append((x,y))
        d+=1
    return -1

print(shortestPathBinaryMatrix(grid))