# Binary Tree Zigzag Level Order Traversal

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

root = node1
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5

"""
                5
            --------
            4       8
            
        --------
        7       2

"""


"""
    Use appoarch of Level Order Traversal with record of levels so 
    for even level pop nodes from right and append nodes from left and for odd
    level pop nodes from left and append nodes from right and return the ans.
"""

# Time Complexity = O(n) || Space Complexity = O(n)

from queue import deque

def zigzagLevelOrder(root):
    if root is None:
        return []
    level = 1
    ans = []
    queue = deque()
    queue.append(root)
    while queue:
        value = []
        for i in range(len(queue)):
            if level%2==0:
                node = queue.pop()
                value.append(node.val)
                if node.right:
                    queue.appendleft(node.right)
                if node.left:
                    queue.appendleft(node.left)
                
            else:
                node = queue.popleft()
                value.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        ans.append(value)
        level+=1

    return ans

print(zigzagLevelOrder(root))