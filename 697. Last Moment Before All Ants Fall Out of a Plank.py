#  Last Moment Before All Ants Fall Out of a Plank

n = 4
left = [4,3]
right = [0,1]


def getLastMoment(n, left, right):
    # ans = 0
    # for l in left:
    #     ans = max(ans,l)
    # for r in right:
    #     ans=max(ans,n-r) 
    # return ans
    return max(max(left) if left else 0,n-(min(right) if right else n))


print(getLastMoment(n, left, right))
