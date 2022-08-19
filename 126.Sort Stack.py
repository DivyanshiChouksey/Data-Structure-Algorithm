# Sort Stack
"""
    Go through the stack and do pop and insert elements in sorted order 
    by using recursive method in the same stack
"""

# Time Complexity = O(n^2) || Space Complexity = O(n)

stack = [-5, 2, -2, 4, 3, 1]


def sortStack(stack):
    if len(stack) == 0:
        return stack

    top = stack.pop()
    sortStack(stack)
    insertInSortOrder(stack, top)
    return stack


def insertInSortOrder(stack, value):
    if len(stack) == 0 or stack[len(stack) - 1] <= value:
        stack.append(value)
        return
    top = stack.pop()
    insertInSortOrder(stack, value)
    stack.append(top)


print(sortStack(stack))
