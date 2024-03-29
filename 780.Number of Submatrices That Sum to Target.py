# Number of Submatrices That Sum to Target

from collections import defaultdict

matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0

def numSubmatrixSumTarget(matrix, target):
    m, n = len(matrix), len(matrix[0])
    for x in range(m):
        for y in range(1, n):
            matrix[x][y] += matrix[x][y-1]
    # print(matrix)
    res = 0
    for i in range(n):
        for j in range(i, n):
            c = defaultdict(int)
            cur, c[0] = 0, 1
            for k in range(m):
                cur += matrix[k][j] - (matrix[k][i - 1] if i > 0 else 0)
                res += c[cur - target]
                c[cur] += 1
    return (res)


print(numSubmatrixSumTarget(matrix, target))
