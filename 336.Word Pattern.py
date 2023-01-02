# Word Pattern

"""
    Creating a hash map to associate each and unqiue character of pattern to unique word of s 
    for this split the s to get the access of separate words in s
    after that go through the pattern and s string simultaneously with the help of zip funtion
    if the character is already having a distinct word associated with it or a word having
    more than one character associated with it then return False otherwise return True
    For early stoping check the length of both string.
"""

# Time Complexity = O(n) || Space Complexity = O(n)
pattern = "abba"
s = "dog cat cat dog"


def wordPattern(pattern, s):
    s = s.split()

    if len(pattern) != len(s):
        return False

    dct = {}
    for i, j in zip(pattern, s):
        if i in dct and dct[i] != j:
            return False
        elif i not in dct:
            if j in dct.values():
                return False
            dct[i] = j

    return True


print(wordPattern(pattern, s))
