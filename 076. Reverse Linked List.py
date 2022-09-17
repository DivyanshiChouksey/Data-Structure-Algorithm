# Reverse Linked List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
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

"""
    Here we start by taking previous pointer initially as None and then we keep record of next node so that we 
    don't lose access of it after that update current next to its previous node
    and pervious to current node and now current will be the next node ie. the node we have been kept in record
"""

# Time Complexity = O(n) || Space Complexity = O(1)
def reverseList(head):
    prev = None
    while head:
        tmp = head.next
        head.next = prev
        prev = head
        head = tmp
    return prev


newHead = reverseList(head)

# display values
while newHead:
    print(newHead.val)
    newHead = newHead.next
