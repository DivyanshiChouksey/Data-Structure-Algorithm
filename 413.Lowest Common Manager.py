# Lowest Common Manager

# Time Complexity = O(n) || Space Complexity = O(d)

class TreeNode:
    def __init__(self, val, children=None):
        self.val = val
        self.children = []

# # This is an input class. Do not edit.
# class OrgChart:
#     def __init__(self, name):
#         self.name = name
#         self.directReports= []

"""
                A
        -------------------
        B       C         D
    --------    
    E      F
            --
            G
    
"""
node1 = TreeNode("A")
node2 = TreeNode("B")
node3 = TreeNode("C")
node4 = TreeNode("D")
node5 = TreeNode("E")
node6 = TreeNode("F")
node7 = TreeNode("G")


root = node1
node1.children.append(node2)
node1.children.append(node3)
node1.children.append(node4)
node2.children.append(node5)
node2.children.append(node6)
node6.children.append(node7)

reportOne ="E"
reportTwo = "G"

def getLowestCommonManager(root, reportOne, reportTwo):    
    def dfs(node):
        count = 0
        if node.val == reportOne or node.val == reportTwo:
            count+=1
        for neigh in node.children:
            manager,cnt = dfs(neigh) 
            if manager :
                return (manager,2)
            count += cnt
            if count ==2 :
                return (node,2)
        return (None,count) 
    
    manager,count = dfs(root)
    return manager


ans = getLowestCommonManager(root, reportOne, reportTwo)
print(ans.val)