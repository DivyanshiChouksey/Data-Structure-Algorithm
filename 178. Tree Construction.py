# Binary Tree


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

# now printing LNR inorderTraversal
def inOrder(node):
    if node:
        inOrder(node.left)
        print(node.val, end=" ")
        inOrder(node.right)


inOrder(root)
