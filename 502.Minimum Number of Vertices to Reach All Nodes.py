# Minimum Number of Vertices to Reach All Nodes

"""
    Approach - find the non reacheable nodes 

    create an array with False where index representing the node value. 
    If node is reachable then put True otherwise False 
    and return the non reachable nodes in an array 

"""

# Time Complexity - O(n) || Space Complexity - O(n)

n = 6
edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
def findSmallestSetOfVertices(n, edges):
    reachableNodes = [False]*n
    for edge in edges:
        reachableNodes[edge[1]] = True
    
    ans = []
    i=0
    for node in reachableNodes:
        if node==False:
            ans.append(i)
        i+=1
    
    return ans

print(findSmallestSetOfVertices(n,edges))
