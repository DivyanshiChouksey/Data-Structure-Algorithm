# Unique Paths II
"""
    Starting it with a bruteforce approach and keep record of visited indices

    for the first row and col :- if the previous row/col value is "1" means we have path and the current value is "0"
    means we can continue the path then make current value "1" else update value by "0"

    Go through the obstacleGrid and in the each indices keep record of max paths from the
    start point to that indices(place) by adding one above indices value and one previous indices value
    and return last value
    Note :- if found any obstacle while iterating obstacleGrid then update indices value by "0"

"""
# Time Complexity = O(n^2) || Space Complexity = O(1)

obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]


def uniquePathsWithObstacles(obstacleGrid):
    if obstacleGrid[0][0] == 1:
        return 0
    obstacleGrid[0][0] = 1
    rows = len(obstacleGrid)
    cols = len(obstacleGrid[0])

    for i in range(1, rows):
        if obstacleGrid[i - 1][0] == 1 and obstacleGrid[i][0] == 0:
            obstacleGrid[i][0] = 1
        else:
            obstacleGrid[i][0] = 0

    for i in range(1, cols):
        if obstacleGrid[0][i - 1] == 1 and obstacleGrid[0][i] == 0:
            obstacleGrid[0][i] = 1
        else:
            obstacleGrid[0][i] = 0

    for i in range(1, rows):
        for j in range(1, cols):
            if obstacleGrid[i][j] == 1:
                obstacleGrid[i][j] = 0
            else:
                obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
    return obstacleGrid[-1][-1]


print(uniquePathsWithObstacles(obstacleGrid))
