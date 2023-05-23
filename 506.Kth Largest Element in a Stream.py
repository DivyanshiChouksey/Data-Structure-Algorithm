# Kth Largest Element in a Stream
 
import heapq

class KthLargest:
    def __init__(self, k, nums):
        self.heap = []
        self.k = k
        for num in nums:
            heapq.heappush(self.heap,num)
        n = len(self.heap)
        for _ in range(n-k):
            heapq.heappop(self.heap)

    def add(self, val) :
        heapq.heappush(self.heap,val)
        while len(self.heap)>self.k:
            heapq.heappop(self.heap)
        return self.heap[0] 
        

# Your KthLargest object will be instantiated and called as such:

k = 3
nums = [4, 5, 8, 2]
obj = KthLargest(k, nums)
print(obj.add(3))
print(obj.add(5))
print(obj.add(10))
print(obj.add(9))
print(obj.add(4))
