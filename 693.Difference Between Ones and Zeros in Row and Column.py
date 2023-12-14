# Difference Between Ones and Zeros in Row and Column

grid = [[0,1,1],[1,0,1],[0,0,1]]


def onesMinusZeros(grid):
    def summation(nums) : 
        return 2 * sum(nums) - len(nums)
    m, n = len(grid), len(grid[0])
        
    rows = list(map(summation, grid))
    cols = list(map(summation, zip(*grid)))
    
    for i,j in product(range(m), range(n)):
        grid[i][j] = rows[i] + cols[j]
    return grid


print(onesMinusZeros(grid))
