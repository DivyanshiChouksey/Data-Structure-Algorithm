# Make The String Great

string = "leEeetcode"

"""
    lets take a data Structure stack and iterate through the given string 
    lower case alphabet is already in stack, and if we found similar Upper case alphabet or vive versa
    (using ASCII values for checking lower or upper case alphabets)
    then pop the character from the stack and for the edge case if stack is empty then simply push the character
    at the end return the stack as a string.
"""
# Time Complexity = O(n) || Space Complexity = O(n)


def makeGood(string):
    stack = [string[0]]
    for i in range(1, len(string)):
        if len(stack) == 0:
            stack.append(string[i])
            continue
        if abs(ord(stack[-1]) - ord(string[i])) == 32:
            stack.pop()
        else:
            stack.append(string[i])

    return "".join(stack)


print(makeGood(string))
