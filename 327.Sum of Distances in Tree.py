# Sum of Distances in Tree

# Time Complexity = O(n) || Space Complexity = O(n)

from collections import defaultdict

N = 6
edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]


def sumOfDistancesInTree(N, edges):
    graph = defaultdict(list)
    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)

    size, up, down = [1] * N, [0] * N, [0] * N
    # up[i] is the distance from i's descendant to i
    # down[i] is the distance from others nodes to i
    # size[i] is the number of nodes in branch rooted by i (including i itself)

    def post(parent, i):
        for kid in graph[i]:
            if kid != parent:
                post(i, kid)
                size[i] += size[kid]
                up[i] += up[kid] + size[kid]

    def pre(parent, i):
        if parent != -1:
            down[i] = down[parent] + (up[parent] - up[i] - size[i]) + (N - size[i])
        for kid in graph[i]:
            if kid != parent:
                pre(i, kid)

    post(-1, 0)
    pre(-1, 0)
    return [up[i] + down[i] for i in range(N)]


print(sumOfDistancesInTree(N, edges))
