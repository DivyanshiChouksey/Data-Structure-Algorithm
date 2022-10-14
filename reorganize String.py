# 767. Reorganize String

from typing import Counter


s = "aab"


def reorganizeString(s):
    s = Counter(s)
    # print(s)
    for k, v in s.items():
        if v >= len(s) // 2:
            return ""
