# Remove Stones to Minimize the Total

"""
    We can minimise the total number of stone by doing operation on maximum 
    number of stones in the ith pile for this we are using the max-heap data strucute
    that means creating a max-heap of given array piles after that pop the value from the heap and
    perform operation on it and pushing the generated value into the heap ,repeat for k times
    and at the end return the sum of heap . 
"""

# Time Complexity = O(n) || Space Complexity = O(n)

from heapq import heappush, heapify, heappop

piles = [5, 4, 9]
k = 2


def minStoneSum(piles, k):
    for i in range(len(piles)):
        piles[i] *= -1

    heapify(piles)

    for i in range(k):
        heappush(piles, heappop(piles) // 2)

    return sum(piles) * -1


print(minStoneSum(piles, k))
