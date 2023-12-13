# Special Positions in a Binary Matrix

mat = [[1,0,0],[0,0,1],[1,0,0]]


def numSpecial(mat):
    m = len(mat)
    n = len(mat[0])
    row_count = [0] * m
    col_count = [0] * n
    
    for row in range(m):
        for col in range(n):
            if mat[row][col] == 1:
                row_count[row] += 1
                col_count[col] += 1
    
    ans = 0
    for row in range(m):
        for col in range(n):
            if mat[row][col] == 1:
                if row_count[row] == 1 and col_count[col] == 1:
                    ans += 1

    return ans


print(numSpecial(mat))
