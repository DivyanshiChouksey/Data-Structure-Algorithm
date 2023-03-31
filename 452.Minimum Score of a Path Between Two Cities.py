# Minimum Score of a Path Between Two Cities

from collections import defaultdict,deque

n = 4
roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]

def minScore( n, roads):
    graph = defaultdict(dict)
    for u, v, w in roads:
        graph[u][v] = graph[v][u] = w
    
    res = float("inf")
    vis = set()
    dq = deque([1])

    while dq:
        node = dq.popleft()
        for adj, scr in graph[node].items():
            if adj not in vis:
                dq.append(adj)
                vis.add(adj)
            res = min(res,scr)
            
    return res

print( minScore( n, roads))