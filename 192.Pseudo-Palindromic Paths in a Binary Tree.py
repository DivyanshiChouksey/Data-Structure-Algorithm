# Pseudo-Palindromic Paths in a Binary Tree

from collections import defaultdict


root = [2, 3, 1, 3, 1, "null", 1]


def pseudoPalindromicPaths(self, root) -> int:
    self.num_pseudo_palindromic = 0

    def is_pseudo_palindromic(path: dict) -> bool:
        one_odd = False
        for count in path.values():
            if count % 2 == 1:
                if one_odd:
                    return False
                one_odd = True
        return True

    def helper(node, path: dict):  # path is counter/Dict :)
        if node:
            path[node.val] += 1  # increase the counter
            if not node.left and not node.right:
                if is_pseudo_palindromic(path):
                    self.num_pseudo_palindromic += 1
            helper(node.left, path)
            helper(node.right, path)
            path[node.val] -= 1  # clean implemntation

    helper(root, defaultdict(int))
    return self.num_pseudo_palindromic
