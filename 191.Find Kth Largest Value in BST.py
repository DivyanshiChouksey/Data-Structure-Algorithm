# Find Kth Largest Value in BST


class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


node1 = BST(1)
node2 = BST(3)
node3 = BST(2, node1, node2)
node4 = BST(5)
node5 = BST(5, node3, node4)
node6 = BST(17)
node7 = BST(22)
node8 = BST(20, node6, node7)
tree = BST(15, node5, node8)

k = 3

# Naive Solution
"""
    Store all node values in an array with the help of InOrder traversal in BST 
    so that will get sorted array and after that return kth value from the end of the array.

"""
# Time Complexity = O(n) || Space Complexity = O(n)


def findKthLargestValueInBst(tree, k):
    ans = []
    inOrderTraverse(tree, ans)
    return ans[len(ans) - k]


def inOrderTraverse(node, ans):
    if node is None:
        return
    inOrderTraverse(node.left, ans)
    ans.append(node.value)
    inOrderTraverse(node.right, ans)


print(findKthLargestValueInBst(tree, k))


# Optimal Solution
"""
    Here we would keep track of no. of visited nodes and latest visited node value
    and traverse through the tree in reverse InOrder traversal (ie. right, node, left)
    so that we can start from largest value until we visited the kth node
    after that return latest visited node value.
"""
# Time Complexity = O(k+h) , h = height of tree
# Space Complexity = O(h)


class TreeInfo:
    def __init__(self, count, visited):
        self.count = count
        self.visited = visited


def findKthLargestValueInBst2(tree, k):
    treeInfo = TreeInfo(0, -1)
    reverseInOrder(tree, k, treeInfo)
    return treeInfo.visited


def reverseInOrder(node, k, treeInfo):
    if node is None or treeInfo.count >= k:
        return
    reverseInOrder(node.right, k, treeInfo)
    if treeInfo.count < k:
        treeInfo.count += 1
        treeInfo.visited = node.value
        reverseInOrder(node.left, k, treeInfo)


print(findKthLargestValueInBst2(tree, k))
