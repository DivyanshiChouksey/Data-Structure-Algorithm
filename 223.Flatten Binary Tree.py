# Flatten Binary Tree

# Naive solution
# Time Complexity = O(n) || Space Complexity = O(n)


class TreeNode:
    def __init__(self, val, left=None, right=None):
        """
        if this was not a binary tree then we would have an array of children
        """
        self.val = val
        self.left = left
        self.right = right


"""
                5
            --------
            4       8
            
        --------
        7       2

"""
node1 = TreeNode(5)
node2 = TreeNode(4)
node3 = TreeNode(8)
node4 = TreeNode(7)
node5 = TreeNode(2)

root = node1
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5


def flattenTree(root):
    inOrder = getNodesInOrder(root, [])
    for i in range(0, len(inOrder) - 1):
        leftNode = inOrder[i]
        rightNode = inOrder[i + 1]
        leftNode.right = rightNode
        rightNode.left = leftNode
    return inOrder[0]


def getNodesInOrder(node, array):
    if node:
        getNodesInOrder(node.left, array)
        array.append(node)
        getNodesInOrder(node.right, array)
    return


print(flattenTree(root))


# Optimal Solution


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
