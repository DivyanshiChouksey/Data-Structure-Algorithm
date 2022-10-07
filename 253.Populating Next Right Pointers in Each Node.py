# Populating Next Right Pointers in Each Node
# (Similar with Right Sibling Tree)


class TreeNode:
    def __init__(self, value: int = 0, left=None, right=None, next=None):
        self.val = value
        self.left = left
        self.right = right
        self.next = next


"""
                5                             5 --> None
            --------                        /   \
            4       8                      4 --> 8--->None
        ------     ------                /  \    / \
        7     2    3     1              7--> 2-> 3->1-->None

"""


# Iterative Solution
# Time Complexity = O(n) || Space Complexity = O(n)


def connect(root):
    if root is None:
        return None
    queue = [root]
    while queue:
        tmp = []
        for node in queue:
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)

        for i in range(len(tmp) - 1):
            tmp[i].next = tmp[i + 1]

        queue = tmp[:]

    return root


# Recursive Solution
# Time Complexity = O(n) || Space Complexity = O(h)
# but if we ignore recursion stack then space is constant


def connect2(root):
    def findNext(node):
        if node in None:
            return None
        if node.left:
            return node.left
        if node.right:
            return node.right
        return findNext(node.next)

    def helper(node):
        if root is None:
            return None
        if root.left:
            if root.right:
                root.left.next = root.right
            else:
                root.left.next = findNext(root.next)
        if root.right:
            root.right.next = findNext(root.next)

        helper(root.left)
        helper(root.right)

    helper(root)
    return root
