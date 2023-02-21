# Lowest Common Ancestor of a Binary Search Tree

# Time Complexity = O(n) || Space Complexity = O(d)

class TreeNode:
    def __init__(self, val, left=None , right = None):
        self.val = val
        self.left = left
        self.right = right


"""
                6
           -----------
          2           8    
       --------    
       0      4
                --
                 5
    
"""
node1 = TreeNode("6")
node2 = TreeNode("2")
node3 = TreeNode("8")
node5 = TreeNode("0")
node6 = TreeNode("4")
node7 = TreeNode("5")


root = node1
node1.left = node2
node1.right=node3
node2.left=node5
node2.right=node6
node6.right=node7

p =TreeNode("0")
q = TreeNode("5")



def lowestCommonAncestor(root, p, q):
    left = p.val if p.val<q.val else q.val
    right = p.val if p.val>q.val else q.val

    if root:
        if left <= root.val <= right:
            return root
        elif left<root.val and right<root.val:
            return lowestCommonAncestor(root.left, p, q)
        else:
            return lowestCommonAncestor(root.right, p, q)

node = lowestCommonAncestor(root, p, q)
print(node.val)

def lowestCommonAncestor2(root, p, q):
    left = p.val if p.val<q.val else q.val
    right = p.val if p.val>q.val else q.val

    while root:
        if left <= root.val <= right:
            return root
        elif left<root.val and right<root.val:
            root = root.left
        else:
            root = root.right

node1 = lowestCommonAncestor2(root, p, q)
print(node1.val)