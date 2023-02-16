# Maximum Depth of Binary Tree

"""
    Go through the node and add 1 to the max of node left and node right
"""

# Time Complexity = O(n) || Space Complexity = O(n)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root):
    if root is None:
        return 0
    return 1 + max(maxDepth(root.left),maxDepth(root.right))


# def dfs(root,depth):
#     if not root:
#         return depth
#     return max(dfs(root.left,depth+1),dfs(root.right,depth+1))
# return dfs(root,0)
