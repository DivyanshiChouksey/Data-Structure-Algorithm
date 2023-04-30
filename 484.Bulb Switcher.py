# Bulb Switcher 

n = 5

# Time Complexity = O(1) || Space Complexity = O(1)
def bulbSwitch(n):
    return int(n**0.5)
  
print(bulbSwitch(n))
  
# would give TLE
def bulbSwitch(n):
    if n==0:
        return 0
    if n ==1:
        return 1
    dp = [False]*n
    for i in range(1,n+1):
        for tmp in range(i-1,n,i):
            dp[tmp] = not dp[tmp]
    return sum(dp)
