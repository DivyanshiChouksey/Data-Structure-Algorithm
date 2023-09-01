# Counting Bits

n = 5

def countBits(n):
    ans = [0]
    for i in range(1,n+1):
        if i%2 != 0:
            ans.append(ans[i-1]+1)
        else:
            ans.append(ans[i//2])

    return ans


print(countBits(n))
