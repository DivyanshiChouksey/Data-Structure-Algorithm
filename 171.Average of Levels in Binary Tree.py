# Average of Levels in Binary Tree


class TreeNode:
    def __init__(self, val, left=None, right=None):
        """
        if this was not a binary tree then we would have an array of children
        """
        self.val = val
        self.left = left
        self.right = right


"""
                3
            --------
            9      20
            
                 --------
                 15     7

"""

node11 = TreeNode(3)
node12 = TreeNode(9)
node13 = TreeNode(20)
node14 = TreeNode(15)
node15 = TreeNode(7)

root = node11
node11.left = node12
node11.right = node13
node13.left = node14
node13.right = node15


"""
    Do Level Order Traversal and find average of each level and append it to the ans 
    return the ans 
"""

# Time Complexity = O(n) || Space Complexity = O(n)


def averageOfLevels(root):
    # level order traversal
    stack = [root]
    ans = []
    node = root
    while stack:
        tmp = []
        total = 0
        for node in stack:
            total += node.val
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)

        ans.append(total / len(stack))
        stack = tmp[:]

    return ans


print(averageOfLevels(root))
