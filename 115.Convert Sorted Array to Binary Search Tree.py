# Convert Sorted Array to Binary Search Tree

nums = [-10, -3, 0, 5, 9]


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        mid = len(nums) // 2  # l + (r-l)/2
        root = TreeNode(nums[mid])
        # left, right
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1 :])
        return root


s1 = Solution()
s1.sortedArrayToBST(nums)
#
