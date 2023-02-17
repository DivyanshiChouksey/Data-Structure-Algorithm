# Minimum Distance Between BST Nodes

"""
    Algorithm :-
        1. Initialize the minDistance to MAX_VALUE possible; this is the variable to store the minimum difference.
           Initialize prevValue to null, so we can check if we have already traversed any elements before or not.
        2. Perform an in-order traversal of the given binary search tree. Each time we iterate over a node, check
           if prevValue is not null and if it is not, find its difference with the current node value and update 
           minDistance accordingly.
        3. After iterating over the current node, assign it to prevValue.
        4. Return minDistance when the in-order traversal is finished.

"""

# Time Complexity = O(n) || Space Complexity = O(h)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = [4,2,6,1,3]

class Solution:
    pre = -float('inf')
    res = float('inf')
    def minDiffInBST(self, root,prev = None) -> int:
        if root.left:
            self.minDiffInBST(root.left)
        self.res = min(self.res, root.val - self.pre)
        self.pre = root.val
        if root.right:
            self.minDiffInBST(root.right)
        return self.res