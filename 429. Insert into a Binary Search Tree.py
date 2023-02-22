#  Insert into a Binary Search Tree

# Time Complexity = O(n) || Space Complexity = O(n)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insertIntoBST(self, root, val):
    if root is None:
        return TreeNode(val)
    if root.val<val:
        root.right = self.insertIntoBST (root.right,val)
    else:
        root.left = self.insertIntoBST(root.left,val)
    return root