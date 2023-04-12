class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path2 = path.split("/")
        print(path2)
        for dir in path2:
            if dir == "..":
                if len(stack) > 0:
                    stack.pop()
            elif dir == "." or dir == "":
                continue
            else:
                stack.append(dir)

        return("/" + "/".join(stack))
