# Clone Graph

# Time Complexity = O(n) || Space Complexity = O(n)

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node):
    if not node:
        return None
    dct = {}
    def helper(node):
        if node in dct:
            return dct[node]
        copy = Node(node.val)
        dct[node]=copy
        for i in node.neighbors:
            copy.neighbors.append(helper(i))
        return copy
    
node = 1  # node of a graph
adjList = [[2,4],[1,3],[2,4],[1,3]]  # adjacency list of that graph

print(cloneGraph(node))
    


