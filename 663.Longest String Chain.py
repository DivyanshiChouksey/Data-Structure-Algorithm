# Longest String Chain

words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]

def longestStrChain(words):
    words.sort(key = lambda x:len(x))
    dct = {}

    for word in words:
        dct[word] = 1
        for i in range(len(word)):
            successor = word[:i]+word[i+1:]
            if successor in dct:
                dct[word] = max(dct[word],dct[successor]+1)
    res = max(dct.values())
    return res


print(longestStrChain(words))
