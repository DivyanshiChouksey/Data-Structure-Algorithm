# Maximum Width of Binary Tree

from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
    
        self.val = val
        self.left = left
        self.right = right


node1 = TreeNode(5)
node2 = TreeNode(4)
node3 = TreeNode(8)
node4 = TreeNode(7)
node5 = TreeNode(2)
node6 = TreeNode(9)
node7 = TreeNode(1)

root = node1
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node6
node4.left = node7

"""
                5
            --------
            4       8
            
        -------       --
        7     2         9
      --
      1

"""

"""
    EXPLANATION
    0. Pretty sure we have todo bfs, we can use 2 Queus or deque(doubly ended queue)

    1. According to Problem , we have also to count null nodes b/w two nodes.
            
            Tree                No of nodes
            5				1
           / \
          3   6				2
         /   /
        2   4				2

    2. Above example we have max 2 nodes in a level, but if you see the second level you
    will find that right child of 3 is NULL and therefore we also have to count that 
    NULL node, and with that the last level now contain 3 nodes, refer to diagram below.

           5				1
         /   \
       3       6			2
      /  \    /
     2  NULL  4				3 (NULL node also counted)

    So Last Level Contains 3 Nodes Including NULL.

    3 . We will also assign index to every node
        (if we are startting index from 0)
        
        (below is just formula to find index of node of complete binary tree)
        left(idx) = 2 idx + 1			// left child
        right(idx) = 2 idx + 2			// right child

        At starting root, idx = 0 so left node idx would be 2*0 +1 and right node index would be 2*0 + 2
        Index tree would be

            0				1
        /     \
        1       2				2
        /  \    /
        3    4  5				3 

        maxWidth would be 5-3+1 = 3

    Spoilers : Use a 2D queue and
            we will also insert index with node , so that we can keep track of index with their node

"""

# Time Complexity = O(n) || Space Complexity = O(n)

def widthOfBinaryTree( root):
    level = deque([(root,0)])
    maxWidth = 0
    while level:
        _,left = level[0]
        _,right = level[-1]
        maxWidth = max(maxWidth,((right-left)+1))
        for i in range(len(level)):
            node,idx = level.popleft()
            if node.left:
                level.append([node.left,(2*idx+1)])
            if node.right:
                level.append([node.right,(2*idx+2)])
        
    return maxWidth

print(widthOfBinaryTree( root))