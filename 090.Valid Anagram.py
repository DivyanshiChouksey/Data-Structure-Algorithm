#  Valid Anagram

s = "anagram"
t = "nagaram"

# Solution 1
"""
    Sort both strings and then normally compare it.  
"""
# Time Complexity = O(logn) || Space Complexity = O(1)
def isAnagram(s, t):
    return sorted(s) == sorted(t)


# Solution2
"""
    Here we make two hashmaps,
    to store the character of both string with the number of times they appear in string.
"""
# Time Complexity = O(n) || Space Complexity = O(n)
from collections import defaultdict


def isAnagram2(s, t):
    if len(s) != len(t):
        return False
    countS, countT = defaultdict(int), defaultdict(int)
    for i in range(len(s)):
        if s[i] in countS:
            countS[s[i]] += 1
        else:
            countS[s[i]] = 1
    for i in range(len(t)):
        if t[i] in countT:
            countT[t[i]] += 1
        else:
            countT[t[i]] = 1
    for c in countS:
        if countS[c] != countT[c]:
            return False
    return True


print(isAnagram(s, t))
print(isAnagram2(s, t))
