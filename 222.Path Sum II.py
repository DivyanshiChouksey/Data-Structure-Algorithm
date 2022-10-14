# Path Sum II

root = [5]


def pathSum(root, targetSum):
    ans = []
    node = root

    def calSum(node, tmp, runningSum):
        if node:
            if (
                node.left is None
                and node.right is None
                and runningSum + node.val == targetSum
            ):
                ans.append(tmp + [node.val])
                return
            newRunningSum = runningSum + node.val
            calSum(node.left, tmp + [node.val], newRunningSum)
            calSum(node.right, tmp + [node.val], newRunningSum)

    calSum(root, [], 0)
    return ans
