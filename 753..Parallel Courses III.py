# Parallel Courses III

n = 3
relations = [[1,3],[2,3]]
time = [3,2,5]


def minimumTime(n, relations, time):
    graph = defaultdict(list)
    indegree = [0] * n
    
    for (x, y) in relations:
        graph[x - 1].append(y - 1)
        indegree[y - 1] += 1
    
    queue = deque()
    max_time = [0] * n
    for node in range(n):
        if indegree[node] == 0:
            queue.append(node)
            max_time[node] = time[node]

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            max_time[neighbor] = max(max_time[neighbor], max_time[node] + time[neighbor])
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return max(max_time)
