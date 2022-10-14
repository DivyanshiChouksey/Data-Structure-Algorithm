# Maximum Sum Submatrix

matrix = [[5, 3, -1, 5], [-7, 3, 7, 4], [12, 8, 0, 0], [1, -8, -8, 2]]
size = 2


def maximumSumSubmatrix(matrix, size):
    sums = creatSumMatrix(matrix)
    maxSubMatrix = float("-inf")

    for i in range(size - 1, len(matrix)):
        for j in range(size - 1, len(matrix[0])):
            total = sums[i][j]

            touchesTopBorder = i - size < 0
            if not touchesTopBorder:
                total -= sums[i - size][j]

            touchesLeftBorder = j - size < 0
            if not touchesLeftBorder:
                total -= sums[i][j - size]

            touches = touchesTopBorder or touchesLeftBorder
            if not touches:
                total += sums[i - size][j - size]

            maxSubMatrix = max(maxSubMatrix, total)

    return maxSubMatrix


def creatSumMatrix(matrix):
    sums = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    sums[0][0] = matrix[0][0]

    for i in range(1, len(matrix[0])):
        sums[0][i] = sums[0][i - 1] + matrix[0][i]

    for j in range(1, len(matrix)):
        sums[j][0] = sums[j - 1][0] + matrix[j][0]

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            sums[i][j] = (
                sums[i - 1][j] + sums[i][j - 1] - sums[i - 1][j - 1] + matrix[i][j]
            )

    return sums


print(maximumSumSubmatrix(matrix, size))
