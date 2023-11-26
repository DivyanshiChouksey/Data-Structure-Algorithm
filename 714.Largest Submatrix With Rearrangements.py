# Largest Submatrix With Rearrangements


def largestSubmatrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    ans = 0 

    for row in range(m):
        for col in range(n):
            if matrix[row][col] != 0 and row > 0:
                matrix[row][col] += matrix[row - 1][col]

        curr_row = sorted(matrix[row], reverse=True)
        for i in range(n):
            ans = max(ans, curr_row[i] * (i + 1))

    return ans
        
# def largestSubmatrix(matrix):
#     m = len(matrix)
#     n = len(matrix[0])
#     prev_heights = []
#     ans = 0

#     for row in range(m):
#         heights = []
#         seen = [False] * n
        
#         for height, col in prev_heights:
#             if matrix[row][col] == 1:
#                 heights.append((height + 1, col))
#                 seen[col] = True

#         for col in range(n):
#             if seen[col] == False and matrix[row][col] == 1:
#                 heights.append((1, col))
        
#         for i in range(len(heights)):
#             ans = max(ans, heights[i][0] * (i + 1))
            
#         prev_heights = heights

#     return ans


matrix = [[0,0,1],[1,1,1],[1,0,1]]

print(largestSubmatrix(matrix))