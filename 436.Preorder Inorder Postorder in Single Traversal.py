# Preorder Inorder Postorder in Single Traversal

# Time Complexity = O(n) , n =3*n
# Space Complexity = O(n) , n = 4*n

class TreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

node1 = TreeNode(5)
node2 = TreeNode(4)
node3 = TreeNode(8)
node4 = TreeNode(7)
node5 = TreeNode(2)

root = node1
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5

"""
                5
            --------
            4       8
            
        --------
        7       2

"""

def getTreeTraversal(root):
     
    stack = [[root,1]]
    pre = []
    inorder = []
    post = []
    if not root:
        return inorder,pre,post
    while stack:
        node,num = stack.pop()
        if num == 1:
            pre.append(node.data)
            num +=1
            stack.append([node,num])
            if node.left :
                stack.append([node.left,1])
        
        elif num == 2:
            inorder.append(node.data)
            num+=1
            stack.append([node,num])
            if node.right:
                stack.append([node.right,1])
        
        else:
            post.append(node.data)

    return inorder,pre,post



print(getTreeTraversal(root))