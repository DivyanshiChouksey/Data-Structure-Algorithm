# Design Circular Queue


class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class MyCircularQueue:
    def __init__(self, k: int):
        self.maxSize = k
        self.curSize = 0
        self.head = None
        self.tail = None

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        node = LinkedListNode(value)
        node.next = self.head
        if self.isEmpty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.curSize += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = self.head.next
        self.tail.next = self.head
        self.curSize -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.head.value

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.tail.value

    def isEmpty(self) -> bool:
        return self.curSize == 0

    def isFull(self) -> bool:
        return self.curSize == self.maxSize
