# Top K Frequent Elements

from collections import Counter
import heapq

# Time Complexity - O(n) || Space Complexity - O(n)

nums = [1,1,1,2,2,3]
k = 2


def topKFrequent(nums, k) :
    count = Counter(nums)
    heap = []
    for key,v in count.items():
        heapq.heappush(heap,(-v,key))    

    ans = []
    for _ in range(k):
        tmp = heapq.heappop(heap)
        ans.append(tmp[1])
    return ans

print(topKFrequent(nums, k))