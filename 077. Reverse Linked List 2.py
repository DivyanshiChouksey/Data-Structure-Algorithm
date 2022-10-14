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

left = 2
right = 4


def reverseList(head, left, right):
    if left == right:
        return head
    dummyHead = ListNode(0)
    dummyHead.next = head
    cur, prev = head, dummyHead
    for i in range(left - 1):
        cur = cur.next
        prev = prev.next

    for i in range(right - left):
        tmp = cur.next
        cur.next = tmp.next
        tmp.next = prev.next
        prev.next = tmp
        # for i in range(left - 1):
        #     prev = prev.next
        #     cur = cur.next
        # # we are already at our starting point so we directly use end location
        # for j in range((right - left)):
        #     tmp = cur.next  # 3
        #     cur.next = tmp.next  # 2.next = 3..next(4)
        #     tmp.next = prev.next  # 3.next = 1.next(2)
        #     prev.next = tmp  # 1..next = 3
        # cur.next = prev
        # prev = cur
        # cur = tmp

    return dummyHead.next


newHead = reverseList(head, 2, 4)

# while newHead:
for i in range(5):
    print(newHead.val)
    newHead = newHead.next
