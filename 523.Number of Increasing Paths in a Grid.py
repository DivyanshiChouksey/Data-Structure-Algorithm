# Number of Increasing Paths in a Grid

grid = [[1,1],[3,4]]

class Solution:
def countPaths( grid):
    m, n = len(grid), len(grid[0])
    mod = 10 ** 9 + 7
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    dp = [[0] * n for _ in range(m)]

    def dfs(i, j):
        # If dp[i][j] is non-zero, it means we have got the value of dfs(i, j),
        # so just return dp[i][j].
        if dp[i][j]:
            return dp[i][j]

        # Otherwise, set answer = 1, the path made of grid[i][j] itself.
        answer = 1

        # Check its four neighbor cells, if a neighbor cell grid[prevI][prevJ] has a
        # smaller value, we move to this cell and solve the subproblem: dfs(prevI, prevJ).
        for di, dj in directions:
            prev_i, prev_j = i + di, j + dj
            if 0 <= prev_i < m and 0 <= prev_j < n and grid[prev_i][prev_j] < grid[i][j]:
                answer += dfs(prev_i, prev_j) % mod

        # Update dp[i][j], so that we don't recalculate its value later.
        dp[i][j] = answer
        return answer

    # Iterate over all cells grid[i][j] and sum over dfs(i, j).
    return sum(dfs(i, j) for i in range(m) for j in range(n)) % mod
  
  
print(countPaths( grid))
