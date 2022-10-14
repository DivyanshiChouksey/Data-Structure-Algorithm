# River Sizes

matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0],
]


"""

"""
# Time Complexity = O(n) || Space Complexity = O()


def riverSizes(matrix):
    sizes = []
    visited = [[False for value in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if visited[i][j]:
                continue
            traverseNode(i, j, matrix, visited, sizes)
    return sizes


def traverseNode(i, j, matrix, visited, sizes):
    riverSize = 0
    nodes = [[i, j]]
    while len(nodes):
        cur = nodes.pop()
        i = cur[0]
        j = cur[1]
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        riverSize += 1
        unvisited = getUnvisitedNeighbors(i, j, matrix, visited)
        for neighbor in unvisited:
            nodes.append(neighbor)
    if riverSize > 0:
        sizes.append(riverSize)


def getUnvisitedNeighbors(i, j, matrix, visited):
    unvisited = []
    if i > 0 and not visited[i - 1][j]:
        unvisited.append([i - 1, j])
    if i < len(matrix) - 1 and not visited[i + 1][j]:
        unvisited.append([i + 1, j])
    if j > 0 and not visited[i][j - 1]:
        unvisited.append([i, j - 1])
    if j < len(matrix[0]) - 1 and not visited[i][j + 1]:
        unvisited.append([i, j + 1])
    return unvisited


def riverSizes2(matrix):
    ans = []
    visited = set()
    r, c = len(matrix), len(matrix[0])
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 1 and (i, j) not in visited:
                size = 1
                queue = [(i, j)]
                visited.add((i, j))
                while queue:
                    tmp = []
                    for m, n in queue:  # [(0,0),(5,2))]
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


print(riverSizes(matrix))
print(riverSizes2(matrix))
