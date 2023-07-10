# Minimum Depth of Binary Tree

root = [3,9,20,null,null,15,7]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0            
        ans = float("inf")

        def helper(node,depth):
            nonlocal ans
            if not node.left and not node.right:
                ans = min(ans,depth)
                return 
            if node.left:
                helper(node.left,depth+1)
            if node.right:
                helper(node.right,depth+1)

        
        helper(root,1)
        return ans
