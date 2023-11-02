# Count Nodes Equal to Average of Subtree


class TreeNode:
    def __init__(self, val, left=None, right=None):
        """
        if this was not a binary tree then we would have an array of children
        """
        self.val = val
        self.left = left
        self.right = right


"""
                4
            --------
            8       5
            
        --------       ---
        0      1         6

"""
node1 = TreeNode(4)
node2 = TreeNode(8)
node3 = TreeNode(5)
node4 = TreeNode(0)
node5 = TreeNode(1)
node7 = TreeNode(6)


root = node1
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node7



def averageOfSubtree(root):
    ans = 0
    def dfs(node,curSum,count):
        if not node:
            return (0,0)
        nonlocal ans
        if not node.left and not node.right:
            ans+=1
            return (node.val,1)
            
        leftSum, leftCnt, rightSum, rightCnt = 0,0,0,0
        if node.left:
            leftSum, leftCnt = dfs(node.left, curSum, count)
        if node.right:
            rightSum, rightCnt = dfs(node.right, curSum, count)

        curSum = leftSum + node.val + rightSum
        count = leftCnt + rightCnt + 1
        avg = curSum//count
        if avg == node.val:
            ans+=1
        return (curSum,count)
        
    dfs(root,0,0)
    return ans



print(averageOfSubtree(root))