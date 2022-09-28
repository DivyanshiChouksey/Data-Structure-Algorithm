# Backspace String Compare
"""
    Create 2 stacks to store characters for S and T 
    go through the strings S and append the characters in stacks but when we come across "#"
    then pop the top most character of stack and done the same for string T 
    and return True if both stack is equal. 
"""
# Time Complexity = O(n) || Space Complexity = O(n)

s = "ab#c"
t = "ad#c"


def backspace(s, t):
    stack1 = []
    for i in s:
        if i == "#":
            if len(stack1) == 0:
                continue
            else:
                stack1.pop()
        else:
            stack1.append(i)

    stack2 = []
    for i in t:
        if i == "#":
            if len(stack2) == 0:
                continue
            else:
                stack2.pop()
        else:
            stack2.append(i)

    return stack1 == stack2


print(backspace(s, t))
