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


def inOrder(node):
    if node:
        inOrder(node.left)
        print(node.val, end=" ")
        inOrder(node.right)


m = addOneRow2(root, 1, 2)
inOrder(m)
