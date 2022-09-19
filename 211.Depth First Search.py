# Depth First Search

"""
    Start with the very first branch of the given graph(here tree) 
    and explore as much as depth you can then repeat for the next branch and so on.
"""

# Time Complexity = O(v+e) , e = edges
# Space Complexity = O(v),   v = vertices


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(name)
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array


A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")
G = Node("G")
H = Node("H")
I = Node("I")
J = Node("J")
K = Node("K")

for i in [B, C, D]:
    A.addChild(i)

for i in [E, F]:
    B.addChild(i)

for i in [G, H]:
    D.addChild(i)

for i in [I, J]:
    F.addChild(i)

for i in [K]:
    G.addChild(i)

print(A.depthFirstSearch([]))
