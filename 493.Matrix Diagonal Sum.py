# Matrix Diagonal Sum

mat = [[1,1,1,1],
       [1,1,1,1],
       [1,1,1,1],
       [1,1,1,1]]


def diagonalSum(mat):
    ans=0
    n= len(mat)
    for i in range(n):
        ans+=(mat[i][i] + mat[i][n-1-i])  
    if n%2!=0:
        ans-=mat[n//2][n//2]
    return ans
  
print(diagonalSum(mat))
