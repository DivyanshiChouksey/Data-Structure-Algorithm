# Pascal's Triangle
numRow = 5
res = [[1] * i for i in range(1, numRow + 1)]
for i in range(2, numRow):
    for j in range(1, i):
        res[i][j] = res[i - 1][j - 1] + res[i - 1][j]

print(res)
