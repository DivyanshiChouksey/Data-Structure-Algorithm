# Champagne Tower

poured = 7
query_row = 3
query_glass = 3

def champagneTower(poured,query_row, query_glass):
    dp = [[0]*i for i in range(1,query_row+2)]
    dp[0][0] = poured
    for i in range(query_row):
        for j in range(i+1):
            tmp = (dp[i][j]-1)/2
            if tmp>0:
                dp[i+1][j] += tmp
                dp[i+1][j+1] += tmp

            
    return min(1,dp[query_row][query_glass])


print(champagneTower(poured,query_row, query_glass))
