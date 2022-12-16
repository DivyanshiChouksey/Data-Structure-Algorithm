# Implement Queue using Stacks

# Time Complexity = O(n) || Space Complexity = O(n)


class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        n = len(self.s1) - 1
        for i in range(n):
            self.s2.append(self.s1.pop())
        ans = self.s1.pop()
        for i in range(n):
            self.s1.append(self.s2.pop())
        return ans

    def peek(self) -> int:
        n = len(self.s1) - 1
        for i in range(n):
            self.s2.append(self.s1.pop())
        ans = self.s1[-1]
        for i in range(n):
            self.s1.append(self.s2.pop())
        return ans

    def empty(self) -> bool:
        return len(self.s1) == 0


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.pop())
print(obj.peek())
print(obj.empty())
