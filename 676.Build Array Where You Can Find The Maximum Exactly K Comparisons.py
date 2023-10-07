# Build Array Where You Can Find The Maximum Exactly K Comparisons

n = 2
m = 3
k = 1


def numOfArrays(n, m, k):
    @cache
    def dp(i, max_so_far, remain):
        if i == n:
            if remain == 0:
                return 1
            
            return 0
        
        ans = (max_so_far * dp(i + 1, max_so_far, remain)) % MOD
        for num in range(max_so_far + 1, m + 1):
            ans = (ans + dp(i + 1, num, remain - 1)) % MOD
            
        return ans
    
    MOD = 10 ** 9 + 7
    return dp(0, 0, k)

print( numOfArrays(n, m, k))
