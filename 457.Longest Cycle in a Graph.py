# Longest Cycle in a Graph

"""

    This problem can be done by a simple traversal so using for loop to get all nodes
    and a visited set for storing visited nodes and storing index of node in a dictionary , 
    as soon as we find a previously visited node again , 
    we will check the occurence of this node in our path till now .
    like if we have visited 0 -> 1 -> 2 -> 3 -> and then again if we come at 1 , 
    we can check our path dct and say that the cycle formed is of length 3.
    otherwise add node in visited set and increase count of path by 1.
       
"""

# Time Complexity = O(n) || Space Complexity = O(n)

from collections import defaultdict

edges = [3,3,4,2,3]

def longestCycle(edges):
    res = -1
    seen = set()
    for element in range(len(edges)):
        count = 0
        currNode = element
        cycleMap = defaultdict()
        while currNode not in seen and currNode!=-1:
            count+=1
            seen.add(currNode)
            cycleMap[currNode] = count
            currNode = edges[currNode]
        # gets the max distance
        res = max(res, count + 1 - cycleMap.get(currNode, float("inf")))
    return res


print(longestCycle(edges))



# Alternative Solution 

def longestCycle2(edges):
    n = len(edges)
    max_length = float('-inf')
    seen = [False] * n
    visiting = {}
    stack = []
        
    def dfs(node):
        nonlocal max_length
        if not seen[node]:
            if node in visiting:
                max_length = max(max_length, len(stack) - visiting[node])
            elif edges[node] != -1: 
                visiting[node] = len(stack) 
                stack.append(node)
                dfs(edges[node])
                stack.pop()
                visiting.pop(node)
            seen[node] = True

    for i in range(n):            
        dfs(i)
    return max_length if max_length > 0 else -1 

print(longestCycle2(edges))