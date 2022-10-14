# Vertical Order Traversal of a Binary Tree

# Time Complexity = O(nlogn) || Space Complexity = O(n+h)
from collections import defaultdict


def verticalTraversal(self, root):
    dct = defaultdict(list)
    self.minCol = float("inf")
    self.maxCol = float("-inf")

    def helper(node, level, col):
        self.minCol = min(self.minCol, col)
        self.maxCol = max(self.maxCol, col)
        dct[col].append((level, node.val))
        if node.left:
            helper(node.left, level + 1, col - 1)
        if node.right:
            helper(node.right, level + 1, col + 1)

    # dct[0] = [(0,1)], dct[1] =[(-1,2),(1,3)]

    helper(root, 0, 0)
    ans = []
    for i in range(self.minCol, self.maxCol + 1):
        ans += [[j for i, j in sorted(dct[i])]]
    return ans
