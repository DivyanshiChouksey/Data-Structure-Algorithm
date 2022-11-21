# Nearest Exit from Entrance in Maze

"""
    BFS with counting step and stoping condition
"""

# Time Complexity = O(m*n),         m = len(maze)
# Space Complexity = O(max(m,n)),   n = len(maze[0])


maze = [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]]
entrance = [1, 0]


def nearestExit(maze, entrance):
    r = len(maze)
    c = len(maze[0])
    x = entrance[0]
    y = entrance[1]
    cnt = 0
    queue = [entrance]
    maze[x][y] = "+"
    while queue:
        tmp = []
        for i, j in queue:
            for m, n in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= m < r and 0 <= n < c and maze[m][n] == ".":
                    if m == 0 or n == 0 or m == r - 1 or n == c - 1:
                        return cnt + 1
                    tmp.append((m, n))
                    maze[m][n] = "+"
        queue = tmp[:]
        cnt += 1

    return -1


print(nearestExit(maze, entrance))
