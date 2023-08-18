# Maximal Network Rank


"""
    Time complexity = O(E+V^2) || Space = O(E)
    E = number of edges, V = number of nodes in our graph respectively
"""

from collections import defaultdict

n = 5
roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]

def maximalNetworkRank(n, roads):
    maxRank = 0
    dct =  defaultdict(list)
    for a,b in roads:
        dct[a].append(b)
        dct[b].append(a)

    for node1 in range(n):
        for node2 in range(node1+1,n):
            cur = len(dct[node1]) + len(dct[node2])
            if node2 in dct[node1]:
                cur-=1
            
            maxRank = max(maxRank,cur)

    return maxRank


print(maximalNetworkRank(n,roads))
