# Sort Characters By Frequency
"""
    Make a counter to store characters with their frequency because counter is an unordered dct
    so make a list(tmp) append each characters with their frequency in decreasing order then create an ans
    list,go through the tmp and append characters to their frequency times in ans and return ans as a string.
    (super optimization bucket sort pending)
"""
# Time Complexity- O(nlogn) || Space Complexity = O(n)

from typing import Counter

s = "tree"


def sortByFrequency(s):
    cnt = Counter(s)
    tmp = []
    for k, v in cnt.items():
        tmp.append([k, v])

    tmp.sort(key=lambda x: -x[1])

    ans = []
    for k, v in tmp:
        ans.append(v * k)

    return "".join(ans)


print(sortByFrequency(s))
