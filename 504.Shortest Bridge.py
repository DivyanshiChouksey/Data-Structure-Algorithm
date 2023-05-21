# Shortest Bridge

grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
"""
  [[1,1,1,1,1]
   [1,0,0,0,1]
   [1,0,1,0,1]
   [1,0,0,0,1]
   [1,1,1,1,1]]
"""
# dfs then  bfs

def shortestBridge( grid):
    n = len(grid)
    visited = set()

    def dfs(x,y):
        if 0<=x<n and 0<=y<n and (x,y) not in visited:
            if grid[x][y]==1:
                visited.add((x,y))
                return dfs(x-1,y),dfs(x+1,y),dfs(x,y-1),dfs(x,y+1)

    def bfs():
        ans = 0
        queue = deque(visited)

        while queue:
            for _ in range(len(queue)):
                i,j = queue.popleft()
                for x,y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                    if 0<=x<n and 0<=y<n and (x,y) not in visited :

                        if grid[x][y] == 1:
                            return ans
                        visited.add((x,y))
                        queue.append((x,y))
            ans+=1
        return ans

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                dfs(i,j)
                return bfs()
