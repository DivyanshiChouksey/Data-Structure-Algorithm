# Mirror Reflection
"""
    Dealing it with some tricky solution 
    if we found both p,q values even then divide both values by 2 until we reach to some conditions:-
    if p is even and q is odd then return 2 
    or p is odd and q is even then return 0
    or p is odd and q is even then return 1
    and lastly for some edge cases if p,q are equal then return 1.
"""
# Time Complexity = O(logn) , n = min of p,q
# Space Complexity = O(1)

p = 2
q = 1

# Solution 1
def mirrorReflection1(p, q):
    if p == q:
        return 1
    while p % 2 == 0 and q % 2 == 0:
        p //= 2
        q //= 2
    return 1 - p % 2 + q % 2


# Solution 2
def mirrorReflection(p, q):
    if p == q:
        return 1
    while p % 2 == 0 and q % 2 == 0:
        p //= 2
        q //= 2
    if p % 2 == 0 and q % 2 == 1:
        return 2
    if p % 2 == 1 and q % 2 == 0:
        return 0
    if p % 2 == 1 and q % 2 == 1:
        return 1


print(mirrorReflection1(p, q))
print(mirrorReflection(p, q))
