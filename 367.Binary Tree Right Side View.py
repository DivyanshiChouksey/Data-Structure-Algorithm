# Binary Tree Right Side View

"""
                1
            --------
            2       3
            
             --       --
              5        4

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
node3 = TreeNode(4)
node4 = TreeNode(5)


root.left = node1
root.right = node2
node1.right = node4
node2.right = node3

"""
    Traverse the tree in NRL order that means first visit the node then 
    node.right after that node.left and for right side view node keep track of
    depth (level) of tree if depth is equals to length of ans then is means we have reached to the right most node
    so just append is to the our ans
     
"""

# Time Complexity = O(n) || Space Complexity = O(n)


def rightSideView1(root):
    # N R L
    ans = []

    def helper(node, d):
        if node is not None:
            if len(ans) == d:
                ans.append(node.val)
            helper(node.right, d + 1)
            helper(node.left, d + 1)

    helper(root, 0)
    return ans


print(rightSideView1(root))
