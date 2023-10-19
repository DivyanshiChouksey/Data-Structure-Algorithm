# Backspace String Compare
"""
    Create 2 stacks to store characters for S and T 
    go through the strings S and append the characters in stacks but when we come across "#"
    then pop the top most character of stack and done the same for string T 
    and return True if both stack is equal. 
"""
# Time Complexity = O(n) || Space Complexity = O(n)

s = "ab#c"
t = "ad#c"


def backspace(s, t):
    stack1 = []
    for i in s:
        if i == "#":
            if len(stack1) == 0:
                continue
            else:
                stack1.pop()
        else:
            stack1.append(i)

    stack2 = []
    for i in t:
        if i == "#":
            if len(stack2) == 0:
                continue
            else:
                stack2.pop()
        else:
            stack2.append(i)

    return stack1 == stack2


print(backspace(s, t))

# Optimise

s="nzp#o#g"
t="b#nzp#o#g"

def backspaceCompare(s, t):
    # acd#  ad#c
    i = len(s)-1
    j = len(t)-1
    sBack = 0
    tBack = 0
    while True:
        while i>=0 and (sBack or s[i]=="#"):
            if s[i]=="#":
                sBack+=1
            else:
                sBack-=1
            i-=1
        while j>=0 and (tBack or t[j]=="#"):
            if t[j]=="#":
                tBack +=1
            else:
                tBack-=1
            j-=1
            
        # print(i,j)
        if i>=0 and j>= 0 and s[i]==t[j]:
            i-=1
            j-=1
        else:
            return True if (i== j==-1) else False
    return True if (i==-1 and j==-1) else False



print( backspaceCompare(s, t))
