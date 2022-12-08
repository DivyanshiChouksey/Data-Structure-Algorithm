# Leaf-Similar Trees


class TreeNode:
    def __init__(self, val, left=None, right=None):
        """
        if this was not a binary tree then we would have an array of children
        """
        self.val = val
        self.left = left
        self.right = right


"""
                10
            --------
            5       15
            
      --------      -------
      3       7     13    18
     --       --
    1         6

"""
node1 = TreeNode(10)
node2 = TreeNode(5)
node3 = TreeNode(15)
node4 = TreeNode(3)
node5 = TreeNode(7)
node6 = TreeNode(13)
node7 = TreeNode(18)
node8 = TreeNode(1)
node9 = TreeNode(6)


root1 = node1
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node4.right = node8
node5.right = node9

"""
                5
            --------
            4       8
            
        --------
        7       2

"""

node11 = TreeNode(5)
node12 = TreeNode(4)
node13 = TreeNode(8)
node14 = TreeNode(7)
node15 = TreeNode(2)

root2 = node11
node11.left = node12
node11.right = node13
node12.left = node14
node12.right = node15


"""
    Recursive solution
    Traverse the tree using pre-order traversal with an empty array to store the leave nodes in left to right order,
    for leave node - when node.left and node.right both is None this indicates that we have reached to leave node 
    of the that tree then add leave node to the array and do this for both trees after that 
    return Ture if both tree's array are same otherwise False. 
"""

# Time Complexity = O(n) || Space Complexity = O(n)


def leafSimilar(root1, root2):
    def helper(node, ans):
        if node is not None:
            if node.left is None and node.right is None:
                ans.append(node.val)
            helper(node.left, ans)
            helper(node.right, ans)
        return ans

    ans1 = []
    helper(root1, ans1)
    ans2 = []
    helper(root2, ans2)
    return ans1 == ans2


print(leafSimilar(root1, root2))
