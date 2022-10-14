# Breadth-First Search


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(name)
        return self

    def breadthFirstSearch(self, array):
        queue = [self]
        while len(queue) > 0:
            cur = queue.pop(0)
            array.append(cur.name)
            for child in cur.children:
                queue.append(child)
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

print(A.breadthFirstSearch([]))
