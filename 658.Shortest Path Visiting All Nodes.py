# Shortest Path Visiting All Nodes

from collections import deque

graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]


def shortestPathLength(graph):
    n = len(graph)
    queue = deque([(1<<i,i,0)for i in range(n)]) #[(1,0,0),(2,1,0),(4,2,0),(8,3,0)]
    # here 1->0001, 2->0010 in binary so we can see ehich node is visted 
    visited = set((1<<i,i) for i in range(n))
    while queue:
        mask,node,dist = queue.popleft()
        if mask == (1<<n) -1:
            return dist
        for neigh in graph[node]:
            newMask = mask | (1<<neigh) # 0001 | 0010 = 0011
            if (newMask , neigh) not in visited:
                visited.add((newMask,neigh))
                queue.append((newMask,neigh,dist+1))


print(shortestPathLength(graph))

   
