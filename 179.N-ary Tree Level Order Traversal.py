# N-ary Tree Level Order Traversal


# Time Complexity = O(n^2) || Space Complexity = O(n)
class TreeNode:
    def __init__(self, val, children=None):
        """
        if this was not a binary tree then we would have an array of childre
        """
        self.val = val
        self.children = []


"""
                1
        -------------------
        3       2         4
    --------    
    5      6
    
"""
node1 = TreeNode(1)
node2 = TreeNode(3)
node3 = TreeNode(2)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

root = node1
node1.children.append(node2)
node1.children.append(node3)
node1.children.append(node4)
node2.children.append(node5)
node2.children.append(node6)


def levelOrder(root):
    if not root:
        return []
    stack = [root]
    ans = []
    while stack:
        tmp = []
        ans2 = []
        for node in stack:
            for ch in node.children:
                tmp.append(ch)
            ans2.append(node.val)

        stack = tmp[:]
        ans.append(ans2)
    return ans


print(levelOrder(root))

# # now printing LNR inorderTraversal
# def inOrder(node):
#     if node:
#         print(node.val, end=" ")
#         inOrder(node.children)


# inOrder(root)
