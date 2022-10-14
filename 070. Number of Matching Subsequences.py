from bisect import bisect
from collections import defaultdict


s = "abcde"
words = ["a", "bb", "acd", "ace"]
"""
ccaccccbcaade -> acb
"""
ans, mappings = 0, defaultdict(list)
for index, char in enumerate(s):
    mappings[char].append(index)
# print(mappings)
for word in words:
    prev, found = -1, True
    for ch in word:
        tmp = bisect(mappings[ch], prev)  # return the index
        # where to insert item x in list a, assuming a is sorted binary search -> log n
        # print(tmp)  # 7
        # print(ch, mappings[ch][tmp])
        if tmp == len(mappings[ch]):
            found = False
            break
        prev = mappings[ch][tmp]
    if found:
        ans += 1
print(ans)
