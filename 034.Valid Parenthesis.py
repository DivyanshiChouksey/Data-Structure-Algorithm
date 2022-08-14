# Valid Parenthesis
"""
    Make a dictionary to store brackets with their matches
    lets take a data Structure stack and iterate through the given array if we got openning brackets then append it in stack,
    and if there is closing brackets and if an empty stack then return False or else check if match of closing backet is in top of stack then pop openning bracket.
    return True if stack is empty.
    
"""
# Time Complexity = O(n) || Space Complexity = O(n)

s = "[{()}]"


def isValid(s):
    dct = {"}": "{", "]": "[", ")": "("}
    stack = []
    for i in s:
        if i in "[({":
            stack.append(i)
        if i in "])}":
            if len(stack) == 0:
                return False
            temp = stack.pop()
            if dct[i] == temp:
                continue
            else:
                return False
    if len(stack) != 0:
        return False
    return True


print(isValid(s))
