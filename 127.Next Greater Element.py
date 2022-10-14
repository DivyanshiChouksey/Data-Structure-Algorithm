array = [2, 5, -3, -4, 6, 7, 2]


def nextGreaterElement(array):
    res = [-1] * len(array)
    stack = []

    for i in range(2 * len(array)):
        idx = i % len(array)
        while len(stack) > 0 and array[stack[len(stack) - 1]] < array[idx]:
            top = stack.pop()
            res[top] = array[idx]

        stack.append(idx)

    return res


print(nextGreaterElement(array))
