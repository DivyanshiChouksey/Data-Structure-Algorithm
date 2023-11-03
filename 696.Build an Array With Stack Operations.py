# Build an Array With Stack Operations

target = [2,5,8]
n = 9

def buildArray(target, n):  
    stack = []
    i = 1
    for num in target:
        while i<num:
            stack.append("Push")
            stack.append("Pop")
            i+=1
        # if i==num:
        stack.append("Push")
        i+=1
    return stack

print(buildArray(target, n))
