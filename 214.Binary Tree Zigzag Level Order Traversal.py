# Binary Tree Zigzag Level Order Traversal


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(3)
node1 = TreeNode(9)
node2 = TreeNode(20)
node3 = TreeNode(15)
node4 = TreeNode(7)


if root is None:
    print("[]")
ans = []
level = 1
queue = [root]
while queue:
    tmpans = []
    tmp = []
    for node in queue:
        tmpans.append(node.val)
        if node.left:
            tmp.append(node.left)
        if node.right:
            tmp.append(node.right)
    queue = tmp[:]
    if level % 2 == 0:
        ans.append(tmpans[::-1])
    else:
        ans.append(tmpans)
    level += 1
# return ans
print(ans)
