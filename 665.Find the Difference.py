#  Find the Difference

# Optimization  

# Time : O(n)
# Space : O(1)

s = "abcd"
t = "abcde"

def findTheDifference(s,t):
    t1 = 0
    for i in s:
        t1+=ord(i)
    t2 = 0
    for j in t:
        t2+=ord(j)

    return chr(t2-t1)

print(findTheDifference(s,t))

________________________________________________________

# Naive

# Time : O(n)
# Space : O(n)

s = "abcd"
t = "abcde"

def findTheDifference(s,t):
    cnt = Counter(s)
    cnt2 = Counter(t)
    for k,v in cnt2.items():
        if v != cnt[k]:
            return k


print(findTheDifference(s,t))
