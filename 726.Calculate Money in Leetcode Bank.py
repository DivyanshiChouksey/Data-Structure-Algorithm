# Calculate Money in Leetcode Bank

 n = 10

def totalMoney(n):
    ans = 0
    monday = 1
    
    while n > 0:
        for day in range(min(n, 7)):
            ans += monday + day
        
        n -= 7
        monday += 1

    return ans


print(totalMoney(n))
