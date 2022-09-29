# Remove N-th node from the end of a Linked List

"""
    Firstly take two pointers(F-Fast,S-Slow) initially both are at head
    then move one pointer(S) N distance away from the another pointer(F)
    then after that move both pointer simultaneously until the second Pointer's next(S) pointed to Null Node 
    that means our F pointer's next is pointing to the N th node from the end which we have to remove from the list
    so just point the Fpointer's next to Fpointer's next to next and return the head of the list.

    Note :- very imp edge case if the Nth node is the head of list then just made head's next node as Head of 
    new list.

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


head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6


k = 3


def removeKthNodeFromEnd(head, k):
    count = 1
    first = head
    second = head
    while count <= k:
        second = second.next
        count += 1
    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    while second.next is not None:
        second = second.next
        first = first.next
    first.next = first.next.next
    return head


newHead = removeKthNodeFromEnd(head, k)
while newHead:
    print(newHead.value)
    newHead = newHead.next
