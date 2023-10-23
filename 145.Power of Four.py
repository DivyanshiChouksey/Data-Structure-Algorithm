# Power of Four

from math import log


n = 1

#
def isPowerOfFour(n):
    return n > 0 and log(n, 4).is_integer()


#
def isPowerOfFour2(n):
    if n == 1:
        return True
    s = 1
    while n != s and n > s:
        s *= 4
        if n == s:
            return True
    return False

# 
def isPowerOfFour3(n):
    binary = bin(n)
    return n > 0 and (not (n & (n-1))) and len(binary)%2

print(isPowerOfFour(n))
print(isPowerOfFour2(n))
print(isPowerOfFour3(n))
