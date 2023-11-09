# Count Number of Homogenous Substrings

# Time - O(n)
# Space - O(1)

s = "abbcccaa"

def countHomogenous(s):
    i=0
    j=0
    ans=0
    while j<len(s):
        count=0
        while j<len(s) and s[i]==s[j]:
            count+=1
            j+=1
        ans+= (count*(count+1))//2
        i=j
    return ans % ((10**9)+7)

print(countHomogenous(s))
