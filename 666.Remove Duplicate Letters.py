# Remove Duplicate Letters

s = "cbacdcbc"

def removeDuplicateLetters(self, s: str) -> str:
        dct = defaultdict(int)
        for i in range(len(s)):
            dct[s[i]] = i

        stack = []
        for i in range(len(s)):
            if s[i] not in stack:
                while stack and stack[-1] > s[i]:
                    if i < dct[stack[-1]]:
                        stack.pop()
                    else:
                        break
                stack.append(s[i])
        return "".join(stack)



# Remove Duplicate Letters

from collections import defaultdict

s = "cbacdcbc"
# s = ""

dct = defaultdict(int)
for i in range(len(s)):
    dct[s[i]] = i

print(dct)

stack = []
for i in range(len(s)):
    if s[i] not in stack:
        while stack and stack[-1] > s[i]:
            if i < dct[stack[-1]]:
                stack.pop()
            else:
                break
        stack.append(s[i])

print("".join(stack))