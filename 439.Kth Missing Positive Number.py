# Kth Missing Positive Number

A = [2,3,4,7,11]
k = 5

def findKthPositive( A, k):
    l, r = 0, len(A)
    while l < r:
        m = (l + r) // 2
        if A[m] - 1 - m < k:
            l = m + 1
        else:
            r = m
    return l + k 

print(findKthPositive( A, k))