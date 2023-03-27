# Construct Binary Tree from Inorder and Postorder Traversal

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
                 3
            ----------
            9        20
            
                 ---------
                 15      7

"""

"""
    Optimized Solution
    Initialize a dictionary and store value with their index so it take constant time to access the index then 
    define a recursive function with two parameter i.e. two pointer low and high initially at 0 and len(inorder)-1
    then do the same as naive solution make a treenode(root) of popped the value from postorder find the index of that 
    node.val in inorder called mid and then for right node go right side of mid and for left node left side of mid
    recursively and return root.

"""

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]


def buildTree(inorder, postorder):
    dct = {}
    for i ,val in enumerate(inorder):
        dct[val] = i

    def helper(low,high):
        if low > high:
            return None
        root = TreeNode(postorder.pop())
        mid = dct[root.val]
        root.right = helper(mid+1,high)
        root.left = helper(low,mid-1)
        return root
    
    return helper(0,len(inorder)-1)


node = buildTree(inorder, postorder)
def display(node):
    if not node:
        return 
    print(node.val)
    display(node.left)
    display(node.right)
    
print(display(node))
print()


"""
    Naive Solution
    Make a treenode(root) of popped the value from postorder find the index of that node.val in 
    inorder called mid and then for right node go right side of mid and for left node left side of mid
    recursively and return root.

"""


inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]


def buildTree1(inorder, postorder):
    if len(postorder) == 0 or len(inorder)==0:
        return None
    root = TreeNode(postorder.pop())
    mid = inorder.index(root.val)
    root.right = buildTree1(inorder[mid+1:],postorder)
    root.left = buildTree1(inorder[:mid],postorder)
    return root


node = buildTree1(inorder, postorder)
def display(node):
    if not node:
        return 
    print(node.val)
    display(node.left)
    display(node.right)
    
print(display(node))