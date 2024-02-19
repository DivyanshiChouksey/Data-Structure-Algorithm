# Power of Two

n = 16

def isPowerOfTwo(n):
    if n == 0:
        return False
    return False if n & n-1 else True

print(isPowerOfTwo(n))
