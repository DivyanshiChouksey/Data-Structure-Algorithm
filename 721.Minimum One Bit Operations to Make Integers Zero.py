# Minimum One Bit Operations to Make Integers Zero

n = 3


def minimumOneBitOperations(n):
    if n == 0:
        return 0
    
    k = 0
    curr = 1
    while (curr * 2) <= n:
        curr *= 2
        k += 1

    return 2 ** (k + 1) - 1 - self.minimumOneBitOperations(n ^ curr)


print(minimumOneBitOperations(n))
