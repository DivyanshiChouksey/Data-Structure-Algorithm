# Binary Tree Inorder Traversal


def inorderTraversal(root):
    ans = []

    def inOrder(root):
        if root is None:
            return []
        inOrder(root.left)
        ans.append(root.val)
        inOrder(root.right)

    inOrder(root)
    return ans
