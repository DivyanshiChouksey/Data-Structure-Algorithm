matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30],
]
target = 15


def Search(matrix, target):
    i = len(matrix) - 1
    j = 0
    while i >= 0 and j < len(matrix):
        if matrix[i][j] == target:
            return [i, j]
        elif matrix[i][j] > target:
            i -= 1
        else:
            j += 1
    return [-1, -1]


print(Search(matrix, target))
