# Branch Sum

root = 1
#
def branchSums(root):
    sums = []

    def calculateSum(node, runningSum, sums):
        if node is None:
            return
        newRunningSum = runningSum + node.value
        if node.left is None and node.right is None:
            sums.append(newRunningSum)
            return
        calculateSum(node.left, newRunningSum, sums)
        calculateSum(node.right, newRunningSum, sums)

    calculateSum(root, 0, sums)
    return sums
