# Reconstruct BST


preOrderTraversal = [10, 4, 2, 1, 5, 17, 19, 18]

# Time Complexity = O(n^2) || Space Complexity = O(n)


class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversal):
    if len(preOrderTraversal) == 0:
        return None

    current = preOrderTraversal[0]
    rightSubTree = len(preOrderTraversal)

    for i in range(1, len(preOrderTraversal)):
        if preOrderTraversal[i] >= current:
            rightSubTree = i
            break

    leftSubTree = reconstructBst(preOrderTraversal[1:rightSubTree])
    rightSubTree = reconstructBst(preOrderTraversal[rightSubTree:])
    return BST(current, leftSubTree, rightSubTree)
