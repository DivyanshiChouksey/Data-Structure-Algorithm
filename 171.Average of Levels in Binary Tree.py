# Average of Levels in Binary Tree

root = 3

stack = []
ans = []
node = root
while node:
    tmp = []
    total = 0
    for node in stack:
        total += node.val
        if node.left:
            tmp.append(node.left)
        if node.right:
            tmp.append(node.right)

    ans.append(total / len(stack))
    stack = tmp[:]

print(ans)
