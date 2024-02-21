# Bitwise AND of Numbers Range

left = 5
right = 7

def rangeBitwiseAnd(left,right):
    cnt = 0
    while left != right:
        left >>= 1
        right >>= 1
        cnt += 1
    return left << cnt

print(rangeBitwiseAnd(left,right))
