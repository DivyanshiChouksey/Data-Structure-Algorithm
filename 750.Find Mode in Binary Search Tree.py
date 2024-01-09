# Find Mode in Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # [1,1,2,3,3,4,4,4]
        # ans = [4]
        # maxStrak = 3
        # curNum = 4
        # curCount = 3
        arr = []
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)

        inorder(root)
        
        ans = [arr[0]]
        maxStreak = 1
        cur = arr[0]
        count = 1

        print(arr)

        i=1
        while i<len(arr):
            if arr[i-1] == arr[i]:
                count+=1
            if arr[i-1] != arr[i]:
                count = 1
            if count>maxStreak :
                ans = [arr[i]]
                maxStreak = count
            if count == maxStreak: 
                if arr[i]!=ans[-1]:
                    ans.append(arr[i])
            i+=1
        return ans
