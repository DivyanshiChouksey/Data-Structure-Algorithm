# Max Path Sum In Binary Tree
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
            
        --------  -------
        7     -2  -1    4

"""
node1 = TreeNode(5)
node2 = TreeNode(4)
node3 = TreeNode(8)
node4 = TreeNode(7)
node5 = TreeNode(-2)
node6 = TreeNode(-1)
node7 = TreeNode(4)


tree = node1
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node7
node3.left = node6


def maxPathSum(tree):
    _, maxSum = findMaxSum(tree)
    return maxSum


def findMaxSum(tree):
    if tree is None:
        return (0, float("-inf"))

    leftBranch, leftPath = findMaxSum(tree.left)
    rightBranch, rightPath = findMaxSum(tree.right)

    maxChild = max(leftBranch, rightBranch)

    value = tree.val
    maxBranch = max(maxChild + value, value)
    maxRoot = max(leftBranch + value + rightBranch, maxBranch)
    maxPath = max(leftPath, rightPath, maxRoot)

    return (maxBranch, maxPath)


print(maxPathSum(tree))
