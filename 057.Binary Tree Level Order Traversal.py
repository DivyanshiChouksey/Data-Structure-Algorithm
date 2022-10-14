class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        ans = []
        queue = [root]
        while queue:  # height times run hoga
            ans2 = []
            for i in range(len(queue)):  # elements at every level
                node = queue.pop(0)
                ans2.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(ans2)
        return ans


def levelOrder(self, root):
    ans = []
    queue = [root]
    while queue:
        ans2 = []
        tmp = []
        for node in queue:
            ans2.append(node.val)
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
        queue = tmp
        ans.append(ans2)
    return ans
