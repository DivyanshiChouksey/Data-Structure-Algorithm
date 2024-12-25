# Find Largest Value in Each Tree Row

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        node = root
        queue = deque()
        queue.append(node)
        ans = []
        while queue:
            tmp = []
            maxVal = float("-inf")
            for i in range(len(queue)):
                node = queue.popleft()
                maxVal = max(maxVal,node.val)
                if node.left:
                    # if node.left.val> maxVal:
                    #     maxval = node.left.val
                    queue.append(node.left)
                if node.right:
                    # if node.right.val > maxVal:
                    #     maxVal = node.right.val
                    queue.append(node.right)
            
            ans.append(maxVal)
    
        return ans

