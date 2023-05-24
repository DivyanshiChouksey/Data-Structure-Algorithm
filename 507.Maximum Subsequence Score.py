# Maximum Subsequence Score

import heapq

nums1 = [1,3,3,2]
nums2 = [2,1,3,4]
k = 3

def maxScore(nums1, nums2, k):
    # 1,2,3 = 3+1+2 = 6*1
    # 2,3,4 = 1+3+2 = 6*2 12
    pairs = [(a, b) for a, b in zip(nums1, nums2)]
    pairs.sort(key = lambda x: -x[1]) #[(2, 4), (3, 3), (1, 2), (3, 1)]

    # Use a min-heap to maintain the top k elements.
    top_k_heap = [x[0] for x in pairs[:k]] # 2,3,1
    top_k_sum = sum(top_k_heap) # 6
    heapq.heapify(top_k_heap) # creates heap 1,2,3

    # The score of the first k pairs.
    answer = top_k_sum * pairs[k - 1][1]

    # Iterate over every nums2[i] as minimum from nums2.
    for i in range(k, len(nums1)):
        # Remove the smallest integer from the previous top k elements
        # then ddd nums1[i] to the top k elements.
        top_k_sum -= heapq.heappop(top_k_heap) # remove from sum
        top_k_sum += pairs[i][0] # added new elemet
        heapq.heappush(top_k_heap, pairs[i][0]) # heappuched new element

        # Update answer as the maximum score.
        answer = max(answer, top_k_sum * pairs[i][1])

    return answer     
  
print( maxScore(nums1, nums2, k))
