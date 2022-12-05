# Middle of the Linked List

"""
    Using two pointers method (slow and fast pointer method)
    initializing slow and fast as head then move slow to slow next and
    fast as fast next.next until fast reached to none then after return the slow as is now 
    pointing to the middle Node of linkedlist.  
    NOTE :- by initializing slow and fast as head the
            edge case (If there are two middle nodes, return the second middle node.)
            is automatically covered. 

"""

# Time Complexity = O(n) || Space Complexity = O(1)


class ListNode:
    def __init__(self, val=0, next=None):
        self.value = val
        self.next = next


head = ListNode(1)
n1 = ListNode(2)
n2 = ListNode(3)
n3 = ListNode(4)
n4 = ListNode(5)

head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4


def middleNode(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow


m = middleNode(head)
while m:
    print(m.value)
    m = m.next
