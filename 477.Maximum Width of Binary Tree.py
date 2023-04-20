# Maximum Width of Binary Tree

from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
    
        self.val = val
        self.left = left
        self.right = right


node1 = TreeNode(5)
node2 = TreeNode(4)
node3 = TreeNode(8)
node4 = TreeNode(7)
node5 = TreeNode(2)
node6 = TreeNode(9)
node7 = TreeNode(1)

root = node1
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node6
node4.left = node7

"""
                5
            --------
            4       8
            
        -------       --
        7     2         9
      --
      1

"""

# Time Complexity = O(n) || Space Complexity = O(n)

def widthOfBinaryTree( root):
    level = deque([(root,0)])
    maxWidth = 0
    while level:
        _,left = level[0]
        _,right = level[-1]
        maxWidth = max(maxWidth,((right-left)+1))
        for i in range(len(level)):
            node,idx = level.popleft()
            if node.left:
                level.append([node.left,(2*idx+1)])
            if node.right:
                level.append([node.right,(2*idx+2)])
        
    return maxWidth

print(widthOfBinaryTree( root))