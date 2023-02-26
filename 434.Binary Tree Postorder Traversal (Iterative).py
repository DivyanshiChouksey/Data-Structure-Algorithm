# Binary Tree Postorder Traversal (Iterative)

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

# Time Complexity = O(2n) || Space Complexity = O(n)

def postorderTraversal(root):
    if not root:
        return None
    t = False
    ans=[]
    stack = []
    cur = root
    while cur or stack:
        if cur:
            if cur == root and t:
                return ans
            stack.append(cur)
            
            if cur == root:
                t = True
            cur = cur.left
        else:
            tmp = stack[-1].right
            if tmp is None:
                tmp = stack[-1]
                stack.pop()
                ans.append(tmp.val)
                while stack and tmp == stack[-1].right:
                    tmp = stack.pop()
                    ans.append(tmp.val)
            else:
                cur = tmp
    return ans


print(postorderTraversal(root))
