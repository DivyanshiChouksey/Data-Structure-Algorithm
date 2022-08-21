# Remove Duplicates From Linkedlist

"""
    Take two pointers and iterate it through the linkedlist,
    start with a pointer pointing to the value of current node and
    another pointer pointing to the next value of current node
    and while node and next pointer have same value then we increase our pointer to their next 
    until we found any distinguish value , and it to the next of our current node
    at last return the head of the linkedlist 
"""
# Time Complexity = O(n) || Space Complexity = O(1)


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


head = LinkedList(1)
n1 = LinkedList(1)
n2 = LinkedList(3)
n3 = LinkedList(4)
n4 = LinkedList(4)
n5 = LinkedList(4)
n6 = LinkedList(5)
n7 = LinkedList(6)
n8 = LinkedList(6)


head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8


def removeDuplicates(head):
    current = head
    while current:
        newDistinct = current.next
        while newDistinct is not None and newDistinct.value == current.value:
            newDistinct = newDistinct.next
        current.next = newDistinct
        current = newDistinct
    return head


newHead = removeDuplicates(head)
while newHead:
    print(newHead.value)
    newHead = newHead.next
