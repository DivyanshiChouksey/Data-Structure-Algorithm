# Branch Sum

def branchSum(tree):
    node = tree
    if node is None:
        return None
    
    def calculateSum(node,runningSum,sums):
        