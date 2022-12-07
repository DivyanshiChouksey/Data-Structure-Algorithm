# Range Sum of BST


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


root = node1
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node4.right = node8
node5.right = node9


"""
    Recursive solution 
    Taking a variable ans to keep record of sum of node values in range of low and high after that 
    if the current value is not None and the current node value is in the range of low and high 
    then add it to ans and then go to the left node and right node of the current node and check the same condition 
    at the end return ans.  
"""

# Time Complexity = O(n) || Space Complexity = O(h) ,h-height of tree


def rangeSumBST(root, low, high):
    node = root
    ans = 0

    def helper(node, low, high):
        nonlocal ans
        if node is not None:
            if low <= node.val <= high:
                ans += node.val
            helper(node.left, low, high)
            helper(node.right, low, high)

    helper(root, low, high)
    return ans


print(rangeSumBST(root, 6, 10))
