# Binary Search Tree to Greater Sum Tree

# Input : root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
      
def bstToGst(root):
    ans = 0
    def order(node):
        nonlocal ans
        if not node:
            return 0
        order(node.right)
        ans += node.val
        node.val = ans
        order(node.left)

    order(root)
    return root
