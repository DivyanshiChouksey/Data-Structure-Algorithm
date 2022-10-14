grid = [
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
]

"""
So we are givin grid so we have to apply a DFS and then keep record of all
visited elements which will take n space or we can replace all visited islands by 0
"""
seen = set()
ans = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 1 and (i, j) not in seen:
            shape = 0  # current area
            stack = [(i, j)]
            seen.add((i, j))
            while stack:
                r, c = stack.pop()  # 0,1
                shape += 1
                for nr, nc in (
                    (r - 1, c),
                    (r + 1, c),
                    (r, c - 1),
                    (r, c + 1),
                ):  # -1,1- 1,1- 0,0- 0,2
                    if (
                        0 <= nr < len(grid)
                        and 0 <= nc < len(grid[0])
                        and grid[nr][nc] == 1
                        and (nr, nc) not in seen
                    ):
                        stack.append((nr, nc))
                        seen.add((nr, nc))
            ans = max(ans, shape)
print(ans)

# def dfs(i, j):
#     if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] == 0:
#         return 0
#     grid[i][j] = 0
#     return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j - 1) + dfs(i, j + 1)


# ans = 0
# for i in range(len(grid)):
#     for j in range(len(grid[0])):
#         if grid[i][j]:
#             ans = max(ans, dfs(i, j))

# print(ans)
