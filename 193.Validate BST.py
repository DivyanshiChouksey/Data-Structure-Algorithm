# Validate BST


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return validateHelper(tree, float("-inf"), float("inf"))


def validateHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False
    leftIsValid = validateHelper(tree.left, minValue, tree.value)
    return leftIsValid and validateHelper(tree.right, tree.value, maxValue)
