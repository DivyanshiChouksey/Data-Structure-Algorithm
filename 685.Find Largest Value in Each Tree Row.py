# Find Largest Value in Each Tree Row

from collections import deque

# root = [1,3,2,5,3,null,9]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
                5
            --------
            4       8
            
        --------    --
        7       2    6

"""

# root = [5,4,8,7,2,6,null]

node1 = TreeNode(5)
node2 = TreeNode(4)
node3 = TreeNode(8)
node4 = TreeNode(7)
node5 = TreeNode(2)
node6 = TreeNode(6)

root = node1
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6



def largestValues(root):
    if not root:
        return []
    node = root
    queue = deque()
    queue.append(node)
    ans = []
    
    while queue:
        maxVal = float("-inf")
        for i in range(len(queue)):
            node = queue.popleft()
            maxVal = max(maxVal,node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
        ans.append(maxVal)
    
    return ans


print(largestValues(root))