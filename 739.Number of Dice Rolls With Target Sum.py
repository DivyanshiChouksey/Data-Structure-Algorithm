# Number of Dice Rolls With Target Sum

n = 1
k = 6
target = 3


def numRollsToTarget(n, k, target):
    memo = {}
    def dp(n,target):
        if n==0 :
            return 0 if target > 0 else 1
        if (n,target) in memo:
            return memo[(n,target)]
        to_return = 0
        for f in range(max(0, target-k), target):
            to_return += dp(n-1, f)
        memo[(n,target)] = to_return
        return to_return
    
    return dp(n, target)%(10**9+7)


print(numRollsToTarget(n, k, target))
