# Most Frequent Even Element

from collections import defaultdict
from typing import Counter


nums = [0, 1, 2, 2, 4, 4, 1]


def mostFrequentEvenElement(nums):
    nums = Counter(nums)
    dct = defaultdict(int)
    print(dct)
    curMax = -1
    for k, v in nums.items():
        if k % 2 == 0:
            pass
