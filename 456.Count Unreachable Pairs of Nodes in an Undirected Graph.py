# Count Unreachable Pairs of Nodes in an Undirected Graph

"""
    Count the number of node in every connected component say x then our ans will be sum
    of all x*(n-x)
    NOTE - we have counted each pair twice so return half of ans.
"""

# Time Complexity = O(n) || Space Complexity = O(n)

from collections import defaultdict

n = 7
edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]


def countPairs( n, edges):
    dct = defaultdict(list)
    for edge in edges:
        dct[edge[0]].append(edge[1])
        dct[edge[1]].append(edge[0])

    
    def dfs(i):
        count = 1
        stack = [i]
        while stack:
            tmp = []
            for node in stack:
                for x in dct[node]:
                    if x not in visited:
                        visited.add(x)
                        tmp.append(x)
                        count+=1
            stack = tmp[:]

        return count 
    
    visited = set()
    ans = 0

    for i in range(n):
        if i not in visited:
            visited.add(i)
            cnt = dfs(i)
            ans+= (n-cnt)*cnt
            
    return ans//2

print(countPairs(n, edges))