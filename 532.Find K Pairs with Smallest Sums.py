# Find K Pairs with Smallest Sums

nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3

def kSmallestPairs(nums1, nums2, k):
    from heapq import heappush, heappop
    m = len(nums1)
    n = len(nums2)

    ans = []
    visited = set()

    minHeap = [(nums1[0] + nums2[0], (0, 0))]
    visited.add((0, 0))
    count = 0

    while k > 0 and minHeap:
        val, (i, j) = heappop(minHeap)
        ans.append([nums1[i], nums2[j]])

        if i + 1 < m and (i + 1, j) not in visited:
            heappush(minHeap, (nums1[i + 1] + nums2[j], (i + 1, j)))
            visited.add((i + 1, j))

        if j + 1 < n and (i, j + 1) not in visited:
            heappush(minHeap, (nums1[i] + nums2[j + 1], (i, j + 1)))
            visited.add((i, j + 1))
        k = k - 1
    
    return ans


print(def kSmallestPairs(nums1, nums2, k))
