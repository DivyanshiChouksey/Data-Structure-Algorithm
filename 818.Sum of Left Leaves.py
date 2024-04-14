# Sum of Left Leaves

root = [3,9,20,null,null,15,7]

class Solution:
    def __init__(self):
        self.ans = 0
        
    def sumOfLeftLeaves(self, root: Optional[TreeNode],leftNode = False) -> int:
        if root:
            if leftNode and root.left is None and root.right is None:
                self.ans += root.val
            self.sumOfLeftLeaves(root.left,True)
            self.sumOfLeftLeaves(root.right,False)

        return self.ans 
