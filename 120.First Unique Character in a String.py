# First Unique Character in a String

"""
    Create a Counter of given string
    and check :- character having frequencies 1 means non repeating character
    return the index of that character in the given string
    or else return -1 if there is no such character present over the string.
"""
# Time Complexity = O(n) || Space Complexity = O(n)
from typing import Counter

s = "leetcode"


def firstUniqChar(s):
    c = Counter(s)
    for k, v in c.items():
        if v == 1:
            return s.index(k)
    return -1


print(firstUniqChar(s))

# Naive Solution
"""
    Go through the every character in string and check whether it is a non repeating character or not
    and we can keep record by initialising a variable initially False and if found repeated character then update it true
    return index if variable remains False or else return -1 if there is no such character present over the string
"""
# Time Complexity = O(n^2) || Space Complexity = O(1)


def firstUniqChar1(s):
    for i in range(len(s)):
        found = False
        for j in range(len(s)):
            if s[i] == s[j] and i != j:
                found = True
                break
            if not found:
                return i
    return -1


print(firstUniqChar1(s))
