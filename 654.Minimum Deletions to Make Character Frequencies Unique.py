# Minimum Deletions to Make Character Frequencies Unique
from collections import Counter

s = "aaabbbcc"

def minDeletions(s):
    cnt = Counter(s)
    deletions = 0
    usedFreq = set()
    sortedFreq = sorted(cnt.values(),reverse = True)
    for freq in sortedFreq:
        if freq not in usedFreq:
            usedFreq.add(freq)
            continue
        
        while freq>0 and freq in usedFreq:
            freq-=1
            deletions+=1
        
        usedFreq.add(freq)

    return deletions


print(minDeletions(s))
