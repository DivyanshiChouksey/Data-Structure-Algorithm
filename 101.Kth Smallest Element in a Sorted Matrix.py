# Kth Smallest Element in a Sorted Matrix

matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 8

# Optimal Solution
"""
    We can make heap using for loop upto 'k' so we push element to heap and then update it as float("inf") 
    after that we pop the value from our min heap then we goto its right element and below element add them to heap and update it as float("inf")
    finally return the value at our kth heap pop
"""
# Time Complexity = O(klogk) || Space Complexity = O(k)

import heapq


def kthSmallest1(matrix, k):
    n = len(matrix)
    heap = [(matrix[0][0], 0, 0)]  # (value,r,c)
    matrix[0][0] = float("inf")
    heapq.heapify(heap)

    for i in range(k):
        value, row, col = heapq.heappop(heap)
        for r, c in [(row + 1, col), (row, col + 1)]:
            if r < n and c < n and matrix[r][c] != float("inf"):
                heapq.heappush(heap, (matrix[r][c], r, c))
                matrix[r][c] = float("inf")

    return value


# Optimal Solution
"""
    We can make heap using for loop upto 'k' so we push element to heap and then mark it as visited 
    after that we pop the value from our min heap then we goto its right element and below element add them to heap and mark it as visited
    finally return the value at our kth heap pop
"""
# Time Complexity = O(klogk) || Space Complexity = O(n)
matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 8

import heapq


def kthSmallest2(matrix, k):
    n = len(matrix)
    visited = set((0, 0))  # (index)
    heap = [(matrix[0][0], 0, 0)]  # (value,r,c)

    heapq.heapify(heap)

    for i in range(k):
        value, row, col = heapq.heappop(heap)
        for r, c in [(row + 1, col), (row, col + 1)]:
            if r < n and c < n and (r, c) not in visited:
                visited.add((r, c))
                heapq.heappush(heap, (matrix[r][c], r, c))

    return value


# Naive Solution
"""
    For naive solution we can make 2D matrix into 1D array and then sort it and
    return kth index value.
"""
# Time Complexity = O(n^2logn^2) || Space Complexity = O(n^2)

matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 8


def kthSmallest3(matrix, k):
    tmp = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            tmp.append(matrix[i][j])

    tmp.sort()
    return tmp[k - 1]


print(kthSmallest2(matrix, k))
print(kthSmallest3(matrix, k))
print(kthSmallest1(matrix, k))
