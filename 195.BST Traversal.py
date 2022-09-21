# BST Traversal


class TreeNode:
    def __init__(self, val, left=None, right=None):
        """
        if this was not a binary tree then we would have an array of children
        """
        self.val = val
        self.left = left
        self.right = right


node1 = TreeNode(5)
node2 = TreeNode(4)
node3 = TreeNode(8)
node4 = TreeNode(7)
node5 = TreeNode(2)

tree = node1
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

# In-OrderTraverse
"""
    Algorithm Inorder(tree) :-
        1.Traverse the left subtree, i.e., call Inorder(left->subtree)
        2.Visit the root.
        3.Traverse the right subtree, i.e., call Inorder(right->subtree)
"""
# Time Complexity = O(n) || Space Complexity = O(n)


def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.val)
        inOrderTraverse(tree.right, array)
    return array


# Pre-Order Traverse
"""
    Algorithm Preorder(tree) :-
        1.Visit the root.
        2.Traverse the left subtree, i.e., call Preorder(left->subtree)
        3.Traverse the right subtree, i.e., call Preorder(right->subtree) 
"""
# Time Complexity = O(n) || Space Complexity = O(n)


def preOrderTraverse(tree, array):
    if tree is not None:
        array.append(tree.val)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
    return array


# Post-OrderTraverse
"""
    Algorithm Postorder(tree) :-
        1.Traverse the left subtree, i.e., call Postorder(left->subtree)
        2.Traverse the right subtree, i.e., call Postorder(right->subtree)
        3.Visit the root
"""
# Time Complexity = O(n) || Space Complexity = O(n)


def postOrderTraverse(tree, array):
    if tree is not None:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.val)
    return array


print(preOrderTraverse(tree, array=[]))
print(inOrderTraverse(tree, array=[]))
print(postOrderTraverse(tree, array=[]))
