# Everybody Likes Good Arrays!

# Input
"""
3
5
1 7 11 2 13
4
1 2 3 4
6
1 1 1 2 2 3
"""

# Output
"""
2
0
3

"""

for _ in range(int(input())):
    ans=0
    stack = []
    n = int(input())
    tmp = list(map(int,input().split()))
    for i in range(n):
        even = tmp[i]%2==0 
        if stack and stack[-1]%2 == tmp[i]%2:
            a = stack.pop()
            stack.append(a*tmp[i])
            ans+=1
        else:
            stack.append(tmp[i])
    print(ans)


