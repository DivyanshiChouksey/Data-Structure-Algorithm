# Depth First Search

"""

"""

# Time Complexity = O(v+e) , e = edges
# Space Complexity = O(v),   v = vertices

"""
    we have to explore first branch go through it as much as depth we have 
"""


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array
