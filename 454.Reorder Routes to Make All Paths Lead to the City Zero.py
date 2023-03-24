# Reorder Routes to Make All Paths Lead to the City Zero

"""
    As given the road is one direction so for this we will creat bi-directional road connection
    and keep record of original connection in a set after that traverse the graph and check path is in our set
    then increment the ans by one, at the end return ans.
"""

# Time COmplexity = O(n) || Space Complexity = O(n)

from collections import defaultdict

n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]

def minReorder( n, connections):
    dct = defaultdict(list)
    path = set()

    for cn in connections:
        path.add((cn[0],cn[1]))
        dct[cn[0]].append(cn[1])
        dct[cn[1]].append(cn[0])

    ans = 0
    def dfs(node,parent):
        nonlocal ans
        ans += (parent,node) in path
        for v in dct[node]:
            if v == parent:
                continue
            dfs(v,node)
    
    dfs(0,-1)
    return ans

print(minReorder( n, connections))