# Min Max Stack Construction
"""
    Make another stack to keep track of min and max in it 
    note for underflow of stack 
"""

# Time Complexity = O(1) || Space Complexity = O(1)


class StackConstruction:
    def __init__(self):
        self.minMaxStack = []
        self.stack = []

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()

    def push(self, number):
        newMinMax = {"min": number, "max": number}
        if len(self.minMaxStack):
            last = self.minMaxStack[len(self.minMaxStack) - 1]
            newMinMax["min"] = min(last["min"], number)
            newMinMax["max"] = max(last["max"], number)
        self.minMaxStack.append(newMinMax)
        self.stack.append(number)

    def getMin(self):
        return self.minMaxStack[len(self.minMaxStack) - 1]["min"]

    def getMax(self):
        return self.minMaxStack[len(self.minMaxStack) - 1]["max"]


s1 = StackConstruction()
s1.push(2)
s1.push(9)
s1.push(4)
print(s1.getMin())
print(s1.getMax())
print(s1.peek())
