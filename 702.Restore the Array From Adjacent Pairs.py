# Restore the Array From Adjacent Pairs

from collections import defaultdict

adjacentPairs = [[2,1],[3,4],[3,2]]

def restoreArray(adjacentPairs):
    graph = defaultdict(list)
    
    for x, y in adjacentPairs:
        graph[x].append(y)
        graph[y].append(x)
    
    root = None
    for num in graph:
        if len(graph[num]) == 1:
            root = num
            break
    
    curr = root
    ans = [root]
    prev = None

    while len(ans) < len(graph):
        for neighbor in graph[curr]:
            if neighbor != prev:
                ans.append(neighbor)
                prev = curr
                curr = neighbor
                break

    return ans


print(restoreArray(adjacentPairs))
