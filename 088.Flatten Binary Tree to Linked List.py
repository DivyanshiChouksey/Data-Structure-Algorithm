# Flatten Binary Tree to Linked List
"""

"""
# Time Complexity = O(n) || Space Complexity = O(h) ,h-height of tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def flatten(self, root: TreeNode) -> None:
    # LRN
    if root:
        self.flatten(root.left)
        self.flatten(root.right)
        tmp = root.right
        root.right = root.left
        root.left = None
        while root.right:
            root = root.right
        root.right = tmp
