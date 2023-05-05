# Maximum Number of Vowels in a Substring of Given Length

s = "abciiidef"
k = 3


def maxVowels(s, k):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    count = 0
    for ch in s[:k]:
        if ch in vowels:
            count +=1
    tmp = count
    for i in range(k,len(s)):
        if s[i] in vowels:
            tmp +=1
        if s[i-k] in vowels:
            tmp-=1
        count = max(count,tmp)
    return count
  
print(maxVowels(s, k))  
