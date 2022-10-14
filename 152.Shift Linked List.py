# Shift Linked List

# Time Complexity = O(n) || Space Complexity = O(1)


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


head = LinkedList(0)
n1 = LinkedList(1)
n2 = LinkedList(2)
n3 = LinkedList(3)
n4 = LinkedList(4)
n5 = LinkedList(5)

head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5


def shiftLinkedList(head, k):
    leng = 1
    listTail = head
    while listTail.next:
        listTail = listTail.next
        leng += 1

    offset = abs(k) % leng
    if offset == 0:
        return head

    newTailPos = leng - k if k > 0 else offset
    newTail = head
    for i in range(1, newTailPos):
        newTail = newTail.next

    newHead = newTail.next
    newTail.next = None
    listTail.next = head

    return newHead


k = 2
m = shiftLinkedList(head, k)

while m:
    print(m.value)
    m = m.next
