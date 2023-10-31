# Find The Original Array of Prefix Xor

# time - O(n)
# space - O(n)

pref = [5,2,0,3,1]

def findArray(pref):
    ans = [pref[0]]
    for i in range(1,len(pref)):
        ans.append(pref[i-1]^pref[i])
    return ans

print(findArray(pref))

# time - O(n)
# space - O(1)

pref = [5,2,0,3,1]

def findArray(pref):
    i = len(pref)-1
    while i>0:
        pref[i] = pref[i-1]^pref[i]
        i-=1
    return pref

print(findArray(pref))
