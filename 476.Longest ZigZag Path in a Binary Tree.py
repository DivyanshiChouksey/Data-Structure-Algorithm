# Longest ZigZag Path in a Binary Tree

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        res = 0
        def find(node,l=0,r=0):
            nonlocal res
            if node:
                res = max(res,l,r)
                find(node.left,0,l+1)
                find(node.right,r+1,0)

        find(root)
        return res
