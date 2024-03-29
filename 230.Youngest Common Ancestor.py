class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(
    self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
) -> "TreeNode":
    # def __init__(self):
    #     self.ans = None

    stack = [root]
    parent = {root: None}

    while p not in parent or q not in parent:
        node = stack.pop()
        if node.left:
            parent[node.left] = node
            stack.append(node.left)
        if node.right:
            parent[node.right] = node
            stack.append(node.right)
    ancestor = set()
    while p:
        ancestor.add(p)
        p = parent[p]
    while q not in ancestor:
        q = parent[q]
    return q
