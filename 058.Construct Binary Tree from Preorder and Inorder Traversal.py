class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# pre => NLR in => LNR
class Solution:
    def buildTree(self, preorder, inorder):
        preOrderIndex = 0
        dct = {}
        for idx, ele in enumerate(inorder):
            dct[ele] = idx

        def helper(left, right):
            nonlocal preOrderIndex  # Global variable
            if left > right:
                return None
            rootValue = preorder[preOrderIndex]
            root = TreeNode(rootValue)
            preOrderIndex += 1
            root.left = helper(left, dct[rootValue] - 1)
            root.right = helper(dct[rootValue] + 1, right)
            return root

        return helper(0, len(inorder) - 1)


def buildTree(self, preorder, inorder):
    if inorder == [] or preorder == []:
        return None
    root = TreeNode(preorder[0])
    # we need to find 3 in our inorder
    mid = inorder.index(preorder[0])
    root.left = self.buildTree(preorder[1 : mid + 1], inorder[: mid + 1])
    root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
    return root
