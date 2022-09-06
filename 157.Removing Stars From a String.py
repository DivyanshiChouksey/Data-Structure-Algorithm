# Removing Stars From a String
"""
    Create a stack and append character of string "S" one by one and if found a "*" then
    pop the top most character from the stack and return remaining character of stack as a string.
"""
# Time Complexity = O(n) || Space Complexity = O(n)

s = "leet**cod*e"


def removeStars(s: str) -> str:
    stack = []
    for ch in s:
        if ch == "*":
            if len(stack) == 0:
                continue
            else:
                stack.pop()
        else:
            stack.append(ch)
    return "".join(stack)


print(removeStars(s))
