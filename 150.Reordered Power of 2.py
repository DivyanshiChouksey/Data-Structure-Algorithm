# Reordered Power of 2
n = 1

# Time Complexity = O(n^2logn) || Space Complexity = O(logn)
def reorderedPowerOf2(n: int) -> bool:
    return sorted(str(n)) in [sorted(str(2**i)) for i in range(30)]


print(reorderedPowerOf2(n))
