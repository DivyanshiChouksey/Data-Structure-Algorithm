# Number of Operations to Make Network Connected

"""
    If no. of ethernet cables are less than the n-1(n = no. of computer) then return -1 because than only we can't
    connect all the computers after that count all network of computer and lefted single computers by using dfs 
    (or any graph traversal technique) then return count-1 that is the minimum number of times we need to alter
    the cables to make all the computers connected.


    Algorithm :-
    1. Check possible or not
    2. check for number of connected networks
        2.1 Make a visted set
        2.2 visit all nodes and mark connected node as visited
        2.3 for every new node not in visted add +1 in ans 
    3. return no. of network -1 
    
"""

# Time Complexity = O(n) || Space Complexity = O(n) , n = no. of computers

from collections import defaultdict

n = 6
connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]

def makeConnected(n, connections):
    if len(connections) < n-1:
        return -1
    
    dct = defaultdict(list)
    for con in connections:
        dct[con[0]].append(con[1])
        dct[con[1]].append(con[0])
    
    def dfs(i):
        stack = [i]
        while stack:
            tmp = []
            for node in stack:
                for x in dct[node]:
                    if x not in visited:
                        tmp.append(x)
                        visited.add(x)
            stack = tmp[:]
            
    ans = 0
    visited = set()
    for i in range(n):
        if i not in visited:
            visited.add(i)
            dfs(i)
            ans+=1

    return ans-1

print(makeConnected(n, connections))