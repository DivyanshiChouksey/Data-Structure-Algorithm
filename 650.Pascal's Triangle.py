# Pascal's Triangle

numRows = 5

def generate( numRows):
    ans = [[1]*i  for i in range(1,numRows+1)]
    for i in range(2,numRows):
        for j in range(1,i):
            ans[i][j] = ans[i-1][j]+ans[i-1][j-1]
    return ans


print( generate( numRows))
