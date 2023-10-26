# Binary Trees With Factors

arr = [2,4,5,10]

MOD = 10**9 + 7

def numFactoredBinaryTrees(arr):
    arr.sort()
    s = set(arr)
    dp = {x: 1 for x in arr} #[2:1,4:2,5:1,10:3]
    
    for i in arr:   #10
        for j in arr:   #2
            if j > i**0.5:  #2>3.16
                break
            if i % j == 0 and i // j in s:
                if i // j == j: # 10//2==4
                    dp[i] += dp[j] * dp[j]
                else:
                    dp[i] += dp[j] * dp[i // j] * 2
                dp[i] %= MOD
    
    return sum(dp.values()) % MOD 

print(numFactoredBinaryTrees(arr))
