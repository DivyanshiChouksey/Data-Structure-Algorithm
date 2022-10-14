# Power of Four

from math import log


n = 1

#
def isPowerOfFour(n) -> bool:
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


print(isPowerOfFour(n))
print(isPowerOfFour2(n))
