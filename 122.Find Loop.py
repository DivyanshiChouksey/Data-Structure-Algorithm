# Find Loop
"""
    We use 2pointer from head next and head.next.next "Slow" and "Fast" namely
    Then we go through linkedlist and when they meet that means we found loop exist
    or else update our slow by slow.next and fast as fast.next.next until they meet.
"""

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
n6 = LinkedList(6)
n7 = LinkedList(7)
n8 = LinkedList(8)
n9 = LinkedList(9)

head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8
n8.next = n9
n9.next = n4


def findLoop(head):
    slow = head.next
    fast = head.next.next

    while slow != fast:
        slow = slow.next
        fast = fast.next.next

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow.value
    # return slow


print(findLoop(head))
