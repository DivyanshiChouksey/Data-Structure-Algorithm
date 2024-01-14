# Determine if Two Strings Are Close

"""
    Two strings are considered close after attaing given operations 
    so to attain given operations we need to check both words should be of same character and words having 
    excatly same number of frequencies. 
"""

# Time Complexity = O(nlogn)    , n = max(m,n)
# Space Complexity = O(n)       , n = len(word1) ,m = len(word2)

from collections import Counter

word1 = "cabbba"
word2 = "abbccc"


def closeStrings(word1, word2):
    if set(word1) == set(word2):
        freq1 = Counter(word1)
        freq2 = Counter(word2)

        arr1 = []
        for k, v in freq1.items():
            arr1.append(v)

        arr2 = []
        for k, v in freq2.items():
            arr2.append(v)

        return sorted(arr1) == sorted(arr2)


print(closeStrings(word1, word2))

# Solution 2
word1 = "abc"
word2 = "bca"

def closeStrings2(word1, word2):
    # make the code like a general string with pattern
    if len(word1)!=len(word2):
        return False
    
    freq1 = [0]*26
    freq2 = [0]*26

    for i in range(len(word1)):
        j = ord(word1[i]) - ord("a")
        k = ord(word2[i]) - ord("a")
        freq1[j]+=1
        freq2[k]+=1

    for i in range(26):
        if freq1[i]>0 and freq2[i]==0:
            return False
        if freq2[i]>0 and freq1[i]==0:
            return False
            
    return sorted(freq1)==sorted(freq2)
        

print( closeStrings2(word1, word2))
