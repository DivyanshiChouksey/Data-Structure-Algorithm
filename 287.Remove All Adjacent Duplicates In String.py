# Remove All Adjacent Duplicates In String

"""
    lets take a data Structure stack and iterate through the given string
    if current character is same as character on the top of stack then pop character from stack
    else append it in stack
    at the end return stack as string 
    
"""

# Time Complexity = O(n) || Space Complexity = O(n)

s = "abbaca"


def removeDuplicates(s):
    stack = []
    for char in s:
        if stack and char == stack[-1]:
            stack.pop()
        else:
            stack.append(char)
    return "".join(stack)


print(removeDuplicates(s))
