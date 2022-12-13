# Minimum Falling Path Sum

# Time Complexity = O(n*2) || Space Complexity = O(1)

matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]


def minFallingPathSum(matrix):
    for i in range(1, len(matrix)):
        for j in range(len(matrix[0])):
            if j == 0:
                matrix[i][j] = min(
                    matrix[i][j] + matrix[i - 1][j],
                    matrix[i][j] + matrix[i - 1][j + 1],
                )
            elif j == len(matrix[0]) - 1:
                matrix[i][j] = min(
                    matrix[i][j] + matrix[i - 1][j - 1], matrix[i][j] + matrix[i - 1][j]
                )
            else:
                matrix[i][j] = min(
                    matrix[i][j] + matrix[i - 1][j - 1],
                    matrix[i][j] + matrix[i - 1][j],
                    matrix[i][j] + matrix[i - 1][j + 1],
                )
    return min(matrix[-1])


print(minFallingPathSum(matrix))
