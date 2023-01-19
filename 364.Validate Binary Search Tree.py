# Validate Binary Search Tree
"""
    Lets assume that the tree is a valid binary search tree then so we are using a pointer to track it,
    check whether node value is satisfying the condition of binary search tree 
    for root value check by taking left limit as float ("-inf") and right limit as float("inf")
    and for the left subtree values update the right limit to root value [check(root.left, left, root.val)]
    and for the right subtree values update the left limit to root value [check(root.right, root.val, right)]
    return False if any conditions is not satisfied.
"""

# Time Complexity = O(n)
# Space Complexity = O(h) , h - height of tree

# root = [2,1,3]


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root):
        isValid = True

        def check(root, left, right):
            if root and self.isValid:
                if root.val < left and root.val > right:
                    check(root.left, left, root.val)
                    check(root.right, root.val, right)
                else:
                    self.isValid = False

        check(root, float("-inf"), float("inf"))
        return self.isValid
