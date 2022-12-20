# Keys and Rooms

"""
    Traverse the graph and check if length of visited is equal to len of rooms 
    then return true 
        queue -> 0 1 2 3 4 5
        visited = (0,1,2,3,4,5)  
"""

# Time Complexity = O(n) || Space Complexity = O(n)

from collections import defaultdict

rooms = [[1, 3], [3, 0, 1], [2], [0]]


def canVisitAllRooms(rooms):
    visited = set()
    visited.add(0)
    queue = [i for i in rooms[0]]
    while queue:
        tmp = []
        for node in queue:
            visited.add(node)
            # print(queue, node, visited)
            for i in rooms[node]:
                if i not in visited:
                    tmp.append(i)
        queue = tmp[:]
    return len(visited) == len(rooms)


print(canVisitAllRooms(rooms))
