# Find and Replace Pattern

words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
pattern = "abb"

# Optimal Solution
"""
    For given pattern and for each word in words 
    we would create a general pattern by replacing character in words and pattern like "abb" - "011"
    and add the word in our ans if general pattern of given pattern and word is same.  
"""
# Time Complexity = O(m*n) , m = len(pattern)
# Space Complexity = O(n)  , n = len(words)
def findAndReplacePattern(words, pattern):
    def convert(word):
        i = 0
        dct = {}
        tmp = ""
        for ch in word:
            if ch not in dct:
                dct[ch] = str(i)
                i += 1
            tmp += dct[ch]
        return tmp

    ans = []
    pattern = convert(pattern)
    for word in words:
        if convert(word) == pattern:
            ans.append(word)
    return ans


# Naive solution
"""
    for every time create two hashmap one for storing pattern and another for storing word in words
    add word if both hashmaps are equal.
"""
# Time Complexity = O(m*n) ,  m = len(pattern)
# Space Complexity = O(n)  , n ->(2n) = len(words)
def findAndReplacePattern2(words, pattern):
    def match(word):
        m1, m2 = {}, {}
        for w, p in zip(word, pattern):
            if w not in m1:
                m1[w] = p
            if p not in m2:
                m2[p] = w
            if (m1[w], m2[p]) != (p, w):
                return False
        return True

    return [word for word in words if match(word)]


print(findAndReplacePattern(words, pattern))
print(findAndReplacePattern2(words, pattern))
