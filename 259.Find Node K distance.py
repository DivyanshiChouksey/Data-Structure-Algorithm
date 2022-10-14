#
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


"""
                5
            --------
            4       8
            
        --------  -------
        7     -2  -1    4

"""
node1 = TreeNode(5)
node2 = TreeNode(4)
node3 = TreeNode(8)
node4 = TreeNode(7)
node5 = TreeNode(-2)
node6 = TreeNode(-1)
node7 = TreeNode(9)
node8 = TreeNode(1)
node9 = TreeNode(3)

tree = node1
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node7
node3.left = node6
node7.left = node8
node7.right = node9


def findNodesDistanceK(tree, target, k):
    nodeToParent = {}
    populateNodeToParents(tree, nodeToParent)
    targetNode = getNodeFormValue(target, tree, nodeToParent)

    return bfs(targetNode, nodeToParent, k)


def bfs(targetNode, nodeToParent, k):
    seen = {targetNode.value}
    queue = [(targetNode, 0)]
    while queue:
        node, distance = queue.pop(0)
        if distance == k:
            out = [x.value for x, y in queue]
            out.append(node.value)
            return out
        currentNode = [node.left, node.right, nodeToParent[node.value]]
        for node in currentNode:
            if node is not None and node.value not in seen:
                seen.add(node.value)
                queue.append((node, distance + 1))
            else:
                continue
    return []


def getNodeFormValue(val, root, nodeToParent):
    if root.value == val:
        return root
    # find its parent and then
    nodeParent = nodeToParent[val]
    if nodeParent.left and nodeParent.left.value == val:
        return nodeParent.left

    return nodeParent.right


def populateNodeToParents(node, nodeToParent, parent=None):
    if node is not None:
        nodeToParent[node.value] = parent
        populateNodeToParents(node.left, nodeToParent, node)
        populateNodeToParents(node.right, nodeToParent, node)


print(findNodesDistanceK(tree, 8, 2))
