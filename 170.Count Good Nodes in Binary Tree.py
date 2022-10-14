# Count Nodes in Binary Tree

root = 3

count = 0


def helper(node, currentMax):
    if node.val >= currentMax:
        count += 1
        currentMax = max(currentMax, node.val)
    if node.left:
        helper(node.left, currentMax)
    if node.right:
        helper(node.right, currentMax)


helper(root, float("-inf"))
print(count)
