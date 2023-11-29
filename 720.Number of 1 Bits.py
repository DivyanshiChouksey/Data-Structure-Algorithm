# Number of 1 Bits

n = 00000000000000000000000000001011

def hammingWeight(n):
    count = 0
    while n != 0:
        count += n & 1
        n >>= 1
    return count


print(hammingWeight(n))
