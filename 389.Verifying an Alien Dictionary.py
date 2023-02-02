# Verifying an Alien Dictionary

words = ["word","world","row"]
order = "worldabcefghijkmnpqstuvxyz"

"""
    Make an index record of every character of language using a dictionary 
    Then for every word check that next word is lexicographically increasing then previous word
    for this if starting character of current word and prev word is not in order then return False or if
    starting character of same then check all above for next character of the both words 
    after this return True
"""

# Time Complexity = O(nm) , n-len(words) , m-len(word)
# Space Complexity = O(1) 


def isAlienSorted(words, order):
    dct = {}
    for i in range(len(order)):
        dct[order[i]] = i
    # print(dct)
    for i in range(len(words)-1):
        word1 = words[i]
        word2 = words[i+1]
        for j in range(len(word1)):
            if j==len(word2):
                return False
            if word1[j] != word2[j]:
                if dct[word1[j]] > dct[word2[j]]:
                    return False
                else:
                    break
    return True


print(isAlienSorted(words, order))