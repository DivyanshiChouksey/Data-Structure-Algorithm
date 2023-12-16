# 

n = 3
W = 4
val = [1,2,3]
wt= [4,5,1]

dp = [[0 for i in range(W+1)]for j in range(n+1)]
print(dp)
for i in range(1,n):
    for j in range(1,W):
        print(wt[i-1])
        if wt[i-1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-(wt[i-1])]+val[i-1])
            
print(dp)
