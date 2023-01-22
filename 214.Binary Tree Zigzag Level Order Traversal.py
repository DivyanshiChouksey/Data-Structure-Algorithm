# Binary Tree Zigzag Level Order Traversal


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(3)
node1 = TreeNode(9)
node2 = TreeNode(20)
node3 = TreeNode(15)
node4 = TreeNode(7)

root.left = node1
root.right = node2
node2.left = node3
node2.right = node4


# Iterative Solution

"""
    Simple traverse the binary tree by level-order traversal (bfs) 
    but reverse alternate levels befor adding them to the ans  
"""

# Time Complexity = O(n) || Space Complexity = O(n)


def zigzagLevelOrder(root):
    if not root:
        return []
    level = 1
    ans = []
    queue = [root]
    while queue:
        tmp = []
        tmpans = []
        for node in queue:
            tmpans.append(node.val)
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
        queue = tmp[:]
        if level % 2 == 0:
            ans.append(tmpans[::-1])
        else:
            ans.append(tmpans)

        level += 1
    return ans


print(zigzagLevelOrder(root))
