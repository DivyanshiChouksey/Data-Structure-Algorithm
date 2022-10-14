# Binary Tree Diameter

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    return getTreeInfo(tree).diameter

def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(0,0)

    leftTreeInfo = getTreeInfo(tree.left)
    rightTreeInfo = getTreeInfo(tree.right)

    longestPath = leftTreeInfo.height + rightTreeInfo.height
    maxDiameterSoFar = max(leftTreeInfo.diameter, rightTreeInfo.diameter)
    curDiameter = max(longestPath,maxDiameterSoFar)
    curHeight = 1+max(leftTreeInfo.height ,rightTreeInfo.height )

    return TreeInfo(curDiameter,curHeight)

class TreeInfo:
    def __init__(self,diameter,height):
        self.diameter = diameter
        self.height = height
