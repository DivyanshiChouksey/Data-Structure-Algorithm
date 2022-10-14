# Binary Tree Inorder Traversal


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # L N R
        ans = []

        def helper(node):
            if node is not None:
                helper(node.left)
                ans.append(node.val)
                helper(node.right)

        helper(root)
        return ans
