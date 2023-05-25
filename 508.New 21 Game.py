# New 21 Game

n = 6
k = 1
maxPts = 10

def new21Game( n, k,maxPts):
    dp = [0] * (n + 1)
    dp[0] = 1
    s = 1 if k > 0 else 0
    for i in range(1, n + 1):
        dp[i] = s / maxPts
        if i < k:
            s += dp[i]
        if i - maxPts >= 0 and i - maxPts < k:
            s -= dp[i - maxPts]
    return sum(dp[k:])
  
print(new21Game( n, k,maxPts))
