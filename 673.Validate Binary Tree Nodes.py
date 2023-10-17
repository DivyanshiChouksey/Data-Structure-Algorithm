# Validate Binary Tree Nodes

n = 4
leftChild = [1,-1,3,-1]
rightChild = [2,-1,-1,-1]


def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
    def find_root():
        children = set(leftChild) | set(rightChild)
        
        for i in range(n):
            if i not in children:
                return i
            
        return -1
    
    root = find_root()
    if root == -1:
        return False
    
    seen = {root}
    stack = [root]
    while stack:
        node = stack.pop()
        for child in [leftChild[node], rightChild[node]]:
            if child != -1:
                if child in seen:
                    return False
                
                stack.append(child)
                seen.add(child)
    
    return len(seen) == n
