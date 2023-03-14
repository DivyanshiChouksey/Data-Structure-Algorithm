# Symmetrical Tree

class TreeNode:
    def __init__(self, val, left=None, right=None):
        
        self.val = val
        self.left = left
        self.right = right


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(2)
node4 = TreeNode(3)
node5 = TreeNode(3) 
node6 = TreeNode(4)
node7 = TreeNode(4)
node8 = TreeNode(5)
node9 = TreeNode(5)
node10 = TreeNode(6) 
node11 = TreeNode(6) 


"""
Initailize two stack stackLeft with root.left node in it and stackRight with root.right node in it then pop from
both stack and store it in left and right variable respectively then check if popped node are not equal then return 
false after that for symmerty or we can say to keep record
of mirror image we have to check root's rightsubtree is the invert of root's leftsubtree
the tricky part is that in left stack we push left node first then right node second of popped node from left stack
and in right stack we push right node first then left node second of popped node from right and repeat the process
at the end return True 


                  1
            ------------
            2          2
        -------     -------
        3     4     4     3  
     ------             ------   
     5    6             5    6
                     
"""

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Time Complexity = O(n) || Space Complexity = O(n)

def symmetricalTree(tree):
    stackLeft = [tree.left]
    stackRight = [tree.right]

    while len(stackLeft)>0:
        left = stackLeft.pop()
        right = stackRight.pop()
        if left is None and right is None:
            continue
        if left is None or right is None or left.value!= right.value:
            return False

        stackLeft.append(left.left)
        stackLeft.append(left.right)
        stackRight.append(right.right)
        stackRight.append(right.left)

    return True


"""
    Recursive Solution 
    using same approach as above 
"""

def symmetricalTree2(root):
    def helper(nodeleft,noderight):
        if nodeleft is None and noderight is None:
            return True
        if nodeleft is None or noderight is None or nodeleft.val != noderight.val:
            return False
        return helper(nodeleft.left,noderight.right) and helper(nodeleft.right,noderight.left)

    return helper(root.left,root.right)


