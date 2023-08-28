# Implement Stack using Queues

# Time : O(1)
# Space : O(n)

class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

class MyStack:

    def __init__(self):
        self.dummy = Node(0)
          

    def push(self, x: int) -> None:
        cur = Node(x)
        tmp = self.dummy.next
        self.dummy.next = cur
        cur.next = tmp
        

    def pop(self) -> int:
        if self.dummy.next.next:
            tmp = self.dummy.next.next
            ans = self.dummy.next.val
            self.dummy.next = tmp
            return ans
          
        if self.dummy.next:
            ans = self.dummy.next.val
            self.dummy.next = None
            return ans
       
    def top(self) -> int:
        return self.dummy.next.val
        

    def empty(self) -> bool:
        if self.dummy.next :
            return False
        return True
        


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
print(obj.push(1))
print(obj.push(2))
print(obj.push(3))
print(obj.pop())
print(obj.top())
print(obj.empty())
