#


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
node6 = TreeNode(3)

tree = node1
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node5.right = node6


class getTreeInfo:
    def __init__(self, isBalanced, height):
        self.isBalanced = isBalanced
        self.height = height


def heightBalancedBinaryTree(tree):
    TreeInfo = getTreeinfo(tree)
    return TreeInfo.isBalanced


def getTreeinfo(node):
    # Know balanced and height
    if node == None:
        return getTreeInfo(True, -1)
    leftSubtreeInfo = getTreeinfo(node.left)
    rightSubtreeInfo = getTreeinfo(node.right)

    # check balanced tree or not
    isBalanced = (
        leftSubtreeInfo.isBalanced
        and rightSubtreeInfo.isBalanced
        and abs(leftSubtreeInfo.height - rightSubtreeInfo.height) <= 1
    )
    height = max(leftSubtreeInfo.height, rightSubtreeInfo.height) + 1
    return getTreeInfo(isBalanced, height)


print(heightBalancedBinaryTree(tree))
