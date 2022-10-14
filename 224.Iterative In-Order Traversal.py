# Iterative In-Order Traversal


def iterativeInOrderTraversal(tree, callback):
    prev = None
    node = tree
    while node:
        if prev is None or prev == node.parent:
            if node.left:
                next = node.left
            else:
                callback(node)
                next = node.right if node.right is not None else node.parent
        elif prev == node.left:
            callback(node)
            next = node.right if node.right is not None else node.parent
        else:
            next = node.parent

        prev = node
        node = next


# def iterativeInOrderTraversal(tree, callback):
#     prev = None
#     node = tree
#     while node :
#         if prev is None or prev == node.parent:
#             if node.left :
#                 next = node.left
#             else:
#                 callback(node)
#                 next = node.right if node.right is not None else node.parent
#         elif prev == node.left:
#             callback(node)
#             next = node.right if node.right is not None else node.parent
#         else:
#             next = node.parent

#         prev = node
#         node = next
