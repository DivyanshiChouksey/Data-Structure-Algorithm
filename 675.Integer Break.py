# Integer Break

# Time : O(n^2) , Space : O(n)
n = 10
def integerBreak(n):
    if n <= 3:
        return n - 1
    
    dp = [0] * (n + 1)

    # Set base cases
    for i in [1, 2, 3]:
        dp[i] = i
        
    for num in range(4, n + 1):
        ans = num
        for i in range(2, num):
            ans = max(ans, i * dp[num - i])
        
        dp[num] = ans
    
    return dp[n]

print(integerBreak(n))


# Optimization 

# Time : O(n) , Space : O(1)
n = 10
def integerBreak( n):
    if n <= 3:
        return n - 1
    
    ans = 1
    while n > 4:
        ans *= 3
        n -= 3
    
    return ans * n

print(integerBreak( n))

# Optimization

# Time : O(logn) , Space : O(1)
n = 10

def integerBreak(n):
    if n <= 3:
        return n - 1
    
    if n % 3 == 0:
        return 3 ** (n // 3)
    
    if n % 3 == 1:
        return 3 ** (n // 3 - 1) * 4
    
    return 3 ** (n // 3) * 2

print(integerBreak(n))
