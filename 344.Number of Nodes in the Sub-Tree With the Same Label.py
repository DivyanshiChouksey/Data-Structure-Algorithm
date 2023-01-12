# Number of Nodes in the Sub-Tree With the Same Label

# Time Complexity = O(n) || Space Complexity = O(n)


import collections
from collections import Counter

n = 7
edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
labels = "abaedcd"


def countSubTrees(n, edges, labels):
    """
    1. Subtree
    2. Counter
    3. label
    """
    seen = set()
    graph = collections.defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    ans = [0] * n

    def dfs(node):
        cnt = Counter()
        cnt[labels[node]] += 1
        seen.add(node)
        for child in graph[node]:
            if child not in seen:
                cnt += dfs(child)
        ans[node] = cnt[labels[node]]
        return cnt

    dfs(0)

    return ans


print(countSubTrees(n, edges, labels))
