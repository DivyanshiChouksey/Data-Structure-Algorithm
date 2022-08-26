# Ransom Note
"""
    Simply make record of frequencies of character of ransomNote and magazine 
    and return True if every character frequency of magazine is greater than or equal to ransomNote Freq 
"""
# Time Complexity = O(n+m) ,  n = len(ransomNote)
# Space Complexity = O(m+n) , m = length of magazine


from typing import Counter

ransomNote = "a"
magazine = "b"


def canConstruct(ransomNote, magazine):
    st = ransomNote
    ransomNote = Counter(ransomNote)
    magazine = Counter(magazine)
    for ch in st:
        if ransomNote[ch] > magazine[ch]:
            return False
    return True


print(canConstruct(ransomNote, magazine))
