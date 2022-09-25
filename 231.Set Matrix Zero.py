# Set Matrix Zero

# Naive Solution
"""
    Make a separate record of the row and cols where we have found zeroes
    and then go through the recorded rows and cols and update them with zeros
"""
# Time Complexity = O(n*m),  n = len(matrix)
# Space Complexity = O(n+m)  m = len(matrix[0])
matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]


def setZeroes(matrix):
    R = len(matrix)
    C = len(matrix[0])
    rows, cols = set(), set()

    for i in range(R):
        for j in range(C):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    for i in range(R):
        for j in range(C):
            if i in rows or j in cols:
                matrix[i][j] = 0


setZeroes(matrix)
print(matrix)


# Optimal Solution
"""
    Instead of keeping the record separately replace the first row and first col 
    of that place with the zeroes and after that replace all required places
    by the refrence of first row and first col 
"""
# Time Complexity = O(n*m) || Space Complexity = O(1)

matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]


def setZeroes2(matrix):
    is_col = False
    R = len(matrix)
    C = len(matrix[0])
    for i in range(R):
        if matrix[i][0] == 0:
            is_col = True
        for j in range(1, C):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0
    for i in range(1, R):
        for j in range(1, C):
            if not matrix[i][0] or not matrix[0][j]:
                matrix[i][j] = 0

    if matrix[0][0] == 0:
        for j in range(C):
            matrix[0][j] = 0
    if is_col:
        for i in range(R):
            matrix[i][0] = 0


setZeroes2(matrix)
print(matrix)
