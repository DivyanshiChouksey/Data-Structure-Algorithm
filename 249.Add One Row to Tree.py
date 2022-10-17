# Add One Row To Tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
                5
            --------
            4       8
            
        --------
        7       2

"""

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


# Iterative Solution
"""
    In this we make a queue in which we keep record of node with its depth initially root node and 1 depth
    then compare the depth and if true then make new node left as current node left and then make current node left to new node
    and return but if depth is not True then take an another array to store current node's children and then make
    tmp our queue and do the same.
    
"""
# Time Complexity = O(n) || Space Complexity = O(n)


def addOneRow(root, val, depth):
    if root and depth == 1:
        return TreeNode(val, root)
    queue = [(root, 1)]
    while queue and queue[-1][-1] != depth:
        tmp = []
        for node, level in queue:
            if level == depth - 1:
                node1 = TreeNode(val)
                node1.left = node.left
                node.left = node1
                node2 = TreeNode(val)
                node2.right = node.right
                node.right = node2
            if node.left:
                tmp.append((node.left, level + 1))
            if node.right:
                tmp.append((node.right, level + 1))
        queue = tmp[:]
    return root


# Recursive Solution
"""
    Make a recurvise call of left and right nodes until we reach to given level 
    after that store node left to tmp variable and make current node left new node with given value
    and then make new node left tmp and do this for its right node (vice versa) and return the head
"""
# Time Complexity = O(n) || Space Complexity = O(n)


def addOneRow2(root, val, depth):
    if root and depth == 1:
        return TreeNode(val, root)

    def helper(node, level):
        if node:
            if level == depth - 1:
                node1 = TreeNode(val)
                tmp = node.left
                node.left = node1
                node1.left = tmp
                node2 = TreeNode(val)
                tmp2 = node.right
                node.right = node2
                node2.right = tmp2

            helper(node.left, level + 1)
            helper(node.right, level + 1)

    helper(root, 1)
    return root


# Traverse
def inOrder(node):
    if node:
        inOrder(node.left)
        print(node.val, end=" ")
        inOrder(node.right)


m = addOneRow2(root, 1, 2)
inOrder(m)
