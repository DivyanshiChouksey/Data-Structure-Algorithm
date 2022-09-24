# Rotting Oranges

"""
    We have to traverse matrix and have to make some changes at the same level so we use graphs  
    Here we keep record of fresh Oranges 
    and then start from all rotten oranges and check the neighbors of it and if they are freshs then make it rotten 
    and keep record of neighbors also so that we can further check through that neighbors and repeat these steps 
    until all the fresh Oranges converted into rotten oranges.
"""

# Time Complexity = O(m*n) || Space Complexity = O(m*n)

grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]


def orangesRotting(grid):
    r = len(grid)
    c = len(grid[0])
    time = 0
    queue = []
    freshOrange = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1:
                freshOrange += 1
            elif grid[i][j] == 2:
                queue.append((i, j))

    while queue and freshOrange:
        tmp = []
        for i, j in queue:
            for m, n in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= m < r and 0 <= n < c and grid[m][n] == 1:
                    grid[m][n] = 2
                    freshOrange -= 1
                    tmp.append((m, n))

        queue = tmp[:]
        time += 1

    return time if freshOrange == 0 else -1


print(orangesRotting(grid))
