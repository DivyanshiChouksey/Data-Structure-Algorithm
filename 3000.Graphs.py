# River Sizes

matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0],
]


def riverSize(matrix):
    ans = []
    visited = set()
    r, c = len(matrix), len(matrix[0])
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 1 and (i, j) not in visited:
                size = 1
                visited.add((i, j))
                queue = [(i, j)]
                while queue:
                    tmp = []
                    for m, n in queue:
                        for x, y in [(m + 1, n), (m - 1, n), (m, n + 1), (m, n - 1)]:
                            if (
                                0 <= x < r
                                and 0 <= y < c
                                and matrix[x][y] == 1
                                and (x, y) not in visited
                            ):
                                tmp.append((x, y))
                                size += 1
                                visited.add((x, y))
                    queue = tmp[:]
                ans.append(size)
    return ans


print(riverSize(matrix))
