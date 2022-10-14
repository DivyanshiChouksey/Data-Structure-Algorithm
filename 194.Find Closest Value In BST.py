# Find Closest Value In BST

tree = 10
targert = 12

# Recursive solution


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def findClosestValueInBST(tree):
    return findClosestValueHelper(tree, targert, tree.value)


def findClosestValueHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueHelper(tree.right, target, closest)
    else:
        closest


# Iterative solution


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def findClosestValueInBST(tree):
    return findClosestValueHelper(tree, targert, tree.value)


def findClosestValueHelper(tree, target, closest):
    node = tree
    while node is not None:
        if abs(target - closest) > abs(target - node.value):
            closest = node.value
        if target < node.value:
            node = node.left
        elif target > node.value:
            node = node.right
        else:
            break
    return closest
