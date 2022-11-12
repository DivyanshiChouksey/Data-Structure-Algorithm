# Find Median from Data Stream

# Time Complexity = O(logn) || Space Complexity = O(1)

from heapq import *


class MedianFinder:
    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def findMedian(self):
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0


obj = MedianFinder()
obj.addNum(6)
obj.addNum(10)
obj.addNum(2)
print(obj.findMedian())
