# Sum Root to Leaf Numbers
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node1 = TreeNode(4)
node2 = TreeNode(9)
node3 = TreeNode(0)
node4 = TreeNode(5)
node5 = TreeNode(1)

root = node1
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5

"""
                4
            --------
            9       0
            
        --------
        5       1

"""


"""
    Recursive Solution 
    Initialise a varible ans and define a recursive function helper with paramters
    current node a another varible tmp which stores tmp value
    if node left then call recursively helper for left node and (tmp*10)+node.val
    if node right then call recursively helper for right node and (tmp*10)+node.val
    and for base condition if it is a leave node then add the tmp to our ans and return 
    at the end return the ans 


    example above tree :-
    The root-to-leaf path 4->9->5 represents the number 495.
    The root-to-leaf path 4->9->1 represents the number 491.
    The root-to-leaf path 4->0 represents the number 40.
    Therefore, sum = 495 + 491 + 40 = 1026.
"""

# Time Complexity = O(n) || Space Complexity = O(h)

def sumNumbers(root):
    ans = 0
    def helper(node,tmp):
        nonlocal ans
        if node.left is None and node.right is None:
            ans+=(tmp*10)+(node.val)
            return         # break
        if node.left:
            helper(node.left,(tmp*10)+(node.val))
        if node.right:
            helper(node.right,(tmp*10)+(node.val))
    helper(root,0)
    return ans

print(sumNumbers(root))