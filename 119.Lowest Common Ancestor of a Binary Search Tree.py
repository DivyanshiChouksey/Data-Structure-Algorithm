# Lowest Common Ancestor of a Binary Search Tree
"""
    Here we have to find left and right between p and q then check,
    return root value as a common ancestor if root.val is greater than left and smaller than right
    or just iterate in left side of binary search tree by updating root = root.left if both left and right are smaller than root.value
    else iterate in right side of binary search tree as root = root.right.
"""

# Time Complexity = O(h) , h-height of tree
# Space Complexity = O(1)


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        left = p.val if p.val < q.val else q.val
        right = p.val if p.val > q.val else q.val

        while root:
            if left <= root.val <= right:
                return root.val
            elif left < root.val and right < root.val:
                root = root.left
            else:
                root = root.right
