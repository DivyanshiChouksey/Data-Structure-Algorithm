# Count Vowels Permutation

n = 2

def countVowelPermutation(n):
    a, e, i, o, u = 1, 1, 1, 1, 1
    for _ in range(n - 1):
        a, e, i, o, u = e + i + u, a + i, e + o, i, i + o
    return (a + e + i + o + u) % (10**9 + 7)


print(countVowelPermutation(n))
# output -  10 [ "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".]
