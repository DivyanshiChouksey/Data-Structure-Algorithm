# All Nodes Distance K in Binary Tree

root = [3,5,1,6,2,0,8,null,null,7,4]
target = 5
k = 2

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
      

def distanceK(root, target, k) :
    def add_parent(cur, parent):
        if cur:
            cur.parent = parent
            add_parent(cur.left, cur)
            add_parent(cur.right, cur) 
    add_parent(root, None)
    
    answer = []
    visited = set()
    def dfs(cur, distance):
        if not cur or cur in visited:
            return
        visited.add(cur)
        if distance == 0:
            answer.append(cur.val)
            return
        dfs(cur.parent, distance - 1)
        dfs(cur.left, distance - 1)
        dfs(cur.right, distance - 1)
        
    dfs(target, k)
    return answer

print(distanceK(root, target, k))
