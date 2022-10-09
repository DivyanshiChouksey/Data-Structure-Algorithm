# Two Sum IV input BST

"""
                5
            --------
            3       6
            
    --------        ---
    2      4          7

"""

# Time Complexity = O(n) || Space Complexity = O(n)

root = 5


def findTarget(self, root, target: int) -> bool:
    node = root
    self.found = False
    self.visited = set()

    def helper(node):
        if self.found:
            return True
        if node.val in self.visited:
            self.found = True
        self.visited.add(target - node.val)
        if node.left:
            helper(node.left)
        if node.right:
            helper(node.right)

    helper(root)
    return self.found


# output - True
