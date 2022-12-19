# Find if Path Exists in Graph

from collections import defaultdict

n = 3
edges = [[0, 1], [1, 2], [2, 0]]
source = 0
destination = 2

"""
    step1 - creating adjacency list
        0: [1,2]
        1: [0]
        2: [0,3]
        3: [4,5,2]
        4: [3,5]
        5: [3,4]

    step2 - traverse the graph and check if destination is in visited then return true 
        queue -> 0 1 2 3 4 (5)-True
        visited = (0,1,2,3)
"""

# Time Complexity - O(n) || Space Complexity - O(n)


def validPath(n, edges, source, destination):

    dct = defaultdict(list)
    for n, m in edges:
        dct[n].append(m)
        dct[m].append(n)

    visited = set()
    visited.add(source)
    queue = [source]
    while queue:
        tmp = []
        for node in queue:
            for i in dct[node]:
                if i not in visited:
                    tmp.append(i)
                    visited.add(i)
                    if i == destination:
                        return True
        queue = tmp[:]
    return destination in visited


print(validPath(n, edges, source, destination))
