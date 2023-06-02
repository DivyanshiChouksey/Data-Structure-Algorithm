# Detonate the Maximum Bombs

from collections import defaultdict

bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]

def maximumDetonation(bombs):
    graph = collections.defaultdict(list)
    n = len(bombs)

    # Build the graph
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            xi, yi, ri = bombs[i]
            xj, yj, _ = bombs[j]

            # Create a path from node i to node j, if bomb i detonates bomb j.
            if ri ** 2 >= (xi - xj) ** 2 + (yi - yj) ** 2:
                graph[i].append(j)

    # print(graph) -> defaultdict(<class 'list'>, {0: [1, 2], 2: [1, 3], 3: [1, 2, 4], 4: [2, 3]})
    def bfs(i):
        queue = collections.deque([i])
        visited = set([i])
        while queue:
            cur = queue.popleft()
            for neib in graph[cur]:
                if neib not in visited:
                    visited.add(neib)
                    queue.append(neib)
        return len(visited)

    answer = 0
    for i in range(n):
        answer = max(answer, bfs(i))
    return answer
  
print(maximumDetonation(bombs))
