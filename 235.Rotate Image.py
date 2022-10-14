# Rotate Image

matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]


def rotate(matrix) -> None:
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


rotate(matrix)
print(matrix)
