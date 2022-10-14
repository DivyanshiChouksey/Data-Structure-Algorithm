# Longest Balance Substring

string = "(()()))"


def longestBalancedSubstring(string):
    dct = {")": "("}
    stack = []
    i = 0
    count = 0
    while i < len(string):
        if string[i] is "(":
            stack.append(string[i])
        elif string[i] is ")":
            if len(stack) == 0:
                stack.append(string[i])
            elif stack[-1] == dct[string[i]]:
                stack.pop()
                count += 2
            else:
                stack.append(string[i])
        i += 1
    return count


print(longestBalancedSubstring(string))
