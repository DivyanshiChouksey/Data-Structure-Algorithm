class TreeNode:
    def __init__(self, val, left=None, right=None):
        """
        if this was not a binary tree then we would have an array of children
        """
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


# class Solution:
def rightSideView(root):
    # standard code for BFS
    if not root:
        return []
    ans = []
    queue = [root]
    while queue:
        ans.append(queue[-1].val)
        tmp = []
        for node in queue:
            if node.left:  # if node.left is not None
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
        queue = tmp
    return ans


def rightSideView(root):
    #    N R L
    ans = []

    def helper(node, d):
        if node is not None:
            if len(ans) == d:
                ans.append(node.val)
            helper(node.right, d + 1)
            helper(node.left, d + 1)

    helper(root, 0)
    return ans


print(rightSideView(root))


def leftSideView(root):
    #    N L R
    ans = []

    def helper(node, d):
        if node is not None:
            if len(ans) == d:
                ans.append(node.val)
            helper(node.left, d + 1)
            helper(node.right, d + 1)

    helper(root, 0)
    return ans


print(leftSideView(root))
