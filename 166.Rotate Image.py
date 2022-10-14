# 48. Rotate Image

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


l = 0
r = len(matrix) - 1

while l < r:
    top = l
    bottom = r
    for i in range(r - l):
        tmp = matrix[top][l + i]
        matrix[top][l + i] = matrix[bottom - i][l]
        matrix[bottom - i][l] = matrix[bottom][r - i]
        matrix[bottom][r - i] = matrix[top + i][r]
        matrix[top + i][r] = tmp
    l += 1
    r -= 1

print(matrix)
