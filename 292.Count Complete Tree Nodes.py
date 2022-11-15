# Count Complete Tree Nodes

# Time Complexity = O(logn*logn)


class TreeNode:
    def __init__(self, val, left=None, right=None):
        """
        if this was not a binary tree then we would have an array of children
        """
        self.val = val
        self.left = left
        self.right = right


"""
                1
            --------
            2       3
            
        --------
        4       5
"""
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

root = node1
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6


def countNodes(root):
    """
    If left sub tree height equals right sub tree height then,
    a. left sub tree is perfect binary tree
    b. right sub tree is complete binary tree
    If left sub tree height greater than right sub tree height then,
    a. left sub tree is complete binary tree
    b. right sub tree is perfect binary tree
    """
    if not root:
        return 0
    leftDepth = getDepth(root.left)
    rightDepth = getDepth(root.right)
    if leftDepth == rightDepth:
        return pow(2, leftDepth) + countNodes(root.right)
    else:
        return pow(2, rightDepth) + countNodes(root.left)


def getDepth(root):
    if not root:
        return 0
    return 1 + getDepth(root.left)


print(countNodes(root))
