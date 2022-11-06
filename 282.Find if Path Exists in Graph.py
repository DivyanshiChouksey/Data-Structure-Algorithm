# Find if Path Exists in Graph

"""
    Steps
    1. Make adjecency list
    2. start from source and keep track of visited 
    3. check is we reached destination or not then return True or False
"""
# Time Complexity = O(n) || Space Complexity = O(n)

n = 3
edges = [[0, 1], [1, 2], [2, 0]]
source = 0
destination = 2

from collections import defaultdict


def validPath(n, edges, source, destination):
    graph = defaultdict(list)
    for s, d in edges:
        graph[s].append(d)
        graph[d].append(s)
    # print(graph)
    visited = set()
    queue = [source]
    visited.add(sorted)
    while queue:
        tmp = []
        for node in queue:
            if node == destination:
                return True
            for neighbor in graph[node]:
                if neighbor not in visited:
                    tmp.append(neighbor)
                    visited.add(neighbor)
        queue = tmp[:]
    return False


print(validPath(n, edges, source, destination))
