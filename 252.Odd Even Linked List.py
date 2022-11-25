# Odd Even Linked List

"""
    Create two individual linked list of odd and even, then connect odd linkedlist to even
    start by making head as odd's head and head's next as even's head and then grow both list by connecting
    odd.next to odd.next.next and even.next to even.next.next and at the last for connecting odd and even make 
    odd next even's head and return the odd's head.
"""

# Time Complexity = O(n) || Space Complexity = O(1)
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


head = LinkedList(1)
n1 = LinkedList(2)
n2 = LinkedList(3)
n3 = LinkedList(4)
n4 = LinkedList(5)


head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4


def oddEvenList(head):

    if not head:
        return head
    odd = head
    even = head.next
    eHead = even

    while even and even.next:
        odd.next = odd.next.next
        even.next = even.next.next
        odd = odd.next
        even = even.next

    odd.next = eHead
    return head


newHead = oddEvenList(head)
while newHead:
    print(newHead.value)
    newHead = newHead.next
