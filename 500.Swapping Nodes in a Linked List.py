# Swapping Nodes in a Linked List

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


# head = [1,2,3,4,5], 
k = 2

# Time - O(n) || Space - O(1)

def swapNodes(head, k):
    s = head
    f = head
    k-=1
    while k and f.next:
        f = f.next
        k -= 1
    
    tmp = f
    while f.next :
        s=s.next
        f=f.next

    s.val , tmp.val = tmp.val,s.val
    return head

m = swapNodes(head,k)
while m:
    print(m.val)
    m = m.next