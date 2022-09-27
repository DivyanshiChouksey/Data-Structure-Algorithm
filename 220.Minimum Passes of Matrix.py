# Minimum Passes of Matrix

"""
    We have to traverse matrix and have to make some changes at the same level so we use graphs  
    Here we keep record of positive numbers using queue
    and then start from all positive numbers one by one and check their neighbors and if they are negative then make it positive 
    and keep record of neighbors also so that we can further check through that neighbors and repeat these steps 
    until all the negative numbers converted into positive numbers 
    and return number of repeations of these steps 
"""

# Time Complexity = O(n*m) ,  n = len(matrix)
# Space Complexity = O(n*m) , m = len(matrix[0])

matrix = [[0, -1, -3, 2, 0], [1, -2, -5, -1, -3], [3, 0, 0, -4, -1]]


def minimumPassesOfMatrix(matrix):
    time = 0
    negative = 0
    queue = []
    r = len(matrix)
    c = len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] < 0:
                negative += 1
            elif matrix[i][j] > 0:
                queue.append((i, j))

    while queue and negative:
        tmp = []
        for i, j in queue:
            for m, n in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= m and m < r and 0 <= n and n < c and matrix[m][n] < 0:
                    tmp.append((m, n))
                    matrix[m][n] = -1 * (matrix[m][n])
                    negative -= 1
        queue = tmp[:]
        time += 1

    if negative == 0:
        return time
    return -1


print(minimumPassesOfMatrix(matrix))
