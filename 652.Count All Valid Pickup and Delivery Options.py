# Count All Valid Pickup and Delivery Options

from functools import lru_cache

 n = 2

def countOrders(n):
    @lru_cache(None) 
    def helper(unpicked,undeliver):
        if not unpicked and not undeliver:
            return 1
        if unpicked < 0 or undeliver < 0  or undeliver < unpicked:
            return 0

        ans = unpicked*(helper(unpicked-1,undeliver))
        ans %= mod
        ans += (undeliver-unpicked) *( helper(unpicked,undeliver-1))
        ans %= mod

        return ans

    mod = (10**9)+7
    return helper(n,n)

print(countOrders(n))
