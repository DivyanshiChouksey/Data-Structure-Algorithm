# Boundary Traversal of Binary Tree

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


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


def traverseBoundary(root):
    res = []
    if not root:
        return res
    if not isLeaf(root):
        res.append(root.data)
    addLeft(root,res)
    addLeaves(root,res)
    addRight(root,res)
    return res

def isLeaf(node):
    if not node.left and not node.right:
        return True
    else:
        return False

        
def addLeft(root,res):
    cur = root.left
    while cur:
        if not isLeaf(cur):
            res.append(cur.data)
        if cur.left:
            cur = cur.left
        else:
            cur = cur.right


def addRight(root,res):
    cur = root.right
    tmp = []
    while cur:
        if not isLeaf(cur) :
            tmp.append(cur.data)
        if cur.right:
            cur = cur.right
        else:
            cur = cur.left
    for t in tmp[::-1]:
        res.append(t)


def addLeaves(root,res):
    if isLeaf(root):
        res.append(root.data)
        return 
    if root.left:
        addLeaves(root.left,res)
    if root.right:
        addLeaves(root.right,res)
        

print(traverseBoundary(root))