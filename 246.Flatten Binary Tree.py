# Flatten Binary Tree


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def flattenBinaryTree(root):
    inOrder = getNodesInorder(root, [])
    for i in range(0, len(inOrder) - 1):
        leftNode = inOrder[i]
        rightNode = inOrder[i + 1]
        leftNode.right = rightNode
        rightNode.left = leftNode
    return inOrder[0]


def getNodesInorder(node, array):
    if node:
        getNodesInorder(node.left, array)
        array.append(node)
        getNodesInorder(node.right, array)
    return array


#
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def flattenBinaryTree(root):
    leftMost, _ = flattenTree(root)
    return leftMost


def flattenTree(node):
    if node.left is None:
        leftMost = node
    else:
        leftSubtreeLeftMost, leftSubtreeRightMost = flattenTree(node.left)
        # connectNodes(leftSubtreeRightMost , node)
        leftSubtreeRightMost.right = node
        node.left = leftSubtreeRightMost
        leftMost = leftSubtreeLeftMost

    if node.right is None:
        rightMost = node
    else:
        rightSubtreeLeftMost, rightSubtreeRightMost = flattenTree(node.right)
        # connectNodes(node,rightSubtreeLeftMost)
        node.right = rightSubtreeLeftMost
        rightSubtreeLeftMost.left = node
        rightMost = rightSubtreeRightMost

    return [leftMost, rightMost]


def connectNodes(left, right):
    left.right = right
    right.left = left
