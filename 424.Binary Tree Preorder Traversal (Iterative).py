# Binary Tree Preorder Traversal (Iterative)

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
    Algorithm :-

    1. Initialize an empty array answer and an empty stack stack.

    2. Add root to stack.

    3. While stack is not empty, get the top node currNode from stack. If currNode is not NULL:
        add its value to answer.
        add its right child to stack.
        add its left child to stack.
        Then repeat step 3.

    4. Return answer after we empty stack.

"""

# Time Complexity = O(n) || Space Complexity = O(n)

def preorderTraversal(root):
    ans= []
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            ans.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return ans

print(preorderTraversal(root))