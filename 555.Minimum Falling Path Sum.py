# Minimum Falling Path Sum

matrix = [[2,1,3],[6,5,4],[7,8,9]]

def minFallingPathSum(matrix):
    for i in reversed(range(len(matrix)-1)):
        for j in range(len(matrix)):
            if j==0:
                matrix[i][j] += min(matrix[i+1][j+1],matrix[i+1][j])
            elif j==len(matrix)-1:
                matrix[i][j] += min(matrix[i+1][j],matrix[i+1][j-1])    
            else:
                matrix[i][j] += min(matrix[i+1][j+1],matrix[i+1][j],matrix[i+1][j-1])

    return (min(matrix[0]))

print(minFallingPathSum(matrix))