# Unique Binary Search Trees II

from functools import lru_cache

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def generateTrees(n):
    @lru_cache(None)
    def dfs(left, right):
        if left > right: 
            return [None]
        if left == right: 
            return [TreeNode(left)]
        ans = []
        for root in range(left, right+1):
            leftNodes = dfs(left, root - 1)
            rightNodes = dfs(root+1, right)
            for leftNode in leftNodes:
                for rightNode in rightNodes:
                    rootNode = TreeNode(root, leftNode, rightNode)
                    ans.append(rootNode)
        return ans
    
    return dfs(1, n)


n=3 
result = generateTrees(n)

def preTraverse(node, ans):
    if node is None:
        return
    ans.append(node.val)
    preTraverse(node.left, ans)
    preTraverse(node.right, ans)

    return ans
    
for res in result:
    print(preTraverse(res,[]))
    