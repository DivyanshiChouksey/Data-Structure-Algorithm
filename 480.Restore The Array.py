# Restore The Array

s = "1317"
k = 2000

def numberOfArrays(s, k):
    n = len(s)
    mod = 10 ** 9 + 7
    dp = [0] * (n + 1)
    dp[n] = 1
    for i in reversed(range(n)):
        if s[i] == "0":
            continue
        num = int(s[i])
        j = i + 1
        while j <= n and num <= k:
            dp[i] += dp[j]
            num = num * 10 + (int(s[j]) if j < n else 0)
            j += 1
        dp[i] = dp[i] % mod
    return dp[0]
  

print(numberOfArrays(s, k))
