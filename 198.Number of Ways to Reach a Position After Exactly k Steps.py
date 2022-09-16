# Number of Ways to Reach a Position After Exactly k Steps

"""
    Recursive approach + memoziation =(dp) --> optimal solution.
    from the start position we check for +1 position and for -1 minus postion and 
    do the same process for start position + 1  and for start position - 1 do this for kth time and if we reach end position 
    then add 1 in our ans cause we found a path from start position to end position in k steps and 
    for not calculating repeated value we use memoziation with the help of lru_cache.   
"""

startPos = 1
endPos = 2
k = 3

from functools import lru_cache


def numberOfWays(startPos, endPos, k):
    @lru_cache(None)
    def helper(startPos, endPos, n=0):
        if n == k and startPos == endPos:
            return 1
        if n > k:
            return 0
        return helper(startPos - 1, endPos, n + 1) + helper(startPos + 1, endPos, n + 1)

    return helper(startPos, endPos) % (10**9 + 7)


print(numberOfWays(startPos, endPos, k))
