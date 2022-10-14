# Split Array into Consecutive Subsequences

import heapq
from typing import DefaultDict

nums = [1, 2, 3, 3, 4, 5]


def isPossible(nums):
    ends_with = DefaultDict(list)
    for n in nums:
        if ends_with[n - 1]:
            length = heapq.heappop(ends_with[n - 1])
            heapq.heappush(ends_with[n], length + 1)
        else:
            heapq.heappush(ends_with[n], 1)

    for lengths in ends_with.values():
        if lengths and lengths[0] < 3:
            return False

    return True


print(isPossible(nums))
