# Reverse Nodes in k-Group


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


head = 1


def reverseKGroup(head, k):
    dummyNode = ListNode(0, head)
    cur, prev, nxt = dummyNode, dummyNode, dummyNode
    cnt = 0
    while cur.next:
        cnt += 1
        cur = cur.next

    while cnt >= k:
        cur = new = prev.next
        nxt = cur.next
        for _ in range(k - 1):
            tmp = nxt.next
            nxt.next = cur
            cur = nxt
            nxt = tmp

        prev.next = cur
        new.next = nxt
        prev = new
        cnt -= k

    return dummyNode.next
